#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 9:12
# @Author  : Aries
# @Site    : 
# @File    : test_def.py
# @Software: PyCharm
'''
函数试
'''
import pytest

def test_001():
	'''第一个测试用例'''
	print('001')

def test_002():
	'''第二个测试用例'''
	print('002')

def test_003():
	'''第三个测试用例'''
	print('003')

def test_004():
	'''第四个测试用例'''
	print('004')

if __name__ == '__main__':
    pytest.main(['-v','test_def.py','--tb=line'])