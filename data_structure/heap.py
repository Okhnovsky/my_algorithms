class MaxHeap:

    def __init__(self):
        self.heap = [0]
        self.current_size = 0
        self.results = []

    def prec_up(self, i):
        while i // 2 > 0:
            if self.heap[i] > self.heap[i//2]:
                self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i = i // 2

    def insert(self, value):
        self.heap.append(value)
        self.current_size += 1
        self.prec_up(self.current_size)

    def prec_down(self, i):
        while (i*2) <= self.current_size:
            mc = self.max_child(i)
            if self.heap[i] < self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def max_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap[i*2] > self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def extract(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.current_size]
        self.current_size -= 1
        self.heap.pop()
        self.prec_down(1)
        self.results.append(retval)
        return retval


heap = MaxHeap()
