""" Main file for performing Reconciliation on input file. """
import sys
from portfolio import PortfolioTracker

D0_POS = "D0-POS"
D1_TRN = "D1-TRN"
D1_POS = "D1-POS"


def reconciliation():
    """
        reconciliation takes sys.stdin() and will format all three sections of
        input D0-POS, D1-TRN, and D1-POS into the correct data
        structures for processing.
    """
    d0_pos_list = list()
    d1_trn_list = list()
    d1_pos_list = list()
    d0_pos_flag = False
    d1_trn_flag = False
    d1_pos_flag = False

    # This for loop will format the input into 3 main lists
    # for each main section which will we then send to our
    # class for appropriate action
    for line in sys.stdin:
        line = line.strip()
        if line == D0_POS:
            d1_trn_flag = False
            d1_pos_flag = False
            d0_pos_flag = True
        elif line == D1_TRN:
            d0_pos_flag = False
            d1_pos_flag = False
            d1_trn_flag = True
        elif line == D1_POS:
            d1_trn_flag = False
            d0_pos_flag = False
            d1_pos_flag = True
        elif d0_pos_flag and line is not "":
            d0_pos_list.append(line)
        elif d1_trn_flag and line is not "":
            d1_trn_list.append(line)
        elif d1_pos_flag and line is not "":
            d1_pos_list.append(line)
        elif line == "":
            continue
        else:
            raise Exception("Input is formed incorrectly.")

    portfolio = PortfolioTracker(d0_pos_list)
    portfolio.update_portfolio(d1_trn_list)
    portfolio.compare_portfolio(d1_pos_list)


if __name__ == "__main__":
    reconciliation()
