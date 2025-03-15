import numpy as np

class Stack:
    def __init__(self, size):
        self.size = size
        self.array = np.full(self.size, None, dtype=object)
        self.numElements = 0

    def push(self, value):
        if not self.is_full():
            self.array[self.numElements] = value
            self.numElements += 1
            
        else:
            raise IndexError("Stack is full")
        
    def pop(self):
        if not self.is_empty():
            value = self.array[self.numElements - 1]
            self.array[self.numElements - 1] = 0
            self.numElements -= 1
            return value

    def top(self):
        if not self.is_empty():
            return self.array[self.numElements - 1]

    def count(self):
        return self.numElements

    def is_empty(self):
        if self.numElements > 0:
            return False
        
        return True
    
    def is_full(self):
        if self.numElements == self.size:
            return True
        
        return False

    def __str__(self):
        return "[" + ", ".join(str(self.array[i]) for i in range(self.numElements)) + "]"
    