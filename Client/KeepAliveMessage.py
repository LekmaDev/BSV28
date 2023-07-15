from Server.Friend.FriendListMessage import FriendListMessage
from Server.KeepAliveOkMessage import KeepAliveOkMessage
from Utils.Reader import BSMessageReader
from Server.Team.TeamMessage import TeamMessage
from Server.Team.TeamStream2 import TeamStream2
from Server.Team.TeamStream import TeamStream
from Server.Club.AllianceDataMessage import AllianceDataMessage
from Server.Home.LobbyInfoMessage import LobbyInfoMessage
from Utils.Helpers import Helpers
class KeepAliveMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        LobbyInfoMessage(self.client, self.player).send()
        if self.player.online not in [8,5]:
            KeepAliveOkMessage(self.client, self.player).send()
            FriendListMessage(self.client, self.player).send()