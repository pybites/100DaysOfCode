#!python3
#water_reminder.py is a script to email you a reminder to drink water hourly

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email_list import EMAILS

DATA_FILE = 'data'
from_addr = 'your-gmail@gmail.com'
to_addr = EMAILS
msg = MIMEMultipart()
msg['From'] = from_addr
msg['bcc'] = ", ".join(to_addr)
msg['Subject'] = 'DRINK WATER!'

with open(DATA_FILE) as f:
    body = f.read()

msg.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587) #Specify Gmail Mail server

smtp_server.ehlo() #Send mandatory 'hello' message to SMTP server

smtp_server.starttls() #Start TLS Encryption as we're not using SSL.

#Login to gmail: Account | Password
smtp_server.login(' your-gmail@gmail.com ', ' auth-key ')

text = msg.as_string()

#Compile email list: From, To, Email body
smtp_server.sendmail(from_addr, to_addr, text)

#Close connection to SMTP server
smtp_server.quit()

#Test Message to verify all passes
print('Email sent successfully')
