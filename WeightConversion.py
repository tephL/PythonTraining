op = int(input("[1] lb>kg or [2] kg>lb? "))

if op == 1:
    unit = float(input("how many lb? "))
    unit /= 2.205
    type = "kg"
elif op == 2:
    unit = float(input("how many kg? "))
    unit *= 2.205
    type = "lb"
else:
    print("invalid")
    
print(f"{unit} {type}")
