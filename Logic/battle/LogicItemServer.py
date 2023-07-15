from Utils.Helpers import Helpers
import math
class LogicItemServer:
    def encode(stream,self):
        stream.writePositiveVInt(int(self.player.hasbollX), 4)
        stream.writePositiveVInt(int(self.player.hasbollY), 4)
        stream.writePositiveVInt(102, 3)
        stream.writePositiveVInt(0, 4)
        stream.writePositiveInt(10, 4)
        stream.writePositiveInt(0, 3)#0
        stream.writePositiveInt(1, 1)#1
        stream.writePositiveInt(1, 1)#1
        stream.writePositiveInt(0, 1)#0
        stream.writePositiveInt(0, 1)#0
        stream.writePositiveInt(0, 2)#0
        stream.writePositiveInt(1, 13)
        stream.writePositiveInt(1, 13)
        stream.writePositiveInt(0, 2)#2 летит с ульты;1просто кинул
        stream.writePositiveInt(0, 2)#0
        stream.writePositiveInt(0, 2)#0
        stream.writePositiveInt(0, 1)#1 инвиз
        stream.writePositiveInt(0, 9)
        stream.writePositiveInt(0, 5)