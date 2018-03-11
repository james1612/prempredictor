import randompredictor
from csvreader import CsvReader
from league import League
from result import Result


csv = "prem16:17.csv"
csv1 = "prem16:17.csv"


original_prem = League("normal")
random_prem = League("random")

original_prem_reader = CsvReader(csv, original_prem)

random_prem_reader = CsvReader(csv1, random_prem)

for result in original_prem_reader.results:
    original_prem.input_result(result)

for result in random_prem_reader.results:
    result.home_goals=0
    result.away_goals=0
    random_prem.input_result(result)

def read_csv(csv_file, league):
    csv = csv_file
    reader = CsvReader(csv,league)
    return reader


randompredictor.predicts_league(random_prem)

def compares_leagues():

    results_correct = 0

    for result in random_prem.results:
        for result1 in original_prem.results:
            if result.home.name == result1.home.name and result.away.name == result1.away.name:
                if result.get_result() == result1.get_result():
                    results_correct += 1





# original_prem.display_league()

# print("-------------------------------------------------------------")

# random_prem.display_league()

print(compares_leagues())