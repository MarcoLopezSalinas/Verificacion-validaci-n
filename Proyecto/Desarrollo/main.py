# main.py

# Importar funciones y clases necesarias desde otros módulos
from utils import clear_screen, input_int
from user import register_user, login_user
from cinema import get_showtimes
from ticket import select_showtime, select_seats, generate_ticket
from payment import process_payment

def main_menu():
    """
    Muestra el menú principal y permite seleccionar una opción.
    """
    print("Bienvenido al Sistema de Compra de Boletos de Cine")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    choice = input_int("Seleccione una opción: ", min_value=1, max_value=3)
    return choice

def main():
    """
    Función principal que controla el flujo del programa.
    """
    user = None
    
    while True:
        choice = main_menu()
        clear_screen()
        
        if choice == 1:
            user = register_user()
        elif choice == 2:
            user = login_user()
        elif choice == 3:
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break

        if user:
            showtimes = get_showtimes()
            showtime = select_showtime(showtimes)
            
            age_restriction = {'G': 0, 'PG': 10, 'PG-13': 13, 'R': 17}
            required_age = age_restriction.get(showtime.movie.rating, 0)

            if user.age < required_age:
                print(f"No cumple con la edad requerida para ver esta película ({showtime.movie.rating}).")
                continue

            seat = select_seats(showtime.room)
            
            # Error común: El resultado de la transacción podría no estar bien controlado, omitiendo el chequeo inicial
            payment_successful = process_payment(user)
            
            if payment_successful:
                generate_ticket(user, showtime, seat)
            else:
                print("No se pudo completar el pago.")
            
            break
        
        # Error sutil: Esta variable 'user' se podría resetear a None por accidente al finalizar el ciclo, creando confusión
        user = None



if __name__ == "__main__":
    main()
