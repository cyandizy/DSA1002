import numpy as np
import math
DEBUG = False

class DSAHashTable:
    def __init__(self, size):
        self.table_size = self.next_prime(size)
        self.hash_array = np.array([DSAHashEntry() for _ in range(self.table_size)], dtype=DSAHashEntry)
        self.max_step = self.get_max_step()
        self.count = 0
        self.LF_UPPER = 0.7
        self.LF_LOWER = 0.1

    def hash(self, key):
        hash_idx = 0
        for char in key:
            hash_idx = (33 * hash_idx) + ord(char)

        return hash_idx % self.table_size

    def step_hash(self, hashed_key):
        return self.max_step - (hashed_key % self.max_step)

    def put(self, key, value, check_resize=True):
        hashed_key = self.hash(key)
        step_hash = self.step_hash(hashed_key)

        for i in range(self.table_size):
            idx = (hashed_key + (step_hash * i)) % self.table_size
            entry = self.hash_array[idx]
            if not (entry.state == 1 and entry.key != key):
                if entry.key != key:
                    self.count += 1
                entry.update(key, value)
                if check_resize:
                    if self.get_load_factor() > self.LF_UPPER:
                        self.resize(self.table_size * 2)

                return
        
        raise IndexError("Table is full.")

    def get(self, key):
        if not self.has_key(key):
            raise KeyError(key)
        
        hashed_key = self.hash(key)
        step_hash = self.step_hash(hashed_key)

        for i in range(self.table_size):
            idx = (hashed_key + (step_hash * i)) % self.table_size
            entry = self.hash_array[idx]
            if entry.state == 1 and entry.key == key:
                return entry.value
        
    def remove(self, key):
        if not self.has_key(key):
            raise KeyError(key)
        
        hashed_key = self.hash(key)
        step_hash = self.step_hash(hashed_key)

        for i in range(self.table_size):
            idx = (hashed_key + (step_hash * i)) % self.table_size
            entry = self.hash_array[idx]
            if entry.state == 1 and entry.key == key:
                entry.clear()
                self.count -= 1
                
                if self.get_load_factor() < self.LF_LOWER:
                    self.resize(self.table_size // 2)

    def resize(self, size):
        new_size = self.next_prime(size)
        old_array = self.hash_array.copy()

        if DEBUG:
            print(f"Resizing from {self.table_size} to {new_size}")
        
        self.table_size = new_size
        self.hash_array = np.array([DSAHashEntry() for _ in range(self.table_size)], dtype=DSAHashEntry)
        self.max_step = self.get_max_step()
        self.count = 0
        for entry in old_array:
            if entry.state != 0:
                self.put(entry.key, entry.value, False)

        if DEBUG:
            print("-- Resizing Succeeded")

    def get_load_factor(self):
        return self.count / self.table_size

    def next_prime(self, num):
        num += 1
        if num % 2 == 0:
            num += 1

        while not self.is_prime(num):
            num += 2

        return num

    def prev_prime(self, num):
        num -= 1
        if num <= 3:
            return 2
        
        if num % 2 == 0:
            num -= 1

        while num > 2 and not self.is_prime(num):
            num -= 2
        
        return num

    def is_prime(self, num):
        if num <= 1:
            return False
        
        for i in range(2, int(math.sqrt(num)) + 1):
            if (num % i) == 0:
                return False
            
        return True
    
    def get_max_step(self):
        return self.prev_prime(self.table_size)
    
    def has_key(self, key):
        hashed_key = self.hash(key)
        step_hash = self.step_hash(hashed_key)

        for i in range(self.table_size):
            idx = (hashed_key + (step_hash * i)) % self.table_size
            entry = self.hash_array[idx]
            if entry.state == 1 and entry.key == key:
                return True
        
        return False
    
class DSAHashEntry:
    def __init__(self, key: str = "", value: object = None):
        self.key = key
        self.value = value
        self.state = 0

    def update(self, key, value):
        self.key = key
        self.value = value
        self.state = 1

    def clear(self):
        self.key = ""
        self.value = None
        self.state = -1 

    


