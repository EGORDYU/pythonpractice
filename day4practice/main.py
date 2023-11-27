# import random
# import my_module


# random_integer = random.randint(1,10)
# print(random_integer)


# print(random.random())

# random_float = random.random() * 5


# love_score = random.randint(1,100)
# print(f"Your love score is {love_score}")


fruits = ["Cherry","Apple","Pear"]

fruits[2] = "Pickle Johnson"
fruits.append("YEEHAYWWWW")
fruits.extend(["Banana","Kindred"])

print(fruits)
print(fruits[1])

starcraft_units = [["zealot"],["zergling"],["marine"]]


print(starcraft_units)




line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

coordinates = list(position)

letter = coordinates[0]
number = int(coordinates[1])

if letter == "A":
  letter = 0
elif letter == "B":
  letter = 1
elif letter == "C":
  letter = 2
  




map[number-1][letter] = "X"


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")