file = open("data.txt" ) #give the file absolute path
#open means this file is open in file descriptor it can use file read and write
print(type(file))
# <class '_io.TextIOWrapper'>

contents= file.read()
print(contents)
# hello world
# hi,good morning
# bye,good night

content2= file.readline()
print(content2)
# hello world


content3= file.readline()
print(content3)
# hi,good morning
file.close() #when you open the file it should closed after the use

#file open modes
"""
Character	Meaning
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	create a new file and open it for writing
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)
"""
#write mode
file = open("text.txt",'w')
for i in range(0,100):
    file.write(str(i) + '\n')    #create a text file and write it
file.close()

x=['1','2','3','4']
msg = ','.join(x)
print(msg)
# 1,2,3,4  after the 4 ,',' is not printed . these elements should be string

x=[str(i) for i in range(0,100)]
msg =','.join(x)
print(msg)
# 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,
# 30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,
# 57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,
# 84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99

  #we can use append function to append new data to the existing document
file = open("text.txt",'a')
x=[str(i) for i in range(100,200)]
msg ='\n'.join(x)
file.write(msg)
file.close()

