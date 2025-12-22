# .Thread(target = func?, args = (arg1, )
# .start()
## start threading
# .join()
## wait before continuing program

import threading
import time as t

def shoot():
    t.sleep(3)
    print("you shoot the yn")
    
def move():
    print("you are moving")
    
act1 = threading.Thread(target=shoot)
act1.start()

act2 = threading.Thread(target=move)
act2.start()

act1.join()
act2.join()

print("\nmission complete")