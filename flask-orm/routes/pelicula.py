from flask import request
from app import app, db
from models.pelicula import *
from sqlalchemy import exc

@app.route("/pelicula/", methods=['GET'])
def listarPeliculas():
    try:
        mensaje = None
        if request.method == 'GET':
            peliculas = Pelicula.query.all()
            listaPeliculas = []
            for p in peliculas:
                pelicula = {
                    "idPelicula": p.idPelicula,
                    "codigo": p.pelCodigo,
                    "titulo": p.pelTitulo,
                    "protagonista": p.pelProtagonista,
                    "duracion": p.pelDuracion,
                    "genero": {
                        "idGenero": p.genero.idGenero,
                        "nombre": p.genero.genNombre
                    },
                    "foto": p.pelFoto
                }
                listaPeliculas.append(pelicula)
        else:
            mensaje = "Tarea no permitida"
    except exc.SQLAlchemyError as error:
        mensaje = str(error)

    return {"mensaje": mensaje, "Peliculas": listaPeliculas}


@app.route("/pelicula/", methods=['POST'])
def addPelicula():
    try:
        mensaje = None
        estado = False
        if request.method == 'POST':
            datos = request.get_json(force=True)
            pelicula = Pelicula(
                pelCodigo=int(datos['pelCodigo']),
                pelTitulo=datos['pelTitulo'],
                pelProtagonista=datos['pelProtagonista'],
                pelDuracion=datos['pelDuracion'],
                pelResumen=datos['pelResumen'],
                pelFoto=datos['pelFoto'],
                pelGenero=datos['pelGenero']
            )

            db.session.add(pelicula)
            db.session.commit()
            estado = True
            mensaje = f"Pelicula agregada correctamente con el id: {pelicula.idPelicula}"
        else:
            mensaje = "Tarea no permitida"

    except exc.SQLAlchemyError as error:
        db.session.rollback()
        mensaje = str(error)

    return {"estado": estado, "mensaje": mensaje}


@app.route("/pelicula/",methods=['PUT'])
def updatePelicula():
    try:
        estado=False
        mensaje=None
        if request.method=='PUT':
            datos = request.get_json(force=True)
            genero = Pelicula.query.get(int(datos['id']))
            #actualixo nombre de genero co el nombre que llegue
            genero.pelDuracion = datos['duracion']
            db.session.commit()
            estado=True
            mensaje="genero actualizado correctamente"
            
        else:
            mensaje="tarea no permitida"
            
    except exc.SQLAlchemyError as error:
        mensaje=str(error)       
    return{"estado": estado, "mensaje":mensaje}


@app.route("/pelicula/",methods=['DELETE'])
def deletePelicula():
    try:
        estado=False
        mensaje=None
        if request.method=='DELETE':
            datos=request.get_json(force=True)
            peliculaAEliminar=Pelicula.query.get(int(datos['id']))
            db.session.delete(peliculaAEliminar)
            db.session.commit()
            mensaje="mensaje eliminado correctamente"
        else:
            mensaje="Tarea no permitida"
    except exc.SQLAlchemyError as error:
        mensaje=str(error)
    return {"estado":estado,"mensaje":mensaje}