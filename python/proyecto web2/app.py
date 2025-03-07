from flask import Flask, render_template, request

app = Flask(__name__)
personas=[]
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('formulario.html')
    else:
        if request.method == 'POST':
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            correo = request.form['correo']
            persona={'nombre':nombre,'apellido':apellido, 'correo':correo}
            personas.append(persona)
            return render_template('formulario.html',personas=personas)

if __name__ == '__main__':
    app.run(port=3000,debug=True)