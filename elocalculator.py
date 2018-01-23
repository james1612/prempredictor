from team import Team


class Elo_calculator:

    def __init__(self, home, away):
        self.home = home
        self.away = away


    def expected_score_home(self):
        ea = 1 / (1 + 10**((self.away.elo_score - self.home.elo_score)/400))
        return ea

    def expected_score_away(self):
        eb = 1 / (1 + 10**((self.home.elo_score - self.away.elo_score)/400))
        return eb

    def actual_scores(self, expected, result, k=32):
        result = result.get_result()
        if result == 'home':
            number_result = 1
        if result == 'away':
            number_result = 0
        if result == 'draw':
            number_result = 0.5

        return self.home.elo_score + k * (number_result - expected)








