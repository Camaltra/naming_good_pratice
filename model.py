class Movie:
    def __init__(
        self,
        title: str,
        director: str,
        release_year_date: int,
        type=None,
        schedules: list | None = None,
        description: str | None = None,
        stars: str | None = None,
    ):
        if not schedules:
            schedules = []
        self.title = title
        self.director = director
        self.release_year_date = release_year_date
        self.schedules = schedules
        self.description = description
        self.type = type
        self.stars = stars

    def display_infos(self):
        print(
            f"Title: {self.title} ; Current cinema schedules: {self.schedules} ; Notation: {self.stars if self.stars else 'Unknow'} ; Description: {self.description if self.description else 'No description found'}"
        )

def fake_query():
    m1 = Movie("Mission Impossible", "Bruce Geller", 1996, schedules=["11h30", "20h30"], type="Action", stars=4)
    m2 = Movie("Cars", "John Lasseter", 2006, schedules=["14h30", "17h30"], type="Animation", stars=5)
    m3 = Movie("Star Wars, épisode III : La Revanche des Sith", "George Lucas", 2005, description="This is the best film lmao", type="Action", stars=2)
    m4 = Movie("Intouchable", "Olivier Nakache", 2011, schedules=["19h30"], type="Drame")
    m5 = Movie("Moonfall", "Roland Emmerich", 2022, schedules=["13h30"], type="Action")
    m6 = Movie("Eternals", "Chloé Zhao", 2021, type="Action", stars=3)

    return [m1, m2, m3, m4, m5, m6]

def get_movies_from_db():
    # session.query(Movie).all()
    return fake_query()