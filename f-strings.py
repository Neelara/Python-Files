person = "Neela" #format_strings
coins = 3

print("\n" + person + " has " + str(coins) + " coins left. ")

msg = "\n%s has %s coins left." % (person, coins)
print(msg)
msg = "\n{} has {} coins left." .format(person, coins)
print(msg)
msg = "\n{1} has {0} coins left." .format(person, coins) #using index of person and coins
print(msg)
msg = "\n{person} has {coins} coins left." .format(person=person, coins=coins) #using index 
print(msg)

player = {'person': 'Neela', 'coins': 3} #Dict Method

msg = "\n{person} has {coins} coins left." .format(**player) #using index 
print(msg)

msg = f"\n{person} has {coins} coins left."
print(msg)
msg = f"\n{person} has {2*5} coins left."
print(msg)
msg = f"\n{person.lower()} has {2*5} coins left."
print(msg)
msg = f"\n{player['person']} has {2*5} coins left."
print(msg)

#pass formatting options
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.4f}") #2.25 times 10 is 22.5000

for num in range(1,11):
    print(f"\n2.25 times {num} is {2.25 * num:.4f}")
for num in range(1,11):
    print(f"\n{num} is divided by 4.52 is {num/ 4.52:.2%}")