import random

def generates_random_result():
    result = random.randint(1,3)
    if (result == 1):
        return "home"
    if (result == 2):
        return "draw"
    if (result == 3):
        return "away"

def predicts_league(league):
    for result in league.results:
        generates_random_result()
        if generates_random_result() == "home":
            result.home_goals = 1
            result.away_goals = 0
        if generates_random_result() == "draw":
            result.home_goals = 1
            result.away_goals = 1
        if generates_random_result() == "away":
            result.home_goals = 0
            result.away_goals = 1

