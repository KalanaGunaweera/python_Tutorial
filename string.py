#String formating

name = "Kalana"
height = 178

#type 01 >>>> c type formatting

message = "Hello %s. Your height is %d" %(name,height)
print(message)
# Hello Kalana. Your height is 178

#type 02 >>>> using format function

message = "Hello {}. Your height is {}".format(name,height)
print(message)
# Hello Kalana. Your height is 178
message = "Hello {1}. Your height is {0}".format(name,height)
print(message)
# Hello 178. Your height is Kalana
message = "Hello {0}. Your height is {1} ({0})".format(name,height)
print(message)
# Hello Kalana. Your height is 178 (Kalana)


#type 03 >>>> using f strings

message = f"Hello {name}. Your height is {height}"
print(message)
# Hello Kalana. Your height is 178
message = f"Hello {name}. Your height is {height:05d}"
print(message)
# Hello Kalana. Your height is 00178