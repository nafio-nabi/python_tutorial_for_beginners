# hours
# global scope variables
calculation_to_units = 24
name_of_unit = "hours"

# define function
# parameters are local scope variables
def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}.")
    print(custom_message)

# define function
def scope_check():
    # global variable.
    print(name_of_unit)
    # local variable.
    my_var = "This is a local variable"
    print(my_var)
    print(num_of_days)

# call function
# error: NameError
scope_check()