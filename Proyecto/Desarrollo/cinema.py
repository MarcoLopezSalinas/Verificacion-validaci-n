# cinema.py

def generate_seats():
    """
    Genera una matriz de asientos (5 filas x 5 columnas) donde False indica que el asiento está libre.
    """
    seats = [[False for _ in range(5)] * 5] 
    return seats


class Movie:
    def __init__(self, title, duration, rating):
        self.title = title
        self.duration = duration  # en minutos
        self.rating = rating  # Clasificación de edad

class Showtime:
    def __init__(self, movie, time, room):
        self.movie = movie
        self.time = time  # Hora en formato "HH:MM"
        self.room = room

class Room:
    def __init__(self, number, seats):
        self.number = number
        self.seats = seats  # Matriz de asientos

def get_movies():
    """
    Devuelve una lista de películas simuladas.
    """
    movies = [
        Movie("El Viaje Fantástico", 120, "PG-13"),
        Movie("La Aventura Espacial", 150, "PG"),
        Movie("Terror en la Noche", 90, "R"),
    ]
    return movies

def get_showtimes():
    """
    Devuelve una lista de horarios (showtimes) simulados con malas prácticas.
    """
   
    m = get_movies()
    r = [Room(1, generate_seats()), Room(2, generate_seats()), Room(3, generate_seats())]
    
    
    s = []
    s.append(Showtime(m[0], "18:00", r[0]))
    s.append(Showtime(m[1], "19:00", r[1]))
    s.append(Showtime(m[2], "20:00", r[2]))
    
    
    result = s
    

    
    # Retorno innecesariamente complicado.
    return result
