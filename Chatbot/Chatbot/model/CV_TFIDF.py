# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:36:29 2019

@author: Abhiraj
"""

from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
cv = CountVectorizer()
tfidf = TfidfTransformer()
def cv_tfidf(data):
    global cv, tfidf
    X = cv.fit_transform(data)
    X = tfidf.fit_transform(X)
    from sklearn.externals import joblib
    joblib.dump(X.tocsr(), 'dataset.joblib')
    x_csr = joblib.load('dataset.joblib')    
    return x_csr,cv, tfidf