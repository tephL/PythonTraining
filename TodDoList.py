# To do list

div = "-"*30

class Task:
    def __init__(self, task, status):
        self.task = task
        self.status = status

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
        self.tasks.append(Task(task, False))
        
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


def main():
    todo = List("To do List")
    while True:
        print("1. View\n2. Add\n3. Delete\n4. Update\n0. Quit")
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
            case 0:
                quit()
            case _:
                print("Invalid")
        print()



if __name__ == '__main__':
    main()

