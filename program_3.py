# Naomi Puyleart
# 10/17/25
# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example, it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    rows = int(input("Enter the number of lists you would like to input: "))
    all_entered_values = []
    for i in range(rows):
        row = []
        year = int((input("Enter the year for row {}: ".format(i+1))))
        row.append(year)
        state = (input("Enter the state for row {}: ".format(i+1))).upper()
        row.append(state)
        population = int((input("Enter the population for row {}: ".format(i+1))).upper())
        row.append(population)
        all_entered_values.append(row)

    # Now have the user enter a year.
    print("Here are all of the values you entered: ", all_entered_values)
    total_population_year = int(input("What year would you like the total population of? "))
    sum_population_for_year(all_entered_values, total_population_year)
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

def sum_population_for_year(all_entered_values, year_to_sum):
    pass
    # Loop through and sum the populations for the appropriate year.
    # e.g. for the list on line 7 the total would be 8,860,637 if the user entered 2010 for the year to sum,
    # or 3,421,988 if they entered 2011 for the year to sum.
    total_pop = 0
    for entry in all_entered_values:
        if entry[0] == year_to_sum:
            total_pop += entry[2]
    # print the totalled population
    print("The total population of the year you entered is:", total_pop)

# Call the main function.
if __name__ == '__main__':
    main()