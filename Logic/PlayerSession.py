from Server.Battle.VisionUpdate import VisionUpdate
from Server.Battle.StartLoadingMessage import StartLoadingMessage
from Server.Battle.UDPConnectionInfo import UDPConnectionInfo
import time
from threading import Thread
import math
from Utils.Battle import Battle

class PlayerSession(Thread):
    def __init__(self, client, player):
        Thread.__init__(self)
        self.client = client
        self.player = player
        self.subTick = 0
        self.tick = 0
        self.started = 0
    
    def run(self):
        self.startBattle()
    
    def startBattle(self):
        self.player.inmm = False
        self.started = 1
        StartLoadingMessage(self.client, self.player).send()
        UDPConnectionInfo(self.client, self.player).send()
        while self.started:
            if True:
                self.tick += 1
                self.subTick = 0
                self.player.battleTick = self.tick
            self.process()
            time.sleep(0.045) 

    def process(self):
        VisionUpdate(self.client, self.player).send()