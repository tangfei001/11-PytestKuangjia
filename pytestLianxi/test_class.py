#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 9:12
# @Author  : Aries
# @Site    : 
# @File    : test_class.py
# @Software: PyCharm
'''
类式编程
'''
import pytest

class TestLogin():
	'''要执行的测试用例'''
	def test_login_001(self):
		'''第一个测试用例'''
		print('001')
	def test_login_002(self):
		'''第二个测试用例'''
		print('002')

class TestSearch():
	'''要执行的测试类'''
	def test_search_001(self):
		'''第三个测试用例'''
		print('003')
	def test_search_002(self):
		'''第四个测试用例'''
		print('004')

if __name__ == '__main__':
    pytest.main(['-v','test_class.py','--tb=line'])