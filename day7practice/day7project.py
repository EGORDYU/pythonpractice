import random


wordlist = ["leesin","diana","warwick","viego","bigb"]

random_list = random.randint(0,len(wordlist))

chosen_word = wordlist[random_list-1]
lives = 10



answer = ["_ " for _ in chosen_word]
letters_of_word = list(chosen_word)

guessed_letters = []





while lives > 0:
    correct_letters = "".join(answer)
    guess = input(f"Guess a letter of the word with {len(answer)} letters {correct_letters}\n")
    guess.lower()
    if len(guess) > 1:
        print("Please submit a one letter answer")
    elif not guess.isalpha():
        print("Please put in a letter nothing else..")
    elif guess in letters_of_word:
        print(f"You the letter {guess}!")
        index_of_letters = [index for index, letter in enumerate(letters_of_word) if letter == guess]
        for index in index_of_letters:
            answer[index] = guess
        guessed_letters.append(guess)
        guessed_letters.sort()
        print(f"Guessed letters {guessed_letters}")
        if not answer.__contains__("_ "):
            lives = 0
            print(f"You won the game! The word was {chosen_word}")
    else:
        print("Try again..")
        print(f"Lives left {lives-1}")
        guessed_letters.append(guess)
        guessed_letters.sort()
        print(f"Guessed letters {guessed_letters}")
        lives -= 1

