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