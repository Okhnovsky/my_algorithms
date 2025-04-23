# Задача о рюкзаке с целочисленными весами (0/1 Knapsack Problem): 
# Каждый предмет можно либо полностью положить в рюкзак, либо полностью 
# не класть. Нельзя брать части предметов.


def knapsack_01(weights, values, capacity):
    """
    Решает задачу о рюкзаке с целочисленными весами методом динамического программирования.

    Args:
        weights (list): Список весов предметов.
        values (list): Список стоимостей предметов (соответствует весам).
        capacity (int): Максимальная вместимость рюкзака.

    Returns:
        int: Максимальная суммарная стоимость предметов, которые можно поместить в рюкзак.
    """
    n = len(values)
    # Создаем таблицу DP (dynamic programming) размером (n+1) x (capacity+1)
    # dp[i][w] будет хранить максимальную стоимость, которую можно получить,
    # используя первые i предметов и рюкзак вместимостью w.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Заполняем таблицу DP снизу вверх
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # i-й предмет (индекс i-1 в исходных списках)
            weight = weights[i - 1]
            value = values[i - 1]

            # Если вес текущего предмета больше текущей вместимости рюкзака,
            # мы не можем его положить, поэтому значение остается таким же,
            # как и для предыдущих предметов.
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # У нас есть два варианта:
                # 1. Не брать i-й предмет: значение будет dp[i-1][w]
                # 2. Взять i-й предмет: значение будет value (стоимость текущего предмета)
                #    плюс максимальная стоимость, которую можно получить, используя
                #    оставшуюся вместимость (w - weight) и предыдущие предметы (i-1).
                dp[i][w] = max(dp[i - 1][w], value + dp[i - 1][w - weight])

    # Максимальная стоимость будет находиться в правом нижнем углу таблицы DP
    return dp[n][capacity]

# Пример использования
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

max_value = knapsack_01(weights, values, capacity)
print(f"Максимальная стоимость, которую можно поместить в рюкзак: {max_value}")

# Для отслеживания выбранных предметов (необязательно):
def knapsack_01_with_items(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    items = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            weight = weights[i - 1]
            value = values[i - 1]

            if weight > w:
                dp[i][w] = dp[i - 1][w]
                items[i][w] = items[i - 1][w][:]
            else:
                value_without = dp[i - 1][w]
                value_with = value + dp[i - 1][w - weight]

                if value_with > value_without:
                    dp[i][w] = value_with
                    items[i][w] = items[i - 1][w - weight][:]
                    items[i][w].append(i - 1)  # Индекс предмета
                else:
                    dp[i][w] = value_without
                    items[i][w] = items[i - 1][w][:]

    return dp[n][capacity], items[n][capacity]

# Пример использования с отслеживанием предметов
max_value_with_items, selected_items = knapsack_01_with_items(weights, values, capacity)
print(f"Максимальная стоимость (с отслеживанием предметов): {max_value_with_items}")
print(f"Индексы выбранных предметов: {selected_items}")
print(f"Веса выбранных предметов: {[weights[i] for i in selected_items]}")
print(f"Стоимости выбранных предметов: {[values[i] for i in selected_items]}")
