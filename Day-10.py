#  If else statement
# if else and statement in python programming is use to control flow 

a = int(input("Enter your age = "))

if a<18 and a>0:
    print("you can not drive")
    
elif a==18:
    print("you go RTO office and create your licence")

elif a>18 and a<80:
    print("you can drive")

elif a>80 and a<100:
    print("you are not able to drive")

elif a>100 and a<1000:
    print("you are died")

elif a>1000:
    print("you are good not human")

else :
    print("you are not born in earth you will wait", a)

