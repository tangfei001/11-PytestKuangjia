**课时141-PYtest测试框架之命令详解1(-)**

01 -V:输出详细的信息

02:-s :输出测试函数或者测试方法里面的print()里面的内容

03:-K:按分类执行测试点(编写的测试用例需要加装饰器@xxxx)@pytest.mark.xxxxx

04:-m :进行分组

代码:

import pytest
@pytest.mark.ui
def test_001():
	pass
@pytest.mark.ui
def test_002():
	print('1')

class TestUI():
	@pytest.mark.login
	def test_ui_01(self):
		pass
	@pytest.mark.login
	def test_ui_02(self):
		pass

if __name__ == '__main__':
    # -v -s
	pytest.main(['-v','-s','test_05.py'])
    #-k 按分类执行测试点(编写的测试用例需要加装饰器@xxxx)@pytest.mark.xxxxx
    pytest.main(['-v','-k','test_05.py'])
    pytest.main(['-v','-k','login','test_05.py'])