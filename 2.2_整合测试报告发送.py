"""
整合测试报告发送:
	案例：获取...\test_report\目录下最新的测试报告
	latest_report.py

	Python os模块相关知识：http:www.cnblogs.com/MnCu8261/p/5483657.html
	lambda介绍：http://cnblogs.com/evening/archive/2012/03/29/2423554.html

"""

import os   # 用户访问操作系统功能的模块
import unittest
from BSTestRunner import BSTestRunner  # 测试报告模板
import time
import smtplib                          # SMTP邮件
from email.mime.text import MIMEText    # 发送正文只包含简单文本的邮件，引入MIMEText即可
from email.header import Header         # 用来设置邮件头和邮件主题


# 报告存放的位置
report_dir = r"./test_report"

# os.listdir() 方法用户返回指定的文件夹包含的文件或文件夹的名字的列表
lists = os.listdir(report_dir)

# 按时间顺序对改目录文件夹下面的文件进行排序
lists.sort(key=lambda fn: os.path.getatime(report_dir+"\\"+fn))
print(lists)
print("latest report is :"+lists[-1])

# 输出最新报告的路径
file = os.path.join(report_dir, lists[-1])