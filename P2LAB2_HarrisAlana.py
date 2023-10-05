#Alana Harris
#10/5/23
#Formatting floats


#Get float input to users
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))
num4 = float(input("Enter 4th number: "))

#Display values with f-string
#Display product and average with 0 decimal places
product = int(num1 * num2 * num3 * num4)

average = int((num1 + num2 + num3 + num4) / 4)

#Display product and average with 3 decimal places

print(f"{product:.0f} {average:.0f}")
print(f"{product:.3f} {average:.3f}")
