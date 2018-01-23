from team import Team


class Result:
    'A common class for a football result'


    def __init__(self, home, away, home_goals, away_goals):
        self.home = home
        self.away = away
        self.home_goals = home_goals
        self.away_goals = away_goals


    def calulates_result(self):
        if self.home_goals > self.away_goals:
            return "home"
        if self.away_goals > self.home_goals:
            return "away"
        else:
            return "draw"


    def get_result(self):
        return self.calulates_result()
