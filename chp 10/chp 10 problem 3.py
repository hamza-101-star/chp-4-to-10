name = input("What is your name? ")

with open("guest.txt", "w") as file:
    file.write(name)

print(f"Thank you, {name}. Your name has been written to guest.txt.")
