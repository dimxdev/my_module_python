from hero import HeroMage,HeroTank

gord = HeroMage("Gord")
beledog = HeroTank("Belerick")

gord.showInfo()
beledog.showInfo()

gord.gainExp = 200
beledog.gainExp = 300

gord.showInfo()
beledog.showInfo()
