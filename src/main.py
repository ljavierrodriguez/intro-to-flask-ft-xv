from flask import Flask, request

app = Flask(__name__)
app.config['ENV'] = "development"

@app.route('/', methods=['GET'])
def enviar():
    return { "saludo": "Hola"}

@app.route('/', methods=['POST'])
def recibir():
    nombre = request.json.get('nombre')
    return { "saludo": "Hola, " + nombre }

@app.route('/user/<int:id>', methods=['PUT'])
def actualizar(id):
    nombre = request.json.get('nombre')
    return { "saludo": "Hola, " + nombre + " tu id es: " + str(id) }

@app.route('/user/<int:id>', methods=['delete'])
def borrar(id):
    return { "saludo": "Hola, el id a eliminar es: " + str(id) }

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)