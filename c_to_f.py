def get_faren():
	temperature = float(input("What temperature in celsius would you like to convert? "))
	converted = ((temperature * 1.8) + 32)
	print(converted)
	return converted

def get_celsius():
	temperature = float(input("What temperature in fahrenheit would you like to convert? "))
	converted = ((temperature - 32) * (5/9))
	print(converted)
	return converted

convert = str(input("What conversion would you like to do?\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n")).lower()

if convert == "1" or convert == "1." or convert == "celsius to fahrenheit":
	get_faren()
elif convert == "2" or convert == "2." or convert == "fahrenheit to celsius":
	get_celsius()