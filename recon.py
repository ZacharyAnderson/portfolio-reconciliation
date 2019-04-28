class ReconTracker:
    """
        This class is used to keep track of all stocks and cash
        that were bought and sold during a day of trading.
        This class will also be able to output the difference
        between the correct portfolio of stocks and cash and
        what the bank has on record.
    """

    def __init__(self, d0_pos_list):
        self.portfolio = dict()

        self.initiliaze_portfolio(d0_pos_list)

    def initiliaze_portfolio(self, d0_pos_list):
        for line in d0_pos_list:
            tmp = line.split()
            if tmp[0] in self.portfolio.keys():
                self.portfolio[tmp[0]] += tmp[1]
            else:
                self.portfolio[tmp[0]] = tmp[1]
        print(self.portfolio)
