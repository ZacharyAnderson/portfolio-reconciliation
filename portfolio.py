class PortfolioTracker:
    """
        This class is used to keep track of all stocks and cash
        that were bought and sold during a day of trading.
        This class will also be able to output the difference
        between the correct portfolio of stocks and cash and
        what the bank has on record.
    """
    _CASH = "Cash"
    _BUY = "BUY"
    _SELL = "SELL"
    _FEE = "FEE"
    _DEPOSIT = "DEPOSIT"
    _DIVIDEND = "DIVIDEND"

    def __init__(self, d0_pos_list):
        self.portfolio = self.create_dict(d0_pos_list)

    def __repr__(self):
        return repr(self.portfolio)

    def create_dict(self, input_list):
        """
            Creates a dictionary for use with our portfolio.
            Also is used to compare both our portfolio and
            d1-pos data. If "Cash" is not a key in the input
            then we will add that as we will need that key-value
            pair for our update_portfolio function.
        """
        new_dict = dict()
        for line in input_list:
            transaction = line.split()
            if transaction[0] in new_dict.keys():
                new_dict[transaction[0]] += float(transaction[1])
            else:
                new_dict[transaction[0]] = float(transaction[1])
        if self._CASH not in new_dict.keys():
            new_dict[self._CASH] = float(0)
        return new_dict

    def update_portfolio(self, d1_trn_list):
        """
            Takes d1-trn data and updates our existing
            portfolio to have all correct metrics for d0
            and d1 of transactions. If input list is formatted
            incorrectly will raise an Exception error.
        """
        for line in d1_trn_list:
            transaction = line.split()
            if transaction[1] == self._BUY:
                if transaction[0] in self.portfolio.keys():
                    self.portfolio[transaction[0]] += float(transaction[2])
                    self.portfolio[self._CASH] -= float(transaction[3])
                else:
                    self.portfolio[transaction[0]] = float(transaction[2])
                    self.portfolio[self._CASH] -= float(transaction[3])
            elif transaction[1] == self._SELL:
                if transaction[0] in self.portfolio.keys():
                    self.portfolio[transaction[0]] -= float(transaction[2])
                    self.portfolio[self._CASH] += float(transaction[3])
                else:
                    self.portfolio[transaction[0]] =\
                        (float(transaction[2]) * -1)
                    self.portfolio[self._CASH] += float(transaction[3])
            elif transaction[1] == self._FEE:
                self.portfolio[self._CASH] -= float(transaction[3])
            elif transaction[1] == self._DEPOSIT or\
                    transaction[1] == self._DIVIDEND:
                self.portfolio[self._CASH] += float(transaction[3])
            else:
                raise Exception("recon.in is formatted incorrectly.")

    def compare_portfolio(self, d1_pos_list):
        """
            Takes d1-pos and compares it against our portfolio.
            After the compariso we print the correct difference
            listed from d1-pos and our portfolio.
        """
        output_dict = self.create_dict(d1_pos_list)
        matching_keys = self.portfolio.keys() & output_dict.keys()
        portfolio_nonmatching_keys = self.portfolio.keys() - output_dict.keys()
        output_nonmatching_keys = output_dict.keys() - self.portfolio.keys()

        for key in matching_keys:
            difference = output_dict[key] - self.portfolio[key]
            if difference != float(0.0):
                print(key + " " + str(self.format_decimal(difference)))
        for key in portfolio_nonmatching_keys:
            if self.portfolio[key] != 0.0:
                print(key + " -" +
                      str(self.format_decimal(self.portfolio[key])))
        for key in output_nonmatching_keys:
            if output_dict[key] != 0.0:
                print(key + " " + str(self.format_decimal(output_dict[key])))

    def format_decimal(self, num):
        """
            formats our float or int variable to return
            a number with the correct amount of trailing 0's.
        """
        if num % 1 == 0:
            return int(num)
        else:
            return num
