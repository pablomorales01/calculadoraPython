def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

print("Calculadora básica")
print("Operaciones: suma, resta, multiplicacion, division")
op = input("Elige la operación: ")
a = float(input("Primer número: "))
b = float(input("Segundo número: "))

if op == "suma":
    print("Resultado:", suma(a, b))
elif op == "resta":
    print("Resultado:", resta(a, b))
elif op == "multiplicacion":
    print("Resultado:", multiplicacion(a, b))
elif op == "division":
    print("Resultado:", division(a, b))
else:
    print("Operación no válida")
