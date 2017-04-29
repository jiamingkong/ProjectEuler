# -*- coding: utf-8 -*-


import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


EMAIL_SETTING = {
    "RECIPIENTS": ["kinetical@163.com"],
    "SENDER": ("kinetical@163.com", "kinetical@163.com"),
    "PASSWORD": "628stream",
    "SITE": "smtp.163.com",
    "PORT": 994
}


def get_email_connection():
    session = smtplib.SMTP(EMAIL_SETTING["SITE"], EMAIL_SETTING["PORT"])
    session.starttls()
    session.login(EMAIL_SETTING["SENDER"][0], EMAIL_SETTING["PASSWORD"])
    return session


def close_email_connection(session):
    session.quit()
    del session


def send_email(session, msg):
    session.sendmail(
        EMAIL_SETTING["SENDER"][0], EMAIL_SETTING["RECIPIENTS"], msg.as_string())
    return True


def compose_control_email(answer):
    author = formataddr(
        (str(Header(u'Ala艂', 'utf-8')), "kinetical@163.com"))
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Answer"
    msg['From'] = author
    msg["To"] = ", ".join(EMAIL_SETTING["RECIPIENTS"])
    text = answer
    body_part = MIMEText(text)
    msg.attach(body_part)
    return msg


if __name__ == '__main__':
    session = get_email_connection()
    send_email(session, compose_control_email(30))
    close_email_connection(session)
