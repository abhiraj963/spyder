import pandas as pd
import numpy as np
#import nltk
#nltk.download('stopwords')
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
data = pd.read_excel('Data_Train.xlsx')

ps = PorterStemmer()
def text_clean(article):
    global ps
    clean_text = re.sub('[^a-zA-Z]',' ', article)
    clean_text = clean_text.lower()
    clean_text = clean_text.split()
    clean_text = [ps.stem(word) for word in clean_text if word not in set(stopwords.words('english'))]
    clean_text = ' '.join(clean_text)
    return clean_text

data['STORY'] = data['STORY'].apply(text_clean)
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
cv = CountVectorizer()
X = cv.fit_transform(data['STORY'])
y = data['SECTION']

tfidf = TfidfTransformer()
X = tfidf.fit_transform(X)

from sklearn.model_selection import train_test_split
y = pd.get_dummies(y,drop_first = True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from keras.models import Sequential
from keras.layers import Dense
news_category = Sequential()
news_category.add(Dense(10000,input_shape = (21659,), kernel_initializer= 'uniform', activation= 'relu'))
news_category.add(Dense(3, kernel_initializer= 'uniform', activation= 'softmax'))
news_category.compile(optimizer='adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

news_category.fit(X_train,y_train, batch_size=1, epochs=10)
predictions = news_category.predict(X_test)

from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

test_data = pd.read_excel('Data_Test.xlsx')
test_data['STORY'] = test_data['STORY'].apply(text_clean)
test_fit = cv.transform(test_data['STORY'])
test_X = tfidf.transform(test_fit)
test_pred = news_category.predict(test_X)

np.savetxt('pred.csv',test_pred,delimiter = ',')