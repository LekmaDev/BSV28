import json
import random
import schedule
import time
from datetime import datetime, timedelta

# Скины
skins = {
    29: (29, 0, 1),
    52: (149, 0, 1),
    159: (149, 0, 1),

    15: (29, 0, 1),
    79: (149, 0, 1),

    2: (29, 0, 1),
    103: (29, 0, 1),

    25: (79, 0, 1),
    64: (149, 0, 1),
    102: (79, 0, 1),

    44: (149, 0, 1),
    123: (149, 0, 1),
    163: (149, 0, 1),

    58: (79, 0, 1),
    91: (149, 0, 1),

    57: (149, 0, 1),
    97: (299, 0, 1),
    160: (149, 0, 1),

    94: (299, 0, 1),
    98: (79, 0, 1),
    99: (149, 0, 1),

    109: (29, 0, 1),

    167: (29, 0, 1),

    28: (79, 0, 1),
    30: (149, 0, 1),
    128: (149, 0, 1),

    71: (149, 0, 1),

    27: (29, 0, 1),
    59: (149, 0, 1),
    92: (79, 0, 1),

    158: (79, 0, 1),

    26: (149, 0, 1),
    68: (149, 0, 1),
    130: (79, 0, 1),

    88: (79, 0, 1),
    165: (79, 0, 1),

    93: (79, 0, 1),
    104: (79, 59, 1),
    132: (79, 0, 1),

    108: (79, 0, 1),
    120: (29, 0, 1),
    147: (149, 0, 1),

    45: (79, 0, 1),
    125: (79, 0, 1),

    139: (29, 0, 1),

    111: (29, 0, 1),

    50: (149, 79, 1),
    75: (149, 0, 1),

    117: (79, 0, 1),

    137: (29, 0, 1),

    152: (29, 0, 1),

    11: (79, 0, 1),
    96: (149, 0, 1),

    110: (149, 0, 1),
    126: (79, 0, 1),
    131: (79, 0, 1),

    20: (79, 0, 1),
    49: (299, 0, 1),
    95: (299, 0, 1),
    100: (79, 0, 1),
    101: (149, 0, 1),

    118: (149, 0, 1),
}

def update_offers():
    skin1 = random.choice([29, 52, 159, 15, 79, 2, 25, 64, 102, 44, 123, 163])
    skin2 = random.choice([58, 91, 57, 97, 160, 94, 98, 99, 109, 167, 28, 30])
    skin3 = random.choice([128, 71, 27, 59, 92, 158, 26, 68, 130, 88, 165, 93])
    skin4 = random.choice([104, 132, 108, 120, 147, 45, 125, 139, 111, 50, 75, 117])
    skin5 = random.choice([137, 152, 11, 96, 110, 126, 131, 20, 49, 95, 100, 101, 118])
    boici0 = random.choice([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 37])
    boici1 = random.choice([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 37])
    boici2 = random.choice([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 37])
    boici3 = random.choice([0, 3])
    
    cost0 = random.randrange(1, 50)
    cost1 = random.randrange(1, 50)
    cost2 = random.randrange(1, 50)
    cost3 = random.randrange(1, 50)
    
    mult0 = random.randrange(10, 100)
    mult1 = random.randrange(10, 100)
    mult2 = random.randrange(10, 100)
    mult3 = random.randrange(10, 100)

    with open('offers.json', 'r') as f:
        data = json.load(f)

    data['0']['WhoBuyed'] = []
    data['1']['WhoBuyed'] = []
    data['2']['WhoBuyed'] = []
    data['3']['WhoBuyed'] = []
    data['4']['WhoBuyed'] = []
    data['5']['WhoBuyed'] = []
    data['6']['WhoBuyed'] = []
    data['7']['WhoBuyed'] = []
    data['8']['WhoBuyed'] = []

    # Скины
    data['4']['SkinID'] = [skin1, 0, 0, 0]
    data['5']['SkinID'] = [skin2, 0, 0, 0]
    data['6']['SkinID'] = [skin3, 0, 0, 0]
    data['7']['SkinID'] = [skin4, 0, 0, 0]
    data['8']['SkinID'] = [skin5, 0, 0, 0]

    data['4']['Cost'] = skins[skin1][0]
    data['4']['OldCost'] = skins[skin1][1]
    data['4']['Multiplier'] = [skins[skin1][2], 0, 0, 0]

    data['5']['Cost'] = skins[skin2][0]
    data['5']['OldCost'] = skins[skin2][1]
    data['5']['Multiplier'] = [skins[skin1][2], 0, 0, 0]

    data['6']['Cost'] = skins[skin3][0]
    data['6']['OldCost'] = skins[skin3][1]
    data['6']['Multiplier'] = [skins[skin3][2], 0, 0, 0]

    data['7']['Cost'] = skins[skin4][0]
    data['7']['OldCost'] = skins[skin4][1]
    data['7']['Multiplier'] = [skins[skin4][2], 0, 0, 0]

    data['8']['Cost'] = skins[skin5][0]
    data['8']['OldCost'] = skins[skin5][1]
    data['8']['Multiplier'] = [skins[skin5][2], 0, 0, 0]
	
    #Акции дня
    data['0']['Cost'] = cost0
    data['0']['Multiplier'] = [mult0, 0, 0, 0]
    data['0']['BrawlerID'] = [boici0, 0, 0, 0]

    data['1']['Cost'] = cost1
    data['1']['Multiplier'] = [mult1, 0, 0, 0]
    data['1']['BrawlerID'] = [boici1, 0, 0, 0]

    data['2']['Cost'] = cost2
    data['2']['Multiplier'] = [mult2, 0, 0, 0]
    data['2']['BrawlerID'] = [boici2, 0, 0, 0]

    data['3']['Cost'] = cost3
    data['3']['Multiplier'] = [mult3, 0, 0, 0]
    data['3']['BrawlerID'] = [boici3, 0, 0, 0]

    with open('offers.json', 'w') as f:
        json.dump(data, f)

    # Магаз обновлён в консоси
    now = datetime.now()
    print(f"Магазин обновлен: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Херня котоаря обновляет шопку
schedule.every().day.at("19:27").do(update_offers)

# Инфинити цикл, чтобы не завершался.
while True:
    schedule.run_pending()
    time.sleep(1)
