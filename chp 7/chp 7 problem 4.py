
while True:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")

    if topping.lower() == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza.")
