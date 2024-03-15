def greedy_algorithm(items, budget):
    # Створюємо список кортежів (ім'я, співвідношення калорій/вартість)
    item_ratios = [(item, items[item]["calories"] / items[item]["cost"]) for item in items]
    # Сортуємо список за спаданням співвідношення калорій/вартість
    item_ratios.sort(key=lambda x: x[1], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, ratio in item_ratios:
        if total_cost + items[item]["cost"] <= budget:
            selected_items.append(item)
            total_cost += items[item]["cost"]
            total_calories += items[item]["calories"]

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    # Створюємо матрицю для збереження найкращої кількості калорій для кожного бюджету
    dp_table = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    for i, item in enumerate(items, start=1):
        for j in range(1, budget + 1):
            cost = items[item]["cost"]
            calories = items[item]["calories"]

            if cost > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i - 1][j - cost] + calories)

    # Відновлюємо набір страв, які входять до оптимального рішення
    selected_items = []
    j = budget
    for i in range(len(items), 0, -1):
        if dp_table[i][j] != dp_table[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]

    selected_items.reverse()
    return selected_items, dp_table[-1][-1]


# Задання даних про страви
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Виклик жадібного алгоритму
greedy_selected_items, greedy_total_cost, greedy_total_calories = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected Items:", greedy_selected_items)
print("Total Cost:", greedy_total_cost)
print("Total Calories:", greedy_total_calories)

# Виклик алгоритму динамічного програмування
dp_selected_items, dp_total_calories = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print("Selected Items:", dp_selected_items)
print("Total Calories:", dp_total_calories)
