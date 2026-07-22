# What is string
# String is a enclosed between single and double quators 
# like

a = "Hi, I am kartik sen From Bina "
b = "Zuned"
c = "sachinandsonic"

# This is a string 

print("Hello", a)

# Multiline strings

z = """ Hi, I am kartik every person who is see my code is very
        jenious because I am very jenious but you know my friend is very jenious such as 
        piyush sacchu khan """
# This is a multiline strings 
print(z)

# How to access strings characters 
print(z[8])
print(a[9])
print(c[-1])

# Access strings with loop 
for i in c:
    print(i)
    break

# How to find strings woards length

print(len(z))
print(len(a))

# String slicing

print(z[:9]) # string start 
print(a[0:]) # string end
print(c[6:9]) # between the slicing

# String methods
# Python provides a set of built-in methods that we can use to alter and modify the strings.


## upper() :
# The upper() method converts a string to upper case.

### Example:
str1 = "AbcDEfghIJ"
print(str1.upper())

## lower()
# The lower() method converts a string to lower case.
### Example:

str1 = "AbcDEfghIJ"
print(str1.lower())

