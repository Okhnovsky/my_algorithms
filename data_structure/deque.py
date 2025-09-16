# Добавление элемента в конец O(1)
# Извлечение элемента из конца O(1)
# Проверка вхождения элемента O(n)
# Добавление элемента в начало O(1)
# Извлечение элемента из начала O(1)
# Доступ к элементу по индексу O(n)
# Добавление элемента в середениу O(n)
# Удаление элемента из середны O(n)
# Получение длины O(1)


from collections import deque


# Создание пустого дека
d = deque()

# Добавление элементов в конец
d.append('a')
d.append('b')
print(d)  # Output: deque(['a', 'b'])

# Добавление элементов в начало
d.appendleft('c')
print(d)  # Output: deque(['c', 'a', 'b'])

# Удаление последнего элемента
last_element = d.pop()
print(last_element)  # Output: b
print(d)  # Output: deque(['c', 'a'])

# Удаление первого элемента
first_element = d.popleft()
print(first_element)  # Output: c
print(d)  # Output: deque(['a'])

d.extend([1, 2, 3])

d.extendleft([4,5])

d.rotate(1)
