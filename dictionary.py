# Dictionary

k={}
y={"23":"kalana","67":"Saman"}
print(y)
# {'23': 'kalana', '67': 'Saman'}

# Add values into dictionary
y["34"]="Nimal"
print(y)
# {'23': 'kalana', '67': 'Saman', '34': 'Nimal'}

print(y.keys())
# dict_keys(['23', '67', '34'])

print(y.values())
# dict_values(['kalana', 'Saman', 'Nimal'])

print(y["23"])
# kalana
z=y.get(3)
print(z)
# None
z=y.get(3,"return this value")
print(z)
# return this value

# delete values
print(y)
# {'23': 'kalana', '67': 'Saman', '34': 'Nimal'}
del y["23"]
print(y)
# {'67': 'Saman', '34': 'Nimal'}

# clear dictionary
y.clear()
print(y)
# {}

x={
    "a":["hi","hello","good morning"],
    "b":["bye","good night"],
    "c":67
}

print(x)
# {'a': ['hi', 'hello', 'good morning'], 'b': ['bye', 'good night']}
z=x["a"]
print(z)
# ['hi', 'hello', 'good morning']
z.append("ayubowan")
print(z)
# ['hi', 'hello', 'good morning', 'ayubowan']
print(x)
# {'a': ['hi', 'hello', 'good morning', 'ayubowan'], 'b': ['bye', 'good night']}

# for basic data types...
z=x["c"]
print(z)
# 67
z=89
print(z)
print(x)
# 89
# {'a': ['hi', 'hello', 'good morning', 'ayubowan'], 'b': ['bye', 'good night'], 'c': 67}


