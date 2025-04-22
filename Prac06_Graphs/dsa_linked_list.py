# From practical 4 with addition methods

class DSAListNode:
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

class DSALinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, value):
        new_node = DSAListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node

    def insert_last(self, value):
        new_node = DSAListNode(value)
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
        
    def remove(self, value):
        if self.is_empty():
            return
        current = self.head
        while current != None:
            if current.get_value() == value:
                if current == self.head:
                    if self.head.get_next() is None:
                        self.head = None
                    else:
                        self.head = self.head.get_next()
                        self.head.set_prev(None)
                        if self.head.get_next() == None:
                            self.tail = self.head
                elif current == self.tail:
                    previous = current.get_prev()
                    self.tail = previous
                    self.tail.set_next(None)
                else:    
                    previous = current.get_prev()
                    next = current.get_next()
                    previous.set_next(next)
                    next.set_prev(previous)
                
                return

            current = current.get_next()
        
    def display(self):
        values = []
        current = self.head
        while current != None:
            values.append(current.get_value())
            current = current.get_next()

        return values
    
    def find(self, value):
        current = self.head
        while current:
            if current.get_value() == value:
                return current
            current = current.get_next()
            
        return None

