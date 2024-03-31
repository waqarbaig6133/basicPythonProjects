import random
b = ["1" ,"2" ,"3" ,"4" ,"5" ,"6", "7", "8", "9"]
me = []
comp = []
winning_conditions = [ ["1", "4", "7"], ["1","2","3"], ["1","5", "9"], ["3","5","7"], ["3","5","9"],["3","6","9"],["7","8","9"],["2","5","8"]]

def winning():
    for n in winning_conditions:
        if all(elem in me for elem in n):
            print("You win!")
            return True
    return False

def losing():
    for n in winning_conditions:
        if all(elem in comp for elem in n):
            print("You lose!")
            return True
    return False
square = 0
for i in range(1,9):
    e = input("pick a square: ")
    b.remove(e)
    me.append(e)
    square+=1
    
    if winning():
        break


    
    f = random.choice(b)
    print("Opponent chose", f)
    b.remove(f)
    comp.append(f)
    square+=1
    
    if losing():
        break
    
    if square == 8:
        print("draw")
        break
