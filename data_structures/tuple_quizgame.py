q_num = 0
border = "-" * 20 + "+"

questions = ("1. Best cookies?", 
                      "2. Best Animal?",
                      "3. Best Color?",
                      "4. Best skin color?",
                      "5. Best baby?")
                      
answers = [("A. Crinkles", "B. Chocolate Chip", "C. Milk Dipped", "D. Milk Cookies"),
                    ("A. Bunny", "B. Goat", "C. Bird", "D. Wolf"),
                    ("A. Green", "B. Blue", "C. Red", "D. Black"),
                    ("A. Nigga", "B. White", "C. Yellow", "D. Rotting "),
                    ("A. Suvi", "B. Suvi", "C. Suvi", "D. Suvi"),]
                    
correct = [("A"),("B"),("D"),("D"),("SUVI")]

guess = []

for q in questions:
    print(border)
    print(q)
    for ans in answers[q_num]:
        print(ans)
    guess.append(input("Answer: ").upper())
    q_num += 1
    print()
    
pts = 0
q_num = 0
    
for c in correct:
    if correct[q_num] == guess[q_num]:
        pts+=1
    q_num += 1
    
if pts == len(correct):
    print("You got a perfect score! 100% Correct!")
else:
    print(f"You got {pts} correct! {(pts/len(questions))*100}%")
    