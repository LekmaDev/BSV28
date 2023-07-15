from database.DataBase import DataBase
from Utils.Reader import BSMessageReader
from Server.Login.LoginFailedMessage import LoginFailedMessage

class LogicSetPlayerNameColorCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.name_color = self.read_Vint()


    def process(self):
        vip = [1,2,3,4,5,6,7,8,9,10,11]
        DataBase.replaceValue(self, 'name_color', self.name_color)