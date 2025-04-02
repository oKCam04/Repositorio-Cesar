from flask import Flask, render_template
from flask_mongoengine import MongoEngine

app = Flask(__name__)

#uri="mongodb+srv://CamiloH:admin0000@cluster0.r94m6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

app.config["UPLOAD_FOLDER"]= "./static/imagenes"
app.config['MONGODB_SETTINGS']=[{
    "db":"gestion_peliculas",
    "host":"localhost",
    "port":27017
}]
db=MongoEngine(app)

@app.route("/")
def login():
    return render_template("iniciarSesion.html")

@app.route("/home/")
def home():
    return render_template("contenido.html")


if __name__=="__main__":
    from routes.genero import *
    from routes.pelicula import *
    from routes.usuario import *
    app.run(port=3000, host="0.0.0.0",debug=True)