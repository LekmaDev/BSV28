from Utils.Writer import Writer
import random
from database.DataBase import DataBase
from Utils.Battle import Battle

class StartLoadingMessage(Writer):

	def __init__(self, client, player):
		super().__init__(client)
		self.id = 20559
		self.player = player
		
	def encode(self):
		self.writeInt(6) #6
		self.writeInt(0)
		self.writeInt(0)
		
		self.writeInt(6) #players count
		index = 0
		for i in range(6):
			self.writeInt(0) #High ID
			self.writeInt(self.player.low_id) #Low ID
			self.writeVint(i)
			if i > 2:
				index = 1
			self.writeVint(index)
			self.writeVint(0)
			
			self.writeInt(0) #unk
			
			self.writeScId(16, 0)
			self.writeVint(0)
			self.writeBoolean(False) #boolean
			self.writeString(f"{self.player.name}")
			self.writeVint(100)
			self.writeVint(28000000)
			self.writeVint(43000000)
			self.writeVint(43000000)
			self.writeBoolean(False) #boolean
		#PLAYERS SLOT END#
		
		self.writeInt(0) #count...
		
		self.writeInt(0) #Count
		
		self.writeInt(0) # Unknown
		
		self.writeVint(0)
		self.writeVint(1) #DrawMap
		self.writeVint(1)
		
		self.writeBoolean(True) #boolean
		self.writeVint(0) # is Spectating
		self.writeVint(0)
		
		self.writeScId(15, 7) # map
		self.writeBoolean(False) #boolean