class Calendar:
    week = 0
    year = 0

    winter = False
    spring = False
    summer = False
    autumn = False

    season_list = ("WINTER", "SPRING", "SUMMER", "AUTUMN")
    curr_season = season_list[0]

    @classmethod
    def next_week(cls):
        if Calendar.week < 52:
            Calendar.week += 1

        elif Calendar.week == 52:
            Calendar.year += 1
            Calendar.week = 0

    @classmethod
    def reset_seasons(cls):
        Calendar.winter = False
        Calendar.spring = False
        Calendar.summer = False
        Calendar.autumn = False

    @classmethod
    def season(cls):
        if Calendar.week > 47 or Calendar.week < 8:
            Calendar.reset_seasons()
            Calendar.winter = True
            Calendar.curr_season = Calendar.season_list[0]

        elif 8 < Calendar.week < 21:
            Calendar.reset_seasons()
            Calendar.spring = True
            Calendar.curr_season = Calendar.season_list[1]

        elif 21 < Calendar.week < 34:
            Calendar.reset_seasons()
            Calendar.summer = True
            Calendar.curr_season = Calendar.season_list[2]

        elif 34 < Calendar.week < 47:
            Calendar.reset_seasons()
            Calendar.autumn = True
            Calendar.curr_season = Calendar.season_list[3]
