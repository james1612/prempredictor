from team import Team

class League:
    'Common class for a football league'

    teams = []
    results = []

    def __init__(self, name):
        self.name = name

    def addTeam(self, team):
        self.teams.append(team)

    def removeTeam(self, team):
        self.teams.remove(team)

    # def inputResult(self, team1, team2, result):
    #     if (result == "win"):
    #         team1.addWin()
    #         team2.addLoss()
    #     if (result == "draw"):
    #         team1.addDraw()
    #         team2.addDraw()
    #     if (result == "loss"):
    #         team1.addLoss()
    #         team2.addWin()

    def inputResult(self, result):
        self.results.append(result)

    def removeResult(self, result):
        self.results.remove(result)


    # def displayLeague(self):
    #     for team in self.teams:
    #         team.calulatePoints()
    #         print(team.name, "- Points: ", team.points, " Wins -", team.wins, " Draws -", team.draws, " Losses -", team.losses)




    def sortLeague(self):
        self.teams = sorted(self.teams, key=lambda team: team.points, reverse = True)
