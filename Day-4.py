
'''1. Write a program to print Twinkle twinkle little star poem in python.
2. Use REPL and print the table of 5 using it.
3. Install an external module and use it to perform an operation of your interest.
online for the function which does that.
CHAPTER 01
4. Write a python program to print the contents of a directory using the os module. Search
5. Label the program written in problem 4 with comments'''

a = "Twinkle, twinkle, little star,\n\tHow I wonder what you are\n\t up above the world so high,\n\tlike a diamond in the sky."
print(a)

import os
print(os.listdir())

import pandas as pd
data = pd.DataFrame({'Name': ['Alice', 'Bob', 'charlie', ], 'age': [39000, 39, 30]})

import cv2
img = cv2.imread(r"C:\Users\professer_kartik\Downloads\file_00000000c13c7206a343858005394c20_1.png")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()