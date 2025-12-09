#timer
import time

seconds = int(input("Seconds: "))

for x in reversed(range(1,seconds+1)):
    print(x)
    time.sleep(1)
print("Time's up!")