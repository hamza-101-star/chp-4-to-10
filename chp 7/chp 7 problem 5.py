while True:
    age = int(input("Please enter your age (or type 'quit' to stop): "))
    
    if age < 3:
        print("Your movie ticket is free!")
    elif 3 <= age <= 12:
        print("Your movie ticket costs $10.")
    elif age > 12:
        print("Your movie ticket costs $15.")
    
    continue_prompt = input("Would you like to check another age? (yes to continue, quit to stop): ").lower()
    if continue_prompt == 'quit':
        break
