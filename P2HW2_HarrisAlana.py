#CTI-110
#Alana Harris
#10/10/23
#Working with lists

#Create variables and get user input (6)

mod1_grade = int(input("Enter your Module 1 grade: "))
mod2_grade = int(input("Enter your Module 2 grade: "))
mod3_grade = int(input("Enter your Module 3 grade: "))
mod4_grade = int(input("Enter your Module 4 grade: "))
mod5_grade = int(input("Enter your Module 5 grade: "))
mod6_grade = int(input("Enter your Module 6 grade: "))

#Create an empty list

grades_list = []

#Add variables to list

grades_list.append(mod1_grade)
grades_list.append(mod2_grade)
grades_list.append(mod3_grade)
grades_list.append(mod4_grade)
grades_list.append(mod5_grade)
grades_list.append(mod6_grade)

#Calculate min, max, sum, and average / assign to variables

min_grade = min(grades_list)
max_grade = max(grades_list)
sum_grade = sum(grades_list)
avg_grade = sum(grades_list) / len(grades_list)

#Display info to user / use print statements

print()
print("------------Results------------")
print("Lowest Grade: ", min_grade)
print("Highest Grade: ", max_grade)
print("Sum of Grades: ", sum_grade)
print("Average: ", avg_grade)
