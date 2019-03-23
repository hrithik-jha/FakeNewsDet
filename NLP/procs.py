#Importing Libraries
import nltk
import spacy
import re

from prepr import art, Article

#Initializing SpaCy
snlp = spacy.load('en_core_web_sm')
document = snlp(art[1])
features = []

#Initializing a score for the article
score = 0

#Function to extract details
def extractData():
    urls = art[2].split('/')
    
    #Finding the Source
    source = urls[2]
    features.append(["SOURCE", source])

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

    features.append(["OG DATE", date])
    #print(date)

    #Name Entity Recognition
    for i in document.ents:
        features.append([i.label_, i])

    #Checking the header of the site
    if urls[0] == "https":
        score += 1
    elif urls[0] == "http":
        score += 0
    
    print(features)    
    
extractData()

#print(features)