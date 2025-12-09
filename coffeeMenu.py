#coffeeMenu

types = {"Chocolate":"100", "Macchiato":"120",                       "Capuccino":"120", "Matcha":"200",                            "Strawberry":"150"}

print("-"*24)
print(f"{'Menu':^23}" + "|")
print("-"*24)
for key, value in types.items():
    print(f"${value:<5}| {key:15}|")
print("-"*24)