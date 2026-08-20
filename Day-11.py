# Create a python program to print a good morning , good afernoon , and good evening using a time module 
Name = input("Enter your name = ")
import time
a = time.strftime('%H:%M:%S' )
print("The current time is ", a)
b = int(time.strftime('%H'))
print("The hours is  ", b ,"hours")
c = time.strftime("%M")
print("The minute is ", c ,"Minute")
d = time.strftime("%S" )
print("The second is ", d ,"second")

if b > 1 and b < 12:
    print( "Good morning", Name , "sir")

elif b < 12 and b <18:
    print("Good afternoon", Name ," sir")

elif b > 18 and b < 24 :
    print("Good evening ", Name , "sir")


# Today we are discuss about time module in python 



x = (time.strftime(f'year {'%Y'}, Month{'%B'},  Date {'%d'} \n\t\t hour {'%H'} minute {'%M'} second{'%S'}'))

print(f'The current time is \n \t\t {x}')
print(type(x))




print("Start:", time.time())
time.sleep(2)
print("End:", time.time())
# Output:
# Start: 1602299933.233374
# End: 1602299935.233376



t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)
# Output: 2022-11-08 08:45:33



def usingWhile():
  i = 0
  while i<50000:
    i = i +1
    print(i) 

def usingFor():
  for i in range(50000):
    print(i)

init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
print(time.time() - init)
print(t1)


print(4)
time.sleep(3)
print("This is printed after 3 seconds")
 
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time) 