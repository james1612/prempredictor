from team import Team
from league import League


chelsea = Team("Chelsea")
arsenal = Team("Arsenal")

arsenal.addWin()
arsenal.addDraw()
arsenal.addDraw()

chelsea.addWin()
chelsea.addLoss()


prem = League("Premier League")

prem.addTeam(arsenal)
prem.addTeam(chelsea)

prem.displayLeague()

prem.inputResult(chelsea,arsenal,"win")


print("----")
prem.displayLeague()

