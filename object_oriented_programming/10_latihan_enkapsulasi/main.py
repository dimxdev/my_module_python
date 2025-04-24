import os
os.system("cls")

class Hero: 
    __jumlah = 0

    def __init__(self,name,health,attPower,armor):
        self.__name = name
        self.__healthStandard = health
        self.__attpowerStandard = attPower
        self.__armorStandard = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandard * self.__level
        self.__attpower = self.__attpowerStandard * self.__level
        self.__armor = self.__armorStandard * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1 

    @property
    def info(self):
        return f"{self.__name} level {self.__level}: \n\thealth = {self.__healthStandard}/{self.__healthMax} \n\tattack = {self.__attpower} \n\tarmor  = {self.__armor}"
    
    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if(self.__exp >= 100):
            print(self.__name, "level up")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandard * self.__level
            self.__attpower = self.__attpowerStandard * self.__level
            self.__armor = self.__armorStandard * self.__level

    def attack(self, musuh):
        self.gainExp = 50

zilong = Hero("zilong",100,30,70)
lapu_lapu = Hero("lapu-lapu",30,40,70)
print(zilong.info)
print(lapu_lapu.info)
zilong.gainExp = 30
zilong.attack(lapu_lapu)
zilong.attack(lapu_lapu)
zilong.attack(lapu_lapu)
zilong.attack(lapu_lapu)
zilong.attack(lapu_lapu)
print(zilong.info)
print(zilong.__dict__)
