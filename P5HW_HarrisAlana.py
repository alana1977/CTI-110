import random

def adding():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    random_sum = num1 + num2
    print(" ", num1)
    print("+", num2)
    return random_sum

def subtracting():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    random_sum = num1 - num2
    print(" ", num1)
    print("-", num2)
    return random_sum

def menu():
    print("Welcome to Math Quiz")
    print()
    print()
    print()
    print("MAIN MENU")
    print("----------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()

def main():
    menu()
    num_guess = 1
    menu_choice = int(input("Please choose one of the menu options: "))
    while menu_choice != 3:
        if menu_choice == 1:
            adding_sum = adding()
            print()
            user_guess = int(input("Enter answer: "))
            print()
            while user_guess != adding_sum:
                if user_guess > adding_sum:
                    print("Guess is too high")
                    print()
                    user_guess = int(input("Enter answer: "))
                    num_guess = num_guess + 1
                else:
                    print("Guess is too low")
                    print()
                    user_guess = int(input("Enter answer: "))
                    num_guess = num_guess + 1
            print()
            print("Your answer is correct")
            print("Number of guesses: ", num_guess)
            print()
            menu()
            num_guess = 1
            menu_choice = int(input("Please choose one of the menu options: "))
        

        
        if menu_choice == 2:
            subtract_sum = subtracting()
            print()
            user_guess = int(input("Enter answer: "))
            print()
            while user_guess != subtract_sum:
                if user_guess > subtract_sum:
                    print("Guess is too high")
                    print()
                    user_guess = int(input("Enter answer: "))
                    num_guess = num_guess + 1
                else:
                    print("Guess is too low")
                    print()
                    user_guess = int(input("Enter answer: "))
                    num_guess = num_guess + 1
            print()
            print("Your answer is correct")
            print("Number of guesses: ", num_guess)
            print()
            menu()
            num_guess = 1
            menu_choice = int(input("Please choose one of the menu options: "))
    print()
    print("Thank you for playing!!!")
    
main()

