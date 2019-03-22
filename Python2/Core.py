SteelPrice = 2
TitaniumPrice = 3

Generation = 1
MaxGeneration = 14

OceanMax = 9
Oceans = 0

TempMax = 8
Temperature = -30


def SpendMoney(Money, Cost, A):
    if Money < Cost:
        print "Not enough money."
        A = False
    if A:
        Money -= Cost


def SpendSteel(Steel, SteelPrice, Cost, A):
    if Steel > 0:
        N = input("Spend # steel? (/"+Steel+";"+SteelPrice+" each)")
    else:
        N = 0
    if N > Steel:
        A = False
        print "Not enough Steel."
    elif A:
        Cost = max(Cost-N*SteelPrice, 0)
        Steel -= N


def SpendTitanium(Titanium, TitaniumPrice, Cost, A):
    if Titanium > 0:
        N = input("Spend # Titanium? (/"+Titanium+";"+TitaniumPrice+" each)")
    else:
        N = 0
    if N > Titanium:
        A = False
        print "Not enough Titanium."
    elif A:
        Cost = max(Cost-N*TitaniumPrice, 0)
        Titanium -= N


def SpendHeat(Heat, Cost, A):
    if Heat > 0:
        N = input("Spend # Heat (/"+Heat+"; 1 each)")
    if N > Heat:
        A = False
        print "Not enough Heat."
    elif A:
        Cost = max(Cost-N*Heat, 0)
        Heat -= N


def BuyThing(ThingName, Titanium, Steel, Money, Heat, SpendHeat, Slaves):
    Cost = ThingName[0]
    if Slaves == 1:
        Cost -= 8
        Slaves = 0
    A = True
    if 'Space' in ThingName[-1]:
        SpendTitanium(Titanium, TitaniumPrice, Cost, A)
    if 'Building' in ThingName[-1]:
        SpendSteel(Steel, SteelPrice, Cost, A)
    if SpendHeat == 1:
        SpendHeat(Heat, Cost, A)
    SpendMoney(Money, Cost, A)
    if A:
        for B in ThingName[1]:
            eval(B)
    else:
        print "Something went wrong."


def Generation(Money, TR, MoneyProd, Titanium, TitaniumProd, Steel, SteelProd, Plant, PlantProd, Energy, EnergyProd, Heat, HeatProd):
    Money += TR + MoneyProd
    Titanium += TitaniumProd
    Steel += SteelProd
    Plant += PlantProd
    Heat += Energy + HeatProd
    Energy = EnergyProd


def TempCheck(Temperature, T, M, A, Leeway):
    if M == -1:
        if Temperature+Leeway > T:
            print "Too hot."
            A = False
    else:
        if Temperature-Leeway < T:
            print "Too cold."
            A = False


def OceanCheck(Ocean, O, M, A, Leeway):
    if M == -1:
        if Ocean+Leeway > O:
            print "Too many oceans."
            A = False
    else:
        if Ocean-Leeway < O:
            print "Too few oceans."
            A = False


def OxCheck(Oxygen, O2, M, A, Leeway):
    if M == -1:
        if Oxygen+Leeway > O2:
            print "Too much Oxygen."
            A = False
    else:
        if Oxygen-Leeway < O2:
            print "Too little Oxygen."
            A = False
            
            
def CityCheck(CityCount, N, A):
    if CityCount < N:
        print "Not enough cities."
        A = False