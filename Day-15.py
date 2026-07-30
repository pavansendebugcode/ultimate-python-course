# Today we  can discus about what is function in python programming
# Function is block of code to perform special task the user define task 
# Function are two type 
#  1. Build in function like min(), max(), range(), etc
#  2. user define function

def average(a, b):
    c = (a+b)/2
    print(c)
average(2, 3)

e = 8
f = 9
average(e, f)

def drivecar():
    a = int(input("Enter you age = "))
    if a >= 18:
        print("you can drive the car ")
    else:
        print("you can not drive the car")

drivecar()

def kartik(zuned, sachin):
    print("Hi", zuned, sachin )


kartik("sonic", "eigenvalue")

# Arguments of Function in python programming 
# Four type of arguments in py
# 1. Default arguments

def name(joshan = "my father", kirti = "panka" , chanchal = "intelligent"):
    print(joshan ,kirti , chanchal)

name()

# 2. keyword argument

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")

# 3. Required arguments

def avg(a , b = 6, c = 6):
    print((a+b+c)/3)

avg(a = 69)

# Varabile lenght argument argument
# we can discuss next time ok 