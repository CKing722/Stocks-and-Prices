stocks_dict = {'AAPL' : 178.71, 'MSFT' : 334.55, 'AMZN' : 138.26, 'NVDA' : 455.45, 'GOOGL' : 136.72, \
'GOOG' : 137.49, 'TSLA' : 249.00, 'META' : 297.78, 'BRK.B' : 362.83 , 'XOM' : 115.55}

print('\nEnter Ticker Symbol (Example: AAPL) (type EXIT to quit)')
ticker = ''

keys = stocks_dict.keys()

while True:
  ticker = input('\nInput: ').strip().upper()

  if ticker == 'EXIT':
    break

  if ticker in stocks_dict:
    print(f"{ticker} has a current stock price of {stocks_dict[ticker]}")

  else:
    print(f'{ticker} was not located in our Stocks Dictionary, our Dictionary contains the following Stocks:')
    print(keys)
    
   
    







    

  

