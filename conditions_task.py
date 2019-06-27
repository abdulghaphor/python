v1 = input("Enter the first number: ")
v2 = input("Enter the second number: ")
if v1.isdigit() == True & v2.isdigit() == True:
	v1 = int(v1)
	v2 = int(v2)
	o = input("Choose the operation (+, -, /, *): ")
	if o == "*":
		r = v1 * v2
		print("The answer is:",r)
	elif o == "+":
		r = v1 + v2
		print("The answer is:",r)
	elif o == "-":
		r = v1 - v2
		print("The answer is:",r)
	elif o == "/":
		r = v1 / v2
		print("The answer is:",r)
else:
	print("ERROR")
