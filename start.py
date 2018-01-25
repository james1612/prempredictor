from team import Team
from league import League
from result import Result
from elocalculator import Elo_calculator

prem = League("Premier League")

chelsea = Team("Chelsea", prem, 1600)
arsenal = Team("Arsenal", prem)

prem.addTeam(chelsea)
prem.addTeam(arsenal)

# elo_calculator = Elo_calculator(chelsea, arsenal)

result = Result(chelsea, arsenal, 1, 0)

# exp1 = elo_calculator.expected()
#
# print(exp1)
#
# elo_calculator.actual_scores(exp1, result)
#
# print(elo_calculator.get_team_a_elo())
#
# print(elo_calculator.get_team_b_elo())


chelsea.wins += 345

print(chelsea.wins)


prem.inputResult(result)
