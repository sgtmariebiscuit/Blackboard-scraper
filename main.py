#Python3

from functions import *
from Webdriver_options import *
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_submit = subparsers.add_parser('submit')
parser_submit.add_argument("-url",default="LAB",metavar = "URL", help="Specifies URL to go to, options[LAB,TUT] or enter your own url")
parser_submit.add_argument("-u","--username",metavar="Student number",default= username,help="Specifies username to login with default is set in config.py")
parser_submit.add_argument("-p","--password",metavar="password",default=password, help="Specifies password used to login with default is set in config.py")
parser_submit.add_argument("-d","--driver", metavar= "NUM",default="2",choices=['1','2'],help="Specifies driver with relevant options")
parser_submit.set_defaults(func=Get_upload)

parser_download = subparsers.add_parser('download-latest')
parser_download.add_argument("-url",default="LAB",metavar="URL",help="Specifies URL to go to, options[LAB,TUT] or your own url")
parser_download.add_argument("-P","--path",default=path,metavar="/path/to/folder",help="Specifies path where downloads will be placed,default is set in config.py")
parser_download.add_argument("-u","--username",metavar="Student number",default= username,help="Specifies username to login with default is set in config.py")
parser_download.add_argument("-p","--password",metavar="password",default=password,help="Specifies password used to login with default is set in config.py")
parser_download.add_argument("-d","--driver", metavar= "NUM",default="1",choices=['1','2'],help="Specifies driver with relevant options")
parser_download.set_defaults(func=Dwnld_latest)

parser_download_all = subparsers.add_parser('download-all')
parser_download_all.add_argument("-url",default="LAB",metavar="URL",help="Specifies URL to go to, options[LAB,TUT] or your own url")
parser_download_all.add_argument("-P","--path",default=path,metavar="/path/to/folder",help="Specifies path where downloads will be placed,default is set in config.py")
parser_download_all.add_argument("-u","--username",metavar="Student number",default= username,help="Specifies username to login with default is set in config.py")
parser_download_all.add_argument("-p","--password",metavar="password",default=password,help="Specifies password used to login with default is set in config.py")
parser_download_all.add_argument("-d","--driver", metavar= "NUM",default="1",choices=['1','2'],help="Specifies driver with relevant options")
parser_download_all.set_defaults(func=Dwnld_all)

parser_login = subparsers.add_parser('login')
parser_login.add_argument("-u","--username",metavar="Student number",default= username,help="Specifies username to login with default is set in config.py")
parser_login.add_argument("-p","--password",metavar="password",default=password,help="Specifies password used to login with default is set in config.py")
parser_login.add_argument("-d","--driver", metavar= "NUM",default="2",choices=['1','2'],help="Specifies driver with relevant options" )
parser_login.set_defaults(func=login_BB)

args = parser.parse_args()
args.func(args)


