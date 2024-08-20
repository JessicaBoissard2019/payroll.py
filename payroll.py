"""
Program: payroll.py
Chapter2 practice project (page 63)
Jessica Boissard
7/24/2024
Application that needs inputs for hourly wage, regular hours worked and overtime hours for an employee. It should output the total weekly pay.
"""

# Input phase
wage = float(input("Please enter you hourly wage: "))
regHours = float(input("How many regular hours have you worked this week?: "))
otHours = float(input("Enter any overtime hours worked, enter 0 for none: "))

#Processing phase
totalPay = (regHours * wage) + (otHours * wage * 1.5)

#Output phase
print("\nThe total weekly pay is $" + str(round(totalPay, 2)))

input("\nPress Enter to exit this program...")

