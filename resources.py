res_list = []


class Resources:

    def __init__(self, name, rectype, seasonal, stored):
        self.name = name
        self.rectype = rectype
        self.seasonal = seasonal
        self.stored = stored

        res_list.append(self)


timber = Resources("Timber", "Wood", False, 5)
cedar = Resources("Cedarwood", "Wood", False, 0)
stone = Resources("Stone", "Construct", False, 0)
clay = Resources("Clay", "Construct", False, 10)

copper_ore = Resources("Copper Ore", "Ore", False, 0)
tin_ore = Resources("Tin Ore", "Ore", False, 0)
copper_ingots = Resources("Copper Ingots", "Metal", False, 0)
tin_ingots = Resources("Tin Ingots", "Metal", False, 0)
bronze_ingots = Resources("Bronze Ingots", "Metal", False, 0)

grain = Resources("Grain", "Food", True, 5)
meat = Resources("Meat", "Food", False, 0)
fruit = Resources("Fruit", "Food", True, 0)
beer = Resources("Beer", "Food", False, 0)
bread = Resources("Bread", "Food", False, 0)

leather = Resources("Leather", "Clothing", False, 0)
wool = Resources("Wool", "Clothing", False, 0)
cloth = Resources("Cloth", "Clothing", False, 0)
garments = Resources("Garments", "Clothing", False, 0)

sheep = Resources("Sheep", "Livestock", True, 0)
donkey = Resources("Donkey", "Livestock", False, 0)
