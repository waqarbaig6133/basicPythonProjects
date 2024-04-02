#Rock paper scissors basic python code

import random
options = ['scissors', 'paper', 'rock']

me = 0
comp = 0

#Game goes up to 5 points
while me <5 and comp <5:
    my_choice = input("Pick rock, paper or scissors: ")
    comp_choice = random.choice(options)

    winning_conditions = [
        (my_choice == "rock" and comp_choice == "scissors"),
        (my_choice == "paper" and comp_choice == "rock"),
        (my_choice == "scissors" and comp_choice == "paper")
        ]
    losing_conditions = [
        (comp_choice == "rock" and my_choice == "scissors"),
        (comp_choice == "paper" and my_choice == "rock"),
        (comp_choice == "scissors" and my_choice == "paper")
        ]
    for n in winning_conditions:
        if n == True:
            me+=1
            print("You got a point!")
            print(me)
            print(comp)
    for n in losing_conditions:
        if n == True:
            comp +=1
            print("It got a point!")
            print(me)
            print(comp)
    if my_choice == comp_choice:
        print("Both chose", comp_choice)
        print(me)
        print(comp)
    if my_choice not in options:
        print("Pick rock paper or scissors")

if me == 5:
    print("You won!")
else:
    print("You lose!")
        
            
    
    
    
