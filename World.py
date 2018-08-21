import matplotlib.pyplot as plt

X = [2, 3, 4, 5, 6, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 1, 2, 3, 4, 5, 6, 7, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 1, 2, 3, 4, 5, 6, 7, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 2, 3, 4, 5, 6]
Y = [-4, -4, -4, -4, -4, -3, -3, -3, -3, -3, -3, -2, -2, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]
OceanTilesX = [3, 5, 6, 6.5, 3, 4, 5, 5.5, 6.5, 7.5, 6]
OceanTilesY = [4, 4, 4, 3, 0, 0, 0, -1, -1, -1, -4]
NoctisX = 2
NoctisY = 0

World = []

plt.ioff()

i = 1
while i < len(X) + 1:
    World.append([X[i - 1], Y[i - 1], i])
    i += 1

i = 1
while i<len(OceanTilesX):
    OceanTiles.append([OceanTilesX[i - 1], OceanTilesY[i - 1])




plt.plot(X,Y,'ro')
plt.plot(OceanTilesX,OceanTilesY,'bo')
plt.plot(NoctisX,NoctisY,'yo')
plt.show()

GreeneryX = []
GreeneryY = []

CityX = []
CityY = []

