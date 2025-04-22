import numpy as np


class DSAHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap_arr = np.array([None for _ in range(self.capacity)], dtype=object)
        self.count = 0
        self.root_idx = 0

    def add(self, priority, value=None):
        if self.is_full():
            raise IndexError("Heap array is full.")
                
        if self.is_empty():
            self.heap_arr[self.root_idx] = DSAHeapEntry(priority, value)
            self.count += 1
            return

        current_idx = self.count
        self.heap_arr[current_idx] = DSAHeapEntry(priority, value)
        self.trickle_up(current_idx)
        self.count += 1

    def remove(self):
        if self.is_empty():
            raise IndexError("Heap is empty.")
        
        self.count -= 1
        to_remove = self.heap_arr[self.root_idx]
        self.heap_arr[self.root_idx] = self.heap_arr[self.count]
        self.heap_arr[self.count] = None
        self.trickle_down(self.root_idx)

        return to_remove

    def display(self):
        print(self.__str__())

    def trickle_up(self, current_idx):
        parent_idx = self.get_parent_idx(current_idx)
        while (current_idx > self.root_idx and
                self.heap_arr[current_idx].get_priority() > 
                self.heap_arr[parent_idx].get_priority()):
            self.heap_arr[parent_idx], self.heap_arr[current_idx] = self.heap_arr[current_idx], self.heap_arr[parent_idx]
            current_idx = parent_idx
            parent_idx = self.get_parent_idx(current_idx)

    def trickle_down(self, current_idx):
        left_idx = self.get_left_idx(current_idx)
        right_idx = self.get_right_idx(current_idx)
        keep_going = True
        while keep_going and left_idx < self.count:
            keep_going = False
            largest_idx = left_idx

            if right_idx < self.count:
                if (self.heap_arr[left_idx].get_priority() < 
                        self.heap_arr[right_idx].get_priority()):
                    largest_idx = right_idx

            if (self.heap_arr[largest_idx].get_priority() > 
                    self.heap_arr[current_idx].get_priority()):
                self.heap_arr[largest_idx], self.heap_arr[current_idx] = self.heap_arr[current_idx], self.heap_arr[largest_idx]
                current_idx = largest_idx
                keep_going = True

            current_idx = largest_idx
            left_idx = self.get_left_idx(current_idx)
            right_idx = self.get_right_idx(current_idx)

    def get_left_idx(self, current_idx):
        return (current_idx * 2) + 1
    
    def get_right_idx(self, current_idx):
        return (current_idx * 2) + 2
    
    def get_parent_idx(self, current_idx):
        return (current_idx - 1) // 2
    
    def is_full(self):
        return self.count == self.capacity
    
    def is_empty(self):
        return self.count == 0
    
    def __str__(self):
        return str([i for i in self.heap_arr])
    
    def __repr__(self):
        return self.__str__()


class DSAHeapEntry:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def get_priority(self):
        return self.priority

    def set_priority(self, priority):
        self.priority = priority

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return f"({self.priority}, {self.value})"
    
    def __repr__(self):
        return self.__str__()
    
    def __lt__(self, other):
        return self.priority < other.priority


if __name__ == "__main__":
    test = DSAHeap(10)
    test.add(3)
    test.add(2)
    test.add(6)
    test.add(1)
    test.add(5)
    test.add(4)
    test.add(8)
    test.add(7)
    test.add(10)
    test.add(9)
    test.display()

