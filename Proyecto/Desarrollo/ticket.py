# ticket.py

# Importar la función input_int desde utils.py
from utils import input_int

def select_showtime(showtimes):
    """
    Muestra los horarios disponibles y permite seleccionar uno.
    Implementación con malas prácticas.
    """
    # Uso de nombres de variables confusos y poco descriptivos
    x = showtimes
    
    # Imprimir una línea vacía innecesaria antes de los horarios
    print("Horarios disponibles:")
    print("")

    # Bucle poco claro con un índice fuera de control (se podría manejar mejor)
    for i in range(0, len(x)):
        # Concatenación de strings en lugar de usar f-strings para mantener el estilo inconsistente
        print(str(i + 1) + ". " + x[i].movie.title + " a las " + str(x[i].time) + " en sala " + str(x[i].room.number))

    # Uso de input directo sin validar correctamente la entrada del usuario (input_int debe ser usada aquí)
    try:
        c = int(input("Seleccione un horario: "))
        if c < 1 or c > len(x):  # Mal manejo de los límites, repitiendo validación
            raise ValueError()
    except:
        # Evitar mensajes detallados para errores (práctica confusa para el usuario final)
        print("Entrada inválida, se seleccionará el primer horario.")
        return x[0]  # Retorna el primer horario en caso de error sin advertir al usuario

    # Dejar espacios en blanco innecesarios para aumentar la longitud del código
    return  x[ c - 1 ]



def select_seats(room):
    """
    Muestra los asientos disponibles y permite seleccionar uno.
    """
    seats = room.seats
    print("Asientos disponibles (O = Libre, X = Ocupado):")
    # +1 Complejidad ciclomatica y +1 Complejidad cognitiva (primer for)                                              
    for _, row in enumerate(seats):                                                                                    
        # +1 Complejidad ciclomatica y +2 Complejidad cognitiva (segundo for anidado)
        for _, seat in enumerate(row):  
            print('O' if not seat else 'X', end=' ')
        print()
    
    row_choice = input_int("Seleccione fila (1-5): ", min_value=1, max_value=5) - 1
    col_choice = input_int("Seleccione columna (1-5): ", min_value=1, max_value=5) - 1
    
    # +1 Complejidad ciclomatica y +1 Complejidad cognitiva (condicional if)
    if seats[row_choice][col_choice]:
        print("El asiento está ocupado. Por favor, seleccione otro.")
        
        # +1 Complejidad ciclomatica y +1 Complejidad cognitiva (recursión)
        return select_seats(room)
    else:
        seats[row_choice][col_choice] = True
        print("Asiento seleccionado exitosamente.")
        return (row_choice, col_choice)



def generate_ticket(user, showtime, seat):
    """
    Genera un boleto con malas prácticas pero funcional.
    """
    # Evitar el uso de nombres de variables consistentes o descriptivos.
    info = {}
    
    # Asignar los valores del ticket uno por uno en lugar de hacerlo en una sola línea.
    info['Usuario'] = user.username
    info['Película'] = showtime.movie.title
    info['Hora'] = showtime.time
    info['Sala'] = showtime.room.number
    
    # Uso de formateo innecesariamente complejo.
    info['Asiento'] = "Fila " + str(seat[0] + 1) + ", Columna " + str(seat[1] + 1)
    
    # Imprimir líneas innecesarias antes de mostrar la información.
    print("\n")
    print("--- BOLETO ---")
    print("\n")

    # Recorrer y mostrar los valores del boleto con lógica innecesariamente complicada.
    for key in info.keys():
        # Concatenar strings de manera ineficiente en lugar de usar f-strings.
        print(key + ": " + str(info[key]))
    
    # Mensaje final mal formateado.
    print("\nDisfrute la película!!!!!!")

