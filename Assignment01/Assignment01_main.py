# ------------------------------------------------------------------------------------------ #
# Title: Assignment01
# Desc: Introduction Assignment
# Change Log: (Who, When, What)
#   SFoley,7/7/2024, Assignment 1 Script Creation
# ------------------------------------------------------------------------------------------ #

# 1 Create 3 variables and assign them a value.

print('-----------------------------------------')
print('1 Create 3 variables and assign them a value.')
my_string: str = 'Pleasure to be working with you through this certificate, I hope to get'
my_integer: int = 100
my_float: float = 4.0

# 2 Create two new integer variables with any values.

print('-----------------------------------------')
print('2 Create two new integer variables with any values.')
int_variable_1: int = 1
int_variable_2: int = 2
int_variable_3: int = int_variable_1 + int_variable_2 #I expect the value of int_variable_3 to be 3.
print(int_variable_3)

# 3 Create two new float variables with any values.

print('-----------------------------------------')
print('3 Create two new float variables with any values.')
float_variable_1: float = 20.5
float_variable_2: float = 50.7
float_variable_3: float = float_variable_1 + float_variable_2 #I expect the value of float_variable_3 to be 71.2.
print(float_variable_3)

# 4 Create two new string variables with any values.

print('-----------------------------------------')
print('4 Create two new string variables with any values.')
string_variable_1: str = 'hold my '
string_variable_2: str = 'beer'
string_variable_3: str = string_variable_1 + string_variable_2 # We all know where this is going "Hold my beer", missed the space in there the first time.
print(string_variable_3)

# 5 Add any integer variable and any float variable from the previous steps, storing the result in a third variable.

print('-----------------------------------------')
print('5 Add any integer variable and any float variable from the previous steps, storing the result in a third variable.')
random_variable_1 = int_variable_3+float_variable_3
print(random_variable_1)
# I would expect this to be 74.2

# 6 Add any integer variable and any string variable from the previous steps, storing the result in a third variable.

#random_variable_2 = int_variable_1 + string_variable_2
#I expect the result to be "2 beer"
#print(random_variable_2)
#Resulted in an error trying to combine both int and str. Most codes will do this automatically but for Python I'd need to convert the int to a string first.

# Part 2 of Assignment
print('=======================')
print('Assignment 01 - Part 2')
print('=======================')

# 1 Print out the types of my_string, my_integer, and my_float.
print('-----------------------------------------')
print('1 Print out the types of my_string, my_integer, and my_float.')
print(type(my_string))
print(type(my_integer))
print(type(my_float))

# 2 Create a string variable and assign it an integer value (value should be in quotes).
print('-----------------------------------------')
print('2 Create a string variable and assign it an integer value (value should be in quotes).')
string_int_variable: str = '54'
print(type(string_int_variable))
new_string_int_variable: int = int(string_int_variable)
print(type(new_string_int_variable))

# 3 Multiply 5 by 7.654321 and round to 3 decimal places. Print out the resulting value.
print('-----------------------------------------')
print('3. Multiply 5 by 7.654321 and round to 3 decimal places. Print out the resulting value.')

float_variable_part2: float = 5*7.654321
print(format(float_variable_part2,'.3f'))

# 4 Use the input function to display a message that says “Enter your name” and places the result in a variable called my_name.
print('-----------------------------------------')
print('4. Use the input function to display a message that says “Enter your name” and places the result in a variable called my_name.')

user_input_name: str = input('Please input your name here: ')
print(user_input_name)

# 5 Use the input function to display a message that says “Enter your favorite number” and places the result in a variable called favorite_number.
print('-----------------------------------------')
print('5. Use the input function to display a message that says “Enter your favorite number” and places the result in a variable called favorite_number.')
favorite_number = input('Enter your favorite number: ')
print(favorite_number)
# Expecting this to be of type String.
print(type(favorite_number))
# I didn't specify what type to put the input into, so it defaulted to string.

# 6 Now, ask the user for two integers (use the input function twice).
print('-----------------------------------------')
print('6. Now, ask the user for two integers (use the input function twice).')
input_variable_int1: int = input(' Please input the first int variable: ')
input_variable_int2: int = input(' Please input the second int variable: ')
sum_of_input_variables = input_variable_int1 + input_variable_int2
# Going to input 15 and 13 for input_variable_int1 and input_variable_int2 respectively. Would expect the sum to be 28 of type int.
print(sum_of_input_variables)
print(type(sum_of_input_variables))
#Still treating the inputs like strings, so it concatenated instead of added.
input_variable_int3: int = int(input(' Please input the first int variable: '))
input_variable_int4: int = int(input(' Please input the second int variable: '))
sum_of_input_variables2 = input_variable_int3 + input_variable_int4
print(sum_of_input_variables2)
print(type(sum_of_input_variables2))

print('Thank you for looking at my code!')