from netmiko import ConnectHandler
import sys
import time


ip_address = sys.argv[4]
username = sys.argv[1]
password = sys.argv[2]
enable_password =  sys.argv[3]

cisco = {
    "device_type": "cisco_ios",
    "host": ip_address,
    "username": username,
    "password": password,
    "secret": enable_password,
}

with ConnectHandler(**cisco) as net_connect:
  net_connect.enable()
  output1 = net_connect.send_command("show run")
  output2 = net_connect.send_command("show interfaces")

print(output1)
print(output2)
