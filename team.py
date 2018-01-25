class Team:
    'Common class for football teams'

    played = 0
    wins = 0
    losses = 0
    draws = 0
    points = 0

    def get_wins(self):
        return self.wins

    def set_wins(self, wins):
        self.wins = wins

    def __init__(self, name, league, elo_score = 1200):
        self.name = name
        self.league = league
        self.elo_score = elo_score

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

    # def calculatePoints(self):
    #     self.points =  (3*self.wins) + self.draws

    def calculate_points(self):
        self.calculateDraws()
        self.calculateWins()
        self.calculateLosses()
        self.points =  (3*self.wins) + self.draws


    def display_points(self):
        self.calculatePoints()
        print(self.points)

    def last5results(self):
        return self.totalResults[-5:]

    def calculateWins(self):
        for result in self.league.results:
            if result.home == self.name and result.get_result() == "home":
                self.wins += 1
            if result.away == self.name and result.get_result == "away":
                self.wins += 1

    def calculateLosses(self):
        for result in self.league.results:
            if result.home == self.name and result.get_result == "away":
                self.losses += 1
            if result.away == self.name and result.get_result == "home":
                self.losses += 1

    def calculateDraws(self):
        for result in self.league.results:
            if result.home == self.name and result.get_result == "draw":
                self.draws += 1
            if result.away == self.name and result.get_result == "draw":
                self.draws += 1

