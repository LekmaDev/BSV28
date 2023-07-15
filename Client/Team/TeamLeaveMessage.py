from database.DataBase import DataBase
from Logic.Player import Players
from Server.Team.TeamLeaveOkMessage import TeamLeaveOkMessage
from Utils.Helpers import Helpers
from Utils.Reader import BSMessageReader


class TeamLeaveMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        TeamLeaveOkMessage(self.client, self.player).send()
        for player in Helpers.rooms[self.player.room_id-1]['plrs']:
            if player['id'] == self.player.low_id:
                Helpers.rooms[self.player.room_id-1]['plrs'].remove(player)
                self.player.room_id = 0
                DataBase.replaceValue(self, 'roomID', self.player.room_id)