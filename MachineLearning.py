# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:36:21 2017

@author: tz
"""

from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()
#print(digits.data)
#print(digits)

from sklearn import linear_model
clf = linear_model.LinearRegression()
X = [[0,0],[1,1],[2,2]]
y = [0,1,2]
clf.fit(X,y)
print(clf.coef_)  #存放相关系数
print(clf.intercept_)  #是否存在截距，默认存在


