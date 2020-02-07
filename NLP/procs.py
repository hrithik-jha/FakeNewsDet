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
document = snlp(art[0])
features = []

#Scraping Google Results
api_key = ''
search_id = ''
url = 'https://www.googleapis.com/customsearch/v1?'

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
    #urls = art[2].split('/')
    
    #Finding the Source
    #source = urls[2]
    #features.append(["SOURCE", str(source)])

    #Name Entity Recognition
    for i in document.ents:
        features.append([i.label_, str(i)])
  
    
extractData()

featurettes = []
for i in features:
    if i[1] not in featurettes and i[0] == "PERSON" or i[0] == "ORG":
        featurettes.append(i[1])
print(featurettes)

counts = Counter(featurettes).most_common(5)
print(counts)
strn = ""
for i in range(0, len(counts)):
    strn += str(counts[i][0])
    if i != len(counts) - 1:
        strn += "+"

#GoogleRes(strn)

api_req = "https://newsapi.org/v2/top-headlines?"
api_keyy = "&apiKey=9bb879b3283d4f90b7202bd015ccf9af"

'''top_headlines = newsapi.get_top_headlines(
        q='Project Kuiper',
        language='en',
        )
print(top_headlines)
'''
#print(features)