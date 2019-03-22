class Corporation:
    def __init__(self, number, name, startcash, tags, description):
        self.number = number
        self.name = name
        self.nummoney = startcash
        self.tags = tags
        self.description = description

Credicor = Corporation(1, 'Credicor', 57, [],
                       'Start with 57 Megaeuros, get a refund of 4ME when base cost of project or standard project is >19')
Credicor.other = ['refundOver20 + 4, refundOver20']
Ecoline = Corporation(2, 'Ecoline', 36, ['Plant'],
                      'Start with 36 Megaeuros, 3 Plants, 2 Plant Production, Greenery tiles take 7 plants instead of 8')
Ecoline.plantprod = 2
Ecoline.numplants = 3
Ecoline.other = ['plantsPerTile - 1, plantsPerTile']
Helion = Corporation(3, 'Helion', 42, ['Space'],
                     'Start with 42 Megaeuros, 3 Heat Production, can spend Heat as Money')
Helion.heatprod = 3
Helion.other = ['heatValue + 1, heatValue']
Cinematics = Corporation(4, 'Interplanetary Cinematics', 30, ['Building'],
                         'Start with 30 Megaeuros, 20 Steel, get a refund of 2 whenever you play an Event')
Cinematics.numsteel = 20
Cinematics.other = ['refundEvents + 2, refundEvents']
Inventrix = Corporation(5, 'Inventrix', 45, ['Science'],
                        'Start with 45 Megaeuros, Temperature/Oxygen/Ocean requirements are 2 steps laxer than usual, as your first action in the game draw 3 cards')
Inventrix.other = ['lax + 2, lax', 'firstAction + 1, firstAction']
Mining = Corporation(6, 'Mining Guild', 30, ['Building', 'Building'],
                     'Start with 30 Megaeuros, 5 Steel, 1 Steel Production, whenever you gain Steel or Titanium as a placement bonus also gain 1 Steel Production')
Mining.numsteel = 5
Mining.other = ['steelProdPlacement + 1, steelProdPlacement']
Phoblog = Corporation(7, 'Phoblog', 23, ['Space'],
                      'Start with 23 Megaeuros, 10 Titanium, your Titanium are worth 1 extra')
Phoblog.other = ['titaniumValue + 1, titaniumValue']
Saturn = Corporation(8, 'Saturn Systems', 42, ['Jovian'],
                     'Start with 42 Megaeuros, 1 Titanium Production, whenever a Jovian tag is played [including this one] gain 1 Money Production')
Saturn.other = ['jovianMoneyProd + 1, jovianMoneyProd']
Saturn.titaniumprod = 1
Teractor = Corporation(9, 'Teractor', 60, ['Earth'],
                       'Start with 60 Megaeuros, get a 3ME discount on all cards with an Earth tag')
Teractor.other = ['earthDiscount + 3, earthDiscount']
Tharsis = Corporation(10, 'Tharsis Republic', 40, ['Building'],
                      'Start with 40 Megaeuros, as your first action place a City tile, whenever you place a City tile gain 3ME, whenever anyone [including you] places a City tile gain 1 Money Production')
Tharsis.other = ['firstAction + 2, firstAction']
Thorgate = Corporation(11, 'Thorgate', 48, ['Power'],
                       'Start with 48 Megaeuros, 1 Power Prouction, get a 3ME discount on all cards with a Power tag and also the Standard Project: Powerplant.')
Thorgate.powerprod = 1
Thorgate.other = ['powerDiscount + 3, powerDiscount']
UMNI = Corporation(12, 'United Nations Mars Initiative', 40, ['Earth'],
                   'Start with 40 Megaeuros, once per generation if you have raised the Terraform Rating this generation you may spend 3ME to raise it again')
UMNI.other = ['UN + 1, UN']

corps = [Credicor, Ecoline, Helion, Cinematics, Inventrix, Mining, Phoblog,
         Saturn, Teractor, Tharsis, Thorgate, UMNI]