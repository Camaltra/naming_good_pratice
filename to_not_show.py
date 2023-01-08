from model import Atw

def fake_query():
    m1 = Atw("Mission Impossible", "Bruce Geller", 1996, schle=["11h30", "20h30"], type="Action", strs=4)
    m2 = Atw("Cars", "John Lasseter", 2006, schle=["14h30", "17h30"], type="Animation", strs=5)
    m3 = Atw("Star Wars, épisode III : La Revanche des Sith", "George Lucas", 2005, dsc="This is the best film lmao", type="Action", strs=2)
    m4 = Atw("Intouchable", "Olivier Nakache", 2011, schle=["19h30"], type="Drame")
    m5 = Atw("Moonfall", "Roland Emmerich", 2022, schle=["13h30"], type="Action")
    m6 = Atw("Eternals", "Chloé Zhao", 2021, type="Action", strs=3)

    return [m1, m2, m3, m4, m5, m6]