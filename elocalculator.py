

def expected(team_a, team_b):
    return 1.0 / (1 + 10 ** ((team_b.elo_score - team_a.elo_score) / 400))


def update_result(result, k=32):
    team_a = result.home
    team_b = result.away

    e = expected(team_a, team_b)

    result = result.get_result()
    number_result = 0
    if result == 'home':
        number_result = 1
    if result == 'away':
        number_result = 0
    if result == 'draw':
        number_result = 0.5

    team_a.elo_score = team_a.elo_score + k * (number_result - e)
    team_b.elo_score = team_b.elo_score - k * (number_result - e)
