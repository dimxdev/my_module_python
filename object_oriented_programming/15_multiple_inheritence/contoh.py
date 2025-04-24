class Team:
    def setTeam(self,team):
        self.team = team

    def showTeam(self):
        print(self.team)

class Tipe:
    def setTipe(self,tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)

class Hero(Team,Tipe):

    def __init__(self,name,health):
        self.nama = name
        self.health = health


ucup = Hero("ucup",1000)
print(ucup.health)
ucup.setTeam("ungu")
ucup.setTipe("ox")
ucup.showTeam()
ucup.showTipe()
        

    