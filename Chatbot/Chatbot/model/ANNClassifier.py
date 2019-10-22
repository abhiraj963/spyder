# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:46:36 2019

@author: Abhiraj
"""

from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
def ann_classifier(X,y):
    model.add(Dense(int((X.shape[1]/2) + 1),input_shape = (X.shape[1],), kernel_initializer= 'uniform', activation= 'relu'))
    model.add(Dense(y.shape[1], kernel_initializer= 'uniform', activation= 'softmax'))
    model.compile(optimizer='adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
    model.fit(X,y, batch_size=10, epochs=100)
    return model