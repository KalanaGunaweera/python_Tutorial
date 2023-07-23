# Set
x={"HELLO","WORLD","HELLO"}
print(x)
# {'WORLD', 'HELLO'}

x.add("hello") #using hash value
print(x)
# {'HELLO', 'hello', 'WORLD'}

x.remove("hello")
print(x)
# {'HELLO', 'WORLD'}

y={'a','b','c'}
print(x.union(y))
# {'HELLO', 'a', 'WORLD', 'b', 'c'}

print(x|y) # using pipe operator
# {'c', 'a', 'WORLD', 'b', 'HELLO'}

a={'1','2','3','4'}
b={'1','2'}
c=a-b  # we can substitute sets
print(c)
# {'3', '4'}

print('1' in a)
# True