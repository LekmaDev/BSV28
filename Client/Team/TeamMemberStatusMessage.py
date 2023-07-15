from database.DataBase import DataBase
from Server.Team.TeamMessage import TeamMessage
from Utils.Reader import BSMessageReader
from Utils.Helpers import Helpers
import json
class TeamMemberStatusMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.state = self.read_Vint()
        self.player.pin = self.read_Vint()
        self.player.mode = self.read_Vint()

    def process(self):
        for plr in Helpers.rooms[self.player.room_id-1]['plrs']:
            if plr['id'] == self.player.low_id:
                if self.player.state == 8: #5
                    plr['state'] = 5
                else:
                    plr['state'] = self.player.state
                TeamMessage(self.client, self.player)
                break