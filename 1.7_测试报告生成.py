"""
	测试报告生成:
		HTMLTestRunner模块可以直接生成Html格式的报告;
		下载地址：http://tungwaiyip.info/software/HTMLTestRunner.py
	下载后的修改(HTMLTestRunner是基于py2写的):
		1.  94行引入的名称，从import StringIO 改成 import io
		2.  539行 self.outputBuffer = StringIO.StringIO() 改成 self.outputBuffer = io.StringIO()
		3.  631行 print >>sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime)改成
					print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime))
		4.  642行  if not rmap.has_key(cls): 改成      if not cls in rmap:
		5.  766行   uo = o.decode('latin-1') 改成  uo = o
		6.  772行   ue = e.decode('latin-1') 改成  ue = e

	存放路径：
		将修改完成的模板存放在Python路径下Lib目录里面
"""


import unittest
from HTMLTestRunner import HTMLTestRunner
import time


# 定义测试用例路径
test_dir = "./test_case"
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test* .py")

if __name__ == '__main__':
	# 存放报告的文件夹
	report_dir = "./test_report"
	# 报告命名时间格式化
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	# 报告文件完整路径
	report_name = report_dir + "/" + now + "result.html"

# 打开文件再报告文件写入测试结果
with open(report_name, "wb") as f:
	runer = HTMLTestRunner(stream=f, title="Test Report", description="Test case result")
	runer.run(discover)
	f.close()

