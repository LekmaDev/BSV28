from Utils.Writer import Writer


class BattleLogMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23458
        self.player = player

    def encode(self):
        self.writeBoolean(True)

        self.writeVint(1) # Count

        self.writeVint(0)
        self.writeVint(1)     # Timestamp
        self.writeVint(1)       # Unknown
        self.writeVint(8)      # Trophies
        self.writeVint(100)      # Time Survived 1 = second
        self.writeUInt8(3)      # Type [0 = Power Play, 1 = Friendly, 2 = Championship
        # 3 = Friendly, 4 = Ranked]
        self.writeScId(15, 56) # Map SCID
        self.writeVint(0)       # Victory/Defeat
        self.writeVint(2)

        self.writeInt(1)
        self.writeInt(1)

        self.writeVint(2)
        self.writeUInt8(2)

        self.writeVint(2)  # array
        self.writeVint(16)
        self.writeVint(self.player.brawler_id)
        self.writeVint(29)
        self.writeVint(self.player.skin_id)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.name)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(0)
		
        self.writeVint(16)
        self.writeVint(self.player.brawler_id)
        self.writeVint(29)
        self.writeVint(self.player.skin_id)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.name)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(0)

        self.writeVint(1)
        self.writeUInt8(1)
        self.writeVint(1)
        self.writeUInt8(1)
        self.writeVint(1)