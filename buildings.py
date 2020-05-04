import player
import calendar

build_list = []
build_queue = []


class Buildings:

    def __init__(self, name, buildtype, buildtime, workers, built, build_exp, seasonal):
        self.name = name
        self.buildtype = buildtype
        self.buildtime = buildtime  # Time in weeks to complete build
        self.workers = workers  # How many permenant workers required to function
        self.built = built  # How many you have built
        self.build_exp = build_exp  # XP gained for building
        self.seasonal = seasonal  # production boost? idk

        build_list.append(self)


hut = Buildings("Hut", "Dwelling", 1, 0, 4, 3, False)

clay_house = Buildings("House", "Dwelling", 2, 0, 0, 8, False)

grain_field = Buildings("Grain Field", "Farm", 2, 2, 0, 13, False)

total_buildings = 0
farms_built = 0

for building in build_list:
    total_buildings += building.built
    if building.buildtype == "Farm":
        farms_built += building.built


def construct(building):
    if player.Player.population > (player.Player.employed + building.workers):
        build_queue.append(building)
        setattr(building, "queued_num", calendar.Calendar.turn)
        print(f"Added {building.name} to queue...")
    else:
        pass
