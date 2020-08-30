**课时140-Pytest测试框架之断言详解**

格式:assert xxxxx

常用断言:

01 == :内容与类型必须同时满足

02 in : 后者包含前者

03 is : 前后两个值相等

代码:
import pytest

#验证断言 ==
def add(a,b):
	return a+b
def test_001():
	assert add(1,2)==3

#验证断言 in
str1='admin'
def test_002():
	assert 'a'in str1

#验证断言 is
str2='tangfei'
str3='tangfei'
def test_003():
	assert str2 is str3

if __name__ == '__main__':
    pytest.main(['-v','test_04.py'])