import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import bookScrap

dataset = pd.read_csv('data.tsv', delimiter = '\t', quoting = 3)

# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(len(dataset)):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Book_Name'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [str(ps.stem(word)) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=3000)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1:2].values


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.10, random_state = 0)


# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

#y_pred = classifier.predict(X_test)
loop=True
while(loop):
    print("Enter ex to exit")
    x=input()
    if(x=='ex'):
        break
    x=[x]
    x=cv.transform(x).toarray()
    ans=classifier.predict(x)
    print('Genre is : '+bookScrap.Edited_Genre_list[ans])