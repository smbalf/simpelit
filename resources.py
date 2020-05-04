res_list = []


class Resources:

    def __init__(self, name, restype, stored):
        self.name = name
        self.restype = restype
        self.stored = stored

        res_list.append(self)


timber = Resources("Timber", "Wood", 5)

clay = Resources("Clay", "Construct", 10)

grain = Resources("Grain", "Food", 12)

total_resources = 0
for resources in res_list:
    total_resources += resources.stored

