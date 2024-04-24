class A:
    def is_prime(n):
    """Function to check if a number is prime."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_magical_prime(n):
        """Function to check if a number is a 'magical' prime."""
        if is_prime(n):
        # Check if the reverse of the number is also prime
            reversed_n = int(str(n)[::-1])  # Reverse the digits of the number
            return is_prime(reversed_n)
        return False
# Test the program
    num = int(input("Enter a number to check if it's a magical prime: "))

    if is_magical_prime(num):
        print(f"{num} is a magical prime!")
    else:
        print(f"{num} is not a magical prime.")
class B(A):
    def is_neon_number(num):
    # Calculate the square of the number
        square = num * num
    
    # Calculate the sum of the digits of the square
        digit_sum = sum(int(digit) for digit in str(square))
    
    # Check if the sum of digits of the square is equal to the original number
        return digit_sum == num

# Get user input for the number to check
    num = int(input("Enter a number to check if it's a neon number: "))

# Check if the number is a neon number and print the result
    if is_neon_number(num):
        print(f"{num} is a neon number.")
    else:
        print(f"{num} is not a neon number.")
class C(A):
        def print_name_in_x_shape(name):
        name_length = len(name)
    
    # Iterate through each character index of the name
        for i in range(name_length):
            # Initialize an empty string for each line of the 'X' shape
            line = ""
        
        # Loop to build the first part of the 'X' pattern
            for j in range(name_length):
                if j == i or j == (name_length - 1 - i):
                    line += name[j]  # Add the character at index j to the line
                else:
                    line += " "  # Add a space if the condition is not met
        
        # Print the line
            print(line)

# Define the name to print in 'X' shape
    name = "tejashwini"

# Call the function to print the name in 'X' shape
    print_name_in_x_shape(name)
    
class D:
    def reverse_string(s):
    # Initialize an empty string to store the reversed string
        reversed_str = ""
    
    # Iterate over each character in the string in reverse order
        for char in s[::-1]:
        # Append each character to the reversed string
            reversed_str += char
    
    return reversed_str

# Test the reverse_string function
    input_string = input("Enter a string to reverse: ")
    reversed_string = reverse_string(input_string)
    print("Reversed string:", reversed_string)
    
class E(B)(D):
    # Define users with email and password
users = [
    {'email': 'cat@gmail.com', 'password': 1234},
    {'email': 'dog@gmail.com', 'password': 5678},
    {'email': 'pig@gmail.com', 'password': 9012}
]

def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    print(f"Deposit successful. Remaining balance: ${account['balance']}")

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']

# Initialize account
account = {
    'balance': 1000,
    'transactions': []
}

# Dictionary to map user choices to functions
choices = {
    '1': deposit,
    '2': withdraw,
    '3': get_balance,
    '4': get_transaction_history
}

# User authentication
uemail = input("Enter your email: ")
upwd = int(input("Enter your password: "))

flage=0
for user in users:
    if user['email'] == uemail and user['password'] == upwd:
        flage=1
        break

if flage==0:
    print("Invalid email or password. Access denied.")
else:
    # Main banking operations loop
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '5':
            print("Exiting program.")
            break

        if choice in choices:
            if choice == '1' or choice == '2':
                amount = float(input("Enter amount: "))
                choices[choice](account, amount)
            else:
                print(choices[choice](account))
        else:
            print("Invalid choice. Please try again.")

class info:
    a=A
    a.is_prime
    a.
    