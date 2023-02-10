#Create a rug
user_width = int(input("What width will your rug be: "))
user_length = int(input("What length will you rug be: "))
design = input("Enter a design pattern (Ex. AaA): ")

def rugs(n, m, proc = '#'):
    col = proc*n
    for i in range(m):
        print(col)

rugs(user_length,user_width, design)