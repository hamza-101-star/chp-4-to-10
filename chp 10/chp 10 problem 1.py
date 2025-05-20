filename = 'learning_python.txt'

print("=== Reading entire file ===")
with open(filename) as file:
    contents = file.read()
    print(contents)

print("=== Reading line by line using a loop ===")
with open(filename) as file:
    for line in file:
        print(line.rstrip())
print("=== Reading lines into a list and printing them later ===")
with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())
