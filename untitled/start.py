import elocalculator
from csvreader import CsvReader
from league import League

K = 64

THRESHOLD = 0.05
WIN_THRESHOLD = 0.5 + THRESHOLD
LOSE_THRESHOLD = 0.5 - THRESHOLD

prem = League("Premier League")
prem_reader = CsvReader('./prem16:17.csv', prem)

for result in prem_reader.results:
    prem.input_result(result)

count_guessed_correctly = 0

for result in prem.results:
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

print("Guessed {correct}/{total} correctly!".format(
    correct=count_guessed_correctly,
    total=len(prem.results)
))



