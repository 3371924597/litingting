#coding:utf-8
import smtplib
from email.mime.text import MIMEText
msg_from='3371624597@qq.com'
passwd='abvghbwvnpttcjbb'
msg_to='57820048@qq.com'
subject="20191441Today-TEST"
content="2019144110 李婷婷一.连接校园网 手机IP:10.101.102.196, 查看IP:220.164.161.126,二.切换至数据 手机IP:10.229.58.52,   查看IP:172.68.142.103"
msg=MIMEText(content)
msg['Subject']=subject
msg['From']=msg_from
msg['To']=msg_to
try:
    s=smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from,passwd)
    s.sendmail(msg_from,msg_to,msg.as_string())
    print("发送成功")
except(s.SMTPException,e):
    print("发送失败")
finally:
    s.quit()
