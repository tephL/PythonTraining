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
            for task in self.tasks:
                ctr = 1
                print(f"{task.getStatus():<10}| {task.task:<18}|")
                ctr += 1
            print(f"{div}|")
        else:
            print("none")

    def addTask(self, task):
        self.tasks.append(Task(task, False))


def main():
    todo = List("To do List")
    while True:
        print("1. View\n2. Add\n3. Delete\n0. Quit")
        chc = int(input("Enter your choice: "))

        print()
        match chc:
            case 1:
                todo.viewTasks()
            case 2:
                todo.addTask(input("Task: "))
            case 3:
                todo.deleteTask(input("Task: "))
            case 0:
                quit()
            case _:
                print("Invalid")
        print()



if __name__ == '__main__':
    main()

