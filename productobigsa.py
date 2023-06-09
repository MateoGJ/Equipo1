import mysql.conector

from bd_big_bread import bd_big_bread
class Conectar():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connet(
                anfitrion = '127.0.0.1',
                puerto = 3306,
                usuario = 'root',
                contraseña = 'usain10879',
                db = 'bd_big_bread'
                )
            if self.conexion.is_connected():
            
             print ("LA CONEXION FUE EXITOSA") 
                   
        except:
            print(
"NO SE PUDO CONECTAR A LA BASE DE DATOS")
                            
def Insertar_Producto(self.producto):
    if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sentenciaSQL = "INSERT INTO Productos VALUES(%s,%s,%s,%s,%s,%s,null)"
            data = (producto.getiD_Producto(),
                    producto.getnombre_Producto(),
                    producto.getstock(),
                    producto.getprecio(),
                    producto.unidad_de_medida(),
                    producto.getiD_Receta)
            cursor.execute(sentenciaSQL,data)
            cursor.Conexion.commit()
            cursor.Conexion.close()
            print("productoinsertado correctamente")
               
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)

def  Listado_De_Productos(self):
        if self.conexión.is_connected():
            try:
                cursor  =  self.conexión.cursor() 
                sentenciaSQL  =  "SELEC * from Productos"
                cursor.execute(sentenciaSQL)
                resultados=  cursor.fetchall()
                cursor.Conexion.close()
                return resultados 
            except mysql:connector.Error as descripcionDelError:
        print("¡hubo un erroral intentar conectar a la Base de datos", decripcionDelError)