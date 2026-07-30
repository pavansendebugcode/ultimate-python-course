# List Method 
# 1. append mehod
#      append method are use to add value in list 

a = [1, 3, 30.3, 30, 38, 200, 380, 99, ]
a.append(1000)
print(a)

# 2. sort mehod 
#       sort mehod are used to value are arrenged in increasing order
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# 3. reverse mehod
#       reverse method are use to reverse print the value
a.reverse()
print(a)

# 4. indexing mehod
#       indexing mehtod are use to give index number form the list

print(a.index(1))
print(a.index(30.3))

# 5. Count Mehod
#       count method are use to count the value of list

b = ['mydreamisiwant', 'howtofindeigenvalue']
print(b.count('howtofindeigenvalue'))

# 6. copy mehod
#       copy mehod are used to copy the list value

c = a.copy()
print(c)

# 7. Insert Method
#       inesert value are used insert the specfic value with indexing

b.insert(2, "sonic")
print(b)

# 8. Extend Method 
#       Extend mehod are used to add list with {touple , string, dictnory}

a.extend(b)
print(a)

# 9. add to list by addtion
#       add list by addtion +
print(a+b)