import json, random
class Everyday:
    """
    << Shop Offers IDs List >>

    0 = Free Brawl Box
    1 = Gold
    2 = Random Brawler
    3 = Brawler
    4 = Skin
    5 = StarPower/ Gadget
    6 = Brawl Box
    7 = Tickets (not working anymore)
    8 = Power Points (for a specific brawler)
    9 = Token Doubler
    10 = Mega Box
    11 = Keys (???)
    12 = Power Points
    13 = EventSlot (???)
    14 = Big Box
    15 = AdBox (not working anymore)
    16 = Gems
    19 = Pin for Brawler
    20 = Pin Collection
    21 = Pin Pack
    22 = Pins Pack For Brawler
    23 = Pin Common (???)
    24 = Shop Skin Offer (May Not Work)
    94 = Skin???
    

    << Shop Offers BGR List >>

    Token Offer = offer_generic
    Special Offer = offer_special
    Starpoint Offer = offer_legendary
    Coin Offer = offer_coins(in v29 like offer_moon_festival)
    Gem Offer = offer_gems
    Box Offer = offer_boxes
    Brawler Offer = offer_finals
    LNY Offer = offer_lny
    Archive Offer = offer_archive
    Chromatic = offer_chromatic
    Moon Festival = offer_moon_festival
    Xmas = offer_xmas
    


    ET is Extra Text

    """



    def loadOffers(self):
        self.offers=[]
        with open("Logic/offers.json", "r",encoding='utf-8') as f:
            data = json.load(f)
            for i in data.values():
                self.offers.append(i)
    def UpdateOfferData(self, i):
        with open("Logic/offers.json", "r") as f:
            data = json.load(f)
        data[str(i)]["Buyed"].append(int(self.player.low_id))
        with open("Logic/offers.json", "w") as f:
            json.dump(data, f, ensure_ascii=False)
    def RemoveOffer(self, i):
        with open("Logic/offers.json", "r") as f:
            data = json.load(f)
        data.pop(str(i))
        with open("Logic/offers.json", "w") as f:
            json.dump(data, f, ensure_ascii=False)



    def EncodeShopOffers(self):
        for i in range(0):
            self.writeVint(1)
            self.writeVint(8) # ItemID
            self.writeVint(random.randint(1,320)) # Ammount
            self.writeScId(16, random.randint(0,34))
            self.writeVint(0) # ItemID
            self.writeVint(1)  # [0 = Offer, 2 = Skins 3 = Star Shop]

            self.writeVint(random.randint(1,100))  # Cost
            self.writeVint(172800)

            self.writeVint(2)# Offer View | 0 = Absolutely "NEW", 1 = "NEW", 2 = Viewed
            self.writeVint(100)
            self.writeBoolean(False)
        
            self.writeBoolean(False)
            self.writeVint(1)# [0 = Normal, 1 = Daily Deals]
            self.writeBoolean(False)
            self.writeVint(0)

            self.writeInt(0)

            self.writeString()

            self.writeBoolean(False)
            self.writeString()
            self.writeVint(0)
            self.writeBoolean(False)
		#shopend