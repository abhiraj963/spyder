# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 00:48:02 2019

@author: Abhiraj
"""

from sklearn import svm
svmc = svm.SVC(gamma='scale', decision_function_shape='ovo')
def svm_class(X,y):
    global svmc
    svmc.fit(X,y)
    return svmc