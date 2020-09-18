# Blackboard-scraper

## This project was created to assist students struggling with data usuage and to increase efficiency in submitting/downloading assignments
*Currently only works for documents that are in pdf format 

## Installation 
### Debian
 
1) run pip install -r requirements.txt
2) uncomment *geckodriver_autoinstaller.install()* from function.py file under the Start_driver(args) function 
2) Edit config.py to add default variables to make usage a lot more easier
3) run main.py -h

### Windows 

1) You will be required to install geckodriver (Tested to work with firefox drivers) then unzip and move the geckodriver to the project folder
2) run pip install -r .\requirements.txt (should work with pipenv and Anaconda)
3) run main.py -h

## Usage

### python main.py login

This functions logs user in a lot quicker than the standard way of accessing the Blackboard

#### python main.py login --username <student_num> --password <password>

Default settings in config.py can be configured to allow user to just type *python main.py login*

### python main.py download-latest 

Downloads the latest pdf uploaded to specified URL

#### python main.py login --username <student_number> --password <password> -url URL --path </PATH/TO/DIRECTORY/>
default is set to download latest lab

run python main.py download-latest -h to see all options available 

### python main.py download-all 





