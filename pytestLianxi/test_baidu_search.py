#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 9:14
# @Author  : Aries
# @Site    : 
# @File    : test_baidu_search.py
# @Software: PyCharm
'''
命令的验证
'''
import pytest

def add(a,b):
	return a+b

def add2(c,d):
	return c+d

@pytest.mark.login
def test_001():
	'''第一个测试用例--通过'''
	assert add(1,2)==3
	print('001')

class TestLogin():
	'''要执行的测试类'''

	@pytest.mark.ui
	def test_002(self):
		'''第二个测试用例--不通过'''
		str1='tangfei'
		str2='wuya'
		assert str1 in str2
		print('002')

	@pytest.mark.ui
	def test_003(self):
		'''第三个测试用例--通过'''
		assert add(2,3) is add2(0,5)
		print('003')
@pytest.mark.tangfei
def test_004():
	'''第四个测试用例-不通过'''
	assert add2(5,6)==10
	print('004')

class TestSearch():
	'''要执行的测试类--通过'''

	@pytest.mark.wuya
	def test_005(self):
		'''第五个测试用例'''
		assert 'tangfei' == 'tangfei'
		print('005')

	@pytest.mark.wuya
	def test_006(self):
		'''第六个测试用例-不通过'''
		assert 4 is '4'
		print('006')

if __name__ == '__main__':
    #pytest.main(["-v",'test_baidu_search.py','--tb=line'])
    #pytest.main(["-v","-k","tangfei","test_baidu_search.py"])
    #pytest.main(["-v","--maxfail=2","test_baidu_search.py" ])
	pytest.main(["-v","-s","test_baidu_search.py","--tb=line"])

