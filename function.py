def get_marks():
    print("hello")

get_marks()

#Positional parameters/Arguments

def get_results(marks):
    
    if marks<0 or marks>100:
        print("invalid")
    elif marks<35:
        print("S")
    elif marks<50:
        print("C")
    elif marks<75:
        print("B")
    else:
        print("A")

get_results(45)
get_results(67)
get_results(345)
get_results(89)
# C
# B
# invalid
# A

#default arguments
def get_results(marks, subject="unknown"):
    print("My subject is ",subject)
    if marks<0 or marks>100:
        print("invalid")
    elif marks<35:
        print("S")
    elif marks<50:
        print("C")
    elif marks<75:
        print("B")
    else:
        print("A")

get_results(56)
get_results(67,"Maths")
# My subject is  unknown
# B
# My subject is  Maths
# B

#Packed Arguments
def results(*marks):
    print(type(marks))
    total=0
    for i in marks:
        total+=i
    print(total)
results(67,54,76)
# <class 'tuple'>
# 197

#Keyword arguments-kwargs

def kwargs(**params):
    print(type(params))
    print(params)
kwargs(name="kalana", age=30,address="matara")
kwargs(name="sudath", address="ampara")
# <class 'dict'>
# {'name': 'kalana', 'age': 30, 'address': 'matara'}
# <class 'dict'>
# {'name': 'sudath', 'address': 'ampara'}


def kwargs(**params):
    if 'name' not in params:
        print("Error")
    else:
        print("Hello",params['name'])
 
kwargs(name="kalana", age=30,address="matara")
kwargs( address="ampara")
# Hello kalana
# Error

#When I use packed and keyword in boths, packed argument must in the first
def args(*values,**params):
    print(values,params)
args(67,54,name="kalana", age=30,address="matara")
# (67, 54) {'name': 'kalana', 'age': 30, 'address': 'matara'}


#convert dictionary into named arguments
def args(name,age):
    print(name,age)
    print(name)
    print(age)
dic={
    'name':'kalana',
    'age':76
}
args(**dic)
# kalana 76
# kalana
# 76