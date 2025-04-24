class Hero:
    def __init__(self,name,darah,armor):
        self.name = name
        self.__darah = darah
        self.__armor = armor
        # self.info = f"name : {self.name}\nnyawa: {self.__darah}" ## gabisa dirubah isinya

    @property ## akan dianggap variable dan isinya jadi bisa dirubah
    def info(self):
        return f"name : {self.name}\nnyawa: {self.__darah}"
    
    ## ARMOR ARMORAN WKWK
    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("armor di hapus")
        self.__armor = None

    ## DARAH DARAHAN WKWK
    @property
    def darah(self):
        pass

    @darah.getter
    def darah(self):
        return self.__darah
    
    @darah.setter
    def darah(self, input):
        self.__darah = input

    @darah.deleter
    def darah(self):
        self.__darah = None

lesley = Hero("lesley",200,80)
print(lesley.__dict__)
print("-"*15, "\n")

print(lesley.info)
lesley.name = "wanwan"
print(lesley.info)
print("-"*15, "\n")

print(lesley.armor)
lesley.armor = 900 
print(lesley.armor)
del lesley.armor
print(lesley.armor)
print(lesley.__dict__)
print("-"*15, "\n")

print(lesley.darah)
lesley.darah = 9000 
print(lesley.darah)
# del lesley.darah
print(lesley.darah)
print(lesley.__dict__)
print("-"*15, "\n")







