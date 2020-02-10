from random import randint
# Mortal Fibonacci Rabbits

# n = 200
# m = 50
# rabbits = [1, 1]
# i = 2
# while i < n:
#     if i < m:
#         rabbits.append(rabbits[i-2] + rabbits[i-1])
#     elif i == m or i == m + 1:
#         rabbits.append(rabbits[i-2] + rabbits[i-1] - 1)
#     else:
#         rabbits.append(rabbits[i-2] + rabbits[i-1] - rabbits[i-(m + 1)])
#     i += 1
# print(len(rabbits))
# print(rabbits[n - 1])

# population simulation
time = 2000
lifespan = 80
adult_age = 16
old_age = 54
generations = [0] * lifespan
generations[adult_age] = 4
# simulation execution
for time in range(time - 1):
    for g in reversed(range(1, lifespan)):  # growth
        generations[g] = generations[g - 1]
    generations[0] = 0
    for b in reversed(range(adult_age, old_age)):  # birth
        if randint(1, 4) == 1:  # fertility rate
            generations[0] += generations[b] // 2  # two partners for one child
    for d in reversed(range(1, lifespan)):  # death
        rand = randint(1, 8)
        if rand == 1:  # death rate
            generations[d] -= generations[d] // 10
        elif rand < 7:
            generations[d] -= generations[d] // 25
        else:
            generations[d] -= generations[d] // 50
    population = 0
    for generation in generations:
        population += generation
    print(f"population: {population}")

