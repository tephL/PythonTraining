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

    def balance(self):
        for user in self.users:
            print(f"User: {user.username} | Balance: {user.balance}")

    def deposit(self, username, amt):
        for user in self.users:
            if user.username == username:
                user.balance += amt
                notFound = False
        print("not found" if notFound else "found")


class User:
    balance = 100

    def __init__(self, username, password):
        self.username = username
        self.password = password

Crinkles = Bank("Crinkles")
div = "=" * 30
div2 = "-" * 50

# for future use once its all done
'''
def main():

    while True:
        print(div)
        print("Welcome to the Crinkles Banks")
        print(div)
        chc = int(input(f"1. Sign in\n2. Sign Up\n3. Admin\n{div}\n> "))
        print()

        match chc:
            case 1:
                username = input("Username: ")
                password = input("Password: ")
                User.validator(username, password)
            case 2:
                signupPage()
            case 3:
                adminpage()
            case _:
                print("Invalid. Try again.")
        print()
        

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

def adminpage():
    Crinkles.addUser("teph", 1234)

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
                Crinkles.deposit("teph",100)
            case 4:
                Crinkles.withdraw(100)
            case 5:
                Crinkles.balance()
            case _:
                print("invalid")
        print()


def test():
    print(User.balance)
    print(Crinkles.balance())


if __name__ == "__main__":
    adminpage()
