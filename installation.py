# python3

# Used to help user install package
import sys
import subprocess
import pkg_resources
import time
from os import system, name 


requirements_list = []


def Remove_chars (string):

	ret_string = []
	for char in string:
		if ( char == "="):
			break
		else:
			ret_string.append(char)
	result = ''.join(ret_string)
	return result

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 

print("This program is used to help user install the program\nNOTE** your password will be saved in clear text in config.py, I am currently working on a way to hash the password but as of right now, it is not.")



while True:
	usr_input = str(input("Would you like to continue? [y/n]: "))

	if (usr_input == "y"):
		clear()
		print("[!] Starting module check!")
		break
	elif (usr_input == "n"):
		print("Quitting!")
		quit()
	else:
		print(f'Invalid input of {usr_input}')
		continue

f = open("requirements.txt","r")
requirements = f.readlines()
for r in requirements:
	r1 = Remove_chars(r)
	requirements_list.append(r1)

installed = [pkg.key for pkg in pkg_resources.working_set]
set_difference = set(requirements_list) - set(installed)
list_difference = list(set_difference)

if (list_difference == []):
	print("[!] No modules missing")
else:
	for packages in list_difference:
		print(f'[-] module [{packages}] not found!')
		while (True):
			usr_input = str(input(f'[!] Would you like to install {packages} [y/n]: '))

			if (usr_input == "y"):
				print(f"[!] Installing {packages}")
				python = sys.executable
				subprocess.check_call([python, '-m', 'pip', 'install', packages], stdout=subprocess.DEVNULL)
				print(f"[!] Installed {packages}")
				break
			elif (usr_input == "n"):
				print("[!] Skipping")
				break
			else:
				print(f'Invalid input of {usr_input}')
time.sleep(2)

clear()
print("[!] Module check completed!")
print("[!] Would you like to add your username and password to the configuration file for ease of usage?\n**Note if you are worried about saving your password skip this step")

while True:
	usr_input = str(input("Continue? [y/n]: "))

	if (usr_input == "y"):
		clear()
		print("[!] Starting default configuration set-up")

		username = input("Enter your student number: ")
		password = input("Enter your password (used to log into ulink): ")
		path = input("Enter your default directory for downloads (End with a / or \\ please): ")


		f = open("config.py", "r")
		string_list = f.readlines()
		f.close()

		num_lines = len(string_list)
		string_list[num_lines - 3] = (f"path = '{path}'\n")
		string_list[num_lines - 2] = (f"username = '{username}'\n")
		string_list[num_lines - 1] = (f"password = '{password}'\n")

		f = open("config.py","w")
		lines = "".join(string_list)
		f.write(lines)
		f.close
		print(f"[!] Set default settings for {username}!")
		print("[!] Installation complete,quitting!")
		quit()
		break
	elif (usr_input == "n"):
		clear()
		print("[!] Installation complete,quitting!")
		quit()
	else:
		print(f'Invalid input of {usr_input}')
		continue


