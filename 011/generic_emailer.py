#!python3
#emailer.py is a simple script for sending emails using smtplib
#The idea is to assign a web-scraped file to the DATA_FILE constant.
#The data in the file is then read in and sent as the body of the email.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email_list import EMAILS

DATA_FILE = 'data.txt'
from_addr = 'your_email@gmail.com'
to_addr = 'some_recipient@gmail.com'
bcc = EMAILS

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'My Subject Line'

with open(DATA_FILE) as f:
    body = f.read()

msg.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587) #Specify Gmail Mail server

smtp_server.ehlo() #Send mandatory 'hello' message to SMTP server

smtp_server.starttls() #Start TLS Encryption as we're not using SSL.

#Login to gmail: Account | Password
smtp_server.login(' your_email@gmail.com ', ' GMAIL APPLICATION ID ')

text = msg.as_string()

#Compile email list: From, To, Email body
smtp_server.sendmail(from_addr, [to_addr] + bcc, text)

#Close connection to SMTP server
smtp_server.quit()

#Test Message to verify all passes
print('Email sent successfully')