calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}."

# get user input
user_input = input("Enter number of days: ")
# convert user input from string to integer
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)