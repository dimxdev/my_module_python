class hero:
    ## CLASS VARIABLE
    jumlah = 0

    def __init__(self,nama,nyawa,power):
        ## INSTANCE VARIABLE
        self.nama = nama
        self.nyawa = nyawa
        self.power = power
        hero.jumlah += 1
        print(f"membuat hero dengan nama {nama}")

hero1 = hero("miya",100,250)
print(hero.jumlah)
hero2 = hero("alucard",100,250)
print(hero.jumlah)
hero3 = hero("zilong",100,250)
print(hero.jumlah)


