# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 10:42:33 2019

@author: Abhiraj
"""
import pandas as pd
#import numpy as np
import clean_data.clean as ct
#import model.logistic as ml
import model.CV_TFIDF as cvtf
#import model.SGD_Classifier as sg
import model.SVMClassifier as svc
import model.ANNClassifier as ann

questions = pd.read_excel('questions.xlsx', header = None)
questions[0] = questions[0].apply(ct.text_clean)
questions.to_excel("clean_data.xlsx",index = False, header = False)
y = pd.read_excel('answers.xlsx', header = None)

X,cv,tfidf = cvtf.cv_tfidf(questions[0])

trained_model = svc.svm_class(X,y[0])
#trained_model = ann.ann_classifier(X,y[0])
entry  = 1
while entry:
    string = input(':')
    if string == '':
        print("Ciao")
        entry = 0
    else:
        string = ct.text_clean(string)
        string = cv.transform([string,])
        string = tfidf.transform(string)
        print(trained_model.predict(string)[0])
    