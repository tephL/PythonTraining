#simple login auth
import time as t

class Site:
    
    def __init__(self, name):
        self.name = name
        self.userlist = {"tephL":"1228"}
        
    def sessiontime(func):
        def wrapper(*args, **kwargs):
            startsesh = t.time()
            func(*args, **kwargs)
            endsesh = t.time()
            seshtime = endsesh - startsesh
            print(f"sesh: {seshtime:.2f}s" if seshtime<60 else f"sesh: {(seshtime/60):.2f}min")
        return wrapper
        
    def sessiontime2(func):
        def wrapper(*args, **kwargs):
            start = t.perf_counter()
            func(*args, **kwargs)
            end = t.perf_counter()
            time = start - end
            print(f"sess: {time:.2f}" if time < 60 else f"sess{time:.2f}")
        return wrapper
    
    def auth(func):
        def wrapper(self, user, password, *args, **kwargs):
            if user in self.userlist.keys():
                if self.userlist.get(user) == password:
                    func(self, user, password, *args, **kwargs)
                else:
                    print("err: xpass")
            else: 
                print("err: noexist")
        return wrapper
        
    def settings(self):
        while True:
            chc = int(input("1. Change Password\n0. Exit"))
            
            print()
            match chc:
                case 1:
                    newpass = input("New password: ")
                    self.userlist.update({self.current_user:newpass})
                    print(f"New pass: {self.userlist.get(self.current_user)}")
                case 0:
                    return
            print()
        
    @auth
    @sessiontime2
    @sessiontime
    def dashboard(self, user, password):
        self.current_user = user
        print(f"Welcome! {user}")
        while True:
            chc = int(input("1. Settings\n0. Logout\n> "))
            
            print()
            match chc:
                case 1:
                    self.settings()
                case 0:
                    return
            print()
    
    def register(self, user, password):
        formatteduser = self.formatter(user)
        self.userlist[formatteduser] = password
        print(f"successfully created {formatteduser}")
        return
        
    def formatter(self, user):
        formatteduser = user.lower()
        x = 1
        
        while formatteduser in self.userlist:
            reformatteduser = formatteduser #retake original word without concatenation
            reformatteduser += str(x)         
            if reformatteduser not in self.userlist:       
                return reformatteduser
                break
            x+=1
        return formatteduser
        

def main():
    s = Site("tephsite")
    while True:
        chc = int(input("1. Login\n2. Register\n0. Exit\n> "))
        
        print()
        match chc:
            case 1:
                s.dashboard(input("User: "), input("Password: "))
            case 2:
                s.register(input("User: "), input("Set password: "))
            case 0:
                print("000")
                break
        print()
        
if __name__ == '__main__':
    main()    
        