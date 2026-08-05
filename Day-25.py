# welcome to 100 days learn my python journey This is Day - 25 
# I am very excited to learn python Today we are discuss about try except concetpt 

# Try except concept in python

# some time code give me error we can controal this situation with the use of try except concept


try:

    def average():
         a = int(input('Enter your num 1 : '))
         b = int(input('Enter your num 2 : '))

         print(f'The average of this number {a} and {b} = {((a+b)/2)}')
         return 1

    average()

except :
    print('Enter  the interger value')
    print('try again')

# Today is a very special day we are also learn what i finally key in python
# Finally keyword is always run in python any stiuation any want to do anythings

try:
    def multi():
        a = int(input('Enter the number you want to print a multiplication table = '))
        print(f'Multiplication table is {a}')
        for i in range(1, 11):        
            print(f' {a}x{i} =  {a*i}')
            

    multi()
except IndexError  :
    print('Index error')

finally:
    print('hi')

# Hello friend only last concept i will learn today
# custom error - custom error are mode by own  using raise keywoard

p = int(input('Enter the number 0 to 10/; '))
if p<0 or p>10:
    raise ValueError ('invaild input')
