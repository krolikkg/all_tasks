class Students:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        
    def read(self):
          
        print(
            f"name: {self.name}, age: {self.age}, major: {self.major}"
            )
        
Steve = Students("Kalmuratov Mederbek", "19", "IT")
Steve.read()

    
    