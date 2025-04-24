class Manggo:

    ## MAGIC METHOD
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self): ## sama dengan str
        return f"mangga : {self.nama} dengan jumlah : {self.jumlah}"
    
    def __str__(self): ## sama dengan repr
        return f"mangga : {self.nama} dengan jumlah : {self.jumlah}"
    
    def __add__(self,objek):
        return self.jumlah + objek.jumlah
    
    @property
    def __dict__(self):
        return "objek ini mempunyai nama dan jumlah"
    

belanja1 = Manggo("arumanis",100)
belanja2 = Manggo("lepok",30)
print(belanja1)
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)        
        
