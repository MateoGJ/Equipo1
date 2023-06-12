import mysql.connector
import random

class Conectar_BD():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host= "localhost",
                port= 3306, 
                user= "root",
                password= 'maximiliano1o1o',
                db= "bd_big_bread",
                auth_plugin='mysql_native_password'
            )
            if self.conexion.is_connected():
                print("LA CONEXION FUE EXITOSA")

        except Exception as e:
            print(e),
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")


    def Insertar_Producto(self, producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO producto values(%s,%s,%s,%s,%s)"
                data = (
                        #producto.get_id_producto(),
                        random.randint(1,999),
                        producto.get_nombre_producto(),
                        producto.get_descripcion(),
                        producto.get_precio(),
                        producto.get_tiempo_preparacion(),
                        )
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()   
                print("Producto insertado correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)

        
    def Listado_De_Productos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM producto"
                cursor.execute(sentenciaSQL)
                resultados= cursor.fetchall()
                cursor.close()
                return resultados
                
            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)

    def Listado_Produccion_diaria(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM produccion_diaria"
                cursor.execute(sentenciaSQL)
                resultados= cursor.fetchall()
                cursor.close()
                return resultados
                
            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)    

    def Insertar_Produccion_diaria(self, produccion_diaria):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO producto values(%s,%s,%s)"
                data = (
                        #producto.get_id_producto(),
                        random.randint(1,999),
                        produccion_diaria.get_fecha(),
                        produccion_diaria.get_id_producto(),
                        produccion_diaria.get_cantidad_producida(),
                        )
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()   
                print("Producto insertado correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)    
        
                    