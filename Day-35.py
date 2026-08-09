# Decoration function = Decoration function are used Decorate the function
#                       and specialfic the function 

def greet(fx):
    def mfx(*args, **kwargs):
        print('Good Morning')
        fx(*args, **kwargs)
        print('Thankyou running this code')
    return mfx




def aver():
    print('Hello, world')


@greet
def sum(a, b):
    return a+b

aver()
sum(1, 5)
print(sum(1, 5))