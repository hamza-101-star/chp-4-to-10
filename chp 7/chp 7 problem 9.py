sandwich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'ham', 'pastrami', 'chicken']

finished_sandwiches = []

print("Sorry, we have run out of pastrami sandwiches.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()  
    print(f"I made your {current_sandwich} sandwich.")  
    finished_sandwiches.append(current_sandwich)  

print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")
