import random


class Product():

    def __init__(self, name=str, price=10, weight=20, flammability=0.5, identifier=random.randint(100000, 9999999)):
            self.name = name
            self.price = price
            self.weight = weight
            self.flammability = flammability
            self.identifier = identifier

    def stealability(self):
        steal_rating = self.price/self.weight
        if steal_rating < 0.5:
            return "Not so stealable..."
        if steal_rating >= 0.5:
            return "Kinda stealable."
        if steal_rating < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"


    def explode(self):
        flame_rating = self.flammability*self.weight
        if flame_rating < 10:
            return "...fizzle."
        if flame_rating >= 10:
            return "...boom!"
        if flame_rating < 50:
            return "...boom!"
        else:
            return "...BABOOM!"


class BoxingGlove(Product):

    def __init__(self, name=str, price=10, weight=10, flammability=0.5, identifier=random.randint(100000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        return "it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        if self.weight >= 5:
            return "Hey that hurt!"
        if self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"

prod = Product('A Cool Toy')
prod.weight
prod.price
prod.flammability
prod.identifier
print(prod.stealability())
print(prod.explode())
glove = BoxingGlove("Punchy the Third")
glove.weight
glove.punch()
glove.explode()
