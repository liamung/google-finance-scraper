# web-stocker
web scraper that scrapes all relevant data, values and articles relating to a ticker listed on google finance into a custom csv file
developed with python utilizing beautiful soup library

"Ticker: " prompt asks for stock ticker
"Market: " prompt asks for corresponding market
"File: " prompt asks for the name of a csv file to input data.
if the file name is one of an existing csv file, it will write over the old file
if the file name is not one of an existing csv file, it will create a new file with that name
