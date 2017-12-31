class Team:
    'Common class for football teams'

    played = 0
    wins = 0
    losses = 0
    draws = 0
    points = 0

    totalResults = []
    last5Results = []


    def __init__(self, name):
        self.name = name


    def addWin(self):
        self.played +=1
        self.wins += 1

    def addDraw(self):
        self.played +=1
        self.draws += 1

    def addLoss(self):
        self.played +=1
        self.losses += 1

    def calulatePoints(self):
        self.points =  (3*self.wins) + self.draws



