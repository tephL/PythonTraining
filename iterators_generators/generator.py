import time as t

def count_to(n): # 10.69s
    ctr = 1
    while ctr <= n:
        yield ctr
        ctr += 1
        
def count_to2(n): # 10.98s
    ctr = 1
    numbers = []
    while ctr <= n:
        numbers.append(ctr)
        ctr += 1
    return numbers

start = t.time()
for x in count_to(1000000):
    pass
end = t.time()
print(end - start)