from database.DataBase import DataBase
from Utils.Writer import Writer


class LogicTropRoad(Writer):

    def __init__(self, client, player, boxid=10, ammo=0, who=0, brawler=0):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.boxid = boxid
        self.ammo = ammo
        self.who = who
        self.brawler = brawler

    def encode(self):
        # Box info
        self.writeVint(203) # CommandID
        self.writeVint(0)   # Unknown
        self.writeVint(1)   # Unknown
        self.writeVint(self.boxid)  # BoxID 
        if self.boxid == 100:
            if self.who == 6:
                self.writeVint(1) # Reward count
                self.writeVint(self.ammo) # Reward count
                self.writeScId(16, int(self.brawler))  # CsvID
                self.writeVint(6) # RewardID
                self.writeHexa('''00 00 00''')  # Reward end
                self.player.brawlerPoints[str(self.brawler)] += self.ammo
                DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
            else:
                self.writeVint(1) # Reward count
                self.writeVint(self.ammo) # Reward count
                self.writeScId(0, 7) # RewardID
                self.writeHexa('''00 00 00''')  # Reward end
                self.player.gold = self.player.gold + self.ammo
                DataBase.replaceValue(self, "gold", self.player.gold)
        else:
            self.writeVint(1) # Reward count
            self.writeVint(1) # Reward count
            self.writeScId(0, 7) # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
        # Box end
        self.writeVint(self.player.Troproad)