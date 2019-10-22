# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 10:54:51 2019

@author: Abhiraj
"""
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps = PorterStemmer()
def text_clean(article):
    global ps
    clean_text = re.sub('[^a-zA-Z]',' ', article)
    clean_text = clean_text.lower()
    clean_text = clean_text.split()
    clean_text = [ps.stem(word) for word in clean_text if word not in set(stopwords.words('english'))]
    clean_text = ' '.join(clean_text)
    return clean_text