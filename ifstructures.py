gpa = int(input("Enter your gpa: "))

if gpa < 4 and gpa >= 0:
	print("Failed")

elif gpa >= 8 and gpa < 10:
	print("Grade: B")

elif gpa >= 6 and gpa < 8:
	print("Grade: B")

elif gpa >= 4 and gpa < 6:
	print("Grade: C")

elif gpa == 10:
	print("Grade: Perfect 10")

else:
	print("The gpa value is not valid")