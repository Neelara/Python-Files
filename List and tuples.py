a = ['Neela','Jog',"jarry"]
empty = []
b = [56, 'Neela', True, 55.7]
print(56 in a)
print(b[-2])
print(b.index(55.7))
print(a[0:])
print(a[-3:-1])
print(b[-3:])
print(a[-3:-1])
print(a[0:])
a.append("Ram")
print(a)
b +=['Robert']
print(b)
a.extend(['rob', 'Bob'])
print(a)
#a.extend(b)
#print(a)
a.insert(2,'Boberry')
print(a)
print(a)
a[2:2] = ['alex','Eddy']
print(a)
print("**********************")
print(a)
a[2:4] = ['robber','JPJ']
print(a)

b.remove('Robert')
print(b)
print(a)
a.pop()
print(a)

del a[4]
print(a)
print(b)
b.clear()
print(b)