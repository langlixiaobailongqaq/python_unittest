# coding:utf-8    # 强制编码为utf-8

import smtplib                        # 发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header       # 定义邮件标题


# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "xxx@qq.com"  # 用户名
mail_pass = "vocanmhcyywgjgdf"  # 口令

sender = 'xxx@qq.com'      # 发送邮箱
receivers = ['xxx@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# 发送邮件主题和内容
subject = 'Python SMTP 邮件测试'
content = '<html><h1 style = "color:red">Python 邮件发送测试...</h1></html>'


# HTML邮件正文
message = MIMEText(content, 'html', 'utf-8')   # 内容
message['Subject'] = Header(subject, 'utf-8')   # 主题
message['From'] = Header("浪里小白龙", 'utf-8')  # 发送人
message['To'] = Header("浪里小白龙", 'utf-8')         # 收件人

# message['From'] = "xxx@qq.com"
# message['To'] = "xxx@qq.com"
try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
	smtpObj.login(mail_user, mail_pass)      # 用户名密码验证
	smtpObj.sendmail(sender, receivers, message.as_string())
	print("邮件发送成功")
except smtplib.SMTPException:
	print("Error: 无法发送邮件")