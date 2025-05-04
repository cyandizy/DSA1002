# Implemented from the pseudocode in Lecture 4

class ListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_prev(self):
        return self.prev
    
    def set_prev(self, prev):
        self.prev = prev

    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next

class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, value):
        new_node = ListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node

    def insert_last(self, value):
        new_node = ListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node

    def is_empty(self):
        return self.head == None
    
    def peek_first(self):
        if self.is_empty():
            return
        else:
            value = self.head.get_value()

            return value
    
    def peek_last(self):
        if self.is_empty():
            return
        else:
            value = self.tail.get_value()

            return value
    
    def remove_first(self):
        if self.is_empty():
            return
        elif self.head.get_next() == None:
            value = self.head.get_value()
            self.head = None
            self.tail = None

            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.head.set_prev(None)

            return value
    
    def remove_last(self):
        if self.is_empty():
            return
        elif self.head.get_next() == None:
            value = self.head.get_value()
            self.head = None
            self.tail = None
    
            return value
        else:
            value = self.tail.value
            self.tail = self.tail.get_prev()
            self.tail.set_next(None) 

            return value
        
    def display(self):
        values = []
        current = self.head
        while current != None:
            values.append(current.get_value())
            current = current.get_next()

        return values