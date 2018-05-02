def review():
	answer = (str(input("Would you like to go again? Y/N : "))).lower()
	if answer == "y":
		fizzbuzz()
	else:
		exit()
def fizzbuzz():
	divisor = int(input("Please input a number: "))
	if divisor % 3 == 0 and divisor % 5 == 0:
		print("Fizz Buzz")
		review()
	elif divisor % 5 == 0:
		print("Buzz")
		review()
	elif divisor % 3 == 0:
		print("Fizz")
		review()
	else:
		print("You get nothing!")
		review()
		
fizzbuzz()