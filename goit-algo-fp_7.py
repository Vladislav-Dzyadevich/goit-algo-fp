import random
from collections import Counter

def monte_carlo_simulation(num_trials):
    outcomes = Counter()

    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        outcomes[total] += 1

    probabilities = {i: outcomes[i] / num_trials * 100 for i in range(2, 13)}
    return probabilities

def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for i, prob in probabilities.items():
        print(f"{i}\t{prob:.2f}% ({prob/100:.2f})")

# Виконати симуляцію з великою кількістю кидків
num_trials = 1000000
probabilities = monte_carlo_simulation(num_trials)

# Вивести результати
print_probabilities(probabilities)
