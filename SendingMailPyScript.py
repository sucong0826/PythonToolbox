import sys, os, re, urllib
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail_to(subject, msg, to_addrs, from_addr, smtp_addr, pwd):
     mail_msg = MIMEMultipart()

     # if not isinstance(subject, unicode):
     #      subject = unicode(subject, 'utf-8')

     mail_msg['Subject']  = subject
     mail_msg['From']     = from_addr
     mail_msg['To']       = ','.join(to_addrs)

     mail_msg.attach(MIMEText(msg, 'html', 'utf-8'))

     try:
          s = smtplib.SMTP()
          s.connect(smtp_addr)
          s.login(from_addr, pwd)
          s.sendmail(from_addr, to_addrs, mail_msg.as_string())
          s.quit()
     except Exception as e:
          print(traceback.format_exc())
          print("Failed to send this email.")

     if __name__ == '__main__':
          from_addr = "sucong0826@outlook.com"
          smtp_addr = "smtp-mail.outlook.com"
          to_addrs  = ["1508769885@qq.com", "sucong0826@gmail.com"]
          subject   = "Python Script for sending e-mail automatically"
          pwd       = "sucong123456"
          msg       = "Hi, Su\nHow is going recently?"

          send_mail_to(subject, msg, to_addrs, from_addr, smtp_addr, pwd)
