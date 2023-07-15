from Server.Club.AllianceChatServer import AllianceChatServer
from Server.Club.AllianceBotChatServerMessage import AllianceBotChatServerMessage
from database.DataBase import DataBase
from Utils.Reader import BSMessageReader
from Server.Login.LoginFailedMessage import LoginFailedMessage


class AllianceStreamMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.bot_msg = ''
        self.send_ofs = False
        self.IsAcmd = False

    def decode(self):
        self.msg = self.read_string()
        if self.msg.lower() == '/theme':
            if self.player.vip == 1:
                self.bot_msg = f'Выбери ID фона в меню!\n0 - Обычный\n1 - Новый год (Просто снег)\n 2 - Лунный новый год (2019)\n5 - Золотая неделя\n6 - Ретрополис\n7 - Меха (Лето 2019)\n8 - Хеллоуин\n9 - Пираты\n10 - Лунный новый год (2020)\n11 - ПСЖ\n12 - SC10\n13 - Базар Тары\n14 - СуперСити (Custom)\nИспользовать команду /theme ID'
                self.IsAcmd = True
            else:
                self.bot_msg = f'У тебя нет привилегии VIP\nПиши в тг @lekma что бы купить'
                self.IsAcmd = True
        if self.msg.lower() == '/id':
            self.bot_msg = f'Твой айди {self.player.low_id}'
            self.IsAcmd = True
        if self.msg.lower().startswith('/theme'):
            if self.player.vip == 1:
                try:
                    newStarpoints = self.msg.split(" ", 6)[1:]
                    DataBase.replaceValue(self, 'theme', int(newStarpoints[0]))
                    self.bot_msg = f'перезайти в игру фон был успешно изменен'
                    self.IsAcmd = True
                except:
                    pass
            else:
                self.bot_msg = f'У тебя нет привилегии VIP\nПиши в тг @lekma что бы купить'
                self.IsAcmd = True

    def process(self):
        if self.send_ofs == False and self.IsAcmd == False:
            DataBase.Addmsg(self, self.player.club_low_id, 2, 0, self.player.low_id, self.player.name, self.player.club_role, self.msg)
            DataBase.loadClub(self, self.player.club_low_id)
            for i in self.plrids:
                AllianceChatServer(self.client, self.player, self.msg, self.player.club_low_id).send()
        if self.bot_msg != '':
            AllianceChatServer(self.client, self.player, self.msg, self.player.club_low_id, True).send()
            AllianceBotChatServerMessage(self.client, self.player, self.bot_msg).send()