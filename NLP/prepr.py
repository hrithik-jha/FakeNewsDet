#Importing libraries
import csv
import requests
import time
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/2019/03/22/world/asia/indonesia-boeing-737.html?action=click&module=Top%20Stories&pgtype=Homepage"

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
    art = []
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")
    art.append(soup.findAll('h2')[0].string)
    for i in range(0, len(soup.findAll('p'))):
        p += soup.findAll('p')[i].text
    art.append(p)
    
    if art[0] == "We've detected unusual activity from your computer network":
       manualEntry()
       return
    else:
        print(art)
     


scrape(url)
