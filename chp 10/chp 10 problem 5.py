print("Why do you like programming?")
print("Enter 'q' at any time to quit.\n")

while True:
    reason = input("Your reason: ")

    if reason.lower() == 'q':
        print("Thanks for sharing your thoughts!")
        break

    with open("programming_poll.txt", "a") as file:
        file.write(f"{reason}\n")
