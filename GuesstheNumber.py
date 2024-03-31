import random
NumberGuess = []
Number = list(range(1,21))

def guess(chosen):
    NumberGuess.append(chosen)
    a = random.choice(Number)
    while chosen != a:
        NumberGuess.append(chosen)
        print("Wrong, the number was", a)
        a = random.choice(Number)
        chosen = int(input("Pick another number: "))
    print("You got it! It took you", len(NumberGuess), "tries")
        
        
        
    

chosen = int(input("Enter a number: ")  )  
guess(chosen)
    

    





