class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print(f"{self.name} mempunyai darah : {self.health}")

class Hero_mage(Hero):
    def __init__(self,name):
        # Hero.__init__(self,name,100)
        super().__init__(name,100)
        super().showInfo()

class Hero_marksman(Hero):
    def __init__(self,name):
        # Hero.__init__(self,name,200)
        super().__init__(name,200)
        super().showInfo()

lunox = Hero_mage("lunox")
clint = Hero_marksman("clint")