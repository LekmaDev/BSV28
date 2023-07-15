
from Logic.battle.LogicCharacterServer import LogicCharacterServer
from Logic.battle.LogicCharacterServer2 import LogicCharacterServer2
from Logic.battle.LogicProjectileServer import LogicProjectileServer
from Logic.battle.LogicItemServer import LogicItemServer
from Utils.Helpers import Helpers
class LogicGameObjectManagerServer:
    def encode(stream, self):

        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(1, 1)

        stream.writePositiveInt(0, 5)
        stream.writePositiveInt(0, 6)
        stream.writePositiveInt(0, 5)
        stream.writePositiveInt(0, 6)

        stream.writePositiveInt(0, 1)
        stream.writePositiveVInt(0, 3)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(0, 12)#Ульта

        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        
        
        stream.writePositiveVInt(0, 3)# // rotate left

        stream.writePositiveInt(0, 1)# // rotate right
        stream.writePositiveInt(1, 1)# // 0 Убирает крч убраву
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        
        stream.writePositiveInt(0, 4)

        stream.writePositiveInt(0, 1)#1
        stream.writePositiveInt(0, 1)#1
        stream.writePositiveInt(0, 1)#2
        stream.writePositiveInt(0, 1)#2
        stream.writePositiveInt(0, 1)#3
        stream.writePositiveInt(0, 1)#3
        stream.writePositiveInt(0, 1)#4
        stream.writePositiveInt(0, 1)#4

        stream.writePositiveInt(2, 7)
        #plr start
        stream.writePositiveInt(16, 5)
        stream.writePositiveInt(self.player.brawler_id, 8)
        #bot start
        stream.writePositiveInt(16, 5)
        stream.writePositiveInt(3, 8)
        #bot end
		
		
		
        #plr end
        #bullet start
        #for i in range(self.player.bulletCount):
        #    stream.writePositiveInt(6, 5)
        #    stream.writePositiveInt(15, 8)
        #bullet end
        #bool start
        #stream.writePositiveInt(16, 5)
        #stream.writePositiveInt(47, 8)
        #bool end

        stream.writePositiveInt(0, 14)
        stream.writePositiveInt(1, 14)
        #for i in range(self.player.bulletCount):
        #    stream.writePositiveInt(i, 14)
        #stream.writePositiveInt(1, 14)
        #stream.writePositiveInt(5, 14) 
        LogicCharacterServer.encode(stream,self)
        LogicCharacterServer2.encode(stream,self)
        #LogicProjectileServer.encode(stream,self)
        #LogicItemServer.encode(stream,self)