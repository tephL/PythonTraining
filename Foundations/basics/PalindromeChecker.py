while True:
    word = input("Word: ")
    print()
    
    p1 = 0
    p2 = len(word) - 1
    
    while p1 <= p2:
        if word[p1] == word[p2]:
            Palindrome = True
        else:
            Palindrome = False
        p1 += 1
        p2 -= 1
            
    print("ye" if Palindrome==True else "nah")
    print()