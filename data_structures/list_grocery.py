#shopping cart

divider = "================="
pastries = ["crinkles", "cookies", "brownies"]
chocolate = ["m&m","kitkat", "dubai choco"]
meat = ["chicken", "beef", "pig"]

aisle1 = [pastries, chocolate, meat]
cart = []
all_foods = []

print(divider)
for foods in aisle1:
    for food in foods:
        print(food, end=", ")
        all_foods.append(food)
    print()
print(divider)
print("\n'0' to checkout\n")
    
done = False
while not done:
    add = input("wat u buy: ")
    if add.lower() in all_foods:
        cart.append(add)
        print(f"Successfully added {add}\n")
    elif add == "0":
        print(f"\n{divider}")
        print("Your cart: \n")
        for item in cart:
            print(f"{item:^10}")
        print(f"\n{divider}")
        conf = input("sure? (y/n): ")
        if conf=="y":
            done = True
    else:
        print("doesnt exist")
