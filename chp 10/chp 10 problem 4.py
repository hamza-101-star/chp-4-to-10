print("Enter 'q' at any time to quit.")

while True:
    name = input("What is your name? ")

    if name.lower() == 'q':
        print("Goodbye!")
        break

    print(f"Hello, {name}! Welcome!")

    with open("guest_book.txt", "a") as file:
        file.write(f"{name}\n")
