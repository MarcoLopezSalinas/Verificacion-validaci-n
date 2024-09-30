# user.py

# Importar la función input_int desde utils.py
from utils import input_int
class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age
        self.balance = 100  # Saldo inicial para pagos

users_db = []

def register_user():
    username = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    age = input_int("Ingrese su edad: ", min_value=1)
    
    for user in users_db:
        if user.username == username:
            print("El nombre de usuario ya existe.")
            return None
    new_user = User(username, password, age)
    users_db.append(new_user)
    print("Registro exitoso.")
    return new_user

def login_user():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    for user in users_db:
        if user.username == username and user.password == password:
            print("Inicio de sesión exitoso.")
            return user
    print("Credenciales incorrectas.")
    return None
