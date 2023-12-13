import random


playing = False

player_score = 0
ai_score = 0

cards = {
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:10,
    "Jack":10,
    "Queen": 10,
    "King": 10
}

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

if play == "y":
    playing = True
elif play == "n":
    playing = False


def draw_cards(amount):
    drawn_names = random.sample(list(cards.keys()), amount)  # Draw card names
    drawn_values = [cards[name] for name in drawn_names]  # Get corresponding values
    score = sum(drawn_values)  # Calculate score
    return drawn_names, score


def draw_more(current_score, entity):
    drawn_names, additional_score = draw_cards(1)
    if entity == "Player":
        player_score = current_score + additional_score
        print(f"Player drew: {drawn_names}, Updated score: {player_score}")
    elif entity == "Computer":
        ai_score = current_score + additional_score
        print(f"Computer drew: {drawn_names}, Updated score: {ai_score}")


def determine_winner(ai_score, player_score):
    if player_score == 21:
        print("Player wins")
    elif player_score > 21:
        print("You lose!")
    elif ai_score > player_score and ai_score < 21:
        print("You lose!")
    elif player_score > ai_score and player_score < 21:
        print("Player wins!")
    else:
        print("You lose!")

def deal(cards):
    player_names, player_score = draw_cards(2)
    ai_names, ai_score = draw_cards(1)
    print(f"Your cards: {player_names}, Score: {player_score}")
    print(f"Computer's first card: {ai_names}, Score: {ai_score}")
    hitme = input("Type 'y' to get another card, type 'n' to pass:")
    
    if hitme.lower() == "y":
        draw_more(player_score, "Player")
        draw_more(ai_score, "Computer")
    elif hitme.lower() == "n":
        draw_more(ai_score, "Computer")



    

        

deal(cards)
determine_winner(ai_score, player_score)

# while playing == True:
#     print(""" _     _            _    _            _    
# | |   | |          | |  (_)          | |   
# | |__ | | __ _  ___| | ___  __ _  ___| | __
# | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# | |_) | | (_| | (__|   <| | (_| | (__|   < 
# |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\|""")
#     playing = False
    