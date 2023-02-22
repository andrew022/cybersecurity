import requests

user_input1 = str(input("Please enter a URL: "))

get = requests.get(user_input1)
post = requests.post(user_input1)
put = requests.put(user_input1)
delete = requests.delete(user_input1)
head = requests.head(user_input1)
patch = requests.patch(user_input1)
options = requests.options(user_input1)

print("")

print("Please Select an option from below.")
print("GET")
print("POST")
print("PUT")
print("DELETE")
print("HEAD")
print("PATCH")
print("OPTIONS")
print("")
user_data2 = str(input("Your option: "))
user_data3 = str(input("Do you wish to continue (Y/N): "))

if user_data3 == "Y":
    print("Continueing...")
    print("")
    if user_data2 == "GET":
        print(get)
    elif user_data2 == "POST":
        print(post)
    elif user_data2 == "PUT":
        print(put)
    elif user_data2 == "DELETE":
        print(delete)
    elif user_data2 == "HEAD":
        print(head)
    elif user_data2 == "PATCH":
        print(patch)
    elif user_data2 == "OPTIONS":
        print(options)
    else:
        print("Invalid response.")
else:
    print("Invalid response.")