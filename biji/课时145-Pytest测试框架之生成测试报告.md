课时145-如何生成测试报告

# 配置allure和安装allure-pytest #

01:配置环境变量allure

02:安装 pip install allure-pytest


## 生成HTML报告的过程 ##

第一步:  import allure


第二步:主函数中
	if __name__ == '__main__':
	pytest.main(["-s", "-v", "test_login_token_book.py", "--alluredir", "./report/result"])
	import subprocess
	subprocess.call('allure generate report/result/ -o report/html --clean', shell=True)
	subprocess.call('allure open -h 127.0.0.1 -p  8088 ./report/html', shell=True)

第三步:自动生成测试报告进行查看