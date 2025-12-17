#simple login auth
import time as t

class Site:
    userlist = ["tephL"]
    
    def __init__(self, name):
        self.name = name
        
    def auth(func):
        def wrapper(self, user, *args, **kwargs):
            if user in self.userlist:
                startsesh = t.time()
                func(self, user, *args, **kwargs)
                endsesh = t.time()
                seshtime = round(endsesh - startsesh)
                print(f"sesh: {seshtime}s" if seshtime<60 else f"sesh: {round(seshtime/60)}min")
            else: 
                print("err: noexist")
        return wrapper
        
    @auth
    def dashboard(self, user):
        print(f"Welcome! {user}")
        while True:
            chc = int(input("0. Logout\n> "))
            if chc == 0:
                return
    
    def register(self, user):
        formatteduser = self.formatter(user)
        self.userlist.append(formatteduser)
        print(f"successfully created {formatteduser}")
        return
        
    #@staticmethod    
    def formatter(self, user):
        formatteduser = user.lower()
        x = 0
        
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
                s.dashboard(input("User: "))
            case 2:
                s.register(input("User: "))
            case 0:
                print("000")
                break
        print()
        
if __name__ == '__main__':
    main()    
        