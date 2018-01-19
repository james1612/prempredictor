from team import Team
from league import League
from result import Result

prem = League("Premier League")


chelsea = Team("Chelsea", prem)
arsenal = Team("Arsenal", prem)

result = Result(chelsea, arsenal, 2, 1)


prem.addTeam(chelsea)
prem.addTeam(arsenal)

# prem.displayLeague()


prem.inputResult(result)

print("----")


prem.sortLeague()
# prem.displayLeague()


chelsea.display_points()