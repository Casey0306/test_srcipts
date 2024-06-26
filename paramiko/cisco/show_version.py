import paramiko
import sys
import time


ip_address = sys.argv[4]
username = sys.argv[1]
password = sys.argv[2]
enable_password =  sys.argv[3]

print(ip_address)
print(type(ip_address))
print(username)
print(type(username))
print(password)
print(type(password))
print(enable_password)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip_address, username=username, password=password, look_for_keys=False)

command = "show version"
stdin, stdout, stderr = client.exec_command(command)
stdin.close()
output = stdout.read().decode()
time.sleep(60)
print(output)

client.close()
