from dataclasses import dataclass, asdict
@dataclass
class Movie:
    movie_id:int
    title:str
    genre:str
    duration_minutes:int
    age_rating:int=0
    def to_dict(self): return asdict(self)
