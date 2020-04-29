res_list = []


class Resources:

    def __init__(self, name, rectype, stored):
        self.name = name
        self.rectype = rectype
        self.stored = stored

        res_list.append(self)


timber = Resources("Timber", "Wood", 5)
cedar = Resources("Cedarwood", "Wood", 0)
stone = Resources("Stone", "Construct", 0)
clay = Resources("Clay", "Construct", 10)

copper_ore = Resources("Copper Ore", "Ore", 0)
tin_ore = Resources("Tin Ore", "Ore", 0)

copper_ingots = Resources("Copper Ingots", "Metal", 0)
tin_ingots = Resources("Tin Ingots", "Metal", 0)
bronze_ingots = Resources("Bronze Ingots", "Metal", 0)

grain = Resources("Grain", "Staple", 5)
salt = Resources("Salt", "Staple", 0)

meat = Resources("Meat", "Food", 0)
fruit = Resources("Fruit", "Food", 0)
beer = Resources("Beer", "Food", 0)
bread = Resources("Bread", "Food", 0)

leather = Resources("Leather", "Clothing", 0)
wool = Resources("Wool", "Clothing", 0)
cloth = Resources("Cloth", "Clothing", 0)
garments = Resources("Garments", "Clothing", 0)

sheep = Resources("Sheep", "Livestock", 0)
donkeys = Resources("Donkeys", "Livestock", 0)
