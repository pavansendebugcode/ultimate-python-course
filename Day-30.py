'''opening a file in particular folder
Before opening a and manipute the you do write a open and also write the () in 
In bracket to argument are passed first file name and second mode of operation
Modes of operation -
'r' - reading the file only 
'w' - writing the file and if file does not exit to create a file
'a' - is used for add a text to exit file 
'x'- is used for to create a new file and if file is already exit they give the error
't' - these are basic purpose used
'b' - used for handle binary file like (image, text, pdf files)'''

# Read the file 

f = open('kartik.txt2', 'r')

print(f)
g = f.read()
print(g)
f.close()

## write the file

# f = open('kartik.txt1', 'w')
# p = f.write('Hi, Welocme to my world this is my world')
# print(p)
# f.close()

## append in exiting file

# z = open('kartik.txt', 'a')
# y = z.write('  Hi, i am making food')
# print(y)
# z.close()

#@ readline() Method

# q = 0
# while True:
#     q =+ 1
#     q = f.readlines()
#     print(q)
#     if not q :
#         break

#@ writelines() mehtod

# lines = ['line1\n', 'line2\n', 'line3\n']
# b = f.writelines(lines)
# print(b)
# f.close()

#@ seek() function - seek are used to excess a value in file you want to do

# f.seek(10)
# m = f.read()
# print(m)
#f.close()

#@ tell() function - tell function are used to find the seek postion

# i = f.tell()
# print(i)
# f.close()


# also used like 
# with open('myfile.txt', 'r') as f:
# ... do something with the file

