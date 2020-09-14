import random

glup: int
glup2: int
glupFloat: float

print("0 <= Glup =< 2")
glup = random.randint(0, 2)
print(glup)

print("-1 <= Glup =< 1")
glup = random.randint(-1, 1)
print(glup)

print("1,35 =< Glup =< 1,65")
glupFloat = random.uniform(1.35, 1.65)
print(glupFloat)

print("Emulate six-sided face")
glup = random.randint(1, 6)
print(glup)

print("-10,5 =< Glup =< +6,5")
glupFloat = random.uniform(-10.5, 6.5)
print(glupFloat)

print("Emulate two six-sided face")
glup = random.randint(1, 6)
glup2 = random.randint(1, 6)
print(glup+glup2)
