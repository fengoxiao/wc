#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re
a,b=0,0
s = input('输入一串字符：')
if s == '[^0-9a-zA-Z]?':
    a += 1
elif s == '^\#|^\/':
    b += 1
s= re.sub(r'[^0-9a-zA-Z\u4E00-\u9FFF]+',' ',s)
s = s.strip()  # 除去左右的空格,不能删除中间的。
fsf= s.split(' ')# 用一个或连续的空格分割单词
print(fsf,a,b)


'''
#def collect_file(s):
s = input('输入一串字符：')
char = re.findall(r'[a-zA-Z]', s)
num = re.findall(r'[0-9]', s)
blank = re.findall(r' ', s)
chi = re.findall(r'[\u4E00-\u9FFF]', s) # \u4E00-\u9FFF是中文的范围
other = len(s) - len(char) - len(num) - len(blank) - len(chi)
print("字母：", len(char), "\n数字：", len(num), "\n空格：", len(blank), "\n中文：", len(chi), "\n其他：", other)
'''