from mongoengine import *


class Usuario(Document):
    usuario = StringField(unique=True, required=True, max_length=50)
    password = StringField(required=True, min_length=4)  
    nombre_completo = StringField(required=True, max_length=100)
    correo = EmailField(unique=True, required=True)

    def __repr__(self):
        return self.usuario
