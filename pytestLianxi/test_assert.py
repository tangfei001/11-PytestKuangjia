#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 9:13
# @Author  : Aries
# @Site    : 
# @File    : test_assert.py
# @Software: PyCharm
'''
常用断言:
01 == :内容与类型必须同时满足
02 in : 后者包含前者
03 is : 前后两个值相等
'''
import pytest

#验证断言 ==
def add(a,b):
	return a+b

def test_add():
	'''验证断言==的过程'''
	assert add(1,2)==3

#验证断言 in
def test_assertIn():
	'''验证断言in的实现过程'''
	str1='tangfei'
	str2='tangfeiwuya'
	assert str1 in str2

#验证断言is

def add2(c,d):
	return c+d

def add3(e,f):
	return e+f

def test_assertIs():
	'''验证断言is的实现过程'''
	assert add2(2,4) is add3(3,5)

if __name__ == '__main__':
    pytest.main(["-v",'test_assert.py','--tb=line'])



