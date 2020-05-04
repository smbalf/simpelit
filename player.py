import resources as r
import buildings as b


class Player:
    name = ""
    population = 10
    employed = 0
    population_max = 12
    prestige = int((population / 1000) + (b.total_buildings / 50) + (r.total_resources / 1000))
    experience = 0
    growth = 0

    @classmethod
    def growth_factor(cls):
        satisfaction = round(r.grain.stored / Player.population, 2)
        if satisfaction >= 5:
            Player.growth = 0.05  # pop boom!
        elif 0.7 <= satisfaction < 5:
            Player.growth = 0.01  # pop steady growth!
        elif 0.5 <= satisfaction < 0.7:
            Player.growth = -0.05
        else:
            Player.growth = -0.1  # pop decline!

    @classmethod
    def pop_change(cls):
        if Player.population < Player.population_max:
            Player.population += (Player.growth * Player.population)
        elif Player.population > Player.population_max:
            Player.population = Player.population_max
        else:
            pass


