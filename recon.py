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
                self.portfolio[tmp[0]] += float(tmp[1])
            else:
                self.portfolio[tmp[0]] = float(tmp[1])

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
        for line in d1_pos_list:
            tmp = line.split()
            if tmp[0] in self.portfolio.keys():
                print(tmp)
                print(self.portfolio[tmp[0]])
            elif tmp[0] not in self.portfolio.keys():
                print(tmp[0] + " " + tmp[1])
