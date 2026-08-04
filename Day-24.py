# for loop and while loop with else statement
#  we can discuss the for and while loop with if statement but else statement are used with loop
# else statement are when excuted when loop is completed 
for i in range(10):
    if i == 6:
        break
    print(i)
else:
    print(f'loop is completed and the last value is {i}')

def a(a):
    a = int(input('enter the number: '))
    b = a+1
    for i in range(11):
        print(f'{b} * {i} = {b*(i)}')
    else :
        print(f'this is end the prorgramm you want to continue prees your friend mouth')
a(a)