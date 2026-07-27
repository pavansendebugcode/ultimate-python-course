# Today we are learn what is do while loop in python 
# A do while loop is a loop in which a set of instruction will excute atleast one time

while True:
    a = int(input("Enter your cgpa = "))
    print(a)
    if  a < 0:
        break

while True:
    b = int(input("Enter you age = "))
    print(b)
    if b>0:
        break


# Today is a very special day because birthday of my ------
# so we can also learn break continue statement 

# break statement - break statment is a when a loop run to exit a loop imidateley

for i in range(1, 100, 2):
    print(i)
    if i == 51:
        break
    else :
        print("I love you but i dont fuck you")



# continue statment - continue statement are used to skip particular value 
g = 1
while g<10:
    
    g += 1
    if g == 5:
        continue
    print(g)


    
