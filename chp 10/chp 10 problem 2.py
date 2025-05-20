filename = 'learning_python.txt'

with open(filename) as file:
    for line in file:
        modified_line = line.replace('Python', 'C')
        print(modified_line.rstrip())
