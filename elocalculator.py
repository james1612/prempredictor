from team import Team



class Elo_calculator:

    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b


    def expected(self):
        return 1 / (1 + 10 ** ((self.team_b.elo_score - self.team_a.elo_score) / 400))



    def actual_scores(self, expected, result, k=32):
        result = result.get_result()
        number_result = 0
        if result == 'home':
            number_result = 1
        if result == 'away':
            number_result = 0
        if result == 'draw':
            number_result = 0.5

        self.team_a.elo_score = self.team_a.elo_score + k * (number_result - expected)
        self.team_b.elo_score = self.team_b.elo_score + k * (number_result - expected)

        return self.team_a


    def get_team_a_elo(self):
        return self.team_a.elo_score

    def get_team_b_elo(self):
        return self.team_b.elo_score

