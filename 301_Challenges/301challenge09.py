import random

user = input("Please enter a number: ")

n = random.randrange(1,500)

def checker():

    if user.isnumeric() == True:
        code()
    else:
        print("Not a number, try again!")

def code():

    if user == n:
        print("Your number matches my number!")
    elif user != n:
        print("Your number does not match my number :(")
    elif user < n:
        print("Your number is less than mine!")
    elif user <= n:
        print("Your number is less or equal to mine!")
    elif user > n:
        print("Your number is greater!")
    elif user >= n:
        print("Your number is greater or equal!")
    else:
        print("Thats not a number!")

checker()