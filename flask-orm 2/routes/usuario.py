from app import app
from flask import request
from models.usuario import Usuario


@app.route("/usuario/", methods=["GET"])
def listarUsuarios():
    try:
        usuarios = Usuario.objects()
        return {"estado": True, "usuarios": usuarios}
    except Exception as error:
        return {"estado": False, "mensaje": str(error)}


@app.route("/usuario/", methods=["POST"])
def addUsuario():
    try:
        datos = request.get_json(force=True)
        usuario = Usuario(**datos)
        usuario.save()
        return {"estado": True, "mensaje": "Usuario agregado correctamente"}
    except Exception as error:
        return {"estado": False, "mensaje": str(error)}


@app.route("/usuario/", methods=["PUT"])
def updateUsuario():
    try:
        datos = request.get_json(force=True)
        usuario = Usuario.objects(usuario=datos['usuario']).first()
        if usuario:
            usuario.update(
                set__password=datos['password'],
                set__nombre_completo=datos['nombre_completo'],
                set__correo=datos['correo']
            )
            return {"estado": True, "mensaje": "Usuario actualizado"}
        else:
            return {"estado": False, "mensaje": "Usuario no encontrado"}
    except Exception as error:
        return {"estado": False, "mensaje": str(error)}


@app.route("/usuario/", methods=["DELETE"])
def deleteUsuario():
    try:
        datos = request.get_json(force=True)
        usuario = Usuario.objects(usuario=datos['usuario']).first()
        if usuario:
            usuario.delete()
            return {"estado": True, "mensaje": "Usuario eliminado correctamente"}
        else:
            return {"estado": False, "mensaje": "Usuario no encontrado"}
    except Exception as error:
        return {"estado": False, "mensaje": str(error)}
