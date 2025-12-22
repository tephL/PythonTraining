# To do list
import sqlite3

conn = sqlite3.connect("todolist.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    taskname TEXT UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_done INTEGER DEFAULT 0
)
""")
conn.commit()

div = "-"*30

class todolist:
    def __init__(self, name):
        self.name = name

    def viewTasks(self):
        cursor.execute("SELECT id, taskname, created_at, is_done FROM tasks")
        print(f"{'ID':<3}| Task{'|':>18} {'Date':<19} | ")
        for row in cursor.fetchall():
            id = row[0]
            taskname = row[1]
            created_at = row[2]
            is_done = row[3]
            print(f"{id:<3}| {taskname:<20} | {created_at} | {is_done}")
    
    def addTask(self, task):
        cursor.execute("INSERT INTO tasks (taskname) VALUES (?)", (task,))
        conn.commit()
        
    def deleteTask(self, id):
        cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
            
    def editTask(self, ctr2, newTask):
        pass
                
    def taskDone(self, id):
        cursor.execute("UPDATE tasks SET is_done = 1 WHERE id = ?", (id,))
        conn.commit()
                
    def taskUndone(self, id):
        cursor.execute("UPDATE tasks SET is_done = 0 WHERE id = ?", (id,))
        conn.commit()
                
    def switchNum(self, switch1, switch2):
        pass

def main():
    todo = todolist("To do List")
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

