import time
import random
#random.choice([24,25,26,51,118,143,160,161,238,252,253,254,255,256])
class EventSlots:
    Timer = 86399

    maps = [
        # Status = [3 = Nothing, 2 = Star Token, 1 = New Event]
        {
            'ID': random.choice([7,8,9,10,11,12,40,113,114,115,116,117,122,212]),
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },

        {
            'ID': random.choice([16,198,220,228,232,243,270,272,274,276,278,280,282,284,286]),
            'Status': 2,
            'Ended': False,
            'Modifier': 2,
            'Tokens': 10
        },

        {
            'ID': random.choice([53,137,146,216,217,267,268]),
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },



        {
            'ID': random.choice([4,54,82,218,219,265,266]),
            'Status': 2,
            'Ended': False,
            'Modifier': 2,
            'Tokens': 10
        },


        {
            'ID': random.choice([24,25,26,51,118,143,160,161,238,252,253,254,255,256]),
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        }

    ]