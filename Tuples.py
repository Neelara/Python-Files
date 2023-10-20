a = tuple(('Dave','Neela', 45,True)) #constructor
another = (1,2,3,4,4,4,4) #without constructor
print(type(a))
print(type(another))
newlist = list(a) #because we cannot directly append values in tuple
newlist.append('Ram') #so we changing tuple into list
newtuple = tuple(newlist)
print(newtuple)

#unpacking tuple with other variable name
(*one, three, hi) = another
print(one)
print(three)
print(hi)
print(another.count(4))
(*one,) = a
print(one)