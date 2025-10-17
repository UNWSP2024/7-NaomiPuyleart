# Naomi Puyleart
# 10/17/25
# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months
# into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

def get_rainfall():
    rainfall = []
    for i in range(12):
        value = float(input("Enter the rainfall for the month in inches: "))
        rainfall.append(value)

    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / 12
    highest_rainfall = max(rainfall)
    lowest_rainfall = min(rainfall)

    print("The total rainfall in inches is: ", total_rainfall)
    print("The average rainfall in inches is: ", average_rainfall)
    print("The highest rainfall in inches is: ", highest_rainfall)
    print("The lowest rainfall in inches is: ", lowest_rainfall)

get_rainfall()