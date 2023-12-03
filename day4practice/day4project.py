import random

player_num = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
player_choice = int(player_num)


choices = ["Rock", "Paper", "Scissors"]


player_pick = choices[player_choice]
print(f"You chose {player_pick}")





ai_choice = random.randint(0,2)
ai_pick = choices[ai_choice]
print(f"AI chose {ai_pick}")



if player_choice == 0 and ai_choice == 2:
    print("You won!")
elif player_choice == 2 and ai_choice ==1:
    print("You won!")
elif player_choice == 1 and ai_choice ==0:
    print("You won!")
elif player_choice == ai_choice:
    print("It's a tie!")
else:
    print("You lost!")

# win_conditions = {
#     "Rock": "Scissors",  # Rock crushes Scissors
#     "Scissors": "Paper",  # Scissors cuts Paper
#     "Paper": "Rock"      # Paper covers Rock
# }

# if player_pick == ai_pick:
#     print("It's a tie!")
# elif win_conditions[player_pick] == ai_pick:
#     print("You won!")
# else:
#     print("You lost!")