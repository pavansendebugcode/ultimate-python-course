#Introduction of python programming Language

# what is module in python programming Language 

# you can use another person of code in your code 

# Module are two type \]

# 1. Built in Moudle (already available in python programming Language )
# 2. External Moudle (not available in python programming Language you have to install it using pip command )


# 1.

import math

print(math.sqrt(16))

import random
print(random.randint(1, 100))

import datetime
print(datetime.datetime.now())

import os 
print(os.getcwd())

import sys
print(sys.version)


#2 External Moudle (not available in python programming Language you have to install it using pip command )

import pandas as pd
data = {'Name': ['John', 'Alice', 'bob', 'David'], 'Age': [25, 30, 22, 29,], 'City': ['New York', 'Los Angeles', 'mumbai', 'chicago']}

df = pd.DataFrame(data)
print(df)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#import tensorflow as tf
#Print(tf._PYTHON_VERSION)

import cv2
img = cv2.imread(r"C:\Users\professer_kartik\Downloads\file_00000000c13c7206a343858005394c20_1.png")
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
