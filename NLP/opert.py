import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from prepr import art
import procs

#Importing the Dataset 
df = pd.read_csv(r'C:\\Users\\Hrithik Jha\\FakeNewsDet\\Data\\train.csv')
df.dropna()

#Splitting for Train and Test
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], random_state=0)

#Removing NaN entries from the dataset
X_train = X_train.fillna(' ')
X_test = X_test.fillna(' ')

#Vectorizing text to use in a classifier
#Using n-grams to provide context to certain words
vect = TfidfVectorizer(ngram_range=(1,2)).fit(X_train)
X_train_vectorized = vect.transform(X_train)

#Using Logistic Regression and training it
model1 = LogisticRegression()
model1.fit(X_train_vectorized, y_train)

#Predicting the article obtained from the URL
prediction = model1.predict(vect.transform([art[1]]))
print("Prediction: ", prediction)