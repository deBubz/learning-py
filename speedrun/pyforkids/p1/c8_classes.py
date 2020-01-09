# class examples (inheritance?)

class Things:
    pass


# children class of Things
class Inanimate(Things):
    pass

class Animate(Things):
    pass


# children of Inanimate
class Sidewalks(Inanimate):
    pass

# children of Animals
class Animals(Animate):
    def breathe(self):
        pass
    def move(self):
        pass
    def eat_food(self):
        pass
    pass

class Mammals(Animals):
    def feed_young(self):
        pass
    pass

class Giraffes(Mammals):
    def __init__(self, spots):         # constructor
        self.firaffe_spots = spots

    def find_food(self):
        self.move()
        print("ive found food")
        self.eat_food():
    def eat_leaves(self):
        pass
    pass

# The Giraffes class ultimately can use functions from 
# Things-Animate-Animals-Mammals

# Function calling functions