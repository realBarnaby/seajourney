
print(" ******** Welcome to your sea journey! ******** \n               Shall we embark?")

from enum import Enum


# ***** destination options *****
# ***** destination distances from the chosen starting port *****
class destinations(Enum):

    Morocco = 1000
    CapeVerde = 2000
    GoldCoast = 3000
    Benin = 3500
    Congo = 4500
    CapeOfGoodHope = 6000


# ***** nation options, its bonuses and its port *****
class Nation:

    def __init__(self, port: str, bonuses=0, treasury=10):
        self.port = port
        self.bonuses = bonuses
        self.treasury = treasury

    def setPortName(self, name):
        self.port = name

    def getPortName(self):
        return self.port

    def getBonuses(self):
        return self.bonuses

    def getTreasury(self):
        return self.treasury


# ***** ship options and its bonuses *****
class Ship(Nation):

    def __init__(self, port: str, bonuses=0, treasury=10, speed=10, capacity=20):
        super().__init__(port, bonuses, treasury)
        self.capacity = capacity
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def getCapacity(self):
        return self.capacity


# ***** explorer options and its bonuses *****
class Explorer(Nation):

    def __init__(self,  port: str, bonuses=0, treasury=10, maneuver=2, trader=5):
        super().__init__(port, bonuses, treasury)
        self.maneuver = maneuver
        self.trader = trader

    def getManeuver(self):
        return self.maneuver

    def getTrader(self):
        return self.trader

print("***** Choose a nation: ")
Portugal = Nation("Lisboa")
print("Your chosen nation is:", Portugal.getPortName())
print("Your bonuses:", Portugal.getBonuses())
print("Your base treasury:", Portugal.getTreasury())

print("***** Name your ship of choice: ")
Galway = Ship("Lisboa")
print("Your ship's speed is:", Galway.getSpeed())
print("Your ship's capacity:", Galway.getCapacity())

print("***** Name your explorer: ")
Cao = Explorer("Lisboa")
print("The explorer's maneuver:", Cao.getManeuver())
print("The explorer's bonus trade income:", Cao.getTrader())

# ***** nautical miles/hour ~knot *****          one knot equals one nautical mile per hour
knot = 10


fileobject = open("sea.txt", "w")
fileobject.write("Nautical miles: "+ str(destinations.Morocco.value))
fileobject.write("\nThe journey takes "+ str(destinations.Morocco.value / knot)+ "hour")
fileobject.close()

fileobject = open("sea.txt", "r")
print(fileobject.readline())
fileobject.close()


