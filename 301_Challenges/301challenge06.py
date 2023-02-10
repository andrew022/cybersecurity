import os

define_user = os.system("whoami")
define_ip = os.system("ip a")
define_hardware = os.system ("lshw -short")

print("Result of whoami")
print(define_user.read())

print("Result of ip a")
print(define_ip.read())

print("Result of hardware")
print(define_hardware.read())