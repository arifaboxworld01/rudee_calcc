# Python calculator

while True:
    operator = input('Enter an operator (+, -, *, /): ').strip()
    if operator in ("+", "-", "*", "/"):
        break
    print("Input is invalid, please type a valid operator.")

num1 = float(input('Enter 1st number'))
num2 = float(input('Enter 2nd number'))


if operator == "+":
   result = num1 + num2
   print(result)
elif operator == "-":
    result = num1 -num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
#testing