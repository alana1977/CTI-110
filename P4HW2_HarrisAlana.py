#Alana Harris
#11/2/23
#Uses if/else statements

#Get employee name from user

name = input("Enter your name: ")

num_employees = 0

total_pay = 0

while name != "Done":
    
    num_employees = num_employees + 1

    #Get number of hours from the user

    num_hours = int(input("Enter number of hours worked: "))
    ot_hours = 0

    #Get pay rate per hour

    reg_payrate = float(input("Enter your pay rate per hour: "))

    #Determine if employee worked more than 40 hours
    #Calculate regular hours worked

    if num_hours < 40:
        reg_hours = num_hours
    else: reg_hours = 40

    #Calculate OT hours worked

    if num_hours > 40:
        ot_hours = num_hours - 40
    else: ot_hours = 0

    #Calculate pay rate for overtime hours

    if num_hours > 40:
        ot_payrate = reg_payrate * 1.5
    else: ot_payrate = 0

    #Calculate pay for regular hours

    reg_pay = reg_hours * reg_payrate

    #Calculate pay for OT hours

    ot_pay = ot_hours * ot_payrate

    #Calculate gross pay

    gross_pay = ot_pay + reg_pay

    total_pay += gross_pay

    #Display name, pay rate, regular hours, OT hours, OT pay, gross pay

    print("Employee name: ", name)
    print("Hours worked: ", num_hours)
    print("Regular hours worked: ", reg_hours)
    print("Pay Rate: ", reg_payrate)
    print("Overtime hours: ", ot_hours)
    print("Overtime Pay: ", ot_pay)
    print("Regular Hour Pay: ", reg_pay)
    print("Gross Pay: ", gross_pay)

    #Ask user to re-enter to reassign new name to variable

    name = input("Enter your name: ")

print(f'The number of employees entered is {num_employees}')

print(f'The total payment of all employees is {total_pay}')
