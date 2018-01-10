from team import Team
from league import League


chelsea = Team("Chelsea")
arsenal = Team("Arsenal")
everton = Team("Everton")
burnley = Team("Burnley")

arsenal.addWin()
arsenal.addDraw()
arsenal.addDraw()

chelsea.addWin()
chelsea.addLoss()

everton.addDraw()
everton.addDraw()
everton.addLoss()

burnley.addWin()
burnley.addLoss()


prem = League("Premier League")

prem.addTeam(arsenal)
prem.addTeam(chelsea)
prem.addTeam(everton)
prem.addTeam(burnley)

prem.displayLeague()

# prem.inputResult(chelsea,arsenal,"win")

print("----")


prem.sortLeague()
prem.displayLeague()


