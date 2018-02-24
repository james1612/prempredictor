class Team:
    'Common class for football teams'

    def __init__(self, name, league, elo_score = 1200, glicko_score = 1500):
        self.name = name
        self.league = league
        self.elo_score = elo_score
        self.glicko_score = glicko_score

    def __repr__(self):
        return "<Team '{name}'>".format(name=self.name)

    @property
    def points(self):
        return (3 * self.wins) + self.draws

    def display_points(self):
        print(self.points)

    def last5results(self):
        return self.totalResults[-5:]

    @property
    def wins(self):
        wins = 0
        for result in self.league.results:
            if result.home == self and result.get_result() == "home":
                wins += 1
            if result.away == self and result.get_result() == "away":
                wins += 1

        return wins

    @property
    def losses(self):
        losses = 0
        for result in self.league.results:
            if result.home == self and result.get_result() == "away":
                losses += 1
            if result.away == self and result.get_result() == "home":
                losses += 1

        return losses

    @property
    def draws(self):
        draws = 0
        for result in self.league.results:
            if result.home == self and result.get_result() == "draw":
                draws += 1
            if result.away == self and result.get_result() == "draw":
                draws += 1

        return draws
