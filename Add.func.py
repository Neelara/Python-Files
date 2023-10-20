a = ['Rob', 'Bob','Mary','Silva','Chettri']
a.sort()
print(a)
a[1:2] = ['dave']
a.sort()
print(a)
a.sort(key=str.lower)
print(a)
nums = [4,43,1,5,67]
nums.reverse()
print(nums)

#nums.sort(reverse=False)#ascending
#print(nums)
#nums.sort(reverse=True)#descending
#print(nums)

print(sorted(nums, reverse=True)) #global sorted method
print(nums)

numscopy = nums.copy()#1st method
my = list(nums)
mycopy = nums[:]#2nd method of copying
print(numscopy)
print(my)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1,"Neil",True]) #constructor
print(mylist)