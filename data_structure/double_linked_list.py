# Перебирать можно в обе стороны.
# Обращение по индексу O(n)
# Добавление элемента в конец списка O(1)
# Добавление элемента на следующую позицию за текущим элементом O(1)
# Добавление элемента на позицию перед текущим элементом O(1)
# Удаление первого элемента O(1)
# Удаление последнего элемента O(1)
# Удаление текущего элемента O(1)
# Поиск по значению O(n)
# Определение длины списка O(n)


class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def remove(self, key):
        current = self.head

        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.head = current.prev
                
                return True
            
            current = current.next
        
        return False
    
    def find(self, key):
        current = self.head
        index = 0

        while current:
            if current.data == key:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def traverse_forward(self):
        result = []
        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result
    
    def traverse_backward(self):
        result = []
        current = self.tail

        while current:
            result.append(current.data)
            current = current.prev
        
        return result

    def kth_from_end(self, k):
        """Найти k-й элемент с конца списка."""
        slow = fast = self.head

        for _ in range(k):
            if fast is None:
                raise ValueError("k больше длины списка")
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        return slow.data
    
    def reverse_dlist(self):
        """Инвертировать двусвязный список."""
        temp = None
        current = self.head

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        if temp:
            self.head = temp.prev
    
    def has_cycle(self):
        """Проверка на наличие цикла."""
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
