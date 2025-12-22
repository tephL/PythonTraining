# Crinkles Banks
class Bank:
    def __init__(self, bankname):
        self.bankname = bankname
        self.users = []

    #admin funcs
    def addUser(self, username, password):
        self.users.append(User(username, password))

    def userList(self):
        print(f"Username" + f"{'| Password':>27}\n{div2}")
        for user in self.users:
            print(f"{user.username:<24} | {user.password:>5}")
        print(div2)

    def allBalance(self):
        for user in self.users:
            print(f"User: {user.username} | Balance: {user.balance}")

    def balance(self, username):
        for user in self.users:
            if user.username == username:
                print(user.balance)
    
    def deposit(self, username, amt):
        for user in self.users:
            if user.username == username:
                user.balance += amt
                notFound = False
        print("not found" if notFound else "found")
        
    def withdraw(self, username, amt):
        for user in self.users:
            if user.username == username:
                user.balance -= amt
                notFound = False
        print("not found" if notFound else "found")
        
    def validator(self, username, password):
        valid = False
        for user in self.users:
            if user.username == username and user.password == password:
                valid = True
        if valid:
            return True
        else:
            return False


class User:
    balance = 100

    def __init__(self, username, password):
        self.username = username
        self.password = password

Crinkles = Bank("Crinkles")
div = "=" * 30
div2 = "-" * 50

def main():

    while True:
        print(div)
        print("Welcome to the Crinkles Banks")
        print(div)
        chc = int(input(f"1. Client\n2. Admin\n{div}\n> "))
        print()

        match chc:
            case 1:
                username = input("Username: ")
                password = input("Password: ")
                if Crinkles.validator(username, password):
                    clientpage(username)
                else:
                    print("error")
            case 2:
                adminpage()
            case _:
                print("Invalid. Try again.")
        print()

# for future use once its all done
'''
def menupage(username):
    print(f"\nWelcome, {username}!")

    while True:
        print(f"{div}\n{'Menu':>17}\n{div}")
        print(f"1. Balance\n2. Withdraw\n3. Deposit\n0. Log out\n{div}")
        chc = int(input("> "))
        match chc:
            case 1:
                print(f"Your balance is: {User.balance}")
            case 2:
                amt = int(input("Withdraw: "))
                User.removeBalance(amt)
            case 3:
                amt = int(input("Deposit: "))
                User.addBalance(amt)
            case 0:
                print("Bye")
                break
            case _:
                print("Invalid. Try again.")

    def balance():
        print
'''


def clientpage(username):
    while True:
        print(f"{div}\nBank Client Page\n{div}")
        chc = int(input(f"1. Deposit\n2. Withdraw\n3. Balance\n{div}\n> "))

        print()
        match chc:
            case 1:
                amt = int(input("Amount: "))
                Crinkles.deposit(username,amt)
            case 2:
                amt = int(input("Amount: "))
                Crinkles.withdraw(username,amt)
            case 3:
                Crinkles.balance(username)
            case 0:
                return
            case _:
                print("invalid")
        print()

def adminpage():
    while True:
        print(f"{div}\nBank Admin Page\n{div}")
        chc = int(input(f"1. Add User\n2. List of Users\n3. Deposit\n4. Withdraw\n5. Balance\n{div}\n> "))

        print()
        match chc:
            case 1:
                username = input("Username: ")
                password = input("Password: ")
                Crinkles.addUser(username, password)
            case 2:
                Crinkles.userList()
            case 3:
                username = input("Username: ")
                amt = int(input("Amount: "))
                Crinkles.deposit(username,amt)
            case 4:
                username = input("Username: ")
                amt = int(input("Amount: "))
                Crinkles.withdraw(username,amt)
            case 5:
                Crinkles.allBalance()
            case 0:
                return
            case _:
                print("invalid")
        print()


def test():
    print(User.balance)
    print(Crinkles.balance())


if __name__ == "__main__":
    main()
