#Importing libraries
import csv
import requests
import time
from bs4 import BeautifulSoup
import re

url = "https://www.abeldanger.org/if-you-are-not-with-israel-you-are-a-terrorist-or-are-antisemitic/"
art = []

#Cleaning The Data
def cleaning(art):
    text = art[1]
    # remove html markup
    text = re.sub("(<.*?>)","",text)
    #remove non-ascii and digits
    text = re.sub("(\\W)"," ",text)    
    #remove whitespace
    #text = text.strip()

    art[1] = text

    return


#Manual Entry
def manualEntry():
    print("Connection has been denied, please enter manually.")
    body = ""
    body = input()
    return body


#Defining the Article Class
class Article:
    def __init__(self, Webs, Journ, Date, Place, Ent):
        self.Webs = Webs
        self.Journ = Journ
        self.Date = Date
        self.Place = Place
        self.Ent = Ent

#Scraping
def scrape(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    p = ""
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")
    art.append(soup.findAll('h2')[0].string)
    for i in range(0, len(soup.findAll('p'))):
        p += soup.findAll('p')[i].text
    art.append(p)
    
    if art[0] == "We've detected unusual activity from your computer network":
       p = manualEntry()
       art.append(p)
    #else:
        #print(art)
    art.append(url)
    cleaning(art)
    #print(art)
     
scrape(url)