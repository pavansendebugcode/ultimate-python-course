''' Hi Everyone Today is discuss about what is genrator in python---->
                                                                    Generators in Python are special type of functions that allow you to create an iterable sequence of values. 
                                                                    A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it.
                                                                     Generators are a powerful tool for working with large or complex data sets, as they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.

'''


def my_genrator():
    
    for i in range(50):
        yield i



gen = my_genrator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


for j in  gen:
  print(j)



from functools import lru_cache as x
import time

@x(maxsize=None)
def fx(n):
  time.sleep(5)
  return n*5
    

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
print(fx(61))
print("done for 61")
# Output: 6765