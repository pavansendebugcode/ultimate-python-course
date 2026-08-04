# Welcome to Day 23 of my python jorney.
# What I learned What is dictionary in python and how to use it.
# Dictonary is a orderd collection of data item store in singel varabile. Dictonary is a key value pair. Dictonary is sprated by commom and enclosed by curly bracket like this {}

dict = {'kartik': 'pass', 'zuned': 'topper', 'sachin': 'director', 'pankha' :'influencer'}

print(dict)
print(dict['sachin'])
print(dict.get('zuned'))

# Access multiple value

print(dict.values())

# Access multiple keys

print(dict.keys())

# Access key value pair

print(dict.items())

# Dictonary Method

# 1. update Method - update method are to update the value in add the value in dictonary. if the key is not present

dict.update({'prinka': 'true'})
dict.update({'zuned': 'fail'})
print(dict)

#  2. clear Method = clear method are use to clear the dictonary

#dict.clear()
#print(dict)

# 3. pop Method = pop method are use to remove the key value pair from dictonay

dict.pop('kartik')
print(dict)

# 4. popitem Method - popitem method are use to remove the last key value pair from dictonary

dict.popitem()
print(dict)

# 5. del method - del method are use to remove the key value pari from dictonary

del dict['pankha']
print(dict)