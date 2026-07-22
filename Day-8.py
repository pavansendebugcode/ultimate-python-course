# What is typecastion in python language
# Typecasting in python converts the data one type to another data type.
# Typecasting is two types
 # 1. Explicit Conversion (Explicit type casting in python)
 #2. Implicit Conversion (Implicit type casting in python)

a = 10
b = 40.36
c = "39"

print(type(a))

print(type(b))
print(type(c))

x = int(b) # converting float to int
y = float(a) #converting int to float
z = int(c) # converting string to int

print(type(x) , x )
print(type(y), y)
print(type(z), z)

# Today is also learning about the input function in python programming language
# the input function is used to take input from the user 
# Input function provides a value as a string data type.
# But we can convert to other data type using typecasting 

T = input("Enter your name = ")
print("Hello", T)

# Output 
# Enter your name = Kartik
# Hello Kartik

u = input("Enter your date of birth  = ")

print("This date of birth is very funny ", u)
print("you are very lucky")
