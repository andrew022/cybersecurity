import shutil
from datetime import date
import os
import stat

def_dest = "/home/test"

user_source = str(input("Please input a source destination: "))
user_input1 = str(input("Do you have a specific place for an end destination? (Y/N): "))

if user_input1 == "Y":

    today = date.today()
    date_form = today.strftime("%d-%m-%y")

    user_dest = str(input("Please enter a destination for backup: "))

    shutil.copytree(user_source,user_dest)
else:


    today = date.today()
    date_form = today.strftime("%d-%m-%y")
    shutil.copytree(user_source,def_dest)
