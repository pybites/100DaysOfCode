#!python3
#A simple script to pull a log file from a remote host

import paramiko
from scp import SCPClient

username = ''
password = ''
host = ''

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=username, password=password)

with SCPClient(ssh.get_transport()) as scp:
    scp.get("/var/log/messages")
