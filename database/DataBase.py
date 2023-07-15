from Logic.Player import Players
import os, json,datetime
from tinydb import TinyDB, Query, database
import sqlite3 as sql

class DataBase:
    def loadAccount(self):
        self.conn = sql.connect("database/Player/plr.db")
        self.cur = self.conn.cursor()
        try:
            self.cur.execute("SELECT * FROM plrs WHERE token=?", (self.player.token,))
            fetch = self.cur.fetchall()
            user_data = fetch[0]
        except (sql.OperationalError, IndexError):
            user_data=None
            
        if user_data:
            self.player.low_id = user_data[1]
            self.player.name = user_data[2]
            self.player.trophies = user_data[3]
            self.player.gold = user_data[4]
            self.player.gems = user_data[5]
            self.player.starpoints = user_data[6]
            self.player.tickets = user_data[7]
            self.player.Troproad = user_data[8]
            self.player.profile_icon = user_data[9]
            self.player.name_color = user_data[10]
            self.player.club_low_id = user_data[11]
            self.player.club_role = user_data[12]
            self.player.brawler_id = user_data[14]
            self.player.skin_id = user_data[15]
            self.player.room_id = user_data[16]
            self.player.box = user_data[17]
            self.player.bigbox = user_data[18]
            self.player.online = user_data[19]
            self.player.vip = user_data[20]
            self.player.player_experience = user_data[21]
            self.player.ccc = user_data[23]
            self.player.trioWINS = user_data[24]
            self.player.sdWINS = user_data[25]
            self.player.theme = user_data[26]
            self.player.quests = user_data[27]
            self.player.ban = user_data[28]
            friends = json.loads(user_data[22])
            brawlerData = json.loads(user_data[13])
            self.player.highest_trophies = brawlerData["highest_trophies"]
            self.player.brawlers_trophies = brawlerData["brawlersTrophies"]
            self.player.UnlockedBrawlers = brawlerData["UnlockedBrawlers"]
            self.player.UnlockedSkins = brawlerData["UnlockedSkins"]
            self.player.brawlerPowerLevel = brawlerData["brawlerPowerLevel"]
            self.player.brawlerPoints = brawlerData["brawlerPoints"]
            player_total_trophies = 0
            for x in self.player.brawlers_trophies:
                player_total_trophies += self.player.brawlers_trophies[x]
            self.player.trophies = player_total_trophies
            DataBase.replaceValue(self, 'trophies', self.player.trophies)
            player_rank_trophies = 0
            for x in self.player.brawlers_trophies:
                player_rank_trophies += self.player.brawlers_trophies[x]
            self.player.highset_trophies = player_rank_trophies
            DataBase.replaceValue(self, 'highest_trophies', self.player.highset_trophies)
            self.conn.close()

    def createAccount(self):
        self.conn = sql.connect("database/Player/plr.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS plrs (token TEXT, lowID INT, name TEXT, trophies INT, gold INT, gems INT, starpoints INT, tickets INT, Troproad INT, profile_icon INT, name_color INT,clubID INT, clubRole INT, brawlerData JSON, brawlerID INT, skinID INT, roomID INT, box INT, bigbox INT, online INT, vip INT, playerExp INT, friends JSON, SCC TEXT,trioWINS INT,sdWINS INT, theme INT, quests JSON,ban INT)")
        self.conn.commit()
        var = self.player.token, self.player.low_id, self.player.name, self.player.trophies, self.player.gold, self.player.gems, self.player.starpoints, self.player.tickets, self.player.Troproad, self.player.profile_icon, self.player.name_color,self.player.club_low_id,self.player.club_role, json.dumps({"highest_trophies": self.player.highest_trophies,"brawlersTrophies": self.player.brawlers_trophies,"UnlockedBrawlers": self.player.UnlockedBrawlers,"UnlockedSkins": self.player.UnlockedSkins,"brawlerPowerLevel":self.player.brawlerPowerLevel, "brawlerPoints":self.player.brawlerPoints}), self.player.brawler_id, self.player.skin_id, self.player.room_id, self.player.box, self.player.bigbox, self.player.online, self.player.vip, self.player.player_experience, json.dumps([]), self.player.ccc,self.player.trioWINS,self.player.sdWINS, self.player.theme, json.dumps([]),self.player.ban
        self.cur.execute("INSERT INTO plrs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", var)
        self.conn.commit()
        self.conn.close()
    def getLeaders(self):
        self.conn = sql.connect("database/Player/plr.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT lowID,name,trophies,profile_icon,name_color,clubID,vip FROM plrs ORDER BY trophies DESC LIMIT 150")
        return self.cur.fetchall()
        self.conn.close()
    def getAll(self):
        self.conn = sql.connect("database/Player/plr.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM plrs")
        return self.cur.fetchall()
        self.conn.close()
    def GetLeaderboardByBrawler(self, ID):
        self.conn = sql.connect("database/Player/plr.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT lowID,name,brawlerData,profile_icon,name_color,vip FROM plrs LIMIT 200")
        return self.cur.fetchall()
        
    def setImmedatedValue(self, db, table, var, val, sqlsin):
        self.conn = sql.connect(f"database/{db}.db")
        self.cur = self.conn.cursor()
        self.cur.execute(f"UPDATE {table} SET {var}=? {sqlsin}", (val,))
        self.conn.commit()
        self.conn.close()
    def getSpecifiedValue(self, value_name):
        db = TinyDB(f'database/Player/{self.player.token}.db')
        query = Query()
        name_list =[]

        self.requested_val = db.search(query.token == str(self.player.token))[0]['info'][value_name]
    def loadbyID(self, ID):
        self.conn = sql.connect("database/Player/plr.db")
        self.cur = self.conn.cursor()
        self.cur.execute(f"SELECT * FROM plrs WHERE lowID=?", (ID,))
        return self.cur.fetchone()
        self.conn.close()
    def set2All(self, var, val):
        self.conn = sql.connect("database/Player/plr.db")
        self.cur = self.conn.cursor()
        self.cur.execute(f"UPDATE plrs SET theme={val}")
        self.conn.commit()
        self.conn.close()
    def callbackSQLQ(self, sqlcallback):
        self.conn = sql.connect("database/Player/plr.db")
        self.cur = self.conn.cursor()
        self.cur.execute(sqlcallback)
        self.conn.commit()
    #Replace Value
    def replaceValue(self, value_name, new_value):
        self.conn = sql.connect("database/Player/plr.db")
        self.cur = self.conn.cursor()
        if value_name=="3vs3Wins":
            value_name="TvsTWins"
        if value_name=="tranim":
            pass
        if value_name in ["UnlockedSkins", "UnlockedPins", "StarPowerUnlocked", "brawlersTrophies","brawlersTrophiesForRank","brawlersSkins", "brawlerPoints", "UnlockedBrawlers", "brawlerPowerLevel", "chwins", "highest_trophies"]:
            self.cur.execute("SELECT brawlerData FROM plrs WHERE token=?", (self.player.token,))
            zalupka = self.cur.fetchall()
            data = json.loads(zalupka[0][0])
            data[value_name]=new_value
            self.cur.execute(f"UPDATE plrs SET brawlerData=? WHERE token=?", (json.dumps(data),self.player.token))
        elif value_name == "Skins":
            self.cur.execute("SELECT skinsData FROM plrs WHERE token=?", (self.player.token,))
            zalupka = self.cur.fetchall()
            #print(zalupka)
            data = json.loads(zalupka[0][0])
            data[value_name]=new_value
            self.cur.execute(f"UPDATE plrs SET skinsData=? WHERE token=?", (json.dumps(data),self.player.token))
        else:
            if value_name != "tranim":
                self.cur.execute(f"UPDATE plrs SET '{value_name}'=? WHERE token=?", (new_value, self.player.token))
        self.conn.commit()
        self.conn.close()
    def loadByToken(self, token):
        db = TinyDB(f"database/Player/{token}.db")
        data = db.search(Query().token == token)
        return data[0]
        
    def replaceOtherValue(self, ID, value_name, new_value):
        self.conn = sql.connect("database/Player/plr.db")
        self.cur = self.conn.cursor()
        if value_name in ["UnlockedSkins", "UnlockedPins" "brawlersTrophies","brawlersTrophiesForRank","brawlersSkins"]:
            self.cur.execute("SELECT brawlerData FROM plrs WHERE lowID=?", (ID,))
            zalupka = self.cur.fetchall()
            data = json.loads(zalupka[0][0])
            data[value_name]=new_value
            self.cur.execute(f"UPDATE plrs SET brawlerData=? WHERE lowID=?", (json.dumps(data),ID))
        elif value_name == "Skins":
            self.cur.execute("SELECT skinsData FROM plrs WHERE lowID=?", (ID,))
            zalupka = self.cur.fetchall()
            #print(zalupka)
            data = json.loads(zalupka[0][0])
            data[value_name]=new_value
            self.cur.execute(f"UPDATE plrs SET brawlerData=? WHERE lowID=?", (json.dumps(data),ID))
        else:
            self.cur.execute(f"UPDATE plrs SET '{value_name}'=? WHERE lowID=?", (new_value, ID))
        self.conn.commit()
        self.conn.close()
    def UpdateValue(self, var, new):
        self.conn = sql.connect("database/Player/plr.db")
        self.cur = self.conn.cursor()
        self.cur.execute(f"SELECT {var} FROM plrs WHERE token=?", (self.player.token,))
        self.cur.execute(f"UPDATE plrs SET {var}=? WHERE token=?", (self.cur.fetchone()[0]+new, self.player.token))
        self.conn.commit()
    # Gameroom
    def createGameroomDB(self):
        self.conn = sql.connect("database/Gameroom/gr.db")
        self.con = sql.connect("database/Gameroom/chats.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS gr (roomID INT, mapID INT, gadget INT, players JSON, type INT)")
        plrs = {"0": {"host": 1, "lowID": self.player.low_id, "name": self.player.name, "Team": self.player.team, "ctick": self.player.ctick, "message": self.player.message, "Ready": self.player.isReady, "brawlerID": self.player.brawler_id, "skinID": self.player.skin_id, "starpower": self.player.starpower, "gadget": self.player.gadget, "profileIcon": self.player.profile_icon, "namecolor": self.player.name_color, "status": 0}}
        self.cur.execute("INSERT INTO gr VALUES (?,?,?,?,?)", (self.player.room_id, self.player.map_id, 1, json.dumps(plrs), self.player.roomType))
        self.conn.commit()

        self.c = self.con.cursor()
        self.c.execute(f"CREATE TABLE IF NOT EXISTS chats (roomID INT, Event INT, Tick INT, plrid INT, plrname TEXT, plrrole INT, Msg TEXT)")
        sss = "INSERT INTO chats VALUES (?, ?, ?,?,?,?,?)"
        var = self.player.room_id, 2, 1, 0, "Cosmo Bot", 2, "Удачной игры!"
        self.c.execute(sss, var)
        self.con.commit()
    def AddroomMSG(self, clubID, event, tick, Low_id, name, message):
        self.con = sql.connect("database/Gameroom/chats.db")
        self.c = self.con.cursor()
        self.c.execute(f"CREATE TABLE IF NOT EXISTS chats (roomID INT, Event INT, Tick INT, plrid INT, plrname TEXT, plrrole INT, Msg TEXT)")
        clubid = self.player.room_id
        self.conn = sql.connect("database/Gameroom/gr.db")
        self.con = sql.connect("database/Gameroom/chats.db")
        self.cur= self.conn.cursor()
        self.chat = self.con.cursor()
        self.chat.execute(f"SELECT * FROM chats WHERE roomID={clubID}")
        fetch = self.chat.fetchall()
        sss = "INSERT INTO chats VALUES (?, ?, ?, ?, ?, ?, ?)"
        var = clubid, event, len(fetch)+1, Low_id, name, 0, message
        self.chat.execute(sss, var)
        self.con.commit()
        self.con.close()
        self.conn.close()

    def GetMsgRoom(self, clubID):
        self.con = sql.connect("database/Gameroom/chats.db")
        self.c = self.con.cursor()
        self.c.execute(f"CREATE TABLE IF NOT EXISTS chats (roomID INT, Event INT, Tick INT, plrid INT, plrname TEXT, plrrole INT, Msg TEXT)")
        clubid = clubID
        self.conn = sql.connect("database/Gameroom/gr.db")
        self.con = sql.connect("database/Gameroom/chats.db")
        self.cur= self.conn.cursor()
        self.chat = self.con.cursor()
        self.chat.execute(f"SELECT * FROM chats WHERE roomID={clubID}")
        fetch = self.chat.fetchall()
        if len(fetch)>0:
            self.MessageCount = len(fetch)
        else:
            self.MessageCount = 1
        self.conn.close()
        self.con.close()

    def removeRoom(self):
        self.conn = sql.connect("database/Gameroom/gr.db")
        self.cur = self.conn.cursor()
        self.cur.execute("DELETE FROM gr WHERE roomID=?", (self.player.room_id,))
        self.conn.commit()
    def getRandomroomAndJoin(self, mapslot):
        self.conn = sql.connect("database/Gameroom/gr.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM gr")
        fetch = self.cur.fetchall()
        if fetch:
            for i in fetch:
                plrData = json.loads(i[3])
                if len(plrData)<3:
                    l = str(len(plrData))
                    plrData[l]={}
                    plrData[l]["host"] = 0
                    plrData[l]["lowID"] = self.player.low_id
                    plrData[l]["name"] = self.player.name
                    plrData[l]["Team"] = 0
                    plrData[l]["ctick"] = self.player.ctick
                    plrData[l]["message"] = self.player.message
                    plrData[l]["Ready"] = self.player.isReady
                    plrData[l]["brawlerID"] = self.player.brawler_id
                    plrData[l]["skinID"] = self.player.skin_id
                    plrData[l]["starpower"] = self.player.starpower
                    plrData[l]["gadget"] = self.player.gadget
                    plrData[l]["profileIcon"] = self.player.profile_icon
                    plrData[l]["namecolor"] = self.player.name_color
                    plrData[l]["status"] = 0
                    self.cur.execute("UPDATE gr SET players=? WHERE roomID=?", (json.dumps(plrData), fetch[0][0]))
                    self.conn.commit()
                    self.mapID = fetch[0][1]
                    self.useGadget = fetch[0][2]
                    self.playerCount = len(plrData)
                    self.plrData = plrData
                    self.player.roomType = fetch[0][4]
                    self.player.room_id = fetch[0][0]
                    break
    def leaveRoom(self,reqID):
        self.conn = sql.connect("database/Gameroom/gr.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM gr WHERE roomID=?", (self.player.room_id,))
        fetch = self.cur.fetchall()
        if fetch:
            plrData = json.loads(fetch[0][3])
            for i in plrData:
            	if plrData[i]["lowID"]==reqID:
                    plrData.pop(str(i))
                    self.cur.execute("UPDATE gr SET players=? WHERE roomID=?", (json.dumps(plrsData), self.reqID))
                    self.conn.commit()
    def loadGameroom(self):
        self.conn = sql.connect("database/Gameroom/gr.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS gr (roomID INT, mapID INT, gadget INT, players JSON, type INT)")
        plrs = {"0": {"host": 1, "lowID": self.player.low_id, "name": self.player.name, "Team": self.player.team, "ctick": self.player.ctick, "message": self.player.message, "Ready": self.player.isReady, "brawlerID": self.player.brawler_id, "skinID": self.player.skin_id, "starpower": self.player.starpower, "gadget": self.player.gadget, "profileIcon": self.player.profile_icon, "namecolor": self.player.name_color, "status": 0}}
        self.cur.execute("SELECT * FROM gr WHERE roomID=?", (self.player.room_id,))
        fetch = self.cur.fetchall()
        if fetch:
            self.mapID = fetch[0][1]
            self.useGadget = fetch[0][2]
            plrs = json.loads(fetch[0][3])
            self.playerCount = len(plrs)
            self.plrData = plrs
            self.roomType = fetch[0][4]
    def leaveFromRoom(self, lowID):
        self.conn = sql.connect("database/Gameroom/gr.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM gr WHERE roomID=?", (self.player.room_id,))
        fetch = self.cur.fetchall()
        if fetch:
            plrData = json.loads(fetch[0][3])
            for i in plrData:
            	if plrData[i]["lowID"]==lowID:
                    plrData.pop(str(i))
                    self.cur.execute("UPDATE gr SET players=? WHERE roomID=?", (json.dumps(plrData), fetch[0][0]))
                    self.conn.commit()
                    break
    def replaceGameroomValue(self, value_name, new_value, type):
        self.conn = sql.connect("database/Gameroom/gr.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM gr WHERE roomID=?", (self.player.room_id,))
        fetch = self.cur.fetchall()
        if fetch:
            if type=="room":
                self.cur.execute(f"UPDATE gr SET {value_name}=? WHERE roomID=?", (new_value, self.player.room_id))
                self.conn.commit()
        elif type == "player":
            gameroom_data["info"][str(value_name)] = new_value
            db.update(gameroom_data, query.room_id == self.player.room_id)
            plrData = json.loads(fetch[0][3])
            for i in plrData:
                if i["lowID"]==self.player.low_id:
                    plrData[str(plrData.index(i))][str(value_name)]=new_value
                    self.cur.execute(f"UPDATE gr SET players=?", (json.dumps(plrData),))
                    self.conn.commit()
        elif type == "removePlayer":
            plrData = json.loads(fetch[0][3])
            for i in plrData:
                if i["host"]==1:
                   self.cur.execute("DELETE FROM gr WHERE roomID=?", (fetch[0][0],))
                   self.conn.commit()
    def getRoomAndJoin(self, joinerToken, roomID):
        self.conn = sql.connect("database/Gameroom/gr.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM gr WHERE roomID=?", (roomID,))
        fetch = self.cur.fetchall()
        if fetch:
            print("FetchOK")
            self.reqID = fetch[0][0]
            plrsData = json.loads(fetch[0][3])
            l = str(len(plrsData))
            plrsData[l]={}
            plrsData[l]["host"] = 0
            plrsData[l]["lowID"] = self.player.low_id
            plrsData[l]["name"] = self.player.name
            plrsData[l]["Team"] = 0
            plrsData[l]["ctick"] = self.player.ctick
            plrsData[l]["message"] = self.player.message
            plrsData[l]["Ready"] = self.player.isReady
            plrsData[l]["brawlerID"] = self.player.brawler_id
            plrsData[l]["skinID"] = self.player.skin_id
            plrsData[l]["starpower"] = self.player.starpower
            plrsData[l]["gadget"] = self.player.gadget
            plrsData[l]["profileIcon"] = self.player.profile_icon
            plrsData[l]["namecolor"] = self.player.name_color
            plrsData[l]["status"] = 0
            self.mapID = fetch[0][1]
            self.useGadget = fetch[0][2]
            self.playerCount = len(plrsData)
            self.plrData = plrsData
            self.cur.execute("UPDATE gr SET players=? WHERE roomID=?", (json.dumps(plrsData), self.reqID))
            self.conn.commit()
    def UpdateGameroomPlayerInfo(self, low_id):
        self.conn = sql.connect("database/Gameroom/gr.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM gr WHERE roomID=?", (self.player.room_id,))
        fetch = self.cur.fetchall()
        if fetch:
            plrsData = json.loads(fetch[0][3])
            self.reqID = fetch[0][0]
            for i in plrsData:
                if plrsData[i]["lowID"]==low_id:
                    plrsData[i]["Team"] = self.player.team
                    plrsData[i]["ctick"] = self.player.ctick
                    plrsData[i]["message"] = self.player.message
                    plrsData[i]["Ready"] = self.player.isReady
                    plrsData[i]["brawlerID"] = self.player.brawler_id
                    plrsData[i]["skinID"] = self.player.skin_id
                    plrsData[i]["starpower"] = self.player.starpower
                    plrsData[i]["gadget"] = self.player.gadget
                    plrsData[i]["profileIcon"] = self.player.profile_icon
                    plrsData[i]["namecolor"] = self.player.name_color
                    plrsData[i]["status"] = self.player.state
                    self.cur.execute("UPDATE gr SET players=? WHERE roomID=?", (json.dumps(plrsData), self.reqID))
                    self.conn.commit()
                    self.conn.close()
                    break


    def createClub(self, clubid):
        self.conn = sql.connect("database/Club/clubs.db")
        self.con = sql.connect("database/Club/chats.db")
        self.cur = self.conn.cursor()
        self.c = self.con.cursor()
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS clubs (clubID INT, name TEXT, desc TEXT, region TEXT, badgeID INT, type INT, trophiesneeded INT, friendlyfamily INT, trophies INT, members JSON, notif JSON)")
        self.c.execute(f"CREATE TABLE IF NOT EXISTS chats (clubID INT, Event INT, Tick INT, plrid INT, plrname TEXT, plrrole INT, Msg TEXT)")
        self.con.commit()
        self.conn.commit()
        data = {"members": {self.player.low_id:self.player.name}}
        notif = {}
        var = clubid,str(self.clubName),str(self.clubdescription),"RU",self.clubbadgeID,self.clubtype,self.clubtrophiesneeded,self.clubfriendlyfamily,self.player.trophies,json.dumps(data), json.dumps(notif)
        self.cur.execute(f"INSERT INTO clubs VALUES (?,?,?,?,?,?,?,?,?,?,?)", var)
        self.conn.commit()

        sss = "INSERT INTO chats VALUES (?, ?, ?,?,?,?,?)"
        var = clubid, 2, 1, self.player.low_id, str(self.player.name), 2, "Привет"
        self.c.execute(sss, var)
        self.con.commit()
    def setNotifData(self, text, by):
        self.conn = sql.connect("database/Club/clubs.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM clubs WHERE clubID=?", (self.player.club_low_id,))
        fetch = self.cur.fetchall()
        if fetch:
               notifData = json.loads(fetch[0][10])
               l = str(len(notifData))
               notifData[l]={}
               notifData[l]["text"]=text
               notifData[l]["by"]=by
               notifData[l]["timer"]=datetime.datetime.timestamp(datetime.datetime.now())
               self.cur.execute("UPDATE clubs SET notif=? WHERE clubID=?", (json.dumps(notifData),self.player.club_low_id))
               self.conn.commit()
               self.conn.close()
    def CountClub(self):
        self.AllianceCount = 0
        self.club_list = []
        self.conn = sql.connect("database/Club/clubs.db")
        self.con = sql.connect("database/Club/chats.db")
        self.cur = self.conn.cursor()
        self.c = self.con.cursor()
        try:
                        self.cur.execute(f"SELECT * FROM clubs")
                        fetch = self.cur.fetchall()
                        if len(fetch)>0:
                            for i in fetch:
                                self.club_list.append(int(i[0]))
                                self.AllianceCount+=1
                        self.conn.close()
                        self.con.close()
        except:
            pass
            
    def LeaderClub(self):
        self.AllianceCount = 0
        self.club_list = []
        self.conn = sql.connect("database/Club/clubs.db")
        self.con = sql.connect("database/Club/chats.db")
        self.cur = self.conn.cursor()
        self.c = self.con.cursor()
        try:
                        self.cur.execute(f"SELECT * FROM clubs ORDER BY trophies DESC LIMIT 200")
                        fetch = self.cur.fetchall()
                        if len(fetch)>0:
                            for i in fetch:
                                self.club_list.append(int(i[0]))
                                self.AllianceCount+=1
                        self.conn.close()
                        self.con.close()
        except:
            pass
	
	
    def loadClub(self, clubid):
        self.conn = sql.connect("database/Club/clubs.db")
        self.con = sql.connect("database/Club/chats.db")
        self.cur = self.conn.cursor()
        self.c = self.con.cursor()
        
        self.cur.execute(f"SELECT * FROM clubs WHERE clubID={clubid}")
        fetch = self.cur.fetchall()
        if len(fetch)>0:
                for i in fetch:
                    self.clubmembercount = 0
                    self.plrids = []
                    self.clubName = i[1]
                    self.clubdescription = i[2]
                    self.clubregion = i[3]
                    
                    self.clubbadgeID = i[4]
                    self.clubtype = i[5]
                    self.clubtrophiesneeded = i[6]
                    self.clubfriendlyfamily = i[7]
                    try:
                        self.notifData = json.loads(i[10])
                    except:
                        self.cur.execute("ALTER TABLE clubs ADD COLUMN notif JSON")
                        self.conn.commit()
                    self.clubtrophies = 0
                    data = json.loads(i[9])
                    for ID in data["members"]:
                             if ID != "members":
                                 self.plrids.append(int(ID))
                                 self.clubmembercount += 1
                                 DataBase.GetMemberData(self, int(ID))
                                 self.clubtrophies += self.plrtrophies
                    #self.cur.execute(f"UPDATE clubs SET trophies={self.clubtrophies} WHERE clubID={clubid}")
                    #self.cur.execute(f"UPDATE clubs SET trophies={self.clubtrophies} WHERE clubID={clubid}")
                    self.conn.commit()
                    self.conn.close()
                    self.con.close()
                    

    def AddMember(self, AllianceID, PlayerID, PlayerName, Action):
        self.conn = sql.connect("database/Club/clubs.db")
        self.con = sql.connect("database/Club/chats.db")
        self.cur= self.conn.cursor()
        self.chat = self.con.cursor()
        query = Query()
        self.cur.execute(f"SELECT * FROM clubs WHERE clubID={AllianceID}")
        fetch = self.cur.fetchall()
        if len(fetch)>0:
            data = json.loads(fetch[0][9])
            if Action == 0:
                self.chat.execute(f"DELETE FROM chats WHERE clubID={AllianceID}")
                self.cur.execute(f"DELETE FROM clubs WHERE clubID={AllianceID}")
                self.con.commit()
                self.conn.commit()
            elif Action == 1:
               data["members"][str(PlayerID)] = PlayerName
               self.cur.execute(f"UPDATE clubs SET members=? WHERE clubID=?",(json.dumps(data),AllianceID))
               ol = fetch[0][8]
               self.cur.execute(f"UPDATE clubs SET trophies={ol+self.player.trophies} WHERE clubID={AllianceID}")
               self.conn.commit()
            elif Action == 2:
                   data['members'].pop(str(PlayerID))
                   self.cur.execute(f"UPDATE clubs SET members=? WHERE clubID=?", (json.dumps(data), AllianceID))
                   ol = fetch[0][8]
                   self.cur.execute(f"UPDATE clubs SET trophies={ol-self.player.trophies} WHERE clubID={AllianceID}")
                   self.conn.commit()
            self.con.close()
            self.conn.close()
    def GetMemberData(self, Low_id):
        try:
            self.players = DataBase.loadbyID(self, Low_id)
            if self.players[1]== int(Low_id):
                    self.lowplrid = self.players[1]
                    self.plrrole = self.players[12]
                    self.plrtrophies = self.players[3]
                    self.plrname = self.players[2]
                    self.plricon = self.players[9]
                    self.plrnamecolor = self.players[10]
                    self.plrexperience = self.players[21]
                    self.plrstatus = self.players[19]
                    self.plrvip = self.players[20]

        except Exception as e:
            self.lowplrid = 1
            self.plrrole = 0
            self.plrtrophies = 0
            self.plrname = "Falied to load account!"
            self.plricon = 5
            self.plrnamecolor = 1
            self.plrexperience = 999
            self.plrvip = 0
            self.plrstatus = 0

    def replaceClubValue(self, target, inf1, inf2, inf3, inf4, inf5):
        self.conn = sql.connect("database/Club/clubs.db")
        self.con = sql.connect("database/Club/chats.db")
        self.cur= self.conn.cursor()
        self.chat = self.con.cursor()
        query = Query()
        self.cur.execute(f"SELECT * FROM clubs WHERE clubID={self.player.club_low_id}")
        fetch = self.chat.fetchall()
        if 1==1:
            
            self.cur.execute(f"UPDATE clubs SET desc='{inf1}' WHERE clubID={self.player.club_low_id}")
            self.cur.execute(f"UPDATE clubs SET badgeID={inf2} WHERE clubID={self.player.club_low_id}")
            self.cur.execute(f"UPDATE clubs SET type={inf3} WHERE clubID={self.player.club_low_id}")
            self.cur.execute(f"UPDATE clubs SET trophiesneeded={inf4} WHERE clubID={self.player.club_low_id}")
            self.cur.execute(f"UPDATE clubs SET friendlyfamily={inf5} WHERE clubID={self.player.club_low_id}")
            
            self.conn.commit()
            self.conn.close()
            self.con.close()

    def GetmsgCount(self, clubID):
        clubid = clubID
        self.conn = sql.connect("database/Club/clubs.db")
        self.con = sql.connect("database/Club/chats.db")
        self.cur= self.conn.cursor()
        self.chat = self.con.cursor()
        self.chat.execute(f"SELECT * FROM chats WHERE clubID={clubID}")
        fetch = self.chat.fetchall()
        if len(fetch)>0:
            self.MessageCount = len(fetch)
        else:
            self.MessageCount = 1
        self.conn.close()
        self.con.close()

    def Addmsg(self, clubID, event, tick, Low_id, name, role, msg):
        clubid = self.player.club_low_id
        self.conn = sql.connect("database/Club/clubs.db")
        self.con = sql.connect("database/Club/chats.db")
        self.cur= self.conn.cursor()
        self.chat = self.con.cursor()
        self.chat.execute(f"SELECT * FROM chats WHERE clubID={clubID}")
        fetch = self.chat.fetchall()
        sss = "INSERT INTO chats VALUES (?, ?, ?,?,?,?,?)"
        var = clubid, event, len(fetch)+1, Low_id, name, role, msg
        self.chat.execute(sss, var)
        self.con.commit()
        self.con.close()
        self.conn.close()
    def DeleteAllMsg(self, clubID):
        self.con = sql.connect("database/Club/chats.db")
        self.chat = self.con.cursor()
        self.chat.execute(f"SELECT * FROM chats WHERE clubID={clubID}")
        fetch = self.chat.fetchall()
        if len(fetch)>=50:
            self.chat.execute(f"DELETE FROM chats WHERE clubID={clubID}")
            self.con.commit()