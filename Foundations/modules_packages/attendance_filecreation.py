# Attendance
# Change {file_path} with your own File Directory names

def name_list(file_path):
    
    try:
        with open(file_path, "x") as x:
            pass
    except FileExistsError:
        with open(file_path, "w") as x: 
            pass            
    
    while True:
        chc = int(input("1. Add name\n2. Read names\n0. Done\n> "))
        
        print()
        match chc:
            case 1:
                name = input("name: ")
                with open(file_path, "a") as x:
                    x.write("\n" + name)
            case 2:
                with open(file_path, "r") as x:
                    print(x.read())
            case 0:
                return
            case _:
                print()
        print()

def main():
    x = 1
    
    while True:
        file_path = f"Python/attendance/day{x}.txt"
        chc = int(input("1. Current Day\n2. New day\n> "))
        
        print()
        match chc:
            case 1:
                name_list(file_path)
            case 2:
                x+=1
            case 0:
                break
            case _:
                print()
        print()
            

if __name__ == '__main__':
    main()