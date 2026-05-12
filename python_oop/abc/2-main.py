#!/usr/bin/env python3
from flyingfish import Fish, Bird, FlyingFish

print("=== OFFICIAL TESTS ===")
flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

print("=== CUSTOM TESTS ===")
myFish = Fish()
myBird = Bird()
myMix = FlyingFish()

# Method provided from object class
# Warning: method provided on the CLASS itself
#   NOT the instances
# myFish.mro()
# myMix.mro()
print(Bird.mro())
print(FlyingFish.mro())
