from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

#crear clase Movie con atributos
class Movie(BaseModel):
    id: Optional[int] = None # id definido como opcional
    title: str
    overview: str
    year: int
    rating: float
    category: str

#lista de peliculas
movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

#metodos HTTPS
#Get -> consultar peliculas
@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

#Get -> consultar peliculas por id
@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

#Get -> Consultar pelicula por categoria y año
@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [ item for item in movies if item['category'] == category ]



#metodo POST -> Crear Peliculas
@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies

#metodo PUT -> Editar peliculas
@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
	for item in movies:
		if item["id"] == id:
			item['title'] = movie.title
			item['overview'] = movie.overview
			item['year'] = movie.year
			item['rating'] = movie.rating
			item['category'] = movie.category
			return movies

#metodo DELETE -> Eliminar peliculas
@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies
    
    