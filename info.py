# coding: utf-8
# Here your code !
import random
class Info:
    def __init__(self,info_id,name):
        self.info_id = info_id
        self.name = name
    def get_id(self):
        return self.info_id
    def get_name(self):
        return self.name
    def clear_name(self):
        self.name = ''

class PlayerInfo(Info):
    def __init__(self, player_id, name, money):
        if name == 'player':
            name = "%s-%d" % (name,self.player_id)
        Info.__init__(self,player_id, name)
        self.money = money
        self.position = self.GO
        self.jail = False
        self.stay_jail = 0
        self.jail_card = 0
        self.lands = []
        self.repdigit = 0
    def add_money(self,money):
        self.money += money
    def lose_money(self,money):
        self.money -= money
    def move(self, position):
        self.position = position
    def go2Jail(self):
        self.position = self.JAIL
        self.jail = True
    def free(self):
        self.jail = False
        self.stay_jail = 0
    def add_stay_jail(self):
        self.stay_jail += 1
    def add_jail_card(self):
        self.jail_card += 1
    def lose_jail_card(self):
        self.jail_card -= 1
    def add_land(self,land):
        self.land.append(land)
    def get_lands(self):
        for land in self.land:
            yield land
    def has_land(self,land):
        return land in self.land
    def add_repdigit(self):
        self.repdigit += 1
    def clear_repdigit(self):
        self.repdigit = 0

class LandInfo(Info):
    def __init__(self,land_id,name):
        Info.__init__(self,land_id, name)
        self.position = self.GO
        self.price = 0
        self.owner  = -1
        self.mortgage = False
        self.group = []
    def new_owener(self,player_id):
        self.owner = player_id
    def owener_left(self):
        self.owner = -1
    def who_is_oweer(self):
        return self.owener
    def exist_owner(self):
        return self.owner != -1
    def mortgaged(self):
        self.mortgage = True
    def unmortgaged(self):
        self.mortgage = False
    def how_much_unmortgaged(self):
        return self.mortage/2 + self.mortage/10
    def how_much_interest(self):
        return self.mortage/10

class Colors(LandInfo):
    def __init__(self,land_id, name):
        LandInfo.__init__(self,land_id, name)
        self.buildfee = 0
        self.house = 0
        self.hotel = 0
        self.fee = [0]*6
    def build_house(self):
        self.house += 1
    def sell_house(self):
        self.house -= 1
    def build_hotel(self):
        self.hotel += 1
    def sell_hotel(self):
        self.hotel -= 1
    def get_group(self):
        for land in self.group:
            yield land
    def how_much_fee(self):
        if self.hotel:
            return self.rental_fee[-1]
        else:
            return self.rental_fee[self.house]
            
class A1(Colors):
    def __init__(self):
        Colors.__init__(self,self.A1, 'A1')
        self.position = self.A1
        self.price = 60
        self.buildfee = 50
        self.rental_fee = [2, 10, 30, 90, 160, 250] 

class A2(Colors):
    def __init__(self):
        Colors.__init__(self,self.A2, 'A2')
        self.position = self.A2
        self.price = 60
        self.buildfee = 50
        self.rental_fee = [4, 20, 50, 180, 320, 450]

class B1(Colors):
    def __init__(self):
        Colors.__init__(self,self.B1, 'B1')
        self.position = self.B1
        self.price = 100
        self.buildfee = 50
        self.rental_fee = [6, 30, 90, 270, 400, 550]

class B2(Colors):
    def __init__(self):
        Colors.__init__(self,self.B2, 'B2')
        self.position = self.B2
        self.price = 100
        self.buildfee = 50
        self.rental_fee = [6, 30, 90, 270, 400, 550]
        
class B3(Colors):
    def __init__(self):
        Colors.__init__(self,self.B3, 'B3')
        self.position = self.B3
        self.price = 120
        self.buildfee = 50
        self.rental_fee = [8, 40, 100, 300, 450, 600]

class C1(Colors):
    def __init__(self):
        Colors.__init__(self,self.C1, 'C1')
        self.position = self.C1
        self.price = 140
        self.buildfee = 100
        self.rental_fee = [10, 50, 150, 450, 625, 750]

class C2(Colors):
    def __init__(self):
        Colors.__init__(self,self.C2, 'C2')
        self.position = self.C2
        self.price = 140
        self.buildfee = 100
        self.rental_fee = [10, 50, 150, 450, 625, 750]

class C3(Colors):
    def __init__(self):
        Colors.__init__(self,self.C3, 'C3')
        self.position = self.C3
        self.price = 160
        self.buildfee = 100
        self.rental_fee = [12, 60, 180, 500, 700, 900]

class D1(Colors):
    def __init__(self):
        Colors.__init__(self,self.D1, 'D1')
        self.position = self.D1
        self.price = 180
        self.buildfee = 100
        self.rental_fee = [14, 70, 200, 550, 750, 950]

class D2(Colors):
    def __init__(self):
        Colors.__init__(self,self.D2, 'D2')
        self.position = self.D2
        self.price = 180
        self.buildfee = 100
        self.rental_fee = [14, 70, 200, 550, 750, 950]

class D3(Colors):
    def __init__(self):
        Colors.__init__(self,self.D3, 'D3')
        self.position = self.D3
        self.price = 200
        self.buildfee = 100
        self.rental_fee = [16, 80, 220, 600, 800, 1000]

class E1(Colors):
    def __init__(self):
        Colors.__init__(self,self.E1, 'E1')
        self.position = self.E1
        self.price = 220
        self.buildfee = 150
        self.rental_fee = [18, 90, 250, 700, 875, 1050]

