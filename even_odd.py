def even_odd():
	number1 = int(input("Please provide a number: "))
	if number1 % 2 == 0:
		print("Your number is even!")
		again = str(input("Again? Y/N :"))
		if again.lower() == "y" or again.lower() == "yes":
			even_odd()
		else:
			exit()
	else:
		print("Your number is odd!")
		again = str(input("Again? Y/N :"))
		if again.lower() == "y" or again.lower() == "yes":
			even_odd()
		else:
			exit()
even_odd()