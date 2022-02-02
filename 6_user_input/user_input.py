# hours
calculation_to_units = 24
name_of_unit = "hours"

# define function
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}."

# call function
user_input = input("Enter number of days: ")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)