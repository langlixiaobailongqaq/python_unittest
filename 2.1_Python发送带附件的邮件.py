#!/usr/bin/python3

import smtplib                                 # 发送邮件模块
from email.mime.text import MIMEText            # 发送正文只包含简单文本的邮件，引入MIMEText即可
from email.mime.multipart import MIMEMultipart
from email.header import Header                 # 用来设置邮件头和邮件主题

sender = 'xx@qq.com '
receivers = ['xx@qq.com ']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# 所使用的用来发送邮件的SMTP服务器
smtpServer = 'smtp.qq.com'

# 发送邮箱的用户名和授权码（不是登录邮箱的密码）
username = 'xx@qq.com '
password = 'vocanmhcyywgjgdf'


# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
message.attach(att2)



try:
	smtpObj = smtplib.SMTP()       # 创建一个连接
	smtpObj.connect(smtpServer)  # 连接发送邮件的服务器
	smtpObj.login(username, password)  # 登录服务器
	smtpObj.sendmail(sender, receivers, message.as_string())   # 填入邮件的相关信息并发送
	print("邮件发送成功")
except smtplib.SMTPException:
	print("Error: 无法发送邮件")