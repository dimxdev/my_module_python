class Hero:
    def __init__(self,nama,nyawa,demage,armor):
        self.nama = nama
        self.nyawa = nyawa
        self.demage = demage
        self.armor = armor
    
    def serang(self, musuh):
        print(f"{self.nama} menyerang {musuh.nama}")
        musuh.diserang(self, self.demage)
    
    def diserang(self, musuh, demageMusuh):
        print(f"{self.nama} diserang {musuh.nama}")
        demageDiterima = demageMusuh/self.armor
        print(f"demage terasa = {demageDiterima}")
        self.nyawa -= demageDiterima
        print(f"darah {self.nama} tersisa {self.nyawa}")

wanwan = Hero("wanwan", 100, 20, 10)
lesley = Hero("lesley", 100, 25, 5)

wanwan.serang(lesley)
print("")
lesley.serang(wanwan)
print("")
wanwan.serang(lesley)
print("")
wanwan.serang(lesley)
print("")
wanwan.serang(lesley)
print("")