from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route("/calculadora", methods=["GET", "POST"])
def calculadora():
    imc = None
    categoria = ""
    if request.method == "POST":
        try:
            peso = float(request.form["peso"])
            altura = float(request.form["altura"])
            imc = round(peso / (altura ** 2), 2)

            if imc < 18.5:
                categoria = "Bajo peso"
            elif 18.5 <= imc < 24.9:
                categoria = "Peso normal"
            elif 25 <= imc < 29.9:
                categoria = "Sobrepeso"
            else:
                categoria = "Obesidad"
        except:
            imc = None
            categoria = "Error en los datos ingresados"

    return render_template("calculadora.html", imc=imc, categoria=categoria)

@app.route('/declaracion', methods=["GET", "POST"])
def declaracion():
    resultado = None
    if request.method == "POST":
        patrimonio = int(request.form["patrimonio"])
        ingresos = int(request.form["ingresos"])
        tarjetas = int(request.form["tarjetas"])
        compras = int(request.form["compras"])
        consignaciones = int(request.form["consignaciones"])

        if patrimonio >= 21179300 or ingresos >= 65891000 or tarjetas >= 65891000 or compras >= 65891000 or consignaciones >= 65891000:
            resultado = "Usted debe declarar renta"
        else:
            resultado = "Usted NO debe declarar renta"

    return render_template("declaracion.html", resultado=resultado)

@app.route('/api/imc', methods=['POST'])
def api_imc():
    data = request.get_json()
    try:
        peso = float(data.get("peso", 0))
        altura = float(data.get("altura", 0))
        if altura <= 0:
            return jsonify({"error": "Altura inválida"}), 400
        imc = round(peso / (altura ** 2), 2)
        if imc < 18.5:
            categoria = "Bajo peso"
        elif 18.5 <= imc < 24.9:
            categoria = "Peso normal"
        elif 25 <= imc < 29.9:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidad"
        return jsonify({"imc": imc, "categoria": categoria})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/renta', methods=['POST'])
def api_renta():
    data = request.get_json()
    try:
        patrimonio = int(data.get("patrimonio", 0))
        ingresos = int(data.get("ingresos", 0))
        tarjetas = int(data.get("tarjetas", 0))
        compras = int(data.get("compras", 0))
        consignaciones = int(data.get("consignaciones", 0))

        debe_declarar = (
            patrimonio >= 21179300 or ingresos >= 65891000 or tarjetas >= 65891000
            or compras >= 65891000 or consignaciones >= 65891000
        )

        resultado = "Usted debe declarar renta" if debe_declarar else "Usted NO debe declarar renta"
        return jsonify({"resultado": resultado})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)