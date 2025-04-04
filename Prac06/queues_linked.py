from dsa_linked_list import DSALinkedList

class Queue: # This class is from Practical 4 of Komes Pispol: 90035701
    def __init__(self):
        self.list = DSALinkedList()
        self.numElements = 0

    def enqueue(self, value):
        self.list.insert_last(value)
        self.numElements += 1

    def dequeue(self):
        if not self.is_empty():
            value = self.list.peek_first()
            self.list.remove_first()
            self.numElements -= 1
            
            return value
        else:
            raise IndexError("Queue is empty")
             
    def count(self):
        return self.numElements
    
    def peek(self):
        if not self.is_empty():
            return self.list.peek_first()
        
    def is_empty(self):
        if self.numElements > 0:
            return False
        
        return True