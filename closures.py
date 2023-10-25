# Closure is a fn have access to scope of its parent fn after parent fn has returned.

def parent_fn(person, coins):
    #coins = 2

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left. ")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coins left. ")   
        else:
            print("\n" + person + " is out of coins ")

    return play_game

tom = parent_fn("Tom", 3)
jenny = parent_fn("jenny", 5)
tom()
jenny()
