#Inserts commas into you number.
user = int(input("Enter a number: "))

conv = ('{:,}'.format(user))
if user > 0:
    print("Converted numvber is: " +str(conv))
else:
    print("Not a positive number, please run code and try again.")
    print("Quitting.")