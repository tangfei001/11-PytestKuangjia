#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 9:15
# @Author  : Aries
# @Site    : 
# @File    : test_login_html.py
# @Software: PyCharm
'''
生成测试报告
'''
import pytest
import allure

def add(a,b):
	return a+b

def test_001():
	'''第一个测试用例'''
	assert add(1,4) == 5

class TestLogin():
	'''要执行的测试类'''
	def test_002(self):
		'''第二个测试用例'''
		str1='tangfei'
		str2='tangfeiwuya'
		assert str1 in str2

	def test_003(self):
		'''第三个测试用例'''
		a=1
		b='1'
		assert a is b

def test_004():
	'''第四个测试用例'''
	assert add(2,5) == 8

if __name__ == '__main__':
    pytest.main(["-v","test_login_html.py","--tb=line","--alluredir", "./report/result"])
    import subprocess
    subprocess.call('allure generate report/result/ -o report/html --clean', shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p  8088 ./report/html', shell=True)

