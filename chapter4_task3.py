class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.odometer = 0
        self.fuel = 700
            
    def drive(self, kettic): #кеттик это значение которое мы вводим где хонда 
        if kettic <=700:       # 1) значение хонда драйф идет к кеттик
            self.__add_distance(kettic) # 2)с кеттик он сравнивается с условием иф
            self.__subtract_fuel(kettic)  
            print("let's drive!")   # 5) и потом выводит результат, что и как осталось
            print(self.odometer)    
            print(self.fuel/10)     # 6) тут мы делим рузельтат на 10, чтоб уравнить литры
        else:
            print("Need more fuel, please, fill more!")
                  
    def __subtract_fuel(self, oil): # 4) потом сюда, и минусуется с фуел
        self.fuel -= oil           
       
            
    def __add_distance(self, km): # 3) если уловие верное, то он идет сюда и плюсуется к одометру
        self.odometer += km
       

honda = Car("honda", "Fit", "2010")

honda.drive(70)
honda.drive(70)
honda.drive(569)

