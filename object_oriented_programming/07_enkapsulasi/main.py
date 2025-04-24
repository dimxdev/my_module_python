class Hero:

    def __init__(self,name,darah,demage):
        self.__name = name
        self.__darah = darah
        self.__demage = demage

    ## GETTER
    def getName(self):
        return self.__name
    
    def getDarah(self):
        return self.__darah
    
    def getDemage(self):
        return self.__demage
    

    ## SETTER
    def diserang(self,demageMusuh):
        self.__darah -= demageMusuh

    def setDemage(self, nilaiBaru):
        self.__demage = nilaiBaru

## awal game
miya = Hero("miya",200,400)
print(miya.__dict__)
print(miya.getName())
print("-"*15, "\n")

print(miya.getDarah())
miya.diserang(90)
print(miya.getDarah())
print("-"*15, "\n")

print(miya.getDemage())
miya.setDemage(900)
print(miya.getDemage())
print("-"*15, "\n")


 