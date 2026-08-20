# Shutil Module in python ---->   High level file operation 



import shutil
import os

#shutil.copy('Day-47.py', 'kartik.txt')
#shutil.copy('Day-47.py', 'zuned.txt')

#shutil.move('Day-48', 'Day-1.py')


os.remove('osfolder')


##shutil.copytree('Day-47.py' ,'Day-48.py')


# shutil.copy("main.py", "main2.py")
# shutil.move(".tutorial/file.file", "file.file")
# shutil.rmtree("mytutorial")
#os.remove("file.file")





# Specify the path
path = r"C:\Users\professer_kartik\Desktop"

# Specify the file name
file = 'pavan.py'

# Before creating

# Creating a file at specified location
with open(os.path.join(path, file), 'w') :
    pass
   