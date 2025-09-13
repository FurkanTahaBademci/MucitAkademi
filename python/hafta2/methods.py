import random

random.seed(10)

print(random.random())
print(random.randint(1, 10))
print(random.random())  # 0.0 - 1.0 arası

print("---",random.randrange(1, 20,1))  # 1-20 arası