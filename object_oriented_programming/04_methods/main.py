class Hero:
    ## CLASS VARIABLE
    jumlah_hero = 0

    def __init__(self, input_nama, input_nyawa, input_demage):
        ## INSTANCE VARIABLE
        self.nama = input_nama
        self.nyawa = input_nyawa
        self.demage = input_demage
        Hero.jumlah_hero += 1

    ## METHOD TANPA ARGUMENT
    def nama_hero(self):
        print(f"hallo namaku {self.nama}")

    ## METHOD DENGAN ARGUMENT
    def heal_up(self, up):
        self.nyawa += up

    ## METHOD MENGGUNAKAN RETURN
    def getNyawa(self):
        return self.nyawa
    
wanwan = Hero("wanwan", 2000, 350)
lesley = Hero("lesley", 1500, 550)
harith = Hero("harith", 4500, 250)

wanwan.nama_hero()
print(f"nyawa semula = {wanwan.nyawa}")
wanwan.heal_up(400)
print(f"nyawa sekarang = {wanwan.getNyawa()}")



