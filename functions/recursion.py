# iterative
def walk(x):
    for y in range(1, x + 1):
        print(f"You walked {y}")
        
# recursive
def walk2(x):
    if x == 0:
        return
    else:
        walk2(x - 1)
        print(f"You walked {x}")
        
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
        
def speed(x):
    if x == 0:
        return 0
    else:
        print(x)
        speed(x-1)
        
print(walk(15))
print(walk2(15))
print(factorial(6))

print(speed(7))