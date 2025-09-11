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

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def remove(self, key):
        current = self.head

        if current is not None and current.data == key:
            self.head = current.next
            return
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if current is None:
            return
        
        prev.next = current.next
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, ' ')
            current = current.next
        print()
    
    def traverse_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def search_element(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False
    
    def reverse_list(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev
