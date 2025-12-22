# Iteration dunder
# Uses:
# 1. Iteration outside the object 
### for student in room = Classroom(["Stephen"])
# 2. Turning an object into a Local list
### local_list = list(room)
# 3. Checking elements within the Object
### if "name" in room

class Classroom:
    def __init__(self, student = None):
        if student == None: # just making an object
            self.student = []
        else: # if it was a List
            self.student = student           
        self.index = 0
        
    def addStudent(self, student):
        self.student.append(student)
        
    def viewStudents(self): # (Not needed) This is less flexible than iteration
        print(f"Student List (function)\n{'='*20}")
        for student in self.student:
            print(student)
        print("="*20)
    
    def __iter__(self):
        self.index = 0
        return self
        
    def __next__(self):
        if self.index >= len(self.student):
            raise StopIteration
        value = self.student[self.index]
        self.index += 1
        return value
        
        
def main():
    fg = Classroom()
    while True:
        chc = int(input("1. Add Student\n2. View Students\n3. View Students (func)\n4. Check Student\n5. Local List\n> ")) 
        
        print()        
        match chc:        
            case 1:
                fg.addStudent(input("Name: "))
            case 2:
                print(f"Student List\n{'='*20}")
                for student in fg:
                    print(f"1. {student}")
                print("="*20)
            case 3:
                fg.viewStudents()
            case 4:
                find = input("Name: ")
                if find in fg:
                    print("Found")
                else:
                    print("Not found")
            case 5:
                pullStudents = list(fg)
                for student in pullStudents:
                    print(pullStudents)
        print()
                    
    
if __name__ == '__main__':
    main()