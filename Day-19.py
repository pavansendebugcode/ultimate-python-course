# Exercise 2 - create a python program to print a kbc question after question print a how many rupess are win

print
a = ["who is the prime minister in india", "who is the president of india", 'who is the first president of india' ]

print(a[0])
b = input("what is answer = ")
if b == 'narendra modi':
    print('Right answer')
else:
    print('wrong answer')

print(a[1])
c = input('what is answer = ')
if c == 'dropati murmu':
    print('right answer')
else:
    print('worng answer')

print(a[2])
d = input("what is answer = ")
if d == 'rajendra prasad':
    print("Right answer")
else:
    print('wrong answer')

    # calculation money

if b == "narendra modi"   and c == "dropati murmu" and d == 'rajendra prasad' :
    print('you are win 1 cr')

elif b == "narendra modi"   and c == "dropati murmu" :
    print('you are win 50 laksh')

elif b == "narendra modi"  and d == 'rajendra prasad' :
    print('you are win 50 laksh')

elif c == "dropati murmu" and d == 'rajendra prasad' :
    print('you are win 52 laksh')

print('you are so lucky you are win large money')




