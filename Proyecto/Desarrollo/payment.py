# payment.py

# Importar la función input_int desde utils.py
from utils import input_int

def process_payment(user):
    """
    Procesa el pago del usuario mediante diferentes métodos de pago.
    """
    print("\nProcesando pago...")
    # Simular diferentes métodos de pago
    print("Seleccione método de pago:")
    print("1. Tarjeta de crédito")
    print("2. PayPal")
    print("3. Saldo en cuenta")
    choice = input_int("Opción: ", min_value=1, max_value=3)
    if choice == 1:
        card_number = input("Ingrese el número de su tarjeta: ")
        print("Verificando tarjeta...")
        # Aquí podría haber lógica para verificar la tarjeta
    elif choice == 2:
        paypal_account = input("Ingrese su cuenta de PayPal: ")
        print("Conectando con PayPal...")
        # Lógica de PayPal
    elif choice == 3:
        if user.balance >= 10:
            user.balance -= 10
            print(f"Pago realizado con el saldo de su cuenta. Saldo restante: ${user.balance}")
        else:
            print("Saldo insuficiente.")
            return False
    print("Pago exitoso.\n")
    return True
