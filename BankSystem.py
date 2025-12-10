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
                validator(username, password)
            case 2:
                signupPage()
            case _:
                print("Invalid. Try again.")
        print()


def validator(username, password):
    if username == "tephL" and password == "1":
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
                print(1)
            case 2:
                print(2)
            case 3:
                print(3)
            case 0:
                print("Bye")
                break
            case _:
                print("Invalid. Try again.")

if __name__ == "__main__":
    main()
