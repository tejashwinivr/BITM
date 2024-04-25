'''
#divisible by 5
def binary_number(sequence):
    binary_numbers = sequence.split(',')
    result = []

    for binary in binary_numbers:
        decimal_number = int(binary, 2)
        if decimal_number % 5 == 0:
            result.append(binary)

    return ','.join(result)

input_sequence = input("Enter a sequence of comma-separated 4-digit binary numbers: ")
print("Numbers divisible by 5:", binary_number(input_sequence))



#calculate the number of digits and alphabets
input_string=input("enter the string:")
letter=0
digit=0
or char in input_string:
    if char.isalpha():
        letter+=1
    elif char.isdigit():
         digit+=1
print("number of letter=",letter)
print("number of digit=",digit)


#password
import re
def check_password(password):
    # Length should be between 6 and 20 characters
    if len(password) < 6 or len(password) > 20:
        return False
    
    # Should contain at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # Should contain at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False

    # Should contain at least one digit
    if not re.search(r"\d", password):
        return False

    # Should contain at least one special character
    if not re.search(r"[!@#$%^&*()]", password):
        return False

    return True

# Get password input from user
password = input("Enter your password: ")

# Check password validity
if check_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")


#E pattern
def print_e_pattern(n):
    for i in range(n):
        if i == 0 or i == n // 2 or i == n - 1:
            print("*" * (n - 1))
        else:
            print("*")

# Get user input for size of the pattern
size = int(input("Enter the size of the pattern: "))
print_e_pattern(size)
'''

# month number
def months(month):
    if month==jan or month==mar or month==may or month==july or month==aug or month==oct or month==dec:
        print("no of days are 31")
    elif month==april or month==june or month==sep or month==nov:
        print("no of days are 30")
    else:
        print("no of days are 29/28")
m=input("enter the month:")
months(m)