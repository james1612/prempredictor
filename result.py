from team import Team


class Result:
    'A common class for a football result'

    result = "tbc"

    def __init__(self, opposition, scored, conceded):
        self.opposition = opposition
        self.scored = scored
        self.conceded = conceded

    def calulatesResult(self):
        if self.scored > self.conceded:
            self.result = "win"
        if self.conceded > self.scored:
            self.result = "loss"
        else:
            self.result = "draw"
