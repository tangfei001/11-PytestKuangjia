**课时138-Pytest测试框架之执行规则**


'''
在pytest测试框架中,他的搜索规则是
01:在一个被执行的目录下,寻找以test开头或者以test结尾的测试模块
02:然后执行以test开头或者以test结尾的测试方法或者测试函数
'''

代码演示
import pytest

#创建一个函数--函数名 test_xxx()
def test_001():
	print('我是面向编程')

#创建一个类 类名叫 TestF1():
class TestF1():
	#在测试类中创建一个函数  test_002()
	def test_002(self):
		print('我是面向对象编程')

#主函数
if __name__ == '__main__':
    #执行的规则是  pytest.main(['-v','xxxx'])  测试模块
	pytest.main(['-v','test_pytest_001.py'])

在命令行模式中: pytest -v test_pytest_002.py