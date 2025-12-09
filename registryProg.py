#User Registry
print("Hello, Register now!")
name = input("\nName: ")

# Num anonymizer
numStatus = False

while not numStatus:
    phnum = input("\nPhone Num: ")
    
    if len(phnum) == 11:
        first4 = phnum[0:4]
        last2 = phnum[-2:]
        anonNum = f"{first4}-XXX-XX{last2}"
        numStatus = True
    else:
        print("Try again.\n")
        
# email slicer
mailStatus = False
while not mailStatus:
    email = (input("\nEmail: "))
         
    locAt = email.find("@")
    beforeAt = email[0:locAt]
    site = email[locAt+1:]
    com = site[-4:]
    
    if email.find("@") and com==".com":
        choppedMail = f"{beforeAt} | ix@: {locAt} | {site}"
        mailStatus = True
    else:
        print("Invalid email.")
        
print("\nSuccessfully Registered!")
print(f"\nHello {name}!")
print(f"Phone Num: {anonNum:>10}")
print(f"Email: {choppedMail:>10}")