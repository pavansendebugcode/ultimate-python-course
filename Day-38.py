
# Class Method --> class n object-oriented programming, the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class. 
# The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.



class adina():

    collage = 'adina collage'
    def __init__(self,  name, post,  salary):
        self.name = name
        self.post = post
      
        self.salary = salary

    def detail(self):
        print(f'My name is {self.name} and i am {self.post} of {self.collage} and my salary is {self.salary}')


    @classmethod
    def changecollage(cls, newcollage):
        cls.newcollage = newcollage



x = adina('Anurag', 'HOD',  30000)
x.detail()

y = adina('kesari', 'Head of cs', 100000)
y.detail()

y.changecollage("BTIRT COLLAGE")
y.detail()
print(adina.collage)



class Employee:
  def __init__(self, name, salary):
    self.name = name 
    self.salary = salary
    
  @classmethod
  def fromStr(cls, string):
    return cls(string.split("-")[0], int(string.split("-")[1]))
    
e1 = Employee("kartik", 12000)
print(e1.name)
print(e1.salary)

string = "John-12000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

person = Person.from_string("John Doe, 30")
print(person.name, person.age)















