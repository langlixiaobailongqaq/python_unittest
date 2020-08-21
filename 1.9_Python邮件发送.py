"""
	Python邮件发送
		SMTP(Simple Mail Transfer Protocol):
			即简单邮件传输协议。它是一组用于从源地址到目的地址传输邮件的规范，通过它来控制邮件额中转方式。SMTP协议属于TCP/IP
				协议簇，它帮助每台计算机在发送中转信件时找到下一个目的地。SMTP服务器就是遵循SMTOP协议的发送邮件服务器.

		SMTP认证：
			SMTP认证，简单地说就是要求必须在提供了账号和密码之后才可以登录SMTP服务器，这就使得那些垃圾邮件的散播者无可乘之机.
			增加SMTP认证的目的是为了使用户避免受到垃圾邮件的侵扰.

		更多资料：http://help.163.com/09/1223/14/5R7P6CJ600753VB8.html

	smtplib模块:
		Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件.
		Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发生邮件.

		注意：使用前需开启SMTP服务
		案例：使用163邮箱来结合smtp模块发送邮件
"""

import smtplib                        # 发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header       # 定义邮件标题


# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "xx@qq.com"  # 用户名
mail_pass = "vocanmhcyywgjgdf"  # 口令

sender = 'xx@qq.com'      # 发送邮箱
receivers = ['xx@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# 发送邮件主题和内容
subject = 'Python SMTP 邮件测试'
content = '<html><h1 style = "color:red">Python 邮件发送测试...</h1></html>'

# HTML邮件正文
message = MIMEText(content, 'html', 'utf-8')   # 内容
message['Subject'] = Header(subject, 'utf-8')   # 主题
# message['From'] = Header("菜鸟教程", 'utf-8')  # 发送人
# message['To'] = Header("测试", 'utf-8')         # 收件人

message['From'] = "xx@qq.com"
message['To'] = "xx@qq.com"
try:
	smtpObj = smtplib.SMTP()          # 创建一个连接
	smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
	smtpObj.login(mail_user, mail_pass)      # 用户名密码验证
	smtpObj.sendmail(sender, receivers, message.as_string())   # 填入邮件的相关信息并发送
	print("邮件发送成功")
except smtplib.SMTPException:
	print("Error: 无法发送邮件")