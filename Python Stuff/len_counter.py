#Counts the length of you number or word without using the buit in function.
#Determines if your input is a string or integer.
#Negative numbers do not count as integers.
user = input("Enter a number or string: ")
counter=0
if user.isnumeric() == True:
    for i in user:
        counter=counter+1
    print("Length of inputed integer: " +str(counter))
else:
    for i in user:
        counter=counter+1
    print("Length of inputed string: " +str(counter))