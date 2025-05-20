# Version 1: Conditional test in the while statement
while True:
    age = int(input("Please enter your age (or enter a negative number to stop): "))
    
    if age < 0:
        print("Stopping the program.")
        break
    elif age < 3:
        print("Your movie ticket is free!")
    elif 3 <= age <= 12:
        print("Your movie ticket costs $10.")
    else:
        print("Your movie ticket costs $15.")


# Version 2: Active variable to control how long the loop runs
count = 5  # Loop will run 5 times

while count > 0:
    age = int(input(f"Please enter your age ({count} attempts left): "))
    
    if age < 3:
        print("Your movie ticket is free!")
    elif 3 <= age <= 12:
        print("Your movie ticket costs $10.")
    else:
        print("Your movie ticket costs $15.")
    
    count -= 1  # Decrement the active variable

print("Thanks for using the movie ticket program!")


# Version 3: Using break to exit the loop on 'quit'
while True:
    user_input = input("Please enter your age (or type 'quit' to exit): ")
    
    if user_input.lower() == 'quit':
        print("Exiting the program.")
        break
    
    age = int(user_input)
    
    if age < 3:
        print("Your movie ticket is free!")
    elif 3 <= age <= 12:
        print("Your movie ticket costs $10.")
    else:
        print("Your movie ticket costs $15.")
