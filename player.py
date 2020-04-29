import resources as r
import buildings as b


class Player:
    name = ""
    population = 20
    population_max = (b.hut.built * 3) + (b.clay_house.built * 5)
    prestige = 0
    satisfaction = (r.grain.stored + r.meat.stored + r.fruit.stored + r.bread.stored) / population
    growth = 0

    #   prestige = population size + number of buildings + number of resources?
    #   satisfaction = (food + staples) / population
    #   above 2 = growth
    #   below 1.5 = no growth
    #   below 1 = leaving settlement?
