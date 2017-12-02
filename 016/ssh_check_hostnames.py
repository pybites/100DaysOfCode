import paramiko
from contextlib import contextmanager

from hosts import HOSTS

username = ''
password = ''
host_list = HOSTS

#@contextmanager
def check_hostname(host_list):
    for host in host_list:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=username, password=password)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cat /etc/hostname')
            yield ssh_stdout.readlines()
        finally:
            ssh.close()

gen = check_hostname(host_list)

for i in host_list:
    print(next(gen))
    print('Hit Enter to try the next host.'); input()
