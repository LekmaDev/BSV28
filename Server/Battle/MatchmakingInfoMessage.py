from Utils.Writer import Writer
from Utils.Battle import Battle
from Logic.PlayerSession import PlayerSession
from Server.Battle.UDPConnectionInfo import UDPConnectionInfo
class MatchmakingInfoMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20405
        self.player = player

    def encode(self):
        for room in Battle.onlineBattle:
            if room['index'] == self.player.index:
                self.writeInt(30) # Timer (but it's don't work in v12 :( )
                self.writeInt(room['plr_count']) # Players founded
                self.writeInt(2) # Max players
                if room['plr_count'] == 2:
                    plrs = room['plrs']
                    self.player.inmm == False
                    UDPConnectionInfo(self.client, self.player).send()
                    battle = PlayerSession(self.client, self.player, plrs)
                    battle.start()