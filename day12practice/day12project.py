import random




print("Welcome to the Number Guessing Game!\nIm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty Type 'easy' or 'hard':")
number = random.randint(1,100)
attempts = 0

def play_game(difficulty):


    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        return
        
    
    def guess(attempts):
        while attempts > 0:
            player_guess = int(input(f"Guess the number you have {attempts} attempts left:"))
            if player_guess != number:
                attempts-=1
                if attempts == 0:
                    print("You lost!!!")
                if player_guess > number:
                    print("Your number is too high!")
                elif player_guess < number:
                    print("Your number is too low!")
            elif player_guess == number:
                print("YOU WON!!!")
                attempts = 0
        
    
    
    guess(attempts)
    
def restart():
    if attempts == 0 and difficulty == "easy" or difficulty == "hard":
        again = input("Try again? 'y'/'n'")
        if again == "y":
            number = random.randint(1,100)
            print(number)
            play_game(difficulty)
            restart()
        elif again == "n":
            print("Better luck next time!")

play_game(difficulty)
restart()