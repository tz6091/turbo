# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:41:51 2017
带噪声的曲线拟合
@author: tz
"""
import numpy as np 
from scipy.optimize import leastsq 
import pylab as pl 
  
def func(x, p): 
    ''' 
    数据拟合所需要的函数 
    A*sin(2*K*np.pi*x + theta) 
    '''
    A, k, theta = p 
    return A*np.sin(2*k*np.pi*x + theta) 
  
def residuals(p , y, x): 
    ''' 
    实验数据和拟合函数之差，p为拟合需要的参数 
    '''
    return (y-func(x, p)) 
      
x = np.linspace(0, -2*np.pi, 100) 
A, k, theta = 10, 0.34, np.pi/6  # 真实数据的函数参数 
y0 = func(x, [A, k, theta])  # 真实数据 
y1 = y0 + 2 * np.random.randn(len(x))  # 加入噪声之后的数据 
  
p0 = [7, 0.2, 0]  # 第一次猜测的函数拟合函数 
# 调用leastsq进行数据拟合 
# residuals为计算误差的函数 
# p0为拟合参数的初始值 
# args为需要拟合的实验数据 
plsq = leastsq(residuals, p0, args=(y1, x)) 
print("Real-->", [A, k, theta]) 
print("Curfit-->", plsq[0]) 
  
pl.plot(x, y0, label = "real data") 
pl.plot(x, y1, label = "test data") 
pl.plot(x, func(x, plsq[0]), label = "CurFit") 
pl.legend() 
pl.show() 
