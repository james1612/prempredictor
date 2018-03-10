
import elocalculator
from csvreader import CsvReader
from league import League

K = 78

THRESHOLD = 0.1
WIN_THRESHOLD = 0.5 + THRESHOLD
LOSE_THRESHOLD = 0.5 - THRESHOLD

# prem_reader = CsvReader('./prem16:17.csv', prem)

historical = [
    "prem93:94.csv",
    "prem94:95.csv",
    "prem95:96.csv",
    "prem96:97.csv",
    "prem97:98.csv",
    "prem98:99.csv",
    "prem99:00.csv",
    "prem00:01.csv",
    "prem01:02.csv",
    "prem02:03.csv",
    "prem03:04.csv",
    "prem04:05.csv",
    "prem05:06.csv",
    "prem06:07.csv",
    "prem07:08.csv",
    "prem08:09.csv",
    "prem09:10.csv",
    "prem10:11.csv",
    "prem11:12.csv",
    "prem12:13.csv",
    "prem13:14.csv",
    "prem14:15.csv",
    "prem15:16.csv",
]

results_to_predict_file = "prem16:17.csv"

for threshold in range(0, 100, 10):
    THRESHOLD = 1.0 * threshold / 100
    WIN_THRESHOLD = 0.5 + THRESHOLD
    LOSE_THRESHOLD = 0.5 - THRESHOLD


    prem = League("Premier League")

    for season in historical:
        prem_reader = CsvReader(season, prem)
        for result in prem_reader.results:
            prem.input_result(result)

    count_guessed_correctly = 0

    results_to_predict = CsvReader(results_to_predict_file, prem).results
    for result in results_to_predict:
        expected_result = elocalculator.expected(result.home, result.away)

        if expected_result > WIN_THRESHOLD:
            expected_result = 'home'
        elif expected_result < LOSE_THRESHOLD:
            expected_result = 'away'
        else:
            expected_result = 'draw'

        guessed_correctly = expected_result == result.get_result()

        if guessed_correctly:
            count_guessed_correctly += 1

        elocalculator.update_result(result, k=K)

    print(threshold, (1.0 * count_guessed_correctly) / len(results_to_predict))
