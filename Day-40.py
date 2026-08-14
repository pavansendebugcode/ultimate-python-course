# Today we are learn about what is dir(), __dict__() , help(), method in python
# dir() --> dir() Method are used to find the how to work any function its give me all the information about the class



# x = [1, 2, 3 , 4 , 5]
# print(dir(x))

# __dict__()  ---> These method are used to how to know about the class It's give me all varabile instant varabile
# help Method----> help Mehtod give  full information about the class such as how to create how to work and also give how to end
class Emoplyee():
    def __init__(self, name, age, occ):
        self.name = name
        self.age = age
        self.occ = occ
    def showdetail(self):
        print(f'My name is {self.name} and i am {self.age} year old and my post is {self.occ}')


    

x = Emoplyee('kartik', '20', 'HR')
x.showdetail()
print(x.__dict__)
print(help(Emoplyee))















