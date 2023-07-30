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