phnum = input("Phone Num: ")

if len(phnum) == 11:
    first4 = phnum[0:4]
    last2 = phnum[-2:]
    print(f"Anon num: {first4}-XXX-XX{last2}")
else:
    print("invalid")