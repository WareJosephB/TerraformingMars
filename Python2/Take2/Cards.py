class Card:
    def __init__(self, price, name, tags, description, colour):
        self.colour = colour
        self.price = price
        self.name = name
        self.tags = tags
        self.description = description
        self.heatIncrease = 0
        self.oceanIncrease = 0
        self.oxygenIncrease = 0
        self.moneyProd = 0
        self.steelProd = 0
        self.titaniumProd = 0
        self.plantProd = 0
        self.energyProd = 0
        self.heatProd = 0
        self.numMoney = 0
        self.numSteel = 0
        self.numTitanium = 0
        self.numPlant = 0
        self.numEnergy = 0
        self.numHeat = 0
        self.oxygenLimit = 0
        self.oxygenDirection = 0  # 0 = none, -1 = needs less than, +1 = more
        self.oceanLimit = 0
        self.oceanDirection = 0  # as above
        self.temperatureLimit = 0
        self.temperatureDirection = 0