books = ["Atomic Habits", "The Catcher in the Rye", "Bible", "Niggas vs Jews"]
author = ["James Clear", "J.D. Sallinger", "Moses, etc.", "White W."]
lists = [books, author]
chc = True
div = "====================="

while chc:
    chc = input(f"{div}\nLibrary Menu\n{div}\n1. View books\n2. Add books\n3. Delete book\n0. Exit\n{div}\nChoice: ")
    print()
    
    if chc=="1":
        if len(books) == 0:
            print("Library is empty")
        else:
            print("----------------------------------------------------------")
            print(f"{'Name':<33} | {'Author':<20} |")
            print("----------------------------------------------------------")
            for x in range(0, len(books)):
                print(f"{x+1}. {books[x]:<30} | {author[x]:<20} |")
            print("----------------------------------------------------------")
    elif chc=="2":
        add = input("Book: ")
        books.append(add)
        auth = input("Author: ")
        author.append(auth)
    elif chc=="3":
        delete = input("name: ")
        if delete in books:
            books.remove(delete)
            print(f"Successfuly Deleted {delete}")
        else:
            print("Does not exist")
    elif chc=="0":
        chc = False
    else:
        print("Invalid")-0
        
    print()
