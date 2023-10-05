#Alana Harris
#10/5/23
#Introduction to dictionaries

#Get user input
name = input("Enter your name: ")
hair = input("Enter your hair color: ")
eye = input("Enter your eye color: ")
height = float(input("Enter your height: "))
age = int(input("Enter your age: "))
food = input("Enter your favorite food: ")

#Create a dictionary

my_dict = {"Name":name, "hair_color":hair, "eye_color":eye, "Height":height, "Age":age, "favorite_food":food}

#Get value using key

print(f"{my_dict['Name']} is a {my_dict['Height']} tall student with {my_dict['hair_color']} hair and {my_dict['eye_color']} eyes. They are {my_dict['Age']} years old and their favorite food is {my_dict['favorite_food']}.")
