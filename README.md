# Sistema de Compra de Boletos de Cine

Este proyecto simula un sistema de compra de boletos de cine con diferentes módulos. El código fue analizado utilizando la extensión SonarLint en Visual Studio Code para detectar y corregir violaciones de buenas prácticas de codificación.

## Análisis SonarLint

### Violación 1: Variable no utilizada

- **Descripción**: Se detectaron variables que fueron declaradas pero no utilizadas, lo que genera un code smell.
- **Tipo**: Code smell.
- **Archivo**: `cinema.py`
- **Línea**: 55
- **Corrección**: Se eliminó la variable `temp` que no era utilizada.
- **Fragmento de Código**:

  - **Antes**:
    ```python
    temp = none  
    ```

  - **Después**:
    ```python
    # Elimina la variable 'temp'
    ```

### Violación 2: Variables no utilizadas en `payment.py`

- **Descripción**: Las variables `card_number` y `paypal_account` no fueron utilizadas en el archivo `payment.py`.
- **Tipo**: Code smell.
- **Archivo**: `payment.py`
- **Línea**: 18, 22
- **Corrección**: Se eliminaron ambas variables.
- **Fragmento de Código**:

  - **Antes**:
    ```python
       if choice == 1:
        card_number = input("Ingrese el número de su tarjeta: ")
        print("Verificando tarjeta...") 
    elif choice == 2:
        paypal_account = input("Ingrese su cuenta de PayPal: ")
        print("Conectando con PayPal...")
        
    elif choice == 3:
        if user.balance >= 10:
            user.balance -= 10
            print(f"Pago realizado con el saldo de su cuenta. Saldo restante: ${user.balance}")
        else:
            print("Saldo insuficiente.")
            return False
    print("Pago exitoso.\n")
    ```

  - **Después**:
    ```python
    if choice == 3:
        if user.balance >= 10:
            user.balance -= 10
            print(f"Pago realizado con el saldo de su cuenta. Saldo restante: ${user.balance}")
        else:
            print("Saldo insuficiente.")
            return False
    print("Pago exitoso.\n")
    ```

### Violación 3: Excepción no especificada

- **Descripción**: Se detectaron bloques `try-except` que no especificaban el tipo de excepción a capturar.
- **Tipo**: Code smell.
- **Archivo**: `ticket.py`
- **Línea**: 28
- **Corrección**: Se especificó la clase de excepción `ValueError` para capturar errores de valor.
- **Fragmento de Código**:

  - **Antes**:
    ```python
    try:
        c = int(input("Seleccione un horario: "))
        if c < 1 or c > len(x):  
            raise ValueError()
    except:
        print("Entrada inválida, se seleccionará el primer horario.")
        return x[0]  
    ```

  - **Después**:
    ```python
   choice = input_int("Seleccione un horario: ", min_value=1, max_value=len(showtimes))
    ```

### Violación 4: Excepción no especificada en `utils.py`

- **Descripción**: Se detectaron bloques `try-except` que no especificaban el tipo de excepción a capturar.
- **Tipo**: Code smell.
- **Archivo**: `utils.py`
- **Línea**: 37
- **Corrección**: Se especificó la clase de excepción `Exception` para capturar cualquier error.
- **Fragmento de Código**:

  - **Antes**:
    ```python
    while True:
        try:
            value = input(prompt)
            
            value = int(value)  
            if min_value != None:  
                if value < min_value:
                    print("Valor demasiado bajo.")
                    continue
            if max_value != None:  
                if value > max_value:
                    print("Valor demasiado alto.")
                    continue

           
            return value
        except:
            # Capturar cualquier excepción sin especificar el tipo, mala práctica
            print("Error de entrada.")
    ```

  - **Después**:
    ```python
    try:
        # código
    except Exception as e:
        print(f"Se produjo un error: {e}")
    ```

---

### Violación 5: `if` anidado innecesariamente

- **Descripción**: SonarLint detectó que las sentencias `if` en las líneas 25 y 29 estaban anidadas innecesariamente.
- **Tipo**: Code smell.
- **Archivo**: `utils.py`
- **Líneas**: 25 y 29
- **Corrección**: Se combinaron las sentencias `if` para simplificar el código y mejorar la legibilidad.
- **Fragmento de Código**:

  - **Antes**:
    ```python
    if min_value != None:  
        if value < min_value:
            print("Valor demasiado bajo.")
            continue
    if max_value != None:  
        if value > max_value:
            print("Valor demasiado alto.")
            continue
    ```

  - **Después**:
    ```python
    if min_value is not None and value < min_value:
        print("Valor demasiado bajo.")
        continue
    if max_value is not None and value > max_value:
        print("Valor demasiado alto.")
        continue
    ```

### Violación 6: Excepción no especificada

- **Descripción**: SonarLint detectó que una excepción estaba siendo capturada sin especificar el tipo. Esto es una mala práctica, ya que podría capturar excepciones no deseadas y dificultar la depuración.
- **Tipo**: Code smell.
- **Archivo**: `utils.py`
- **Línea**: 35
- **Corrección**: Se especificó el tipo de excepción `ValueError`, que es la excepción adecuada para el problema de conversión de tipos con `int()`.
- **Fragmento de Código**:

  - **Antes**:
    ```python
    except:
        print("Error de entrada.")
    ```

  - **Después**:
    ```python
    except ValueError:
        print("Error de entrada. Por favor, ingresa un número entero.")
    ```

---

## Conclusión

Las violaciones de las buenas prácticas de codificación detectadas por **SonarLint** fueron corregidas para mejorar la calidad y la legibilidad del código, cumpliendo con las recomendaciones de Clean Code.

## Conclusión

Gracias al análisis de SonarLint, se corrigieron múltiples code smells en el proyecto, mejorando la calidad del código y siguiendo mejores prácticas de Clean Code.
