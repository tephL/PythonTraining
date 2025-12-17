# To do list

div = "-"*30

class Task:
    status = False
    
    def __init__(self, task):
        self.task = task

    def getStatus(self):
        if self.status == False:
            return "X"
        else:
            return "Y"

class List:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def viewTasks(self):
        if self.tasks:
            print(f"{div}|\n{'Status':<10}| {'Tasks':<18}|\n{div}|")
            ctr = 1
            for task in self.tasks:
                print(f"{task.getStatus():<10}| {ctr}. {task.task:<15}|")
                ctr += 1
            print(f"{div}|")
        else:
            print("none")
    
    def addTask(self, task):
        self.tasks.append(Task(task))
        
    def deleteTask(self, ctr):
        if self.tasks:
            self.tasks.pop(ctr-1)
        else:
            print("empty")
            
    def editTask(self, ctr2, newTask):
        if self.tasks:
            ctr = 0
            for task in self.tasks:
                if ctr == ctr2-1:
                    task.task = newTask
                    break;
                ctr += 1
                
    def taskDone(self, ctr2):
        if self.tasks:
            ctr = 0
            for task in self.tasks:
                if ctr == ctr2-1:
                    task.status = True
                    break;
                ctr += 1
                
    def taskUndone(self, ctr2):
        if self.tasks:
            ctr = 0
            for task in self.tasks:
                if ctr == ctr2-1:
                    task.status = False
                    break;
                ctr += 1
                
    def switchNum(self, switch1, switch2):
        if self.tasks:
            ctr = 0
            for task in self.tasks:
                if ctr == switch1-1:
                    ctr=0
                    for task2 in self.tasks:
                        if ctr == switch2-1:
                            holder = task.task
                            holderstatus = task.status
                            task.task = task2.task
                            task.status = task2.status
                            task2.task = holder
                            task2.status = holderstatus
                            break;                            
                    break;
                ctr += 1

def main():
    todo = List("To do List")
    while True:
        print("1. View\n2. Add\n3. Delete\n4. Update\n5. Done")
        print("6. Undone\n7. Switch\n0. Quit")
        chc = int(input("Enter your choice: "))

        print()
        match chc:
            case 1:
                todo.viewTasks()
            case 2:
                todo.addTask(input("Task: "))
            case 3:
                todo.deleteTask(int(input("Task: ")))
            case 4:
                todo.editTask(int(input("Num: ")), input("Task: "))
            case 5:
                todo.taskDone((int(input("Num: "))))
            case 6:
                todo.taskUndone((int(input("Num: "))))
            case 7:
                todo.switchNum(int(input("Num1: ")), int(input("Num2: ")))
            case 0:
                quit()
            case _:
                print("Invalid")
        print()



if __name__ == '__main__':
    main()

