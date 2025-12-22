import os

helps = dir(os)

x = 0

for h in helps:
    print(h, end = ", ")
    x += 1
    if x % 3 == 0:
        print()