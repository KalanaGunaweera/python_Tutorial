#Generators....>>>using yield

def get_odd_numbers(upper_limit):
    for i in range(0,upper_limit):
        if i%2==1:
            print("odd", i)
            yield i
x= get_odd_numbers(9)
print(x)
# <generator object get_odd_numbers at 0x00000110A95310E0>
for i in x:
    print(i)

# odd 1
# 1
# odd 3
# 3
# odd 5
# 5
# odd 7
# 7

#***when we used generater , it can  not iterate more thaa one time. only one time only. we can use iterately using reset methods.
#example:
for i in x:
    print(i)

print("*"*20)
for i in x:
    print(i)

print("end")

# odd 1
# 1
# odd 3
# 3
# odd 5
# 5
# odd 7
# 7
# ********************
# end

