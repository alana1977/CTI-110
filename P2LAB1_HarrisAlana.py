#Alana Harris
#10/3/23
#Uses floats and expressions to calculate gas cost

#Create input variables

mpg = float(input("Enter the car's mph: "))
cost_per_gallon = float(input("How much does a gallon of gas cost: "))

#Calculate gas cost based off gallons needed and price per gallon
#Calculate for 20 miles, 75 miles, and 100 miles

cost_20 = (20 / mpg) * cost_per_gallon
cost_75 = (75 / mpg) * cost_per_gallon
cost_500 = (500 / mpg) * cost_per_gallon

#Output values using f string and format the floats

print(f"{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}")
