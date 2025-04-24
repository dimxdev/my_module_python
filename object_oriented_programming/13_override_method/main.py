class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("Show info di class Hero")
        print(f"{self.name} \n\thealth = {self.health}\n")


class HeroMage(Hero):
    def __init__(self,name):
        super().__init__(name,100)
    
    ## OVERRIDE(MENIMPA METHOD DI SUPERCLASS)
    def showInfo(self):
        print("show info di class hero mage")
        print(f"{self.name} \n\trole = mage \n\thealth = {self.health}\n")


class HeroTank(Hero):
    def __init__(self,name):
        super().__init__(name,400)


eudora = HeroMage("Eudora")
tigreal = HeroTank("Tigreal")

eudora.showInfo()
tigreal.showInfo()