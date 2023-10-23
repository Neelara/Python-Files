def add(n):
    if(n >= 9):
        return n + 1
    total = n + 1
    print(total)

    return add(total) #rec fn

mynewtotal = add(0)
print(mynewtotal)