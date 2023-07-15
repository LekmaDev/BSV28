from database.DataBase import DataBase
from Logic.Commands.Server.LogicTropRoad import LogicTropRoad
from Logic.Commands.Server.LogicBrawlerDataCommand import LogicBrawlerDataCommand
from Logic.Commands.Client.LogicBoxDataCommand import LogicBoxDataCommand
from Utils.Reader import BSMessageReader

class LogicClaimRankUpRewardCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.a = self.read_Vint()
        self.b = self.read_Vint()
        self.g = self.read_Vint()
        self.j = self.read_Vint()
        self.bp = self.read_Vint()
        self.p = self.read_Vint()
        self.k = self.read_Vint()
    def process(self):
        DataBase.loadAccount(self)
        if self.player.Troproad in [1,3,4,5,11,14,20,27,37,40,42,49,52,62]:#MICRO BOX
            LogicBoxDataCommand(self.client, self.player, 6).send()
        if self.player.Troproad in [18,31,33,58,67,73,76,78,84]:#BIG BOX
            LogicBoxDataCommand(self.client, self.player, 7).send()
        if self.player.Troproad in [60,70,80,85,87,89,91,93]:#MEEGA BOX
            LogicBoxDataCommand(self.client, self.player, 8).send()
        elif self.player.Troproad in [7,51]: #JETONS FOR UP
            LogicTropRoad(self.client, self.player, 100, 250).send()
        elif self.player.Troproad in [4,8,12,21,24]: #SHLAK
            LogicTropRoad(self.client, self.player, 100, 500).send()

        elif self.player.Troproad in [9,13,17,22,28,30,34,38,43,47,53,56,59,61,64,68,72,77,82,88,92]: #JETONS FOR UP BRAWLER
            if self.player.Troproad in [9,13,17,22,43,47,53,59,61,64,72]:
                LogicTropRoad(self.client, self.player, 100, 25, 6, self.k).send()
            elif self.player.Troproad in [30,34,82]:
                LogicTropRoad(self.client, self.player, 100, 50, 6, self.k).send()
            elif self.player.Troproad in [28]:
                LogicTropRoad(self.client, self.player, 100, 75, 6, self.k).send()
            elif self.player.Troproad in [38,56,68,77]:
                LogicTropRoad(self.client, self.player, 100, 150, 6, self.k).send()
            elif self.player.Troproad in [88,92]:
                LogicTropRoad(self.client, self.player, 100, 200, 6, self.k).send()

        elif self.player.Troproad in [16,19,23,26,29,32,36,39,41,44,46,48,50,54,57,63,66,69,71,74,79,81,83,86,90,94]: #GOLD
            if self.player.Troproad in [16,19,23,26,36,39,44,46,50,54,71,74]:
                LogicTropRoad(self.client, self.player, 100, 50).send()
            elif self.player.Troproad in [29,32]:
                LogicTropRoad(self.client, self.player, 100, 100).send()
            elif self.player.Troproad in [41,63,81,83]:
                LogicTropRoad(self.client, self.player, 100, 150).send()
            elif self.player.Troproad in [57,66,69,79]:
                LogicTropRoad(self.client, self.player, 100, 200).send()
            elif self.player.Troproad in [48]:
                LogicTropRoad(self.client, self.player, 100, 300).send()
            elif self.player.Troproad in [86,90]:
                LogicTropRoad(self.client, self.player, 100, 500).send()
            elif self.player.Troproad in [94]:
                LogicTropRoad(self.client, self.player, 100, 1000).send()


        elif self.player.Troproad in [2, 6, 10, 15, 25, 35, 45, 55, 65, 75]:#BRAWLER
            if self.player.Troproad == 2:
                LogicBrawlerDataCommand(self.client, self.player, 8).send()

            elif self.player.Troproad == 6:
                LogicBrawlerDataCommand(self.client, self.player, 1).send()

            elif self.player.Troproad == 10:
                LogicBrawlerDataCommand(self.client, self.player, 2).send()

            elif self.player.Troproad == 15:
                LogicBrawlerDataCommand(self.client, self.player, 7).send()

            elif self.player.Troproad == 25:
                LogicBrawlerDataCommand(self.client, self.player, 3).send()

            elif self.player.Troproad == 35:
                LogicBrawlerDataCommand(self.client, self.player, 9).send()

            elif self.player.Troproad == 45:
                LogicBrawlerDataCommand(self.client, self.player, 14).send()

            elif self.player.Troproad == 55:
                LogicBrawlerDataCommand(self.client, self.player, 22).send()

            elif self.player.Troproad == 65:
                LogicBrawlerDataCommand(self.client, self.player, 27).send()

            elif self.player.Troproad == 75:
                LogicBrawlerDataCommand(self.client, self.player, 30).send()
        self.player.Troproad = self.player.Troproad + 1
        DataBase.replaceValue(self, "Troproad", self.player.Troproad)