
class Player:

    def __init__(self):
        self.money = 0
        self.life = 50

    def getMoney(self):
        return self.money

    def getLife(self):
        return self.life

    def addMoney(self, m):
        self.money = self.money + m

    def decLife(self):
        self.life -= 1
