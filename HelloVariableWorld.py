# Create a variable called 'name' that holds a string
from operator import truediv


name = "Steve"

# Create a variable called 'country' that holds a string
country = "America"

# Create a variable called 'age' that holds an integer
age = "18"

# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = "20"

# Calculate the daily wage for the user
daily_wage = int(hourly_wage)*8

# Create a variable called 'satisfied' that holds a boolean
satisfied = True
unsatisfied = False


# Print out "Hello <name>!"
print (f'"Hello {name}!"')

# Print out what country the user entered
print (f'{name} entered {country}')

# Print out the user's age
print (f'{name} is {age} years old')


# With an f-string, print out the daily wage that was calculated
print(f'{name} only makes {daily_wage} per day.')


# With an f-string, print out whether the users were satisfied
print (f'{name}'is {True}')'
