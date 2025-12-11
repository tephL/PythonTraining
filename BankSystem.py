#Crinkles Banks
div = "="*30
def main():
    while True:
        print(div)
        print("Welcome to the Crinkles Banks")
        print(div)
        chc = int(input(f"1. Sign in\n2. Sign Up\n{div}\n> "))
        print()

        match chc:
            case 1:
                username = input("Username: ")
                password = input("Password: ")
                User.validator(username, password)
            case 2:
                signupPage()
            case _:
                print("Invalid. Try again.")
        print()

class User:
    balance = 100

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def addBalance(self, amount):
        self.balance += amount

    def removeBalance(self, amount):
        self.balance -= amount

    def validator(username, password):
        if username == "1" and password == "1":
            menupage(username)

        else:
            print("\nInvalid. Try again.")

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
                User.addBalance( amt)
            case 0:
                print("Bye")
                break
            case _:
                print("Invalid. Try again.")
            
    def balance():
        print


if __name__ == "__main__":
    main()
