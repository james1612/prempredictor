from team import Team


class Result:
    'A common class for a football result'

    def __init__(self, opposition, scored, conceded):
        self.opposition = opposition
        self.scored = scored
        self.conceded = conceded

    def calulatesResult(self):
        if self.scored > self.conceded:
            return "win"
        if self.conceded > self.scored:
            return "loss"
        else:
            return "draw"
