import random
print("Who has a higher banrate")
##Make dictionary
ban_rates = {
    "Draven": ("ADC",37.12),
    "Yone":("Mid or Top",14.69),
    "Rammus":("Jungle", 6.38),
    "Zed":("Mid", 16.00),
    "Fiora":("Top", 14.24),
    "Syndra": ("Middle", 18.84),
    "Jax":("Top", 22.91),
    "Karthus":("Jungle",1.85),
    "Tristana":("ADC",0.57),
    "Skarner":("Jungle",0.07),
    "Illaoi":("Top",9.43),
    "Senna":("Support",15.74),
    "Blitzcrank":("Support",18.75)
}

##Keep track of score

##Make function to select old one and new random key in object
score = 0
game_going = True

def play_game(ban_rates):
    global game_going  
    global score


    modified_banrates = dict(ban_rates)
    initial_pick = random.choice(list(modified_banrates.items()))
    modified_banrates.pop(initial_pick[0])

    comparing_pick = random.choice(list(modified_banrates.items()))
    

    print("Current pick:", initial_pick[0], initial_pick[1],"\n")
    print("Comparing pick:", comparing_pick[0], comparing_pick[1][0],"?\n")


    higher_lower = input(f"Do you think that {initial_pick[0]} has a higher banrate than {comparing_pick[0]}? Type 'y' or 'n'.")

    while game_going and modified_banrates:
        if (higher_lower == 'y' and initial_pick[1][1] > comparing_pick[1][1]) or (higher_lower == 'n' and initial_pick[1][1] < comparing_pick[1][1]):
            print(f"Correct! {initial_pick}% and {comparing_pick}% Next comparison.\n")
            if comparing_pick[1][0] > initial_pick[1][0]:
                initial_pick = comparing_pick
            score+=1
            print(f"Score = {score}\n")
            modified_banrates.pop(comparing_pick[0])
            comparing_pick = random.choice(list(modified_banrates.items()))
            print(f"Current pick:", initial_pick[0], initial_pick[1],"\n")
            print(f"Comparing pick:", comparing_pick[0], comparing_pick[1][0],"?\n")

            higher_lower = input(f"Do you think that {initial_pick[0]} has a higher banrate than {comparing_pick[0]}? Type 'y' or 'n'.")
        else:
            print("You lost!!!\n")
            print(f"Score {score}\n")
            game_going = False


play_game(ban_rates)


