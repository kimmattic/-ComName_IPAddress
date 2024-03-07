'''
หาชื่อ Computer Name และ IP Address
'''
import socket as sc

my_hostname = sc.gethostname()
# Display my hostname
print("ชื่อเครื่องคอมของคุณคือ : " + my_hostname)

my_ip = sc.gethostbyname(my_hostname)
print("IP Address ที่คุณใช้งานคือ: " + my_ip)
