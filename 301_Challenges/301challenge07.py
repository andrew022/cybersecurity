import os

user_input = input("Please input a folder name: ")

def dir_walk(dir_name):

    for (root, dirs, files) in os.walk(dir_name):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        ### Add a print command here to print ==files==
        print(files)

dir_walk(user_input)