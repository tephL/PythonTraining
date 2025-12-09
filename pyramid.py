##pyramid
height = int(input("pyramid height: "))

for a in range(1,height):
    for b in range(1,a+1):
        print("*", end = "")
    print()