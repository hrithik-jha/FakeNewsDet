#Importing Libraries
import nltk
import spacy
import re
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
from prepr import art
from collections import Counter
import requests

#Initializing SpaCy
snlp = spacy.load('en_core_web_sm')
document = snlp(art[0])
features = []

# Removing the very common words
remove_words = ['CNBC', 'Bloomberg', 'nytimes', 'bbc', 'reuters', 'guardian', 'forbes', 'fool', 'times of india', 'quartz', 'politifact']

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
  
#Name Entity Recognition    
extractData()


#Initializing Features
featurettes = []
for i in features:
    if i[0] == "PERSON" or i[0] == "ORG":
        featurettes.append(i[1])
print("Extracted features...") 
print(featurettes)

#Counting 5 most common relevant terms for finding similar articles
counts = Counter(featurettes).most_common(5)
print(counts)
strn = ""
for i in range(0, len(counts)):
    strn += str(counts[i][0])
    if i != len(counts) - 1:
        strn += "+"

if api_key == '' or search_id == '':
    print("Need Google API keys for similar article search.")
else:
    GoogleRes(strn)
