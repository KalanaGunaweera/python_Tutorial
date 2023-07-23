# tuple
Kalana = ("kalana", 29,"matara")
print(type(Kalana))
print(Kalana)
# <class 'tuple'>
# ('kalana', 29, 'matara')
name = Kalana[0]
print(name)
# ('kalana', 29, 'matara')
# kalana

Kalana = ("kalana", 29,"matara", "kalana")
print(Kalana.count("kalana"))
# 2

Kalana = ("kalana", 29,"matara")
name,age,town =Kalana
print(name,age,town)
# kalana 29
