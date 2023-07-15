from Utils.Reader import BSMessageReader


class ClientInfoMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.inet = self.read_string()

    def process(self):
        pass