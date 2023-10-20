# value = 1
# while value <=10:
#     print(value)
#     if value == 5: # 1 3 5
#         break
#     value +=2    
# value = 1
# while value <=10:
#     value +=1
#     if value == 5:
#         continue # 2 3 4 6 7 8 9 10 11
#     print(value)
# else:
#     print("value is now equal to" + str(value))
names = ["Dave", "Sara","John"]
# for y in names:
#     print(y) # Dave Sara John
# for y in "Mississippi":
#     print(y) # M i s s i s s i p p i 
# for x in names:
#     if x =="Sara":
#         break
#     print(x)
# for x in names:
#     if x =="Sara":
#         continue
#     print(x)

# for x in range(4):
#     print(x)     # 0 1 2 3
# for x in range(2,4):#start, stop
#     print(x) #2,3
for x in range(0,101,5):
    print(x) 
else:
    print("Glad that\'s over!")
actions = ["Codes", "eats", "sleeps"]
# for name in names:
#     for action in actions:
#         print(name + " "+ action + ".") #Dave Codes. Dave eats. Dave sleeps. Sara Codes. Sara eats. Sara sleeps. because name is in outer loop
for action in actions:
    for name in names:
        print(name + " "+ action + ".") #Dave Codes. Sara Codes. John codes.....