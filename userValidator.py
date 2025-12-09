usern = input("input username: ")

if not len(usern) <= 12:
    print("usern must only be 12 characters")
elif not usern.find(" "):
    print("no spaces")
elif usern.isdigit():
    print("no digits")
else:
    print(f"success, hello {usern}")
    