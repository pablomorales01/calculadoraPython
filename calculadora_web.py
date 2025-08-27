from flask import Flask, render_template_string, request
from calculadora import suma, resta, multiplicacion, division

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculadora Web</title>
</head>
<body>
    <h2>Calculadora Web</h2>
    <form method="post">
        <input type="number" step="any" name="a" required placeholder="Primer número">
        <input type="number" step="any" name="b" required placeholder="Segundo número">
        <select name="operacion">
            <option value="suma">Suma</option>
            <option value="resta">Resta</option>
            <option value="multiplicacion">Multiplicación</option>
            <option value="division">División</option>
        </select>
        <button type="submit">Calcular</button>
    </form>
    {% if resultado is not none %}
        <h3>Resultado: {{ resultado }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            op = request.form["operacion"]
            if op == "suma":
                resultado = suma(a, b)
            elif op == "resta":
                resultado = resta(a, b)
            elif op == "multiplicacion":
                resultado = multiplicacion(a, b)
            elif op == "division":
                resultado = division(a, b)
            else:
                resultado = "Operación no válida"
        except Exception:
            resultado = "Entrada inválida"
    return render_template_string(HTML, resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)