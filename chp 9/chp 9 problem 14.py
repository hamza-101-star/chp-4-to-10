import random

lottery_pool = [1, 5, 9, 14, 23, 27, 33, 42, 50, 88, 'A', 'B', 'C', 'D', 'E']

winning_ticket = random.sample(lottery_pool, 4)
print("Any ticket matching these numbers or letters wins a prize:")
print(winning_ticket)
