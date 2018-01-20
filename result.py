from team import Team


class Result:
    'A common class for a football result'

    result = "tbc"

    def __init__(self, home, away, home_goals, away_goals):
        self.home = home
        self.away = away
        self.home_goals = home_goals
        self.away_goals = away_goals


    def calulatesResult(self):
        if self.home_goals > self.away_goals:
            self.result = "home win"
        if self.away_goals > self.home_goals:
            self.result = "away"
        else:
            self.result = "draw"

