#message encryption
import string
import random

keys = string.digits + string.ascii_letters + string.punctuation
keys = list(keys)

values = list(keys.copy())
random.shuffle(values)
x = 0
encrypted = None           
div = "—"*45

while True:
    print("—"*20)
    print(f"{'Menu':^20}")    
    print("—"*20)
    chc = int(input("1. View Dictionary\n2. Encrypt Text\n3. Decrypt Text\n0. Exit\n" + "—"*20 + "\n> "))
    print()
    
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
        o=0
        i=0
        word = input("Enter: ")
        encrypted = list(word)

        for letter in word:
            for i in range(0, len(keys), 1):
                if letter == keys[i]:
                    encrypted[o] = values[i]
                    break
            o+=1
            
        print("Encrypted: ", end="")
        for enc in encrypted:
                print(enc, end="")
    elif chc == 3:
        o=0
        i=0
        encrypt = input("Encrypted: ")
        decrypted = list(encrypt)
        
        for ch in encrypt:
            for i in range(0, len(values), 1):
                if ch == values[i]:
                    decrypted[o] = keys[i]
                    break
            o+=1
        print(f"Decrypted message is: ", end="")
        for d in decrypted:
            print(d, end="")
        print()
    elif chc == 0:
        print("Thanks")
        break
    else:
        print("invalid")
    print("\n")
