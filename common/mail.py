from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import sys


FROM_MAIL = os.environ.get('FROM_MAIL')
TO_MAIL = os.environ.get('TO_MAIL').split()


if not FROM_MAIL or not TO_MAIL:
    print('Please set FROM_MAIL and TO_MAIL env vars')
    sys.exit(1)


def mail_html(subject, content, recipients=TO_MAIL):
    sender = FROM_MAIL
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    part = MIMEText(content, 'html')
    msg.attach(part)
    s = smtplib.SMTP('localhost')
    s.sendmail(sender, recipients, msg.as_string())
    s.quit()
