from Tower import Tower


class MagicTower(Tower):

    def __init__(self):
        Tower.__init__(self)

        self.costLv1 = 20
        self.costLv2 = 50
        self.costLv3 = 100
        self.costLv4 = 200
        self.costLv5 = 300

        self.dmg = 20

    def getCost(self):
        if self.level == 1:
            return self.costLv1
        elif self.level == 2:
            return self.costLv2
        elif self.level == 3:
            return self.costLv3
        elif self.level == 4:
            return self.costLv4
        elif self.level == 5:
            return self.costLv5

    def getLevel(self):
        return self.level

    def upgrade(self):
        self.level += 1