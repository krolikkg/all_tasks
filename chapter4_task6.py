class Home:
    def __init__(self, name, area):
        self.name = name
        self.area = area
        self.remain = 0
    
    def bring(self, **kwargs):
        self.remain = self.area - sum(kwargs.values())
        print (f"type of home: {self.name}")
        print (f"total area: {self.area}")
        print (f"remaining area: {self.area}")
        print ("ferniture names: ", ', '.join(kwargs.keys()))
        
mda = Home("болоберет", 97.5)
mda.bring(bad=4, table=1.5, wardrobe=2)





# class Home:
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
        
#     def bring(self):
#         print(f"house tepy: {self.name}")
#         print(f"размер дома: {self.area} м**2")
#         self.__bed()
#         self.__Wardrode()
#         self.__table()
#         print("заносим мебель")
#         print(f"осташее место: {self.area}")
        
        
#     def __bed(self):
#         self.area -= 4
        
#     def __Wardrode(self):
#         self.area -= 2
        
#     def __table(self):
#         self.area -= 1.5
        
# mda = Home("элитка", 15)
# mda.bring()

