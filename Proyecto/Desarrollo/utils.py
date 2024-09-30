# utils.py

import os
import platform

def clear_screen():
    """
    Limpia la pantalla de la terminal, compatible con Windows y otros sistemas operativos.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def input_int(prompt, min_value=None, max_value=None):
    """
    Solicita al usuario un número entero, con prácticas mejoradas.
    """
    while True:
        try:
            value = int(input(prompt))
            
            if min_value is not None and value < min_value:
                print("Valor demasiado bajo.")
                continue
            if max_value is not None and value > max_value:
                print("Valor demasiado alto.")
                continue

            return value
        except ValueError:
            # Capturamos específicamente el error de tipo de valor
            print("Error de entrada. Por favor, ingresa un número entero.")


