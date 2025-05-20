# Variable definitions
car = 'subaru'
favorite_color = 'blue'
age = 25
temperature = 75
fruits = ['apple', 'banana', 'cherry', 'orange', 'grape']
is_tall = True
person_name = 'john'

# Equality and Inequality with strings
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # True

print("\nIs favorite_color != 'red'? I predict True.")
print(favorite_color != 'red')  # True

# Tests using the lower() method
print("\nIs person_name.lower() == 'john'? I predict True.")
print(person_name.lower() == 'john')  # True

print("\nIs favorite_color.lower() == 'blue'? I predict True.")
print(favorite_color.lower() == 'blue')  # True

print("\nIs favorite_color.lower() == 'GREEN'? I predict False.")
print(favorite_color.lower() == 'green')  # False

# Numerical tests (equality, inequality, greater than, less than)
print("\nIs age == 25? I predict True.")
print(age == 25)  # True

print("\nIs age != 30? I predict True.")
print(age != 30)  # True

print("\nIs temperature > 60? I predict True.")
print(temperature > 60)  # True

print("\nIs temperature < 50? I predict False.")
print(temperature < 50)  # False

print("\nIs age >= 25? I predict True.")
print(age >= 25)  # True

print("\nIs age <= 20? I predict False.")
print(age <= 20)  # False

# Using the 'and' and 'or' keywords
print("\nIs age > 20 and temperature > 70? I predict True.")
print(age > 20 and temperature > 70)  # True

print("\nIs age > 30 and temperature > 70? I predict False.")
print(age > 30 and temperature > 70)  # False

print("\nIs age > 30 or temperature > 70? I predict True.")
print(age > 30 or temperature > 70)  # True

print("\nIs age < 20 or temperature > 100? I predict False.")
print(age < 20 or temperature > 100)  # False

# Test if an item is in a list
print("\nIs 'banana' in the fruits list? I predict True.")
print('banana' in fruits)  # True

print("\nIs 'mango' in the fruits list? I predict False.")
print('mango' in fruits)  # False

# Test if an item is not in a list
print("\nIs 'cherry' not in the fruits list? I predict False.")
print('cherry' not in fruits)  # False

print("\nIs 'watermelon' not in the fruits list? I predict True.")
print('watermelon' not in fruits)  # True
