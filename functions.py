# Python3
# Function file

import geckodriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import requests
import os
from config import *
from Webdriver_options import *


def Start_driver(args):
	geckodriver_autoinstaller.install()
	if (args.driver == "1"):
		options = options_1
	else:
		options = options_2
	driver = webdriver.Firefox(options=options)
	print(f'[!] Started webdriver!')
	return(driver)

def login_BB(args):
	driver = Start_driver(args)
	driver.get(blackboard_login)
	driver.find_element_by_id('username').send_keys(args.username)
	driver.find_element_by_id('password').send_keys(args.password)
	driver.find_element_by_class_name("btn-submit").click()
	print(f'[!] Successfully logged in with [{args.username}] !')
	return(driver)

def Get_content_links(driver):

	href_list = []

	urls = ui.WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

	for url in urls:
        	href = (url.get_attribute("href"))
        	if "bbcswebdav" in href:
                	href_list.append(href)

	print("[!] Successfully retrived all links!")
	return(href_list)


def Dwnld_all(args):
	driver = login_BB(args)
	path = args.path

	if (args.url == "LAB"):
		driver.get(blackboard_DEV_labs)
		prefix = "LAB"
	elif (args.url == "TUT"):
		driver.get(blackboard_DEV_tuts)
		prefix = "TUT"
	else:
		driver.get(args.url)
		prefix = "Document"

	href_list = Get_content_links(driver)
	iterator = 1

	for href in href_list:
		if (os.path.isfile(path+prefix+str(iterator))):
			print(f'[!] Found {prefix} {iterator}! in {path}')
			iterator += 1
			continue
		else:
			driver.get(href)
			r = requests.get(driver.current_url)
			with open(path+prefix+str(iterator), 'wb') as f:
				f.write(r.content)
				f.close()
				print(f'[!] Downloaded {prefix} {iterator} ')
				iterator += 1
	print(f'[!] Successfully updated database with {iterator - 1} {prefix}s!\n[!] Output in {path}')
	driver.quit()
	return

def Dwnld_latest(args):
	driver = login_BB(args)
	path = args.path

	if (args.url == "LAB"):
		driver.get(blackboard_DEV_labs)
		prefix = "LAB"
	elif (args.url == "TUT"):
		driver.get(blackboard_DEV_tuts)
		prefix = "TUT"
	else:
		driver.get(args.url)
		prefix = "Document"


	href_list = Get_content_links(driver)


	driver.get(href_list[(len(href_list)) - 1])
	r = requests.get(driver.current_url)
	with open(path+prefix+str("_Latest"), 'wb') as f:
        	f.write(r.content)
        	f.close()

	print(f'[!] Pulled latest {prefix}')
	print(f'[!] Output in {path}')
	driver.quit()
	return

def Get_upload(args):
	driver = login_BB(args)

	if (args.url == "TUT"):
		driver.get(blackboard_DEV_Submission_tuts)
	elif(args.url == "LAB"):
		driver.get(blackboard_DEV_Submission_labs)
	else:
		driver.get(args.url)


	href_list = []
	urls = ui.WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

	for url in urls:
        	href = (url.get_attribute("href"))
        	if "assignment" in href:
                	href_list.append(href)

	print("[!] Successfully retrived all links!")

	if (href_list == [] and  args.driver == "2"):
		print("[!] Found no submission link, retry later!")
	elif (args.driver == "2" and  len(href_list) >= 1 ):
		print("[!] Found submission link!")
		driver.get(href_list[0])
	elif (href_list == [] and args.driver == "1"):
		print("[!] Found no submission link, retry later!")
		driver.quit()
	elif (args.driver == "1" and len(href_list) >= 1):
		print("[!] Found submission link!")
		driver.quit()
	else:
		print("[!] Something went wrong")
	return
