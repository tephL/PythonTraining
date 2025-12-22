import datetime as dt
import time as t
import os

def currtime():
    time = dt.datetime.now().strftime("%H:%M:%S")
    return time

def alarmclock(hour, minute, second, ring_time):
    alarm = dt.time(hour, minute, second).strftime("%H:%M:%S")  
    while True:
        time = dt.datetime.now().strftime("%H:%M:%S")
        print(f"Time: {time}")
        t.sleep(1)
        clear_cli()
        if alarm <= time:
            for x in range(1,ring_time + 1):
                time = dt.datetime.now().strftime("%H:%M:%S")
                print(f"Time: {time} - Alarm ringing for {x}s")
                t.sleep(1)
                clear_cli()
            break

def main():
    print(f"Welcome to alarm clock (Time: {currtime()})\n")
    h = int(input("Hour: "))
    m = int(input("Minutes: ")) 
    s = int(input("Seconds: "))
    r = int(input("Ring time: "))  
    print()
    alarmclock(h, m, s, r) 
    
def clear_cli():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux/macOS
    else:
        os.system('clear')    
    
    
if __name__ == '__main__':
    main()
    #alarmclock(11,21,50,5)