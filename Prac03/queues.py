import numpy as np

class Queue:
    def __init__(self, size):
        self.size = size 
        self.array = np.full(self.size, None, dtype=object)
        self.numElements = 0

    def is_empty(self):
        if self.numElements > 0:
            return False
        
        return True
    
    def is_full(self):
        if self.numElements == self.size:
            return True
        
        return False
    
class ShufflingQueue(Queue):
    def __init__(self, size):
        super().__init__(size)
    
    def enqueue(self, value):
        if not self.is_full():
            self.array[self.numElements] = value
            self.numElements += 1
        else:
            raise IndexError("Queue is full")

    def dequeue(self):
        if not self.is_empty():
            value = self.array[0]
            for i in range(1, self.numElements):
                self.array[i - 1] = self.array[i]
            self.array[self.numElements - 1] = None
            self.numElements -= 1
            
            return value
        else:
            raise IndexError("Queue is empty")
             
    def count(self):
        return self.numElements
    
    def peek(self):
        if not self.is_empty():
            return self.array[0]

    def is_empty(self):
        return super().is_empty()

    def is_full(self):
        return super().is_full()

class CircularQueue(Queue):
    def __init__(self, size):
        super().__init__(size)
        self.front_idx = 0
        self.tail_idx = 0
    
    def enqueue(self, value):
        if not self.is_full():
            self.array[self.tail_idx] = value
            self.tail_idx = (self.tail_idx + 1) % self.size
            self.numElements += 1

        else:
            raise IndexError("Queue is full")

    def dequeue(self):
        if not self.is_empty():
            value = self.array[self.front_idx]
            self.array[self.front_idx] = None
            self.front_idx = (self.front_idx + 1) % self.size
            self.numElements -= 1
            
            return value
        else:
            raise IndexError("Queue is empty")
             
    def count(self):
        return self.numElements
    
    def peek(self):
        if not self.is_empty():
            return self.array[self.front_idx]

    def is_empty(self):
        return super().is_empty()

    def is_full(self):
        return super().is_full()