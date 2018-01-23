import csv
from result import Result
from team import Team

class Csv_reader:
    # file = csv.reader(open('prem16/17.csv'))
    # next(file)

    # for match in file:
    #     home = match[2]
    #     away = match[3]
    #     home_goals = int(match[4])
    #     away_goals = int(match[5])


    def __init__(self, csv_file, league):
        self.csv_file = csv_file
        self.league = league

    file = csv.reader(open('self.csv_file'))
    next(file)

    list_of_teams = []
    list_of_results = []


    def reads_file(self, file):
        for match in file:
            home_team = match[2]
            away_team = match[3]
            home_goals = int(match[4])
            away_goals = int(match[5])

            # if home_team not in list_of_teams:
            #     home = Team(home_team, self.league)
            #     list_of_teams.append(home)
            # if away_team not in list_of_teams:
            #     away = Team(away_team, self.league)
            #     list_of_teams.append(away)

            home = Team(home_team, self.league)
            away = Team(away_team, self.league)



            result = Result(home, away, home_goals, away_goals)
            self.list_of_results.append(result)


