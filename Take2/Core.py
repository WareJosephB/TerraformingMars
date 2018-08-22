import Corporations.py
import Cards.py
import Board.py

plantsPerTile = 8
heatValue = 0
refundOver20 = 0
refundEvents = 0
lax = 0
thisturnlax = lax
firstAction = 0  # 0 = nothing, 1 = draw 3 cards, 2 = place city
steelProdPlacement = 0
jovianMoneyProd = 0
earthDiscount = 0
spaceDiscount = 0
powerDiscount = 0
UN = 0
steelValue = 2
titaniumValue = 3

print "Choose a corporation:"
for a in Corporations.corps:
    Tag = ''
    if len(a.tags) == 1:
        Tag = ': ' + a.tags[0]
    elif len(a.tags) == 2:
        Tag = ': ' + a.tags[0] + ', ' + a.tags[1]
    print str(a.number) + " " + a.name + Tag
    print a.description
    print ''

choice = int(input("#? :"))

Active = Corporations.corps[choice-1]

'''if Active.other != []:
    for a in Active.other:
        eval(a)'''


class Resource:
    def __init__(self, name, quantity, production, value):
        self.name = name
        self.quan = quantity
        self.prod = production
        self.val = value

money = Resource('Megaeuros', Active.nummoney, Active.moneyprod, 1)
steel = Resource('Steel', Active.numsteel, Active.steelprod, steelValue)
titanium = Resource('Titanium', Active.numtitanium, Active.titaniumprod, titaniumValue)
plants = Resource('Plants', Active.numplants, Active.plantprod, 0)
energy = Resource('Energy', Active.numenergy, Active.energyprod, 0)
heat = Resource('Heat', Active.numheat, Active.heatprod, heatValue)
