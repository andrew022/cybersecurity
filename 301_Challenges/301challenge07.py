import os

dir = input("Please input file path: ")

def walk():

    for (root_dir_path, sub_dirs, files) in os.walk(dir):
        ### Add a print command here to print ==root==
        print(root_dir_path)
        ### Add a print command here to print ==dirs==
        print(sub_dirs)
        ### Add a print command here to print ==files==
        print(files)

walk()