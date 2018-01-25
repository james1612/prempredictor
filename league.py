from team import Team

class League:
    'Common class for a football league'

    teams = []
    results = []

    def __init__(self, name):
        self.name = name

    def add_team(self, team):
        self.teams.append(team)

    def remove_team(self, team):
        self.teams.remove(team)

    def input_result(self, result):
        self.results.append(result)

    def remove_result(self, result):
        self.results.remove(result)

    def display_league(self):
        for team in self.teams:
            team.calculate_points()
            print(team.name, ": Points- ", team.points, " Wins -", team.wins, " Draws -", team.draws, " Losses -", team.losses)



    def sortLeague(self):
        self.teams = sorted(self.teams, key=lambda team: team.points, reverse = True)


