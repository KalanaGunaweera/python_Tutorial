a=[23,43,54,76]
b=a
b.append(90)
# when I add somthing to b it will be defalt added to the a,
print(a)
print(b)
# [23, 43, 54, 76, 90]
# [23, 43, 54, 76, 90]

b=list(a)
b.append(90)
print(a)
print(b)
# [23, 43, 54, 76, 90]
# [23, 43, 54, 76, 90, 90]

#OR

b=[]
for i in a:
    b.append(i)
print(b)
# [23, 43, 54, 76, 90]
b.append(0)
print(a)
print(b)
# [23, 43, 54, 76, 90]
# [23, 43, 54, 76, 90, 0]

#using single line for for loop to return a
b=[i for i in a]
print(a)
print(b)
b.append(87)
print(a)
print(b)
# [23, 43, 54, 76, 90]
# [23, 43, 54, 76, 90]
# [23, 43, 54, 76, 90]
# [23, 43, 54, 76, 90, 87]

#example for list comprehension
def is_odd(number):
    return (number%2==1)

c=[is_odd(i) for i in a]
print(a)
print(c)
# [23, 43, 54, 76, 90]
# [True, True, False, False, False]

#example
def is_odd(number):
    return "odd" if(number%2==1) else"even"   #use turnary operator

c=[is_odd(i) for i in a]
print(a)
print(c)
# [23, 43, 54, 76, 90]
# ['odd', 'odd', 'even', 'even', 'even']


#example using enemarate function
x=[12,54,65]
for i in enumerate(x):
    print(i)
# output
# (0, 12)
# (1, 54)
# (2, 65)
for i,value in enumerate(x):
    print(i ,value)
# 0 12
# 1 54
# 2 65
    