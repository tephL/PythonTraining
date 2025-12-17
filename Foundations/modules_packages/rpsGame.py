#rock paper scissors
import random
moves = ["Rock", "Paper", "Scissors"]
r = moves[0]
p = moves[1]
s = moves[2]
W = "Result: Win"
L = "Result: Lose"
D = "Result: Draw"
div = "-"*28

while True:
    move = random.choice(moves)
    opp = f"Bot: {move}"
    print(div)
    for m in moves:
        print(f" {m} |", end=" ")
    print(f"{'[0] to Exit':>15}")
    print(f"{div}")
    user = input("Your move? ").lower().capitalize()
    
    if user==move:
        print(D)
        print(opp)
    elif move==r and user==p:
        print(W)
        print(opp)
    elif move==p and user==r:
        print(W)
        print(opp)
    elif move==s and user==p:
        print(L)
        print(opp)
    elif move==p and user==s:
        print(W)
        print(opp)
    elif move==r and user==s:
        print(L)
        print(opp)
    elif move==s and user==r:
        print(W)
        print(opp)
    elif user=="0":
        print("Bye")
        break
    else:
        print(f"{L} (Invalid)")
    print()
