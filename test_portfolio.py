import unittest
from unittest.mock import patch
from portfolio import PortfolioTracker


class TestPortfolioTracker(unittest.TestCase):
    """
        This class is intended to test multiple cases to ensure
        PortfolioTracker works as intended.
    """

    def test_create_dict_normal_list(self):
        test_list = ['AAPL 100', 'GOOG 200', 'SP500 175.75', 'Cash 1000']
        new_portfolio = PortfolioTracker(test_list)
        expected_output = {'AAPL': 100.0, 'GOOG': 200.0,
                           'SP500': 175.75, 'Cash': 1000.0}
        self.assertEqual(expected_output, new_portfolio.portfolio)

    def test_create_dict_normal_list_with_no_cash(self):
        test_list = ['AAPL 100', 'GOOG 200', 'SP500 175.75']
        new_portfolio = PortfolioTracker(test_list)
        expected_output = {'AAPL': 100.0, 'GOOG': 200.0,
                           'SP500': 175.75, 'Cash': 0.0}
        self.assertEqual(expected_output, new_portfolio.portfolio)

    def test_update_portfolio(self):
        test_list = ['AAPL 100', 'GOOG 200', 'SP500 175.75', 'Cash 1000']
        new_portfolio = PortfolioTracker(test_list)
        test_trn_list = ['AAPL SELL 100 30000', 'GOOG BUY 10 10000',
                         'CASH DEPOSIT 0 1000', 'CASH FEE 0 50',
                         'GOOG DIVIDEND 0 50', 'TD BUY 100 10000']
        new_portfolio.update_portfolio(test_trn_list)
        expected_output = {'AAPL': 0.0, 'GOOG': 210.0, 'SP500': 175.75,
                           'Cash': 12000.0, 'TD': 100.0}
        self.assertEqual(expected_output, new_portfolio.portfolio)

    def test_compare_portfolio(self):
        test_list = ['AAPL 100', 'GOOG 200', 'SP500 175.75', 'Cash 1000']
        new_portfolio = PortfolioTracker(test_list)
        test_trn_list = ['AAPL SELL 100 30000', 'GOOG BUY 10 10000',
                         'CASH DEPOSIT 0 1000', 'CASH FEE 0 50',
                         'GOOG DIVIDEND 0 50', 'TD BUY 100 10000']
        new_portfolio.update_portfolio(test_trn_list)
        test_p1_pos_list = ['GOOG 220', 'SP500 175.75',
                            'Cash 20000', 'MSFT 10']
        with patch('sys.stdout') as fake_output:
            new_portfolio.compare_portfolio(test_p1_pos_list)
            fake_output.assert_has_calls([
                unittest.mock.call.write("Cash 8000"),
                unittest.mock.call.write("\n"),
                unittest.mock.call.write("GOOG 10"),
                unittest.mock.call.write("\n"),
                unittest.mock.call.write("TD -100"),
                unittest.mock.call.write("\n"),
                unittest.mock.call.write("MSFT 10"),
                unittest.mock.call.write("\n")
            ], any_order=True)

    def test_duplicate_stocks_in_d0(self):
        test_list = ['AAPL 100', 'GOOG 200', 'SP500 175.75',
                     'Cash 1000', 'AAPL 50']
        new_portfolio = PortfolioTracker(test_list)
        expected_output = {'AAPL': 150.0, 'GOOG': 200.0,
                           'SP500': 175.75, 'Cash': 1000.0}
        self.assertEqual(expected_output, new_portfolio.portfolio)

    def test_selling_stock_not_in_portfolio(self):
        test_list = ['AAPL 100', 'GOOG 200', 'SP500 175.75', 'Cash 1000']
        new_portfolio = PortfolioTracker(test_list)
        test_trn_list = ['AAPL SELL 100 30000', 'GOOG BUY 10 10000',
                         'CASH DEPOSIT 0 1000', 'CASH FEE 0 50',
                         'GOOG DIVIDEND 0 50', 'TD BUY 100 10000',
                         'AMD SELL 10 270']
        new_portfolio.update_portfolio(test_trn_list)
        expected_output = {'AAPL': 0.0, 'GOOG': 210.0, 'SP500': 175.75,
                           'Cash': 12270.0, 'TD': 100.0, 'AMD': -10.0}
        self.assertEqual(expected_output, new_portfolio.portfolio)

    def test_incorrect_list_in_portfolio(self):
        test_list = ['AAPL 100', 'GOOG 200', 'SP500 175.75', 'Cash 1000']
        new_portfolio = PortfolioTracker(test_list)
        test_trn_list = ['AAPL FAKE 100 30000']
        self.assertRaises(Exception,
                          new_portfolio.update_portfolio, test_trn_list)
   
    def test_format_decimal(self):
        test_list = ['AAPL 100', 'GOOG 200', 'SP500 175.75', 'Cash 1000']
        new_portfolio = PortfolioTracker(test_list)
        self.assertEqual(23, new_portfolio.format_decimal(23))
        self.assertEqual(23.25, new_portfolio.format_decimal(23.25))

if __name__ == "__main__":
    unittest.main()
