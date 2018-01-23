from team import Team
from league import League
from result import Result
from elocalculator import Elo_calculator

prem = League("Premier League")

chelsea = Team("Chelsea", prem)
arsenal = Team("Arsenal", prem)

prem.addTeam(chelsea)
prem.addTeam(arsenal)

elo_calculator = Elo_calculator(chelsea, arsenal)

result = Result(chelsea, arsenal, 4, 1)


exp1 = elo_calculator.expected_score_away()

exp2 = elo_calculator.expected_score_home()

print(exp1)

print(elo_calculator.actual_scores(exp1, result))


