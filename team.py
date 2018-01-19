class Team:
    'Common class for football teams'

    played = 0
    wins = 0
    losses = 0
    draws = 0
    points = 0

    eloScore = 1200

    def get_wins(self):
        return self.wins

    def set_wins(self, wins):
        self.wins = wins



    def __init__(self, name, league):
        self.name = name
        self.league = league

    # def addWin(self):
    #     self.played +=1
    #     self.wins += 1
    #
    # def addDraw(self):
    #     self.played +=1
    #     self.draws += 1
    #
    # def addLoss(self):
    #     self.played +=1
    #     self.losses += 1

    def calulatePoints(self):
        self.points =  (3*self.wins) + self.draws

    def last5results(self):
        return self.totalResults[-5:]

    def calculateWins(self):
        for result in self.league.results:
            if result.home == self.name and result.result == "home win":
                self.wins += 1
            if result.away == self.name and result.result == "away win":
                self.wins += 1

    def calculateLosses(self):
        for result in self.league.results:
            if result.home == self.name and result.result == "away win":
                self.losses += 1
            if result.away == self.name and result.result == "home win":
                self.losses += 1

    def calculateDraws(self):
        for result in self.league.results:
            if result.home == self.name and result.result == "draw":
                self.draws += 1
            if result.away == self.name and result.result == "draw":
                self.draws += 1


    def display_points(self):
        self.calulatePoints()
        print(self.points)