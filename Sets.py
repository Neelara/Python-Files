nums = {1,2,3,4,5}
num2 =set((1,2,3,4,5))
print(nums)
print(type(num2))
print(len(nums))

# No duplicates allowed
nums = {1,2,3,3}
print(nums) #{1, 2, 3}
# True is a dupe of 1, False is a dupe of 0
nums = {1,12,True, 3,False,0,7} #False = 0 True = 1
print(nums) #{False, 1, 3, 7, 12}

#check if value in set
print(12 in nums)
#but u can't refer to an element in set with an index position or a key

#Add a new element to set
nums.add(8)
print(nums)

#Add more elements from one set to another
more = {5,6,7}
nums.update(more)
print(nums) #{False, 1, 3, 5, 6, 7, 8, 12}

#you can use update with lists, tuples, and dicts too.
#merging of sets to form new set
one = {1,2,3,4}
one1 = {7,8,9}
myset = one.union(one1)
print(myset)#{1, 2, 3, 4, 7, 8, 9}
#keep only duplicates
one = {1,2,3,}
one_1 = {2,3,4}
one.intersection_update(one_1)
print(one) #{2, 3} we won't store in variables

#keep everything except duplicates
one = {1,2,3}
one_1 = {2,3,4}
one.symmetric_difference_update(one_1)
print(one) #{1, 4}

