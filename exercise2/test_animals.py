#!/usr/bin/env python3

### alt 1

import animals

m = animals.Mammals()
m.printMembers()

b = animals.Birds()
b.printMembers()

## after restructuring
harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()


### alt 2
'''
from animals import Mammals
from animals import Birds

myMammal = Mammals()
myMammal.printMembers()

myBird = Birds()
myBird.printMembers()
'''