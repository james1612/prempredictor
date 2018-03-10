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


# randompredictor.predicts_league(random_prem)

# def compares_leagues():
#     counter = 0
#     for result in random_prem.results:
#         for result in original_prem.results:
#             counter = 0
#             if result.get_result() == result.get_result():
#                 counter += 1
#     return counter


original_prem.display_league()

print("-------------------------------------------------------------")

# random_prem.display_league()



