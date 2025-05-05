from linkedlist import LinkedList

class Queue: # This class is from Practical 3 of Komes Pispol: 90035701
    """
        Stores items in a linked list, keeps track of number of elements,
        and handle queue operations
    """
    def __init__(self):
        self.list = LinkedList()
        self.num_elements = 0

    def enqueue(self, value):
        self.list.insert_last(value)
        self.num_elements += 1

    def dequeue(self):
        if not self.is_empty():
            value = self.list.peek_first()
            self.list.remove_first()
            self.num_elements -= 1
            
            return value
        else:
            raise IndexError("Queue is empty")
             
    def count(self):
        return self.num_elements
    
    def peek(self):
        if not self.is_empty():
            return self.list.peek_first()
        
    def is_empty(self):
        if self.num_elements > 0:
            return False
        
        return True