# Class varabile and Instant varabile ----->  
#                                             class varabile are define outside the function but inside the class
#                                             Instant varabile are define inside the funcion and also inside the class


class Empoly():

    company = 'google'              # class varabile
    No_of_empoly = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age              # instant varabile
        self.companynum = 9303
        Empoly.No_of_empoly += 1
        
    def showdetail(self):
        print(f'The Name of empoly {self.name} and the age of empoly {self.age} and work on {self.company} and the number of empoly is {self.No_of_empoly}')
  
    def companyshowdetail(self):
        print(f'The name of company {self.company} and the number of company is {self.companynum} ')
 
    
emp1 = Empoly('kartik', 20)
emp1.showdetail()
emp1.company =  'Tesla'
emp1.showdetail()

emp1.companyshowdetail()

emp2 = Empoly('zuned', 45)
emp2.showdetail()

emp3 = Empoly('sachin', 90)
emp3.company = 'kartik ki company '
emp3.showdetail()



# static Method--->


class Math():

    def __init__(self, num):
        self.num = num

    def show(self, n):
        print(f'The sum of these number is {self.num + n}')

    @staticmethod
    def add(a,b):
        return a+b


x = Math(5)
x.show(5)