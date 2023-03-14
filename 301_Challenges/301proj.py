import shutil
from datetime import date

def_dest = "C:\\backups\\"

user_source = str(input("Please input a source destination: "))
user_name = str(input("Please name your backup: "))
user_input1 = str(input("Do you have a specific place for an end destination? (Y/N): "))

if user_input1 == "Y" or user_input1 == "y":

    user_dest = str(input("Please enter a destination for backup: "))

    today = date.today()
    date_form = today.strftime("%d-%m-%y")

    shutil.copytree(user_source,user_dest+"\\"+user_name+"_"+date_form)

else:

    print("Creating backup in defaulted backup location...")

    today = date.today()
    date_form = today.strftime("%d-%m-%y")

    shutil.copytree(user_source,def_dest+user_name+"+"+date_form)

    print("Operation complete, folder sent to 'backups' folder in root directory.")
