""" Main file for performing Reconciliation on input file. """
import sys
from recon import ReconTracker


def format_input():
    """
        format_input takes sys.stdin() and will format all three sections of
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
        if line.strip() == "D0-POS":
            d1_trn_flag = False
            d1_pos_flag = False
            d0_pos_flag = True
        elif line.strip() == "D1-TRN":
            d0_pos_flag = False
            d1_pos_flag = False
            d1_trn_flag = True
        elif line.strip() == "D1-POS":
            d1_trn_flag = False
            d0_pos_flag = False
            d1_pos_flag = True
        elif d0_pos_flag and line.strip() is not "":
            d0_pos_list.append(line.strip())
        elif d1_trn_flag and line.strip() is not "":
            d1_trn_list.append(line.strip())
        elif d1_pos_flag and line.strip() is not "":
            d1_pos_list.append(line.strip())
        elif line.strip() == "":
            continue
        else:
            raise Exception("Input is formed incorrectly.")

    print(d1_trn_list)
    print(d1_pos_list)
    ReconTracker(d0_pos_list)


if __name__ == "__main__":
    format_input()
