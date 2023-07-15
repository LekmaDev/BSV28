from Server.Battle.VisionUpdate import VisionUpdate
from Utils.Reader import BSMessageReader
from Utils.BitStream import BitStream
from Utils.Battle import Battle

class ClientInputMessage(BitStream):
	def __init__(self, client, player, initial_bytes):
		super().__init__(initial_bytes)
		self.player = player
		self.client = client

	def decode(self):
		pomet = []
		self.readPositiveInt(14)
		self.readPositiveInt(10)
		self.readPositiveInt(13)
		self.readPositiveInt(10)
		count = self.readPositiveInt(5)
		for i in range(count):
			pomet.append(self.ogo())
		if pomet != []:
			print(pomet)
		
		if pomet != []:
			ponos = pomet[0]
			self.player.dudu = ponos["counter"]
			
			if ponos["id"] == 2:
				self.player.battleX = ponos["x"]
				self.player.battleY = ponos["y"]

	def process(self):
		VisionUpdate(self.client, self.player).send()
	
	def ogo(self):
		sral = {}
		sral["counter"] = self.readPositiveInt(15)
		sral["id"] = self.readPositiveInt(4)
		sral["x"] = self.readInt(15)
		sral["y"] = self.readInt(15)
		#sral["dudu"] = self.readInt(15)
		return sral