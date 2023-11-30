import random
import string





all_letters = list(string.ascii_letters)  # This includes 'a' to 'z' and 'A' to 'Z'
all_numbers = list(string.digits)  # This includes '0' to '9'
common_symbols = list(string.punctuation)  # This includes symbols like '@', '#', '$', etc.

print("Welcome to my PyPassword Generator!")
letters_input = input("How many letters would you like in your password?")
letters = int(letters_input)  # GETS ME A NUMBER 

symbols_input = input("How many symbols would you like?")
symbols = int(symbols_input) # GETS ME A NUMBER 

numbers_input = input("How many numbers would you like?")
numbers = int(numbers_input) # GETS ME A NUMBER 

password = ""


# for i in all_letters[letters] :

#     password += str(i)

for i in range(letters):
    random_number = random.randint(0,len(all_letters)-1)
    password += all_letters[random_number]


for i in range(numbers):
    random_number = random.randint(0,len(all_numbers)-1)
    password += all_numbers[random_number]

for i in range(symbols) :
    random_number = random.randint(0,len(common_symbols)-1)
    password += common_symbols[random_number]

password = list(password)
random.shuffle(password)
password = ''.join(password)
print(password)




