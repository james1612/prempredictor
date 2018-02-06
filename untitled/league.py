from team import Team


class League:
    'Common class for a football league'

    teams = []
    results = []

    def __init__(self, name):
        self.name = name

    def get_team(self, name):
        '''
        Finds existing team with name, or creates it if it can't be found
        '''

        for team in self.teams:
            if team.name == name:
                return team

        # If we get here, the team didn't exist, we should create it
        team = Team(name, self)
        self.teams.append(team)
        return team

    def input_result(self, result):
        self.results.append(result)

    def remove_result(self, result):
        self.results.remove(result)

    def display_league(self):
        for team in self.sortedTeams():
            print("{teamName}: Points {points}, Wins {wins}, Draws {draws}, Losses {losses}".format(
                teamName=team.name,
                points=team.points,
                wins=team.wins,
                draws=team.draws,
                losses=team.losses,
            ))

    def sortedTeams(self):
        return sorted(self.teams, key=lambda team: team.points, reverse=True)
