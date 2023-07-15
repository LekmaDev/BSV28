from Server.Team.TeamMessage import TeamMessage
from database.DataBase import DataBase
from Server.Battle.MatchmakingInfoMessage import MatchmakingInfoMessage
from Server.Battle.MatchmakeCancelledMessage import MatchmakeCancelledMessage
from Utils.Reader import BSMessageReader
from Utils.Battle import Battle
from Utils.Gameroom import Gameroom
from Utils.Helpers import Helpers
class OnPlay(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
    def decode(self):
        pass

    def process(self):
        self.player.room_id = 1+len(Helpers.rooms)
        self.roomType = 1
        self.map_id = 7
        self.mapSlot = 1
        Gameroom.create(self, self.roomType, self.map_id, self.mapSlot)
        DataBase.replaceValue(self, 'roomID', self.player.room_id)
        MatchmakeCancelledMessage(self.client, self.player).send()
        TeamMessage(self.client, self.player, 1).send()