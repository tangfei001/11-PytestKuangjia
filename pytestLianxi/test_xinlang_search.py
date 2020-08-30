#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 9:14
# @Author  : Aries
# @Site    : 
# @File    : test_xinlang_search.py
# @Software: PyCharm
'''
参数化

def add(a,b):
	return a + b

@pytest.mark.parametrize('a,b,result',[(1,2,3),(4,5,6)])

def test_add(a,b,result):
	assert add(a,b) == result
'''
import pytest

def add(a,b):
	return a+b

@pytest.mark.parametrize('a,b,result',[
	(1,1,2),
	(2,2,4),
	(2,3,6)
])

def test_add(a,b,result):
	'''要执行的测试用例'''
	assert add(a,b) == result

if __name__ == '__main__':
    pytest.main(["-v","test_xinlang_search.py","--tb=line"])