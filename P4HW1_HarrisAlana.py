#CTI-110
#Alana Harris
#10/31/23
#Working with lists and for loops

#Create variables and get user input (6)

num_grades = int(input("How many grades will you enter?: "))

#Create an empty list

grade_list = []

for grade in range(num_grades):
    this_grade = int(input("Enter a grade: "))
    while this_grade < 0 or this_grade > 100:
        print("Invalid grade entered.")
        this_grade = int(input("Enter a grade: "))
              
    grade_list.append(this_grade)
    print(f"{this_grade} has been added to the list")

for grade in grade_list:
    print(grade)
    



#Calculate min, max, sum, and average / assign to variables

min_grade = min(grade_list)
max_grade = max(grade_list)
sum_grade = sum(grade_list)
avg_grade = sum(grade_list) / len(grade_list)

#Display info to user / use print statements

print()
print("------------Results------------")
print("Lowest Grade: ", min_grade)
print("Highest Grade: ", max_grade)
print("Sum of Grades: ", sum_grade)
print("Average: ", avg_grade)
