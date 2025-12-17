#simple login auth
import time as t

class Site:
    userlist = {"tephL":"1228"}
    
    def __init__(self, name):
        self.name = name
        
    def sessiontime(func):
        def wrapper(*args, **kwargs):
            startsesh = t.time()
            func(*args, **kwargs)
            endsesh = t.time()
            seshtime = round(endsesh - startsesh)
            print(f"sesh: {seshtime}s" if seshtime<60 else f"sesh: {round(seshtime/60)}min")
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
        
    @auth
    @sessiontime
    def dashboard(self, user, password):
        print(f"Welcome! {user}")
        while True:
            chc = int(input("0. Logout\n> "))
            if chc == 0:
                return
    
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
        