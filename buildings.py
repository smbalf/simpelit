build_list = []


class Buildings:

    def __init__(self, name, buildtype, buildtime, builders, workers, built, build_exp, seasonal):
        self.name = name
        self.buildtype = buildtype
        self.buildtime = buildtime
        self.builders = builders
        self.workers = workers
        self.built = built
        self.build_exp = build_exp
        self.seasonal = seasonal

        build_list.append(self)


hut = Buildings("Hut", "Dwelling", 1, 1, 0, False, 3, False)
clay_house = Buildings("Clay House", "Dwelling", 2, 2, 0, False, 8, False)
grain_patch = Buildings("Grain Patch", "Farm", 1, 1, 1, False, 5, False)
grain_field = Buildings("Grain Field", "Farm", 1, 2, 2, False, 13, False)
