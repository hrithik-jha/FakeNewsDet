#Importing Libraries
import nltk
import spacy
import re
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
from prepr import art, Article
from collections import Counter
import requests

#Initializing SpaCy
snlp = spacy.load('en_core_web_sm')
document = snlp(art[1])
features = []

api_key = 'AIzaSyDzb1P8F_G4Jz6PRrcn5J3HhtdyW37j_QA'
search_id = '007134015131333087432:wjuyudu_zyw'
url = 'https://www.googleapis.com/customsearch/v1?'

#Initializing a score for the article
score = 0

#Scraping Google Results
def GoogleRes(strn):
    payload = {
        'key': api_key,
        'fields': 'kind,items(title)',
        'cx': search_id,
        'q': str(strn)
    }
    r = requests.get(url, params=payload)
    print(r.text)

#Function to extract details
def extractData():
    urls = art[2].split('/')
    
    #Finding the Source
    source = urls[2]
    features.append(["SOURCE", str(source)])

    #Finding the Date
    date = []
    for u in range(0, len(urls) - 2):
        if re.match(r"[0-9]{4}", urls[u]):
            print(urls[u])
            if re.match(r"[0-9]{2}", urls[u + 1]):
                date.append(urls[u + 1])
                #print(urls[u + 1])
            if re.match(r"[0-9]{2}", urls[u + 2]):    
                date.append(urls[u + 2])
                #print(urls[u + 2])
            date.append(urls[u])

    #features.append(["OG DATE", date])
    #print(date)

    #Name Entity Recognition
    for i in document.ents:
        features.append([i.label_, str(i)])

    #print(features)    
    
extractData()

featurettes = []
for i in features:
    if i[0] == "ORG" or i[0] == "PERSON":
        featurettes.append(i[1])
#print(featurettes)

counts = Counter(featurettes).most_common(5)
print(counts)
strn = ""
for i in range(0, len(counts)):
    strn += str(counts[i][0])
    if i != len(counts) - 1:
        strn += "+"

GoogleRes(strn)

api_req = "https://newsapi.org/v2/top-headlines?"
api_keyy = "&apiKey=9bb879b3283d4f90b7202bd015ccf9af"

'''top_headlines = newsapi.get_top_headlines(
        q='Project Kuiper',
        language='en',
        )
print(top_headlines)
'''
#print(features)