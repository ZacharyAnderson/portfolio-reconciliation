class PortfolioTracker:
    """
        This class is used to keep track of all stocks and cash
        that were bought and sold during a day of trading.
        This class will also be able to output the difference
        between the correct portfolio of stocks and cash and
        what the bank has on record.
    """

    def __init__(self, d0_pos_list):
        self.portfolio = self.create_dict(d0_pos_list)

    def create_dict(self, input_list):
        new_dict = dict()
        for line in input_list:
            tmp = line.split()
            if tmp[0] in new_dict.keys():
                new_dict[tmp[0]] += float(tmp[1])
            else:
                new_dict[tmp[0]] = float(tmp[1])
        return new_dict

    def update_portfolio(self, d1_trn_list):
        for line in d1_trn_list:
            tmp = line.split()
            if tmp[1] == "BUY":
                if tmp[0] in self.portfolio.keys():
                    self.portfolio[tmp[0]] += float(tmp[2])
                    self.portfolio["Cash"] -= float(tmp[3])
                else:
                    self.portfolio[tmp[0]] = float(tmp[2])
                    self.portfolio["Cash"] -= float(tmp[3])
            elif tmp[1] == "SELL":
                if tmp[0] in self.portfolio.keys():
                    self.portfolio[tmp[0]] -= float(tmp[2])
                    self.portfolio["Cash"] += float(tmp[3])
                else:
                    self.portfolio[tmp[0]] = (float(tmp[2]) * -1)
                    self.portfolio["Cash"] += float(tmp[3])
            elif tmp[1] == "FEE":
                self.portfolio["Cash"] -= float(tmp[3])
            elif tmp[1] == "DEPOSIT" or tmp[1] == "DIVIDEND":
                self.portfolio["Cash"] += float(tmp[3])

    def compare_portfolio(self, d1_pos_list):
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
        if num % 1 == 0:
            return int(num)
        else:
            return num
