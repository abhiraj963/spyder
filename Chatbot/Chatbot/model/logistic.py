# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:14:33 2019

@author: Abhiraj
"""

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(solver='saga', multi_class='multinomial',max_iter=1000)
def LogReg(X,y):
    global lr
    lr.fit(X,y)
    return lr