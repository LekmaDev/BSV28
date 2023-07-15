from Utils.Helpers import Helpers
class LogicCharacterServer2:
    def encode(stream, self):
        for i in range(1):
            stream.writePositiveVInt(int(Helpers.game1[2]['battleX']), 4)
            stream.writePositiveVInt(int(Helpers.game1[2]['battleY']), 4)
            stream.writePositiveVInt(5, 3)
            stream.writePositiveVInt(0, 4)
            stream.writePositiveInt(10, 4)
            stream.writePositiveInt(Helpers.game1[2]['angle'] * 180, 9)#isownobj
            stream.writePositiveInt(90, 9)#isownobj
            stream.writePositiveInt(3, 3)
            stream.writePositiveInt(0, 1)
            stream.writeInt(63, 6)
            stream.writePositiveInt(0, 1)#дёргает и не rotate
            stream.writePositiveInt(0, 1)#stan
            stream.writePositiveInt(0, 1)#unk
            stream.writePositiveInt(0, 1)#star power indicator
            stream.writePositiveInt(1, 1)#1
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 2)
            stream.writePositiveInt(Helpers.game1[2]['hp'], 13)
            stream.writePositiveInt(3000, 13)
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)

            stream.writePositiveInt(1, 1)

            stream.writeBoolean(False)#big brawler
            stream.writeBoolean(True)
            stream.writeBoolean(False)
            stream.writeBoolean(Helpers.game1[2]['immun'])#immunity
            stream.writeBoolean(False)#когда ходишь дёргает и ещё не rotate
            stream.writeBoolean(False)#BUll agre
            stream.writeBoolean(False)#unknown?
            stream.writeBoolean(False)#Press ulti
            stream.writeBoolean(False)#unknown?

            stream.writeBoolean(False)
            stream.writePositiveInt(0, 2)
            stream.writePositiveInt(0, 1)

            stream.writePositiveInt(5, 9)
            stream.writePositiveInt(0, 5)

            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(1, 1) 
            stream.writePositiveInt(3000, 12)
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(1, 1)