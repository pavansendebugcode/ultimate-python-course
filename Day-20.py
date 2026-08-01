# We are today going to Learn about the in Python What is f-strings and how to use them in pyhton
# f strings are a way to format strings in python. They allow you to embed expressions inside string literals, using curly brances {}.
# f strings are introduced in python 3.6 and are a more readable and concise way to format strings compared to the older methods like % formatting or strings.


name  = "John"
age = 30
print(f"Hello, My name is {name} amd I am {age} years old.")
a = 9
print(f"{a*9}") # This will print 81


# we are also going to learn about the what is doc strings in python 
# Dog strings are a way to document your code in python. They are define using triple quotes ('''  or''') and are used to provide information about The purpose of a function, class, or module

def square():
    '''This function takes a number as input and returns it's square.'''
    a = int(input(f'Please enter a number to find its square : ='))
    print(f"The square of {a} is ", a*a)

square()

print(square.__doc__)

# Different between comments and doc strings in python 

#  comments are always ignore in python but doc strings are not ignore in python doc string are defined functons, classes, and modules to provide information about their purpose and usage,
# you can try to  import this in your repl .
