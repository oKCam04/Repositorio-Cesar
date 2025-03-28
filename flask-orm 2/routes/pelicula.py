from app import app
from flask import request
from models.pelicula import Pelicula
from models.genero import Genero

@app.route("/pelicula/",methods=["GET"])
def listarPeliculas():
    try:
        mensaje=None
        peliculas=Pelicula.objects()
    
    except Exception as error:
        mensaje=str(error)

    return {"mensaje": mensaje,"peliculas": peliculas}

@app.route("/pelicula/", methods=['POST'])
def addPelicula():
    try:
        mensaje= None
        estado= False
        if request.method=='POST':
            datos=request.get_json(force=True)
            genero=Genero.objects(id=datos['genero']).first()
            if genero is None:
                mensaje="genero no existe, no se puede crear la pelicula"            
           
            else:
                datos['genero']=genero
                pelicula= Pelicula(**datos)
                pelicula.save()
                estado=True
                mensaje="Pelicula agregado correctamente"
        else:
            mensaje="no permitido"
        
    except Exception as error:
        mensaje=str(error)
        
    return{"estado":estado, "mensaje":mensaje}


@app.route("/pelicula/", methods=['PUT'])
def updatePelicula():
    try:
        mensaje= None
        estado= False
        if request.method=='PUT':
            datos=request.get_json(force=True)
            pelicula=Pelicula.objects(id=datos['id']).first()
            pelicula.codigo= datos['codigo']
            pelicula.titulo= datos['titulo']
            pelicula.protagonista= datos['protagonista']
            pelicula.resumen= datos['resumen']
            pelicula.foto= datos['foto']
            genero=Genero.objects(id=datos['genero']).first()
            if genero is None:
                mensaje="no se actualiza el genero."
            else:
                pelicula.genero=genero
            pelicula.save()
            mensaje =f"{mensaje} pelicula actualizada" 
            estado=True
        else: 
            mensaje="no permitido"
    except Exception as error:
        mensaje=str(error)
        
    return{"estado":estado, "mensaje":mensaje}

@app.route("/pelicula/", methods=['DELETE'])
def deletePelicula():
    try:
        mensaje= None
        estado= False
        if request.method=='DELETE':
            datos=request.get_json(force=True)
            pelicula=Pelicula.objects(id=datos['id']).first()
            pelicula.delete()
            estado=True
            mensaje="pelicula eliminada satisfactoriamente"
            
    except Exception as error:
        mensaje=str(error)
    
    return {"estado": estado, "mensaje":mensaje}