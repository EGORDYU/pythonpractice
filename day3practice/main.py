print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child ticket is $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7")
    elif age >= 45 and age <= 50:
        bill = 0
        print("Your ticket is free!")
    else:
        bill = 12
        print("Adult ticket is $12")
    
    wants_photo = input("Do you want a photo taken?($3) Y or N\n")
    if wants_photo == "Y":
        bill +=3
        print(f"Your total is ${bill}")
    else:
        print(f"Your total is ${bill}")
else:
    print("You need to be taller mate")