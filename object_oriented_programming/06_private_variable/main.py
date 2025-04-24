class hero:

    # CLASS VARIABLE
    jumlah = 0
    __privateJumlah = 0

    def __init__(self,name,nyawa,demage):
        self.name = name
        self.nyawa = nyawa
        self.demage = demage

        ## INSTANCE VARIABLE PRIVATE
        self.__private = "hmm"
        
        ## INSTANCE VARIABLE PROTECTED
        self._protected = "hhh"

lina = hero("lina", 100, 100)
print(lina.__dict__)
print(hero.__dict__)
# print(hero.__privateJumlah)
print(lina._protected)