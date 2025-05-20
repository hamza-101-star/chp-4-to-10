filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        print(f"\nReading from {filename}:")
        with open(filename) as file:
            contents = file.read()
            print(contents.rstrip())
    except FileNotFoundError:
        print(f" Sorry, the file '{filename}' was not found.")
