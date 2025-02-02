import random
import pandas as pd
import matplotlib.pyplot as plt

# Симуляція методом Монте-Карло
def monte_carlo_simulation(num_simulations):
    # Можливі суми при киданні двох кубиків
    sums_count = {i: 0 for i in range(2, 13)}
    
    # Виконання симуляцій
    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2
        sums_count[dice_sum] += 1
    
    # Обчислення ймовірностей
    probabilities = {key: count / num_simulations * 100 for key, count in sums_count.items()}
    return sums_count, probabilities

# Аналітичні ймовірності (з таблиці користувача)
analytical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

# Кількість симуляцій
num_simulations = 100000

# Запуск симуляції
simulated_counts, simulated_probabilities = monte_carlo_simulation(num_simulations)

# Порівняння аналітичних і отриманих ймовірностей
results_df = pd.DataFrame({
    "Сума": list(simulated_probabilities.keys()),
    "Ймовірність Монте-Карло (%)": list(simulated_probabilities.values()),
    "Аналітична ймовірність (%)": [analytical_probabilities[i] for i in simulated_probabilities.keys()]
})

# Візуалізація результатів
plt.figure(figsize=(10, 6))
plt.bar(results_df["Сума"] - 0.2, results_df["Ймовірність Монте-Карло (%)"], width=0.4, label="Монте-Карло")
plt.bar(results_df["Сума"] + 0.2, results_df["Аналітична ймовірність (%)"], width=0.4, label="Аналітична")
plt.xlabel("Сума чисел на двох кубиках")
plt.ylabel("Ймовірність (%)")
plt.title("Порівняння ймовірностей: Монте-Карло та аналітичний розрахунок")
plt.xticks(results_df["Сума"])
plt.legend()
plt.grid(True)
plt.show()

# Відображення таблиці
print(results_df)
