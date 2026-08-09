# What is lambda function and their use
# lambda function is a big brother of function 
# function used is this work lambda function do this work

#@ Normal function

def cube(x):
    return x*x*x
y = cube(8)
print(y)

# Lambda function
# 1. 
cube = lambda x: x*x*x
print(cube(5))

# 2.
aver = lambda x, y: (x+y)/2
print(aver(5, 6))

# 3.
try:
    print('Are add three number\n')
    sum = lambda x, y, z: (x+y+z)
    print('sum of three number', sum(int(input('Enter your first number ;  \n'  )), int(input('Enter your second number ;  \n'  )), int(input('Enter your third number ;  \n'  ))))

except:
    print('invalid input try again')