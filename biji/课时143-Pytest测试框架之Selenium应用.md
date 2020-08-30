**课时143-Pytest测试框架之Selenium应用**

pytest与webdriver的应用

pip3 install pytest-selenium



说明:

1:安装pytest-selenium
2:def baidu_spoud_001(selenium): 每一个函数中都有参数selenium


需要安装chromedriver.exe

注意:
01:必须和浏览器的版本要匹配
02:放到python的安装目录中

案例:

import pytest

def test_baidu(selenium):
	'''百度的title'''
	selenium.get('htty:www.baidu.com')
	assert selenium.title =="百度一下"

if __name__ == '__main__':
    xxxxx
