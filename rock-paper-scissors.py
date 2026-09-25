"""
WORKFLOW OF PROJECT:
1- Input from user (Rock, paper, scissor)
2- Computer choice (Computer will choose randomly, not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - Scissor = Rock win

B-Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""

import random

item_list = ["Rock", "Paper", "Scissor"]

User_choice = input("Enter your move = Rock, Paper, Scissor: ")

Comp_choice = random.choice(item_list)

print(f"User choice = {User_choice}, Computer choice = {Comp_choice}")

if User_choice == Comp_choice:
    print("Both chose the same: Match Tie")

elif User_choice == "Rock":
    if Comp_choice == "Paper":
        print("Paper covers Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You Win")

elif User_choice == "Paper":
    if Comp_choice == "Scissor":
        print("Scissor cuts Paper = Computer Win")
    else:
        print("Paper covers Rock = You Win")

elif User_choice == "Scissor":
    if Comp_choice == "Paper":
        print("Scissor cuts Paper = You Win")
    else:
        print("Rock smashes Scissor = Computer Win")
            
          
         
          
     