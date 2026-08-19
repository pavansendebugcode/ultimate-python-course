'''Today I am very happy because my exam is completed 
 operator overloading in python --->
                                      operator overloading means giving a special meaning to an operator (+, -, *, /) for objects of a user define class
                                      python uses special magic methods such as __add__() , __sub__(), and __mul__(), for operator overloading
 '''

class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y 
        self.z = z

    def __str__(self):
        return( (f'{self.x}i + {self.y}j + {self.z}k'))

    def __add__(self, x):
       return(vector(self.x + x.x , self.y + x.y , self.z+ x.z))

    def __mul__(self,y):
        return vector (self.x/y.x, self.y /y.y , self.z/y. z)

  

p1 = vector(2, 3, 5)
print(p1)

p2 = vector(2, 9, 7)
print(p2)

q = str(p1+p2)
print(q)
print(type(q))

r = (p1*p2)
print(r)