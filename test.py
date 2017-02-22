# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 20:39:26 2017

@author: tz
"""
import pandas as pd
data = pd.read_csv('test.csv',nrows = 5)

print data

print 'hehe'
data.to_csv('newOutFile.csv')
