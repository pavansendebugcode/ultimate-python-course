# Super keyword in python programming ---> super keyword are used to when child class are inheriate more than parent class and you want to run particular function in child class you use the 
#                                          super keyword super keywod are used to when you crate a child class  then you create a parent method in child class  and 
#                                          paraent calass is also contain a parent class then you want to run a  paraent method in child class super keyword are used

class kartik:
    def parentbhai(self):
        print('is a very talented')

    def parentmother():
        print('is very bad')

class chinku(kartik):
    def punnu(self):
        print('This is my name')
        super().parentbhai()
    
x = chinku()
x.punnu()
    

class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")

class ParentClass2:
    def parent_method(self):
        print("This is the parent method of ParentClass2.")

class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

y = ChildClass()
y.child_method()


# Today we are also learn about Magic / Dunder Method in python
# These are special methods that you can define in your classes, 
# and when invoked, they give you a powerful way to manipulate objects and their behaviour

class Employee:

  def __init__(self, name):
    self.name = name

  def __len__(self):
    i = 0
    for c in self.name:
      i = i + 1
    return i

  def __str__(self):
    return f"The name of the employee is {self.name} str"
    
  def __repr__(self):
    return f"Employee('{self.name}')"

  def __call__(self):
    print("Hey I am good")


e = Employee("Harry")
print(str(e))
print(repr(e))
# print(e.name)
print(len(e))
e()

# METHOD OVERLOADING ---> 


class Shape:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def area(self):
      return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
      self.radius = radius
      super().__init__(radius, radius)

    def area(self):
        return 3.14 *  super().area()
      
# rec = Shape(3, 5)
# print(rec.area())

c = Circle(5)
print(c.area())