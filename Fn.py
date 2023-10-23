def hello_wo():
    print("Hello World")
hello_wo()

def sum(num1=0, num2=0):# default args
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

total = sum(2,4)#real args
print(total)

def multiple(*args):
    print(args) #('Dave', 'Neela', 'sar')
    print(type(args)) #<class 'tuple'>
multiple("Dave","Neela","sar")

def mul(**kwargs): #Keyword args
    print(kwargs) #{'first': 'Dave', 'second': 'Neela', 'last': 'sar'}
    print(type(kwargs)) #<class 'dict'>
mul(first ="Dave", second = "Neela", last = "sar")