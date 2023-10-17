# string methods
a = "--Neelaram is a good boy!"
print(len(a))
print(len(a.strip('!')))
print('-----------------------')

title = "menu".upper()
print(title.center(20,"-"))
print(("Boost".ljust(16,".")) + "$1".rjust(4))
print(("Bournvita".ljust(16,".")) + "$2".rjust(4))
print(("Milk".ljust(16,".")) + "$0.5".rjust(6))
# indexes
a = "Neelaram Winner"
print(a[3])
print((a[-7]))
# slicing
a = "Hulk defeats anyone"
print(a[:7])
print(a[1:])
print(a[1:7])
print(a[:-1])
print(a[-1:])
print(a[0:12:2])
print('---------------------')
# Mthds for boolean data
print(a.startswith("H"))
print(a.endswith('e'))
# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))
print("-------------")
# Numeric data types
a = 230
b = int(90)
print(type(a))
print(isinstance(b, int))

# float types
a = 34.66
print(isinstance(a,float))
print(type(a))