def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y

while True:
    try:
        chc = int(input("1. Add\n2. Subtract\n> "))
        
        print()
        match chc:
            case 1:
                print(add(int(input("> ")), int(input("> "))))
            case 2:
                print(subtract(int(input("> ")), int(input("> "))))
            case 0:
                print("000")
                break
            case _:
                print("invalid")
        print()
    except ValueError: # error name of inputting mismatch data type
        print("bruh input numbers")
    finally:
        print("whew") # always runs