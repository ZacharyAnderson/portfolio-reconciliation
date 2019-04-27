# The Problem:
Reconciliation is a term YCharts uses for a set of correctness and consistency measures applied to the data we receive and use in financial calculations. One of the most common reconciliation checks is called
*unit reconciliation*, which answers the question, "does the transaction history add up to the number of shares the bank says I have?". For example, if the bank said I had 100 shares of Apple at the end of yesterday, and I bought 20 shares of Apple today, then we expect the bank to report 120 shares at the end of today. This surprisingly isn't always the case! The bank may send incomplete data, we may be parsing it incorrectly, or there may be events like corporate actions or trade settlement lag that cause an inconsistency

## FAQ:
1. Can you sell a stock you don't own already ?
Yes, you can. In finance this is called a short sale. The goal here is to compare data difference simply, so it is acceptable to have a negative position.
2. Do I need to validate the data format?
No, assume the data format in recon.in has no errors (WYSIWYG).
 

## Test Data
recon.in
------------
D0-POS
AAPL 100
GOOG 200
SP500 175.75
Cash 1000

D1-TRN
AAPL SELL 100 30000
GOOG BUY 10 10000
CASH DEPOSIT 0 10000
CASH FEE 0 50
GOOG DIVIDEND 0 50
TD BUY 100 10000

D1-POS
GOOG 220
SP500 175.75
CASH 20000
MSFT 10

recon.out
-----------
CASH 8000
GOOG 10
TD -100
MSFT 10