class Soldier:
    def __init__(self, name):
        self.name = name
             
  
class Guns:
    def __init__(self, bullet):
        self.bullet = bullet
             
        
class Act_of_Shooting(Soldier, Guns):
    def __init__(self, name, bullet):
        Soldier.__init__(self, name)
        Guns.__init__(self, bullet)
        
    def war(self, piu):
        if piu > self.bullet:
            self.__reload()
            print(f"В бой вступает солдат: {self.name}")
            print(f"но {self.name}  перезаряжается, и тиги тигидишь")
        else: 
            print(f"В бой вступает солдат: {self.name}")
            print(f"у него есть: {self.bullet} пуль")
            self.__piu(piu)
            print(f"{self.name}: 'piu piu'(это он так стреляет)")
               
    def __piu(self, piu_piu):
        self.bullet -= piu_piu
        
    def __reload(self):
        self.bullet += 3
        
battle = Act_of_Shooting("Asat", 3)
battle.war(3)
print()
battle = Act_of_Shooting("Darknes", 5)
battle.war(6)