# Day 21: Recursion and Recursive Functions in python 
#           Recursion is a programming are use function in function where a function calls itself  in a function
# Find the factorial of a number using recursion

def a(n):
    if n == 0 or  n == 1:
        return 1
    else:
        return n * a(n-1)
b  = a(int(input('enter a number to find factorial: ')))
print(b)


# Quize find fibonacci series using recursion
