import sys
import paramiko

host1 = sys.argv[4]
user = sys.argv[1]
password = sys.argv[2]
enable_password = sys.argv[3]

port = 22
#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
#ssh.connect(hostname=host1, username=user, password=password, port=port)
#stdin, stdout, stderr = ssh.exec_command('show clock')
#list = stdout.readlines()
#print(list)

ssh = paramiko.SSHClient()
#ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host1 , port=port, username=user, password=password)
print ("Connected successfully.")
connection = ssh.invoke_shell()
connection.send("enable\n")
time.sleep(.5)
connection.send("cisco\n")
time.sleep(.5)
#connection.send("conf t\n")
connection.send("show ip int brief\n")
#connection.send("int loop 2\n")
#connection.send("ip address 2.3.1.1 255.255.255.255\n")
time.sleep(.5)
router_output = connection.recv(65535000)
time.sleep(.5)
print(str(router_output) + "\n")
time.sleep(.5)
