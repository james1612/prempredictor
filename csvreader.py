import csv
from result import Result


class CsvReader:
    def __init__(self, csv_file, league):
        self.csv_file = csv_file
        self.league = league

    @property
    def results(self):
        results = []

        f = open(self.csv_file, encoding='windows-1252')
        matches = csv.reader(f)

        # Skip headers
        next(matches)

        for match in matches:
            home_team = match[2]
            away_team = match[3]
            home_goals = int(match[4])
            away_goals = int(match[5])

            home = self.league.get_team(home_team)
            away = self.league.get_team(away_team)

            result = Result(home, away, home_goals, away_goals)
            results.append(result)

        f.close()

        return results
