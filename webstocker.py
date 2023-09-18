from bs4 import BeautifulSoup
import requests as re
import csv

url = "https://www.google.com/finance/quote/"
name = input("Ticker: ")
market = input("Market: ")
filename = input("File name: ")

page_to_scrape = re.get(url + name + ":" + market)
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
scrpts = soup.findAll("div", attrs={"class":"mfs7Fc"})
nums = soup.findAll("div", attrs={"class":"P6K39c"})
news = soup.findAll("div", attrs={"class":"F2KAFc"})

file = open(filename+".csv", "w")
writer = csv.writer(file)

writer.writerow(["INFO", " VALUES"])

for scrpt, num in zip(scrpts, nums):
    print(scrpt.text + ": " + num.text)
    writer.writerow([scrpt.text, " " + num.text])

writer.writerow(["ARTICLES"])

for article in (news):
    print(article.text)
    writer.writerow([article.text])
file.close