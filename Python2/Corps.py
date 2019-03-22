#  Corporations

Corporationss = ['Credicor', 'Ecoline', 'Helion', 'Interplanetary Cinematics', 'Inventrix', 'Mining Guild', 'Phoblog', 'Tharsis Republic', 'Thorgate', 'UMNI', 'Saturn Systems', 'Teractor']


CorporationDescriptions = ['Start with M€57; get M€4 refund on anything with a base cost >M€19.',
                    'Start with M€36, 2 Plant Production, 3 Plants; Greenery tiles cost 7 instead of 8; Plant Tag.',
                    'Start with M€42, 3 Heat Production; Can spend Heat as Money (but not Money as Heat); Space Tag.',
                    'Start with M€30, 20 Steel; get M€2 refund on Event cards; Building Tag.',
                    'Start with M€45; as your first action draw 3 cards, O2/Ocean/Temp requirements are 2 stages laxer for you; Science Tag.',
                    'Start with M€30, 5 Steel, 1 Steel Production; whenever you gain Steel/Titanium placement bonuses, also get 1 Steel Production; 2 Building Tags.',
                    'Start with M€23, 10 Titanium; Your Titanium is worth M€4; Space Tag.',
                    'Start with M€40; as your first action place a City, whenever a city is placed get M€3, whenever you place a city get 1 Money Production; Building Tag.',
                    'Start with M€48, 1 Energy Production; All cards with a Power tag and the Power Plant standard project are discounted by M€3; Power Tag.',
                    'Start with M€40; As an action can spend M€3 to increase your TR by 1 if your TR has risen this generation already.',
                    'Start with M€42, 1 Titanium Production; Whenever a Jovian Tag is played (including this one) gain 1 Money Production; Jovian Tag.',
                    'Start with M€60; All cards with Earth Tags are discounted by M€3; Earth Tag.']


def Credicor(Money, Refund_Over20):
    Money = 57
    Refund_Over20 = 4


def Ecoline(Money, Greenery, Plant, PlantProd, PlantTag):
    Money = 36
    Plant = 3
    PlantProd = 2
    Greenery = 7
    PlantTag = 1


def Helion(Money, HeatProd, SpaceTag, HeatIsMoney):
    Money = 42
    HeatProd = 3
    SpaceTag = 1
    HeatIsMoney = 1


def Interplanetary_Cinematics(Money, Steel, EventRefund, BuildingTag):
    Money = 30
    Steel = 20
    EventRefund = 2
    BuildingTag = 1

    
def Inventrix(Money, Laxness, ScienceTag, DrawCards):
    Money = 45
    Laxness = 2
    ScienceTag = 1
    DrawCards = 3


def Mining_Guild(Money, Steel, SteelProd, PlacementSP, BuildingTag):
    Money = 30
    Steel = 5
    SteelProd = 1
    PlacementSP = 1
    BuildingTag = 2


def Phoblog(Money, Titanium, TitaniumPrice, SpaceTag):
    Money = 23
    Titanium = 10
    TitaniumPrice = 4
    SpaceTag = 1


def Tharsis_Republic(Money, PlaceCity, CityRefund, CityMoneyProd, BuildingTag):
    Money = 40
    PlaceCity = 1
    CityRefund = 3
    CityMoneyProd = 1
    BuildingTag = 1


def Thorgate(Money, EnergyProd, PowerDiscount, PowerTag):
    Money = 48
    EnergyProd = 1
    PowerDiscount = 3
    PowerTag = 1
 
    
def UMNI(Money, EarthTag, UMNIAction):
    Money = 40
    EarthTag = 1
    UMNIAction = 1


def Saturn_Systems(Money, TitaniumProd, JovianStep, JovianTag):
    Money = 42
    TitaniumProd = 1
    JovianStep = 1
    JovianTag = 1


def Teractor(Money, EarthTag, EarthDiscount):
    Money = 60
    EarthTag = 1
    EarthDiscount = 3


def CorpFunc(A):
    List=[Credicor(Money, Refund_Over20),
          Ecoline(Money, Greenery, Plant, PlantProd, PlantTag),
          Helion(Money, HeatProd, SpaceTag, HeatIsMoney),
          Interplanetary_Cinematics(Money, Steel, EventRefund, BuildingTag),
          Inventrix(Money, Laxness, ScienceTag, DrawCards),
          Mining_Guild(Money, Steel, SteelProd, PlacementSP, BuildingTag),
          Phoblog(Money, Titanium, TitaniumPrice, SpaceTag),
          Tharsis_Republic(Money, PlaceCity, CityRefund, CityMoneyProd, BuildingTag),
          Thorgate(Money, EnergyProd, PowerDiscount, PowerTag),
          UMNI(Money, EarthTag, UMNIAction),
          Saturn_Systems(Money, TitaniumProd, JovianStep, JovianTag),
          Teractor(Money, EarthTag, EarthDiscount)]
    eval(List[A])