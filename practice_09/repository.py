class MovieRepository:
    def __init__(self): self.items={}
    def add(self,movie): self.items[movie.movie_id]=movie
    def get(self,movie_id): return self.items.get(int(movie_id))
    def get_all(self): return list(self.items.values())
    def update(self,movie_id,**fields):
        movie=self.get(movie_id)
        if movie is None: return None
        for key,value in fields.items():
            if value is not None and value != '' and key in {"title","genre","duration_minutes","age_rating"}: setattr(movie,key,value)
        return movie
    def delete(self,movie_id): return self.items.pop(int(movie_id),None)
