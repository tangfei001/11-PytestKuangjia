#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 9:12
# @Author  : Aries
# @Site    : 
# @File    : test_login.py
# @Software: PyCharm
'''
将函数试和类式进行整合
'''
import pytest

def test_login_001():
	'''第一个测试用例'''
	print('001')

def test_login_002():
	'''第二个测试用例'''
	print('002')

class TestBaiduSearch():
	'''要执行的测试类'''
	def test_baidusearch_001(self):
		'''第三个测试用例'''
		print('003')
	def test_baidusearch_002(self):
		'''第四个测试用例'''
		print('004')

if __name__ == '__main__':
    pytest.main(['-v','test_login.py','--tb=line'])