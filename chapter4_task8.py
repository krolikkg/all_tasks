class MoneyFmt:
    def __init__(self, data):
        self.data = data
        self.money = 0
    def updata(self, data2):
        self.money = data2
        print(data2)
    
    def repr(self):
        print(self.data)
    
    def str(self):
        self.money = '${:,.2f}'.format(self.data)
        print(self.money)
        
cash = MoneyFmt(-12412412313)
cash.str()
cash.updata(100000.12)


