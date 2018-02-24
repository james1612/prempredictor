
def calculates_fide(team_a, team_b, result):
    if result.get_result() == 'win':
        number_result = 400
    if result.get_result() == 'draw':
        number_result = -400
    if result.get_result() == 'loss':
        number_result = 400



