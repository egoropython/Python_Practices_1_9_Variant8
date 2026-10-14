from models import Movie
class MovieService:
    def __init__(self,repository):
        self.repository=repository
        if not repository.get_all():
            repository.add(Movie(1,"Интерстеллар","фантастика",169,12))
            repository.add(Movie(2,"Коко","мультфильм",105,6))
            repository.add(Movie(3,"Начало","фантастика",148,12))
            repository.add(Movie(4,"Зелёная книга","драма",130,16))
    def execute(self,command,data):
        if command=="list": return [m.to_dict() for m in self.repository.get_all()]
        if command=="get":
            movie=self.repository.get(data.get("id"))
            if movie is None: raise KeyError("Фильм не найден")
            return movie.to_dict()
        if command=="create":
            title=str(data.get("title","")).strip(); genre=str(data.get("genre","")).strip()
            duration=int(data.get("duration_minutes",0)); age=int(data.get("age_rating",0))
            if not title or not genre or duration<=0 or age<0: raise ValueError("Укажите название, жанр, положительную длительность и корректный возрастной рейтинг")
            new_id=max((m.movie_id for m in self.repository.get_all()),default=0)+1
            movie=Movie(new_id,title,genre,duration,age); self.repository.add(movie); return movie.to_dict()
        if command=="update":
            movie=self.repository.update(data.get("id"),title=data.get("title"),genre=data.get("genre"),duration_minutes=data.get("duration_minutes"),age_rating=data.get("age_rating"))
            if movie is None: raise KeyError("Фильм не найден")
            if movie.duration_minutes<=0 or movie.age_rating<0: raise ValueError("Некорректная длительность или возрастной рейтинг")
            return movie.to_dict()
        if command=="delete":
            movie=self.repository.delete(data.get("id"))
            if movie is None: raise KeyError("Фильм не найден")
            return {"deleted":movie.movie_id}
        if command=="by_genre":
            genre=str(data.get("genre","")).strip()
            if not genre: raise ValueError("Укажите жанр для поиска")
            return [m.to_dict() for m in self.repository.get_all() if m.genre.casefold()==genre.casefold()]
        raise ValueError("Неизвестная команда")
