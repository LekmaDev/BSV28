from Utils.Reader import BSMessageReader
from Server.Team.TeamStream2 import TeamStream2
from database.DataBase import DataBase
from Utils.Helpers import Helpers

class TeamChat(BSMessageReader):
	#14369
	def __init__(self, client, player, initial_bytes):
		super().__init__(initial_bytes)
		self.client = client
		self.player = player
		
	def decode(self):
		self.message = self.read_string()
		 
	def process(self):
		self.player.ctick += 1
		for room in Helpers.rooms:
			if room['roomID'] == self.player.room_id:
				Helpers.rooms[self.player.room_id-1]['Tick'] += 1
				new_msg = {'id': self.player.low_id, 'Message': self.message}
				room['msg'].append(new_msg)
				TeamStream2(self.client, self.player).send()  
				break