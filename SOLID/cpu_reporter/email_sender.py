import smtplib

gmail_username = 'grigorg25@gmail.com'
password = input()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_username, password)
message = """\
Subject: CPU Report
{}"""


def text_send_email(data):
    server.sendmail(gmail_username, gmail_username, message.format(data))


def chart_send_mail(message):
    message['Subject'] = 'CPU Report'
    message['From'] = gmail_username
    message['To'] = gmail_username

    server.sendmail(gmail_username,gmail_username,message.as_string())