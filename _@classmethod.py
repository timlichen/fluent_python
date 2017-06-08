class Brewery(object):
    def __init__(self):
        self.ingredients = "hops"

    def give_ingredients(self):
        return self.ingredients

class Beer(object):
    def __init__(self, type):
        self.size = "1 pint"
        self.type = type
    
    @classmethod
    def set_type(cls, brewery):
        new_object = cls(brewery.give_ingredients())
        return new_object


beer1 = Beer('apple')

brew_house = Brewery()

beer2 = beer1.set_type(brew_house);

print beer2.type
