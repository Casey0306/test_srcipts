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
if ip_address == "10.219.2.57":
    neighbor = "neighbor 1.1.1.57 remote-as 10"
if ip_address == "10.219.2.158":
    neighbor = "neighbor 1.1.1.158 remote-as 10"

commands = ["router bgp 2000", neighbor]
with ConnectHandler(**cisco) as net_connect:
  net_connect.enable()
  output = net_connect.send_command("show run")
  output += net_connect.send_command("show interfaces")
  output += net_connect.send_config_set(commands)
  output += net_connect.save_config()

print(output)
