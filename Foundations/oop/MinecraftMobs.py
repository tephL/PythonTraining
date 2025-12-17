class MinecraftMob:    
    hp = 10
    
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack
    
    def speak(self):
        print(f"Hello, I am {self.name}")
    
    def doDmg(self):
        print(f"I've dealt {self.attack} damage")

class Hostile(MinecraftMob):
     def speak(self):
        print(f"I am {self.name}Zxz")
        
class Animal(MinecraftMob):
     def speak(self):
         print("...")
     
     
def main():
    mob1 = Animal("Sheep", "5")
    mob2 = MinecraftMob("Notch", "100")
    mob3 = Hostile("Zombie", "10")
    
    print(mob1.attack)
    print(mob2.attack)
    print(mob3.attack)
    print()
    
    mob1.speak()
    mob2.speak()
    mob3.speak()
    print()
    
if __name__ == '__main__':
        main()