from Utils.Writer import Writer
from Utils.BitStream import BitStream
from Logic.battle.LogicGameObjectManagerServer import LogicGameObjectManagerServer
from Server.Battle.BattleResult2Message import BattleResult2Message
from Logic.battle.LogicCharacterServer import LogicCharacterServer
from Utils.Battle import Battle

class VisionUpdate(Writer):

	def __init__(self, client, player):
		super().__init__(client)
		self.id = 24109
		self.player = player


	def encode(self):
		self.writeVint(self.player.battleTick) # Battle Ticks
		self.writeVint(self.player.dudu) # wifi posral jidko
		self.writeVint(0) # Commands Count
		self.writeVint(0) # spectators
		self.writeBoolean(False) # Live Boolean
		stream = BitStream()
		stream.writePositiveInt(1000000 + 0, 21)
		stream.writePositiveVInt(0, 4) 
		stream.writePositiveInt(0, 1)
		stream.writeInt(-1, 4) 
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 5)
		stream.writePositiveInt(0, 6)
		stream.writePositiveInt(0, 5)
		stream.writePositiveInt(0, 6)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(1, 1)
		
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 12) # 2000
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)
		for i in range(6):
			stream.writePositiveInt(0, 1)
			stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 4)

		stream.writePositiveInt(1, 8)
		#plr start
		stream.writePositiveInt(16, 5)
		stream.writePositiveInt(0, 7)
		#bot start
		stream.writePositiveInt(0, 14)

		
		stream.writePositiveVInt(self.player.battleX, 4) 
		stream.writePositiveVInt(self.player.battleY, 4) 
		stream.writePositiveVInt(0, 3) 
		stream.writePositiveVInt(0, 4)
		stream.writePositiveInt(10, 4)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 3) 
		stream.writePositiveInt(0, 1) 
		stream.writeInt(63, 6)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(1, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 2)
		stream.writePositiveInt(3600, 13) 
		stream.writePositiveInt(3600, 13) 
		stream.writePVIntMax255OZ(0) 
		stream.writePositiveInt(1, 1) 
		stream.writePositiveInt(0, 1)
		stream.writeBoolean(True)
		stream.writeBoolean(False)
		stream.writeBoolean(False) # shield
		stream.writePositiveInt(0, 1) # stun?
		stream.writePositiveInt(0, 1) # red
		stream.writePositiveInt(0, 1) # ??
		stream.writePositiveInt(0, 1) # aiming ulti
		stream.writePositiveInt(0, 1) # yellow shield
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 4)
		stream.writePositiveInt(0, 2)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 9)
		stream.writePositiveInt(0, 1)
		stream.writePositiveInt(0, 1)		
		stream.writePositiveInt(0, 5)		
		stream.writePVIntMax255OZ(0)
		stream.writePositiveInt(0, 1)
		stream.writePVIntMax255OZ(0)
		stream.writePositiveInt(3000, 12)
		stream.writePVIntMax255OZ(0)
		stream.writePositiveInt(0, 1)
		stream.writePVIntMax255OZ(0)

		stream.writePositiveInt(0, 8)
		self.writeBytes(stream.getBuff())