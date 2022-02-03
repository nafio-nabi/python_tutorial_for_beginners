# defination of a module
def days_to_units(num_of_days, conversion_unit):
    """Convert days to units"""
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}."
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit}."
    else:
        return "Unsupported unit"

# defination of a module
def validate_and_execute(days_and_units_dictionary):
    try:
        user_input_number = int(days_and_units_dictionary["days"])
        # we want to do conversions only for positive integers.
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_units_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered zero, please enter a valid positive number.")
        else:
            print("You entered a negative number, please enter a valid positive number.")
    except ValueError:
        print("Your input is not a valid number. Please enter a positive number.")

# defination of a module
user_input_message = "Enter number of days as a comma seperated list: "