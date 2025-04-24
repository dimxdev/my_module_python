class Hero:

    ## PRIVATE CLASS VARIABLE
    __jumlah = 0

    def __init__(self,name):
        self.name = name
        Hero.__jumlah += 1

    ## method ini hanya berjalan untuk object
    def getJumlah1(self):
        return Hero.__jumlah
    
    ## method ini hanya berjalan untuk class
    def getJumlah2():
        return Hero.__jumlah
    
    ## method static(decorator) nempel ke object dan class
    @staticmethod
    def getJumlah3():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah4(cls):
        return cls.__jumlah
    
wanwan = Hero("wanwan")
print(wanwan.getJumlah1())
lesley = Hero("lesley")
print(Hero.getJumlah2())
harith = Hero("harith")
# print(harith.getJumlah3())
# print(Hero.getJumlah3())
# print(harith.getJumlah4())
print(Hero.getJumlah4())
    