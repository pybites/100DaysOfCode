#!python3
#ftp_downloader is a script to download a file from a remote ftp server. I use this with a cron job to automate downloading a log file.

from ftplib import FTP

URL = "your_ftp_server_url or IP"
username = 'username'
password = 'password'
filename = 'log.txt'

file = open(filename, 'wb')

with FTP(URL, username, email) as ftp:
    ftp.login(username, password)
	ftp.retrbinary('RETR %s' % filename, file.write)

file.close()