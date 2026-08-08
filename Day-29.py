# Today is a very special day, so we are learing about the os module in python programming.
# The os module in python medium of communication between the operating system and vs code
# Os module are a built -in module in python
'''import os 

if (not os.path.exists('kartik')):
    os.mkdir('kartik')

for i in range(0, 6):
    os.mkdir(f'kartik {i+1}')
#os.rename(f'kartik{i+1}', f'kartiksir{i+1}')'''


# what is local and global varabile
# global varabile define in out side the function whenever 
# local varabile define in side the function 
# global varabile are used in the function but local varabile don't use out side the function 

x = 4 # global varabile
print(x)

def ram():
    y = 5 # This is a local varabile
    print(x)
    print(y)

ram()
print(x)
print(y) # This is give me error because local varabile does not define outside the function
