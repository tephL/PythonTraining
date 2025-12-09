books = []
author = []
lists = [books, author]
chc = True
div = "====================="

while chc:
    chc = input(f"Library Menu\n{div}\n1. view books\n2. add books\n3. delete book\n{div}\n")
    print()
    
    if chc=="1":
        print(f"Books\n{div}")
        for x in range(0, len(books)):
            print(f"{x+1}. {books[x]} by {author[x]}")
        print(div)
    elif chc=="2":
        add = input("add: ")
        books.append(add)
        auth = input("author: ")
        author.append(auth)
    elif chc=="3":
        delete = input("name: ")
        books.remove(delete)
    elif chc=="0":
        chc = False
    else:
        print("invalid")
        
    print()
