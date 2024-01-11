name = input("Hello! Please input a name: \n")
age = int(input("Please input an age: \n"))
while(True):
	if(age < 0 or age > 122):
		age = int(input("Error with age, please input a new age: \n"))
	elif(0 <= age and age <= 15):
		yrsToLicense = 16 - age
		print(name + " must wait " + str(yrsToLicense) + " more years to get a driver’s license!")
		break
	elif(age == 16):
		print("Congrats! " + name + " can get their driver’s license now!")
		break
	elif(17 <= age and age <= 122):
		yrsSinceEligible = age - 16
		print(name + " has been elligible for a driver's license for " + str(yrsSinceEligible) + " years!")
		break






