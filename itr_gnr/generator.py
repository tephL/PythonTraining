# Generator
## using yield keyword instead of return
## pause - return process

def count_to(n): # generator
    ctr = 1
    while ctr <= n:
        yield ctr
        ctr += 1
        
def count_to2(n): # normal counter
    ctr = 1
    numbers = []
    while ctr <= n:
        numbers.append(ctr)
        ctr += 1
    return numbers
    

for x in count_to(1000000):
    pass
