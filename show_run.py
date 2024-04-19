import sys
import paramiko

host1 = sys.argv[4]
user = sys.argv[1]
password = sys.argv[2]
enable_password = sys.argv[3]

port = 22
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
ssh.connect(hostname=host1, username=user, password=password, port=port)
stdin, stdout, stderr = ssh.exec_command('show clock')
list = stdout.readlines()
print(list)
