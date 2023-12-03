print("Welcome to the tip calculator")
total_bill = int(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))

split = int(input("How many people to split the bill?"))


calculation = ((total_bill + (total_bill/tip)) / split)

print(f"Each person should pay: ${calculation}")