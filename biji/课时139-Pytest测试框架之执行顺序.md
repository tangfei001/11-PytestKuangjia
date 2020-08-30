**课时139-Pytest测试框架之执行顺序**

import pytest

def test_b():
	print('1')

def test_a():
	print('2')

def test_c():
	print('3')

if __name__ == '__main__':
    pytest.main(['-v','test_pytest_003.py'])