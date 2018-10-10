from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def send_mail(server,user,pwd,sender,receviers,msg):
    smtp_obj = smtplib.SMTP()
    smtp_obj.connect(server,25)
    smtp_obj.login(user,pwd)
    smtp_obj.sendmail(sender, receivers, msg.as_string())

if __name__ == '__main__':

    msg = MIMEText('python test\n','plain','utf8')
    # msg['From'] = Header('liyl0663@163.com','utf8')
    # msg['To'] = Header('Zhanbin_Wu@163.com','utf8')
    msg['From'] = 'liyl0663@163.com'
    msg['To'] = '453503078@qq.com'
    msg['Subject'] =Header('hui yi','utf8')
    sender = 'liyl0663@163.com'
    receivers = ['453503078@qq.com']
    passwd = getpass.getpass()
    mail = send_mail('smtp.163.com',sender,passwd,sender,receivers,msg)
    print(mail)
    if mail:
        print('send sucessful')
