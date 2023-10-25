name = "Dave" #global 
count = 2 # we can't declare it in global and incremenet in local it causes UnboundLocal Error

def another():
    color = "red"
    global count #it is possible
    count +=1
    print(count)
    def greeting(name): #nested fn
         nonlocal color #we will reassign value using this fn
         color = "blue"
         print(name) #John
         print(color) #blue
         print(name) #John
         
    greeting("Dave")

another()

