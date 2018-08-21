#  Game

from numpy import shuffle

import Cards
import Core
import Corps
import World

Generation = 0

Deck = shuffle(Cards.Deck)

i = 0
while i < 3:
    