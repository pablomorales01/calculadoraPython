# calculadora.py

# Funciones de la calculadora (Asegúrate de que estas funciones existen)
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    # Manejo básico de división por cero
    if b == 0:
        return "Error: División por cero"
    return a / b

# Función para manejar la interacción con el usuario (la parte que tiene 'input')
def main():
    print("Calculadora básica")
    print("Operaciones: suma, resta, multiplicacion, division")
    
    # Esta es la línea que causaba el error EOFError en CI/CD
    op = input("Elige la operación: ")
    
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Entrada inválida. Asegúrate de introducir números.")
        return

    if op == 'suma':
        print(f"Resultado: {suma(num1, num2)}")
    elif op == 'resta':
        print(f"Resultado: {resta(num1, num2)}")
    elif op == 'multiplicacion':
        print(f"Resultado: {multiplicacion(num1, num2)}")
    elif op == 'division':
        print(f"Resultado: {division(num1, num2)}")
    else:
        print("Operación no válida.")

# **LÍNEA CRÍTICA CORREGIDA**
# Esto asegura que 'main()' solo se ejecuta si el script se corre directamente, 
# y no cuando se importa por los tests.
if __name__ == "__main__":
    main()