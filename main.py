#Python3

from functions import *
from Webdriver_options import *
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_submit = subparsers.add_parser('submit')
parser_submit.add_argument("-u",default="LAB",metavar = "URL", help="Specifies URL to go to, options[LAB,TUT] or enter your own url")
parser_submit.set_defaults(func=Get_upload)
args = parser.parse_args()
args.func(args)


