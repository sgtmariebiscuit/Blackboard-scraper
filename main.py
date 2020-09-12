#Python3

from functions import *
from Webdriver_options import *
import argparse

path = "/home/suhail/Downloads/"
parser = argparse.ArgumentParser()
parser.add_argument("-DL" , "--Download_latest",action="store_true",help="Downloads the latest lab into specified folder")
parser.add_argument("-S","--Submit",action="store_true",help="Opens the submission link for specified course")
parser.add_argument("-DA", "--Download_all",action="store_true",help="Downloads all files of specified course into specified folder")
parser.add_argument("-L","--Login",action="store_true",help="Logs into account")
args = parser.parse_args()


if args.Download_latest:
	try:
		driver = Start_driver(options_1)
		Dwnld_latest(driver,path)
	except KeyboardInterrupt:
		print("[!] Standby, quitting!")
		driver.quit()

if args.Submit:
	try:
		Get_upload()
	except KeyboardInterrupt:
		print("[!] Standby, quitting!")
		driver.close()
		driver.quit()

if args.Download_all:
	try:
		driver = Start_driver(options_1)
		Dwnld_all(driver,path)
	except KeyboardInterrupt:
		print("[!] Standby,quitting!")
		driver.close()
		driver.quit()
if args.Login:
	try:
		driver = Start_driver(options_2)
		login_BB(driver)
	except KeyboardInterrupt:
		print("[!] Standby, quitting!")
		driver.close()
		driver.quit()







