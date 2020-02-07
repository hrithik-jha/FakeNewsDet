#Importing libraries
import csv
import requests
import time
from bs4 import BeautifulSoup
import re

url = "https://www.cnbc.com/2020/02/07/tidjane-thiam-to-step-down-as-credit-suisse-ceo-on-feb-14.html"
art = []

#Cleaning The Data
def cleaning(art):
    text = art[0]
    # remove html markup
    text = re.sub("(<.*?>)","",text)
    #remove non-ascii and digits
    text = re.sub("(\\W)"," ",text)    
    #remove whitespace
    #text = text.strip()

    art[0] = text

    return


#Manual Entry
def manualEntry():
    print("Connection has been denied, please enter manually.")
    body = ""
    body = input()
    return body

#Scraping
def scrape(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    p = ""
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")
    #art.append(soup.findAll('h2')[0].string)
    for i in range(0, len(soup.findAll('p'))):
        p += soup.findAll('p')[i].text
    art.append(p)
    
    if art[0] == "We've detected unusual activity from your computer network":
       p = manualEntry()
       art.append(p)
    #else:
        #print(art)
    #art.append(url)
    cleaning(art)
    #print(art)
     
scrape(url)