class E2(Colors):
    def __init__(self):
        Colors.__init__(self,self.E2, 'E2')
        self.position = self.E2
        self.price = 220
        self.buildfee = 150
        self.rental_fee = [18, 90, 250, 700, 875, 1050]

class E3(Colors):
    def __init__(self):
        Colors.__init__(self,self.E3, 'E3')
        self.position = self.E3
        self.price = 240
        self.buildfee = 150
        self.group = [self.E1,self.E2]
        self.rental_fee = [20, 100, 300, 750, 925, 1100]

class F1(Colors):
    def __init__(self):
        Colors.__init__(self,self.F1, 'F1')
        self.position = self.F1
        self.price = 260
        self.buildfee = 150
        self.rental_fee = [22, 110, 330, 800, 975, 1150]

class F2(Colors):
    def __init__(self):
        Colors.__init__(self,self.F2, 'F2')
        self.position = self.F2
        self.price = 260
        self.buildfee = 150
        self.rental_fee = [22, 110, 330, 800, 975, 1150]

class F3(Colors):
    def __init__(self):
        Colors.__init__(self,self.F3, 'F3')
        self.position = self.F3
        self.price = 280
        self.buildfee = 150
        self.rental_fee = [24, 120, 360, 850, 1025, 1200]
        
class G1(Colors):
    def __init__(self):
        Colors.__init__(self,self.G1, 'G1')
        self.position = self.G1
        self.price = 300
        self.buildfee = 200
        self.rental_fee = [26, 130, 390, 900, 1100, 1275]

class G2(Colors):
    def __init__(self):
        Colors.__init__(self,self.G2, 'G2')
        self.position = self.G2
        self.price = 300
        self.buildfee = 200
        self.rental_fee = [26, 130, 390, 900, 1100, 1275]

class G3(Colors):
    def __init__(self):
        Colors.__init__(self,self.G3, 'G3')
        self.position = self.G3
        self.price = 320
        self.buildfee = 200
        self.rental_fee = [28, 150, 450, 1000, 1200, 1400]

class H1(Colors):
    def __init__(self):
        Colors.__init__(self,self.H1, 'H1')
        self.position = self.H1
        self.price = 350
        self.buildfee = 200
        self.rental_fee = [35, 175, 500, 1100, 1300, 1500]

class H2(Colors):
    def __init__(self):
        Colors.__init__(self,self.H2, 'H2')
        self.position = self.H2
        self.price = 400
        self.buildfee = 200
        self.rental_fee = [50, 200, 600, 1400, 1700, 2000]

class Railroad(LandInfo):
    def __init__(self,land_id,name,position):
        LandInfo.__init__(self,land_id, name)
        self.position = position
        self.price = 200
        self.rental_fee = [25, 50, 100, 200]
    def how_much_fee(self,own_number):
        return self.rental_fee[len(self.group)]

class R1(Railroad):
    def __init__(self):
        Railroad.__init__(self,self.R1, 'R1', self.R1)

class R2(Railroad):
    def __init__(self):
        Railroad.__init__(self,self.R2, 'R2', self.R2)

class R3(Railroad):
    def __init__(self):
        Railroad.__init__(self,self.R3, 'R3', self.R3)

class R4(Railroad):
    def __init__(self):
        Railroad.__init__(self,self.R4, 'R4', self.R4)
        
class PublicUnitility(LandInfo):
    def __init__(self,land_id,name,position):
        LandInfo.__init__(self,land_id, name)
        self.position = position
        self.price = 150
    def how_much_fee(self):
        if len(self.group) == 2:
            return random.randint(1,6) * 10
        else:
            return random.randint(1,6) * 4

class U1(PublicUnitility):
    def __init__(self):
        Railroad.__init__(self,self.U1, 'U1', self.U1)

class U2(PublicUnitility):
    def __init__(self):
        Railroad.__init__(self,self.U2, 'U2', self.U2)
        
def shuffle(cards,shuffle):
    for i in range(shuffle):
        card = cards.pop(random.randint(0,len(cards)-1))
        cards += [card]
    return cards
    
class CardPoint(Info):
    def __init__(self, name, shuffle_count=1000):
        Info.__init__(self, self.GO, name)
        self.cards = []
    def direction(self):
        card = self.cards[0]
        if card == 'JailCard':
            self.cards = self.cards[1:]
        else:
            self.cards = self.cards[1:] + [self.cards[0]]
        return card
    def returnJailCard(self):
        if not 'JailCard' in self.cards:
            self.cards += ['JailCard'] 

class Chance(CardPoint):
    def __init__(self, shuffle_count=1000):
        CardPoint.__init__(self, self.CH1, 'Chance')
        self.cards = shuffle([
                            'Go2Go','Go2Jail','Go2C1','Go2E3','Go2H2','Go2R1','Go2NextR','Go2NextR','Go2NextU','GoBack3',
                            'Receive150$','Receive50$','Pay15$','Pay50$EachPlayer','Pay25$EachHouseAndPay100$EachHotel','JailCard'
                            ],200)

class CommunityChest(CardPoint):
    def __init__(self, shuffle_count=1000):
        CardPoint.__init__(self, self.CC1, 'CommunityChest')
        self.cards = shuffle([
                            'Go2Go','Go2Jail','Receive100$','Receive100$','Receive100$','Receive10$EachPlayer','Receive50$','Receive25$'
                            'Receive20$','Receive10$','Pay50$','Pay50$','Pay100$','Pay40$EachHouseAndPay115$EachHotel','JailCard'
                            ],200)

