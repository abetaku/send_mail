# -*- coding: utf-8 -*-

import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

class SendMail:

    def __init__(self, g_ac, g_ps):
        self.gmail_account = g_ac
        self.__gmail_password = g_ps


    def set_config(self,
                   from_addr='',
                   to_addr='',
                   subject='Hi', body='hello world!'):
        self.from_addr = from_addr
        self.to_addr= to_addr
        self.msg = MIMEText(body)
        self.msg['Subject'] = subject
        self.msg['From'] = from_addr
        self.msg['To'] = to_addr
        self.msg['Date'] = formatdate()
        return self.msg

    def send_via_gmail(self):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(self.gmail_account, self.__gmail_password)
        s.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        s.close()

if __name__ == '__main__':

    gm = SendMail('your gmail account','your gmail password')
    
    from_addr = 'hogehoge@gmail.com'
    to_addr = 'hogehoge@gmail.com'
    subject = 'test mail'
    body = 'Hello! This is a test mail.'
    gm.set_config(from_addr=from_addr, to_addr=to_addr, subject=subject, body=body)
    gm.send_via_gmail()


