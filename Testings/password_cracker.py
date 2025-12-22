# Change (user input) -> (wifi pass input field's connection status)

import random as r
import os
import time as t

def clear_cli():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

passw = input("password: ")
size = len(passw) + 1

guesses = []
guess = ""
start = t.time()
atm = 0
while passw != guess:
    guess = ""
    for x in range(1, size):
        nums = r.randint(1,9)
        guess += str(nums)
    print(guess)
    atm+=1
    '''
    if guess not in guesses:
        guesses.append(guess)
        print(guess)
        #print(guesses)
        #t.sleep(0.005)
        #clear_cli()
        '''
end = t.time()
time = end - start

x = 0
for g in guesses:
    print(g, end = "| ")
    x += 1
    if x % size/10 == 0:
        print()

print(f"\n\ntook {time:.2f}s, {len(guesses)+atm} guesses\npass = {guess}")
    