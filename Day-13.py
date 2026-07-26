# Today we are discuss what is loop in python programming 
# Introduction of loop
# sometime programm want to excute a group of statement number of time . This is done by using loop 

# loop are two type

# 1. for loop
# 2. while loop

# for loop

a = "zunead"
for i in a:
    print(i)

b = {'sachin', 'aadersh', 'rishi', 'pankha'}

for k in b:
    print(k)

# Range

for p in range(9):
    print(p)


for j in range(10, 90):
    print(j)


# while loop 
# similar to name while loop exute the loop whenever condition is true if condition is false then exit the loop

jarvis = 1
while jarvis < 5:
    print(jarvis)
    jarvis += 1

m = int(input('Enter number = '))
while m < 100:
    print(m)
    m += 1