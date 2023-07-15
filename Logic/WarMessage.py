from Utils.Writer import Writer


class WarMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24776
        self.client = client
        self.player = player


    def encode(self):
        self.writeInt(0) # Player ID
        self.writeInt(self.player.low_id) # Player ID
        self.writeVint(1) # Your Club Faction
        

        # Club War Events Array
        self.writeVint(0) # Count
        # AllianceWarFaction
        self.writeVint(0) # Count