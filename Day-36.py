'''Hello friends we are going to learn 
The concept of Inheritence 
Inheritence is a help for create a child class with the help of exiting class but.
 you create a who child class all property is also include already you create a help of this class
Type of Inheritance 
1. Multiple Inheritance
2. Multilevel Inheritance
3. HYBRIED Inheritance
4. Herical Inheritance
5. single Inheritance
'''


class ADINA():
    def __init__(self, name, position, age):
        self.name = name 
        self.age = age
        self.position = position
        
    def showh(self):
            print(f'My name is {self.name} i am a {self.position} and my age is {self.age}')


anurag = ADINA('anurag_jain', 'HR', 20)
anurag.showh()


class BETECH(ADINA):
    def cs(self):
        print('Hi i am {self.name}')


x = BETECH('Kirti', 'empoly', 80)
x.showh()
x.cs()


class AI(BETECH):
    def kartik(self):
        print('Hi, I am a incent boy')


y = AI('SACHIN ', 'DIRECTOR', 30)
y.showh()



class Student:
    def __init__(self):
        self._name = "kartik"

    def _funName(self):      # protected method
        return "codewithkartik"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())