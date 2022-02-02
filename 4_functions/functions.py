# hours
calculation_to_units = 24
name_of_unit = "hours"

# define function
def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}.")
    print(custom_message)

# call function
days_to_units(20, "Looks good.")
days_to_units(35, "Looks okay.")

# error: TypeError
# days_to_units()