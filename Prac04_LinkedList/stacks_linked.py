from dsa_linked_list import DSALinkedList

class Stack: # This class is from Practical 3 of Komes Pispol: 90035701
    def __init__(self):
        self.list = DSALinkedList()
        self.numElements = 0

    def push(self, value):
        self.list.insert_last(value)
        self.numElements += 1
        
    def pop(self):
        if not self.is_empty():
            value = self.list.peek_last()
            self.list.remove_last()
            self.numElements -= 1
            return value

    def peek(self):
        if not self.is_empty():
            return self.list.peek_last()

    def count(self):
        return self.numElements

    def is_empty(self):
        if self.numElements > 0:
            return False
        
        return True
    