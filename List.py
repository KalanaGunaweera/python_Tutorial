#  list

x=[]
# This is not recomemded
a=[12,"kalana",56.0]
print(a)

b=[12,45,78]
print(b)

# get element
print(b[0])

# change value
b[1]=78
print(b)
# [12, 78, 78]

# add value
b.append(100)
print(b)
# [12, 78, 78, 100]

b.insert(1,400)
print(b)
[12, 400, 78, 78, 100]

b.remove(100)
print(b)
[12, 400, 78, 78]

b.pop(1)
print(b)
[12, 78, 78]

c=[23,65,98]
d=c+b
print(d)
[23, 65, 98, 12, 78, 78]

# check the value is in the list.. in value return bool value
print(65 in d)
# True

print(65 not in d)
# False
print(not 65 in d)
# False








