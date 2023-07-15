from Utils.Helpers import Helpers
class LogicProjectileServer:
    def encode(stream,self):
        for i in range(self.player.bulletCount):

            stream.writePositiveVInt(int(self.player.bulletX), 4)
            stream.writePositiveVInt(int(self.player.bulletY), 4)
            stream.writePositiveVInt(0, 3)
            stream.writePositiveVInt(450, 4)
            stream.writePositiveInt(0, 3)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(284, 10)
            stream.writePositiveInt(self.player.angle, 9)
            stream.writePositiveInt(0, 1)
        