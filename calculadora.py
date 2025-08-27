# calculadora.py

# Funciones de la calculadora
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

# Interfaz gráfica con Tkinter
import tkinter as tk

def calcular():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operacion.get()
        if op == "suma":
            resultado.set(suma(a, b))
        elif op == "resta":
            resultado.set(resta(a, b))
        elif op == "multiplicacion":
            resultado.set(multiplicacion(a, b))
        elif op == "division":
            resultado.set(division(a, b))
        else:
            resultado.set("Operación no válida")
    except ValueError:
        resultado.set("Entrada inválida")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculadora")

    tk.Label(root, text="Primer número:").pack()
    entry1 = tk.Entry(root)
    entry1.pack()

    tk.Label(root, text="Segundo número:").pack()
    entry2 = tk.Entry(root)
    entry2.pack()

    operacion = tk.StringVar(root)
    operacion.set("suma")
    opciones = tk.OptionMenu(root, operacion, "suma", "resta", "multiplicacion", "division")
    opciones.pack()

    tk.Button(root, text="Calcular", command=calcular).pack()
    resultado = tk.StringVar()
    tk.Label(root, textvariable=resultado).pack()

    root.mainloop()