temperature = -30
temperatureMax = 8

oceans = 0
oceansMax = 9

oxygen = 0
oxygenMax = 14


def TempRaise(N, temperature):
    i = 0
    while i < N:
        if temperature < temperatureMax:
            temperature += 2
            TR += 1
            if temperature == -24 or temperature == -20:
                global(heatProd) += 1
            elif temperature == 0:
                OceanRaise(1,oceans)
        i += 1

def OceanRaise(N, oceans):
    i = 0
    while i < N:
        if oceans < oceansMax:
            oceans += 1
            TR += 1