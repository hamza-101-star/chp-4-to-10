vacation_poll = {}

while True:
    name = input("What is your name? ")
    destination = input("If you could visit one place in the world, where would you go? ")

    vacation_poll[name] = destination  
    continue_poll = input("Would you like to add another person? (yes/no): ").lower()
    if continue_poll == 'no':
        break
print("\n--- Dream Vacation Poll Results ---")
for name, destination in vacation_poll.items():
    print(f"{name} would love to visit {destination}.")
