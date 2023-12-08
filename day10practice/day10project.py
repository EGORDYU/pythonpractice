#calculator


print("welcome to calculator")

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

# # Dictionary mapping operation symbols to corresponding functions
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }

# def calculator(number1, operation, number2):
#     # Check if the operation is in the dictionary
#     if operation in operations:
#         # Call the function corresponding to the operation
#         return operations[operation](number1, number2)
#     else:
#         print("Enter a valid operator.")
#         return None

def calculator(number1, operation, number2):

    if operation == "+":
       calculation = number1 + number2
    elif operation =="-":
        calculation = number1 - number2
    elif operation == "*":
        calculation = number1 * number2
    elif operation == "/":
        calculation = number1 / number2
    else:
        print("Enter a valid operator.")
    return calculation


number1 = int(input("What is the first number? "))


while True:
    operation = input("+\n-\n*\n/\nPick an operation: ")
    number2 = int(input("What is the second number? "))

    result = calculator(number1, operation, number2)

    if result is not None:
        print(f"The result is: {result}")
        cont = input(f"Type 'y' to continue calculating with the number {result}, or type 'n' to start a new calculation: \n")
        if cont.lower() != 'y':
            break
        else:
            number1 = result
    else:
        print("Invalid input. Starting over.")