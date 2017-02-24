# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:02:19 2017
运行命令
%run sys_test.py dfa dd

@author: tz
"""

import sys

print('the first  argv: ',len(sys.argv),'\n')#显示第一个参数
im, wd = sys.argv[1], '.' if len(sys.argv) < 3 else sys.argv[2]
print(im,wd)

print('the first  argv: ',sys.argv[0],'\n')#显示第一个参数
print('the second argv: ',sys.argv[1],'\n')#显示第二个参数
print('the third  argv: ',sys.argv[2],'\n')#显示第三个参数，以此类推
