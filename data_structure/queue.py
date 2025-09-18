# FIFO first in first out
# Добавление элемента в конец O(1)
# Извлечение элемента из конца O(1)

class Queue:

    def __init__(self):
        # Как и для стека, используем для хранения элементов очереди список.
        self.__items = []

    def push(self, item):
        """Добавить элемент в очередь."""
        # В отличие от стека, здесь добавляем элемент не в конец списка,
        # а в начало - на место элемента с индексом 0.
        self.__items.insert(0, item)

    def pop(self):
        """Вернуть элемент из очереди."""
        return self.__items.pop()

    def peek(self):
        """Вернуть последний элемент, но не удалять его из очереди."""
        return self.__items[-1]

    def size(self):
        """Вернуть размер очереди."""
        return len(self.__items)


from collections import deque
queue = deque()
queue.appendleft('item')
item = queue.pop()  


# Потоко-безопасная очередь
from queue import Queue
q = Queue(maxsize=0) # size = 0 означает неограниченную длину
q.put("item") # помещает элемент в конец очереди
item = q.get() 


# Реализация очереди, специально разработанная для межпроцессного взаимодействия.
from multiprocessing import Queue
mq = Queue()
mq.put("item")
item = mq.get()  
