# Fake News Detector

## Intro
This project is an application of web-scraping and text classification functionalities to employ the classification of the authenticity of the news article.

## Setup
Enter the news article in the in `prepr.py` as the URL variable. \
To receive similar Google news articles, enter Google key credentials.

## Running
Run `python opert.py` in `/NLP` folder. \
All output will be printed in the terminal.

## Viz
The `plots.py` plots graphs for better inference of the cleaned article after applying NER to identify most commonly written Names or Entities. Add custom word disambiguation for plotting.

## Doc map
```
└── API
    └── app.py
└── Data
    ├── test.csv
    └── train.csv
└── NLP
    ├── opert.py
    ├── prepr.py
    ├── procs.py
    └── FakeNewsPred.py
└── Viz
    └── plots.py
├── README.md
└── requirements.txt
```
