from app import app, db
from flask import request
from models.genero import *
from sqlalchemy import exc

@app.route("/genero/",methods=["GET"])
def listarGeneros():
    try:
        mensaje=None
        generos= Genero.query.order_by(Genero.idGenero).all()
        listaGeneros=[]
        for g in generos:
            genero = {
                "idGenero":g.idGenero,
                "genero":g.genNombre                
            }
            listaGeneros.append(genero)
            
    except exc.SQLAlchemyError as error:
        mensaje=str(error)
    return {"mensaje": mensaje, "generos": listaGeneros}

@app.route("/genero/", methods=['POST'])
def addGenero():
    try:
        mensaje=None
        estado=False
        if request.method=='POST':
            datos=request.get_json(force=True)
            genero=Genero(genNombre=datos['genero'])
            db.session.add(genero)
            db.session.commit()
            estado=True
            mensaje=f"Producto agregado correctamente con el id: {genero.idGenero}"
        else:
            mensaje="tarea no permitida"
    except exc.SQLAlchemyError as error:
        db.session.rollback()
        mensaje=str(error)
    return {"estado":estado,"mensaje":mensaje}

@app.route("/genero/",methods=['PUT'])
def updateGenero():
    try:
        estado=False
        mensaje=None
        if request.method=='PUT':
            datos = request.get_json(force=True)
            genero = Genero.query.get(int(datos['id']))
            #actualixo nombre de genero co el nombre que llegue
            genero.genNombre = datos['nombre']
            db.session.commit()
            estado=True
            mensaje="genero actualizado correctamente"
            
        else:
            mensaje="tarea no permitida"
            
    except exc.SQLAlchemyError as error:
        mensaje=str(error)       
    return{"estado": estado, "mensaje":mensaje}

@app.route("/genero/",methods=['DELETE'])
def deleteGenero():
    try:
        estado=False
        mensaje=None
        if request.method=='DELETE':
            datos=request.get_json(force=True)
            generoAeliminar=Genero.query.get(int(datos['id']))
            db.session.delete(generoAeliminar)
            db.session.commit()
            mensaje="mensaje eliminado correctamente"
        else:
            mensaje="Tarea no permitida"
    except exc.SQLAlchemyError as error:
        mensaje=str(error)
    return {"estado":estado,"mensaje":mensaje}
