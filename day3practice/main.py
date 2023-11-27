print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?\n"))


if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Your ticket is $5")
    elif age <= 18:
        print("Your ticket is $7")
    else:
        print("Your ticket is $12")
else:
    print("You need to be taller mate")