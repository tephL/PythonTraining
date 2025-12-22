import os # or any kind

def howmany(coll):
    x = 0
    for c in coll:
        x += 1
    return x        

def osOptions():
    oshelp = dir(os)
    amt = howmany(oshelp)
    fromX = ""
    toX = ""
    
    ranging = input(f"{amt} items. range? (x -> y)\n> ")
    divisor = ranging.find(",")
    
    #1st num
    for x in range(0, divisor):
        print(x)
        fromX += ranging[x]
    
    #2nd num
    for x in range(divisor + 1, len(ranging)):
        toX += ranging[x]
    
    x = 1
    for helprow in oshelp:
        if int(fromX) <= x and int(toX) <= x:
            print(x)
        else:
            x += 1
    

def main():
    while True:
        try:
            chc = int(input("What module?\n1. OS\n> "))
            print()
            match chc:
                case 1:
                    osOptions()
                case 0:
                    print("000")
                case _:
                    print("invalid")
            print()
        except ValueError:
            print("bruh")

if __name__ == '__main__':
    main()
        