from team import Team


class Result:
    'A common class for a football result'

    result = "tbc"

    def __init__(self, home, away, scored, conceded):
        self.home = home
        self.away = away
        self.scored = scored
        self.conceded = conceded


    def calulatesResult(self):
        if self.scored > self.conceded:
            self.result = "home win"
        if self.conceded > self.scored:
            self.result = "away"
        else:
            self.result = "draw"

