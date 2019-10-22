# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 00:04:30 2019

@author: Abhiraj
"""

from sklearn.linear_model import SGDClassifier
sgdc= SGDClassifier(loss = 'log')
def SGD(X,y):
    global sgdc
    sgdc.fit(X,y)
    return sgdc