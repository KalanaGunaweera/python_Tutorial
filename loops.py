#Forloop
x=[12,45,54,76]
for item in x:
    print(item)

#need to print index and value 
for item in enumerate(x):
    print(type(item),item)
# <class 'tuple'> (0, 12)
# <class 'tuple'> (1, 45)
# <class 'tuple'> (2, 54)
# <class 'tuple'> (3, 76)

for index, value in enumerate(x):
    print(index,value)
# 0 12
# 1 45
# 2 54
# 3 76

for item in range(0,10):
    print(item)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

y=[12,45,54,76,56]
r= range(0,len(y))
print(type(r))
for item in r:
    print(y[item])
# <class 'range'>
# 12
# 45
# 54
# 76
# 56

#WHILE loop

count = 0
while count<10:
    print("count", count)
    count += 1
# count 0
# count 1
# count 2
# count 3
# count 4
# count 5
# count 6
# count 7
# count 8
# count 9

count = 0
while True:
    if count == 15:
        break
    print("Hi", count)
    count += 1
# Hi 0
# Hi 1
# Hi 2
# Hi 3
# Hi 4
# Hi 5
# Hi 6
# Hi 7
# Hi 8
# Hi 9
# Hi 10
# Hi 11
# Hi 12
# Hi 13
# Hi 14

#Loop Example
a=[234,567,765,765]
total = 0
max=a[0]
for i in a:
    total+=i
    if max<i:
        max = i

print("Total ",total)
# Total  2331
print("Average ",total/len(a))
# Average  582.75
print("Max value ",max)
#Max value  765

#For dictionary in forloop
d={
    "saman":345,
    "kasun":657,
    "nimal":879,
    "sudath":456
}
for i in d.items():
    print(type(i))
    print(i)
# <class 'tuple'>
# ('saman', 345)
# <class 'tuple'>
# ('kasun', 657)
# <class 'tuple'>
# ('nimal', 879)
# <class 'tuple'>
# ('sudath', 456)

for name,height in d.items():
    print(type(i))
    print(name,height)
# <class 'tuple'>
# saman 345
# <class 'tuple'>
# kasun 657
# <class 'tuple'>
# nimal 879
# <class 'tuple'>
# sudath 456
