print("Welcome to the Addition Calculator!")
print("Enter 'q' at any time to quit.\n")

while True:
    num1 = input("Enter the first number: ")
    if num1.lower() == 'q':
        break

    num2 = input("Enter the second number: ")
    if num2.lower() == 'q':
        break

    try:
        result = int(num1) + int(num2)
    except ValueError:
        print(" Oops! Please enter valid numbers.\n")
    else:
        print(f" The sum is: {result}\n")
