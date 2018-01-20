import csv
from result import Result


# file = csv.reader(open('prem16/17.csv'))
# next(file)

# for match in file:
#     home = match[2]
#     away = match[3]
#     home_goals = int(match[4])
#     away_goals = int(match[5])


def __init__(self, csv_file):
    self.csv_file = csv_file

file = csv.reader(open('self.csv_file'))
next(file)


list_of_results = []


def reads_file():
    for match in file:
        home = match[2]
        away = match[3]
        home_goals = int(match[4])
        away_goals = int(match[5])
        result = Result(home, away, home_goals, away_goals)
        list_of_results.append(result)
