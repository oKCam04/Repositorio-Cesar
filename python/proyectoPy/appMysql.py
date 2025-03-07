import pymysql as mysql;

user="root"
password="0000"
baseDatos="productospython"
host="localhost"




def agregar():
    myConexion =mysql.connect(host=host, user=user, password=password, database=baseDatos)
    cursor=myConexion.cursor()
    try:
        #crear el producto
        p=(17,"Lavaloza",25006000,"juguete")
        cursor=myConexion.cursor()
        consulta="INSERT INTO productos VALUES (null,%s, %s, %s, %s)"
        resultado=cursor.execute(consulta,p)
        myConexion.commit()
        if (cursor.rowcount==1):
             print("Producto agregado correctamente")
    except myConexion.Error as e:
        print("Error al conectar a la base de datos", e) 
    finally:
        if(myConexion.connect()):
            cursor.close()
            myConexion.close()
            print("Conexión cerrada correctamente")

def listar():
    myConexion = mysql.connect(host=host, user=user, password=password, database=baseDatos)
    cursor=myConexion.cursor()
    try:
        consulta="SELECT * FROM productos"
        cursor.execute(consulta)
        productos=cursor.fetchall()
        for producto in productos:
            print("Producto: ", producto)
            print("Producto: ", producto[0], producto[1], producto[2], producto[3], producto[4])
    except myConexion.Error as e:
        print("Error al conectar a la base de datos", e)
def consultarPorCodigo():
    myConexion = mysql.connect(host=host, user=user, password=password, database=baseDatos)
    cursor=myConexion.cursor()
    try:
        codigo=(17,)
        consulta="SELECT * FROM productos WHERE proCodigo=%s"
        cursor.execute(consulta,codigo)
        producto=cursor.fetchone()
        if producto:
            print("Producto encontrado: ", producto)
            print("Producto encontrado: ",producto[0], producto[1], producto[2], producto[3], producto[4])
        else:
            print("Producto no encontrado con ese código")
    except myConexion.Error as e:
        print("Error al conectar a la base de datos", e)


def actualizar():
    myConexion = mysql.connect(host=host, user=user, password=password, database=baseDatos)
    cursor=myConexion.cursor()
    try:
        datosActualizar=("animal",16)
        consulta="UPDATE productos set proNombre=%s WHERE proCodigo=%s"
        resultado=cursor.execute(consulta,datosActualizar)
        myConexion.commit()
        if (cursor.rowcount==1):
            print("Producto actualizado correctamente")
    except myConexion.Error as e:
        myConexion.rollback()
        print("Error al conectar a la base de datos", e) 
  
def eliminar():
    myConexion = mysql.connect(host=host, user=user, password=password, database=baseDatos)
    cursor=myConexion.cursor()
    try:
        p=(16,)
        consulta="DELETE FROM productos WHERE proCodigo=%s"
        resultado=cursor.execute(consulta,p)
        myConexion.commit()
        if (cursor.rowcount==1):
            print("Producto eliminado correctamente")
        else:
            print("Producto no encontrado con ese código")
    except myConexion.Error as e:
        myConexion.rollback()
        print("Error al conectar a la base de datos", e)

def agregarVarios():
        myConexion = mysql.connect(host=host, user=user, password=password, database=baseDatos)
        cursor=myConexion.cursor()
        try:
            productos=[(18,"zapatilla",25000,"calzado"),(19,"pantalones", 30000,"ropa"),(20,"pantalon de cuero",26000,"ropa")]
            consulta = "insert into productos values(null,%s,%s,%s,%s)"
            cursor.executemany(consulta,productos)
            myConexion.commit()
            if (cursor.rowcount==len(productos)):
                print("Productos agregados correctamente")
        except myConexion.Error as e:
            myConexion.rollback()
            print("Problemas al agregar productos}",e)

#agregar()
#listar()
#consultarPorCodigo()
#actualizar()
#eliminar()
agregarVarios()
