
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('home.html', mensaje="bienvenidos al sitio web")

@app.route('/mostrarTabla/',methods=['GET'])
def mostrar_tabla():
    return render_template('tabla.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    items=[
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"}
    ]
    return {"items":items}
@app.route('/pasarDatos/<int:precio>',methods=['GET'])
def get_pasarDatos(precio):
    return render_template('home.html',mensaje=f"el precio es {precio}")
    
@app.route('/obtenerDatosParametros/',methods=['GET'])
def obtenerDatosParametros():
    id=request.args.get('id')
    nombre = request.args.get('nombre')
    apellido = request.args.get('apellido')
    return render_template('home.html', mensaje=f"Hola {nombre} {apellido}")



if __name__ == '__main__':
    app.run(port=3000,debug=True)

