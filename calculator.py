import math_module as math

def operation():
	num1 = int(input("Please provide a number: "))
	operand = str(input("Please provide a math operator\nex: +, -, *, /\n : "))
	num2 = int(input("Please provide another number: "))

	if operand == "+":
		print(math.add(num1, num2))
	elif operand == "-":
		print(math.subtract(num1, num2))
	elif operand == "*":
		print(math.multiply(num1, num2))
	elif operand == "/":
		print(math.divide(num1, num2))

	again = str(input("Again? Y/N :"))

	if again.lower() == "y" or again.lower() == "yes":
		operation()
	else:
		exit()

operation()