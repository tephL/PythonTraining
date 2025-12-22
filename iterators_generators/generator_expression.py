# Self Multiplier using Generator Expression
## a less flexible way to use a generator, but it works

# formula: (expression? for? if?)

up_to = int(input("Number: "))

multiplies = (x*x for x in range(1, up_to + 1)) # expression

for m in multiplies:
    print(m)