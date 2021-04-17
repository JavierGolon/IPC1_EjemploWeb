from flask import Flask,request,jsonify
from flask_cors import CORS
import json

listapacientes = []
listadcotres = []
listaenfermeroa = []


app = Flask(__name__)
CORS(app)

# SE LE CONOCEN COMO ENDPOINT

#=================== RUTA RAIZ =============
@app.route('/')
def index():
    return jsonify("servidor ipc1")

# ========== RUTA DE NOMBRE ================

@app.route('/minombre')
def minombremetodo():
    return '<h1>Mi nombre es javier</h1>'


# ========= RUTA POST EJEMPLO =========
@app.route('/postejemplo', methods=['POST'])
def postmetodo():
    data = request.get_json(force=True)
    listapacientes.append(data)
    print(data)
    return jsonify("ingresado")


# ========= RUTA POST EJEMPLO =========
@app.route('/obtenerpacientes')
def obtenerpacientes():
    return jsonify(listapacientes)


# ========= RUTA POST EJEMPLO =========
@app.route('/login', methods=['POST'])
def loginmetodo():
    data = request.get_json(force=True)
    user = data["Nombre"]
    password = data["password"]
    print("LLego la informacion y los datos son:" +user +" --> "+ password)
    # for de mi lista pacientes
    if user == "javier" and password == "12345":
        return jsonify("credenciales correctas")
    else:
        return jsonify("credenciales incorrectas")




if __name__ == "__main__":
    app.run("0.0.0.0",port=5050)
