import pymongo
from pymongo import MongoClient

#crear la conexión
miConexion = MongoClient("mongodb://localhost:27017/")

#acceder a la bas datos
baseDatos = miConexion["Negocio"]
print(type(baseDatos))

productos = baseDatos["Productos"]
print(type(productos))


def agregarProducto():
    try:
        codigo=10
        nombre="Camisa"
        precio=99000
        categoria="Ropa"
        producto={
            "codigo":codigo,
            "nombre":nombre,
            "precio":precio,
            "categoria":categoria
        }
        resultado = productos.insert_one(producto)
        print(resultado)
        if(resultado.acknowledged):
            print(f"Producto agregado con id {resultado.inserted_id}")
        else:
            print("Problemas al agregar")
    except pymongo.errors as error:
        print(f"{error}")
        
def listarProductos():
    try:
        listaProductos = productos.find()
        print(listaProductos)
        for producto in listaProductos:
            print(producto)
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']}")
            print(f"Categoria: {producto['categoria']}")
            print("*******************************")
        
    except pymongo.errors as error:
        print(f"{error}")
        
def consultarPorCodigo():
    try:
        codigoAConsultar = 10
        consulta = {"codigo":codigoAConsultar}
        #consulta2 = {"precio":2500000}
        producto=productos.find_one(consulta)
        #producto = productos.find_({"$and":[{"precio":{"$gt":50000}},
                                               #{"precio":{"$lt":100000}}] })
        if(producto is not None):
            print(producto)
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']}")
            print(f"Categoria: {producto['categoria']}")
        else:
            print(f"No existe producto con el código {codigoAConsultar}")
        
        
    except pymongo.errors as error:
        print(f"{error}")
        
def actualizar():
    try:
        codigoProducto=10
        criterio = {"codigo":codigoProducto}
        datosActualizar={
            "nombre":"nombreNuevo",
            "precio":5000
        }
        consulta ={"$set":datosActualizar}
        resultado=productos.update_many(criterio,consulta)
        if(resultado .acknowledged):
            print("Producto Actualizado")
        else:
            print("problemas al actualizar")
    except pymongo.errors as error:
        print(f"{error}")
    
def agregarVariosProductos():
    try:
        codigo=1000
        nombre="Chaqueta"
        precio=199000
        categoria="Ropa"
        producto1={
            "codigo":codigo,
            "nombre":nombre,
            "precio":precio,
            "categoria":categoria
        }
        producto2={
            "codigo":232323,
            "nombre":"sdsadsadsa",
            "precio":434432,
            "categoria":"Ropa"
        }
        
        lista=[producto1,producto2]
        resultado = productos.insert_many(lista)
        print(resultado)
        if(resultado.acknowledged):
            print(f"Producto agregado con id {resultado.inserted_id}")
        else:
            print("Problemas al agregar")
    except pymongo.errors as error:
        print(f"{error}")
    
def eliminar():
    try:
        productoElimniar={"codigo":10}
        resultado=productos.delete_one(productoElimniar)
        if(resultado.acknowledged):
            print("Producto eliminado")
        else:
            print("Problemas al eliminar")
    except pymongo.errors as error:
        print(f"{error}")



#agregarProducto()
#listarProductos()
#consultarPorCodigo()
#actualizar()
#agregarVariosProductos()
#eliminar()