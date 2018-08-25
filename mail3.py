# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header



def notify_error(info):
    '''
    
    '''
    mail_conf = {
    'smtp_host': 'smtp.exmail.qq.com',
    'sender': 'tools@chainup.com',
    'receiver': 'zhanxueyou@chainup.com',
    'user': 'tools@chainup.com',
    'password': '23BejmSZBSwHx2vA',
    'port': 465
    }

    subject = '验证测试错误'
    msg = MIMEText(info, 'text', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    # smtp.connect(mail_conf['smtp_host'], mail_conf['port'])
    smtp.connect(mail_conf['smtp_host'])    # 不需要端口就能连接
    smtp.login(mail_conf['user'], mail_conf['password'])
    smtp.sendmail(mail_conf['sender'], mail_conf['receiver'], msg.as_string())
    smtp.quit()

