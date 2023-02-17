import linecache
import os

open("chal10.txt","x")

path = "/home/andrew/cybersecurity/chal10.txt"

file_append = open("chal10.txt","a+")

for i in range(3):
    file_append.write("Appended line %d\r\n" % (i+1))

file_append.close()

user_input = int(input("What line would you like to print? (1-3): "))

line = linecache.getline(r"/home/andrew/cybersecurity/chal10.txt",user_input)
print(line)

user_input2 = input("Would you like to delete this file now? (Y/N): ")

if user_input2 == "Y":
    os.remove(path)
else:
    print("Keeping file...")
    