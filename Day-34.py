# Today start a introduction of oops
# oops are object oriented programming 

'''RailwayForm   ---> Class [blueprint]
karik --> karitik ki info wala form --> Object [entity]
tom --> tom ki info wala form --> Object [entity]
shubham -- shubham ki info wala form --> Object [entity]'''

class person():
    name = 'kartik'
    occupation = 'Hacker'               
    def info(self):
        print(f'Hi, i am {self.name}, and my occ is {self.occupation}')


a = person()
a.info()

b = person()
b.name = 'zuned'
b.occupation = 'brillent'
b.info()


c = person()
c.name = 'sachin'
c.occupation ='Director'
c.info()

# contructure

class hacker():
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f'My name is {self.name} and my age is {self.age}')


x = hacker('kartik', '20')
x.info()