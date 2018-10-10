from email.mime.text import MIMEText
from email.header import Header
import smtplib

msg = MIMEText('Python send mail test\n','plain','utf8')
msg['From'] = Header('root','utf8')
msg['To'] = Header('zhangsan11','utf8')
msg['Subject'] =Header('py main test','utf8')
sender = 'root'
receivers = ['zhangsan','lisi']
smtp_obj = smtplib.SMTP('localhost')
smtp_obj.sendmail(sender,receivers,msg.as_string())
