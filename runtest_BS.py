
import unittest
from BSTestRunner import BSTestRunner
import time

# 定义测试用例路径
test_dir = "./test_case"
discovery = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

if __name__ == '__main__':
	# 存放报告的文件夹
	report_dir = "./test_report"
	# 报告命名时间格式化
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	# 报告文件完整路径
	report_name = report_dir + "/" + now + "result.html"

	# 打开文件再报告文件写入测试结果
	with open(report_name, "wb") as f:  # wb 表示以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件；如果文件已存在，则覆盖写
		runner = BSTestRunner(stream=f, title="测试报告", description="百度搜索")
		runner.run(discovery)

	# f = open(report_name, "wb")
	# f.write("hello world".encode("utf-8"))
	# print(f)
	f.close()