#Slot Machine
import random

div = "="*19
winborder = "\n$" + "—"*13 + "$"
notwinborder = "\n*" + "—"*13 + "*"
possibilities = [n for n in range(1,7)]
result = []
balance = 10

while True:
    if balance > 0:
        push = int(input(f"Coins: {balance}\n{div}|\n[1] Push  [0] Quit |\n{div}|\n> "))
        print()
    
        if push == 1:
            for i in range(1,4):
                result.append(random.choice(possibilities))
            
            if result[0] == result[1] == result[2]:
                print(f"{'You Win':>11}{winborder}")
                balance += 5
                for r in result:
                    print(f"| {r} ", end = "|")
                print(winborder)
                result.clear()
            else:
                print(f"{'You Lose':>11}{notwinborder}")
                balance -= 1
                for r in result:
                    print(f"| {r} ", end = "|")
                print(notwinborder)
            result.clear()
        else:
             break
        print()
    else:
        print("You've ran out of balance.")
        break