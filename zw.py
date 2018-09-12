#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re
import os

def parsing_file(f):
    read= f.readlines()
    word = []  # 存储单词,得到文章的单词并且存入列表中：
    chars=0
    lines=0
    space_lines=0#空行
    code_lines=0#代码行
    comment_lines=0#注释行
    is_comment = False
    start_comment_line = 0  # 记录以'''或"""开头的注释位置
    for line in read:
        chars+=len(line)
        lines+=1
        line = line.strip()
        if not is_comment:
            if line.startswith("'''") or line.startswith('"""'):
                is_comment = True
                start_comment_line = lines
            # 单行注释
            elif line.startswith('#'):
                comment_lines += 1
            # 空白行
            elif len(line)<=1:
                space_lines += 1
            # 代码行
            else:
                code_lines += 1
            # 多行注释已经开始
        else:
            if line.endswith("'''") or line.endswith('"""'):
                is_comment = False
                comment_lines += lines - start_comment_line + 1
            else:
                pass
        line = re.sub(r'[^0-9a-zA-Z\u4E00-\u9FFF]+',' ',line) # 用空格代替一串非数字和字母
        line = line.strip()  # 除去左右的空格,不能删除中间的。
        wo = line.split(' ')# 空格分割单词
        word.extend(wo)  # 该方法没有返回值，但会在已存在的列表中添加新的列表内容。
    return len(word),chars,lines,space_lines,code_lines,comment_lines

def command(str,name):
    f = open(name,"r")
    word,chars,lines,space_lines,code_lines,comment_lines= parsing_file(f)
    if  str=='-c':
        print('字符数',chars)
    elif str=='-w':
        print('单词数',word)
    elif str=='-l':
        print('行数',lines)
    elif str=='-s':
        eachFile(name)
    elif str=='-a':
        print('空格行',space_lines)
        print('代码行',code_lines)
        print('注释行',comment_lines)
    elif str=='-q':#读取全部信息
        print('字符数', chars)
        print('单词数', word)
        print('行数', lines)
        print('空格行', space_lines)
        print('代码行', code_lines)
        print('注释行', comment_lines)

def eachFile(path):
    pathDir = os.listdir(path)  # 获取当前路径下的文件名，返回List
    for s in pathDir:
        newDir = os.path.join(path, s)  # 将文件命加入到当前文件路径后面
        if os.path.isfile(newDir):  # 如果是文件
            command('-q', newDir)  # 读文件
        else:
            eachFile(newDir)  # 如果不是文件，递归这个文件夹的路径
        #C:\\Users\\ZW\\Desktop\\qaq.java