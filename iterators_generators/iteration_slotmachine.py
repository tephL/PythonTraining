# Slot Machine game using Iterator

import random

class slot_machine:
    def __init__(self, rows):
        self.rows = rows
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.rows:
            self.count += 1
            return random.randint(1, 6)
        else:
            raise StopIteration
            
results = slot_machine(3)

for res in results:
    print(res, end = "| ")