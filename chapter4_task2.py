class Airplane:
    def __init__(self, make, model, year, max_speed, odometer, is_flying):
        self.make      = make
        self.model     = model
        self.year      = year
        self.max_speed = max_speed
        self.odometer  = 0
        self.is_flying = False
        
    def take_off(self):
        self.is_flying = True
        print(
            f"Всем привет на борту: {self.model}, наш самолет набирает высоту, просим вас не поднимать свою пятую точку"
            )
        
        
    def fly(self, km):
        self.odometer = self.odometer + km
        print(f"Борт {self.model} набрал скорость {self.max_speed}, можете размяться. Мы пролетели: {self.odometer} km")
            
    def land(self):
        print(f"{self.make} заходит на посадку,кстати самолет {self.year} года)))")

arabik = Airplane(make='Арабик эирлайнс', model="мк22001119", year="2015", max_speed=300, is_flying="Взлет", odometer=() )
arabik.take_off()
arabik.fly(6.5)
arabik.land()
            