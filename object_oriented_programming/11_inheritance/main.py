"""
   inheritance adalah pewarisan (superclass, subclass)
"""
class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

class HeroMage(Hero):
    pass

class HeroMarksman(Hero):
    pass

default = Hero("hero default",None)
lunox = HeroMage("lunox", 200)
layla = HeroMarksman("layla", 400)

print(default.__dict__)
print(lunox.name)
print(layla.name)