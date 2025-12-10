#message encryption
import string
import random

keys = string.digits + string.ascii_letters + string.punctuation
keys = list(keys)

values = list(keys.copy())
random.shuffle(values)
i = 0
o=0
x = 0
encrypted = None           
div = "—"*45

while True:
    chc = int(input("1. View Dictionary\n2. View Encrypted Text\n3. Encrypt Text\n0. Exit\nChoice: "))
    print("\n")
    
    if chc == 1:
        print(div)
        print(f"{'Dictionary':^40}    |")
        print(div)
        for i in range(0, len(keys), 1):
            print(f" {keys[i]} -> {values[i]}", end=" |")
            x+=1
            if(x==5):
                print()
                x = 0
        print(f"\n{div}")
    elif chc == 2:
        if encrypted is None:
            print("Have not encrypted a text yet")
        else:
            for enc in encrypted:
                print(enc, end="")
    elif chc == 3:
        word = input("Enter: ")
        encrypted = list(word)

        for letter in word:
            for i in range(0, len(keys), 1):
                if letter == keys[i]:
                    encrypted[o] = values[i]
                    break
            o+=1
    elif chc == 0:
        print("Thanks")
        break
    else:
        print("invalid")
    print("\n")
