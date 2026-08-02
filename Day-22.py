# Pyhon sets
# Sets are unordered collection of data item store in single varabile
#  Sets are sprated by comma and enclosed by curly bractes like this {}
#  sets does not allow duplicate value 

s = {3, 6, 96, 78, 76, 3, 45}
print(type(s), s)

se = {'pankha', 'junni', 'sacchu', 'sonic', 'eigenvalue'}

for i in se:
    print(i)

# Quize To crate a emepty set   
p = set()
print(type(p))


'''--------------------------------------------------------------------------------------------------------------'''

# joining Method in set

# 1. uniun Method and update method 

# union method are use to combine two varabile they print a new varaiable
# update mehtod are use to update value in sprated varabile

s1  = {'Toyko', 'china', 'india', 'america', 'brazil'}
s2 = {'pakistan', 'iron', 'new delhi', 'africa', 'india', 'Toyko'}

print(s1.union(s2))
s1.update(s2)
print(s1)

# 2. Intersection and Intersection Method in set
#       intersection are use to find intersection between to varabile
#        intersection update method are use to update intersection in sprated varabile

a = { 8, 9, 98, 67, 38, 39, 20, 48, 3}
b = { 20, 39, 98, 8, 398, 30, 3,48, 40 }

print(a.intersection(b))
a.intersection_update(b)
print(a)

# 3. Symmetric difference and Symmetric difference method in sets
#       symmetric difference are provide a union b - a intersection b but new varabile
#       symmetric difference are provide same but store a sparated varabile

p = {'kirti', 'anjali', 'chanchal', 'nidhi', 'sonic', 'eigenvalue'}
q = { 'sacchu', 'monika', 'junni', 'kirti', 'nidhi', }
# a union b - a intersection b

print(p.symmetric_difference(q))
p.symmetric_difference_update(q)
print(p)

# 4. difference method and difference method in set
#       difference method are print the value not exit in varabile 
#       difference method are store a sparated varabile

c = {1, 2, 3, 4, 5 , 6 , 7 , 8 , 9 }
d = {1, 72, 3, 54, 5 ,9, 7 , 88 , 99 }

print(c.difference(d))
d.difference_update(c)
print(d)

# 5. isdisjoint():
# 

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))