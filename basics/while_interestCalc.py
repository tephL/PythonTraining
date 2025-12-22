#Interest calculator

chc = True

while chc:
    P = float(input(f"{'Principal: ':<18}"))
    r = float(input(f"{'Rate (%): ':<18}"))
    t = float(input(f"{'Time (y): ':<18}"))
    n = int(input(f"{'Compunding num: ':<18}"))
    A =P * pow(1 + (r*0.0100)/n, n*t)
    
    print(f"\nResult: ${A:,.2f}")
    print(f"You gained: ${A-P:,.2f}")
    yn = input("\nAnother? (y/n): ")
    if yn=="n":
        chc = False
    else:
        print("")    