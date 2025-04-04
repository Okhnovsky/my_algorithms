# Перебирать связный список можно только в одну сторону.
# Обращение по индексу O(n)
# Добавление элемента в конец списка O(1)
# Добавление элемента на следующую позицию за текущим элементом O(1)
# Добавление элемента на позицию перед текущим элементом O(n)
# Удаление первого элемента O(1)
# Удаление последнего элемента O(1)
# Удаление текущего элемента O(n)
# Поиск по значению O(n)
# Определение длины списка O(n)


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
