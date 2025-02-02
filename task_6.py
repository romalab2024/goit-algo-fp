# Дані про їжу: вартість і калорійність
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    """
    Функція реалізує жадібний алгоритм вибору страв.
    Вона обирає страви за спаданням співвідношення калорій до вартості,
    додаючи їх до набору, якщо поточна сума не перевищує заданий бюджет.

    :param items: словник зі стравами, де ключ — назва страви,
                  значення — словник з ключами "cost" та "calories"
    :param budget: обмежений бюджет
    :return: список обраних страв
    """
    ratio_items = []
    for name, data in items.items():
        # Обчислюємо співвідношення калорій до вартості
        ratio = data["calories"] / data["cost"] if data["cost"] > 0 else 0
        ratio_items.append((name, data["cost"], data["calories"], ratio))
    
    # Сортуємо за спаданням співвідношення
    ratio_items.sort(key=lambda x: x[3], reverse=True)
    
    chosen = []
    total_cost = 0
    total_calories = 0
    
    for name, cost, calories, ratio in ratio_items:
        if total_cost + cost <= budget:
            chosen.append(name)
            total_cost += cost
            total_calories += calories
    
    print("Жадібний алгоритм:")
    print(f"Обрані страви: {chosen}")
    print(f"Загальна вартість: {total_cost}")
    print(f"Загальна калорійність: {total_calories}")
    return chosen

def dynamic_programming(items, budget):
    """
    Функція реалізує алгоритм динамічного програмування для задачі,
    аналогічної задачі про рюкзак (0/1 knapsack).
    Знаходить оптимальний набір страв, що максимізує сумарну калорійність
    при заданому бюджеті.

    :param items: словник зі стравами, де ключ — назва страви,
                  значення — словник з ключами "cost" та "calories"
    :param budget: обмежений бюджет
    :return: список обраних страв, оптимізуючих калорійність
    """
    names = list(items.keys())
    n = len(names)
    
    # Створюємо DP-таблицю:
    # dp[i][j] – максимальна калорійність, досяжна з перших i страв при бюджеті j
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    # Таблиця для відновлення рішення: keep[i][j] == 1, якщо i-та страва обрана
    keep = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        for j in range(1, budget + 1):
            if cost <= j:
                if dp[i - 1][j] < dp[i - 1][j - cost] + calories:
                    dp[i][j] = dp[i - 1][j - cost] + calories
                    keep[i][j] = 1  # Обираємо страву
                else:
                    dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Відновлюємо набір обраних страв
    chosen = []
    rem_budget = budget
    for i in range(n, 0, -1):
        if keep[i][rem_budget] == 1:
            name = names[i - 1]
            chosen.append(name)
            rem_budget -= items[name]["cost"]
    
    chosen.reverse()  # Змінюємо порядок для коректного відображення
    print("Динамічне програмування:")
    print(f"Оптимальний набір страв: {chosen}")
    print(f"Загальна калорійність: {dp[n][budget]}")
    return chosen

if __name__ == "__main__":
    # Задаємо бюджет, наприклад, 100
    budget = 100
    print("Результати роботи алгоритмів при бюджеті =", budget)
    print("-" * 50)
    
    # Виконуємо жадібний алгоритм
    greedy_result = greedy_algorithm(items, budget)
    print("-" * 50)
    
    # Виконуємо алгоритм динамічного програмування
    dp_result = dynamic_programming(items, budget)
