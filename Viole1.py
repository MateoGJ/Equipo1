import mysqyl.conector

from bd_big_bread import bd_big_bread
class Conectar ():
    def _init_ (auto) -> None:
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
            print ("NO SE PUDO CONECTAR A LA BASE DE DATOS")
                    
        finally:
            if self.conexion.is_connected():
                self.conexion.close()
                print("LA CONEXION FUE CERRADA")
                            
    
                
            
    def  Insertar_Producto (self, iD_Producto, nombre_Producto, stock, precio, unidad_de_medida, iD_Receta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO Productos VALUES(%s,%s,%s,%s,%s,%s)"
                datos = (iD_Producto, nombre_Producto, stock, precio, unidad_de_medida, iD_Receta)
                cursor.execute(sentenciaSQL, datos)
                cursor.conexion.commit()
                cursor.conexion.close()   
            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)

    def  Listado_De_Productos ( self ):
            si  uno mismo . conexión _está_conectado ():
                intentar :
                    cursor  =  uno mismo . conexión _cursor ()
                    sentenciaSQL  =  "SELECCIONAR * DE Productos"
                    cursor _ ejecutar ( sentenciaSQL )
                    resultados =  cursor . buscar ()
                    cursor _ Conexión _ cerca ()
                    devolver resultados

definitivamente  Insertar_Producto ( self , producto ):
    si uno mismo . conexión _ está_conectado ():
        prueba :
            cursor  = uno mismo . conexión _ cursor ()
            sentenciaSQL  =  "INSERT INTO valores de productos (null,%s,%s,%s,%s,null)"
            datos  = ( producto . getiD_Producto () ),
                    producto _ getnombre_Producto (),
                    producto _ obtener stock (),
                    producto _ obtener precio (),
                    producto _ getunidad_de_medida (),
                    producto _ getiD_Receta ()
                    )

            excepto  mysql . conector _ Error  como  descripcionDelError :
                print ( "Hubo un error al intentar conctar la Base de Datos" , descripcionDelError )
            cursor _ ejecutar ( sentenciaSQL , datos )
            cursor _ Conexión _ cometer ()
            cursor _ Conexión _ cerrar ()   
            print ( "Producto insertado correctamente" )

        excepto  mysql . conector _ Error  como  descripcionDelError :
            print ( "Hubo un error al intentar conctar la Base de Datos" , descripcionDelError )


    def  Listado_De_Productos ( self ):
        si  uno mismo . conexión _está_conectado ():
            intentar :
                cursor  =  uno mismo . conexión _cursor ()
                sentenciaSQL  =  "SELECCIONAR * DE Productos"
                cursor _ ejecutar ( sentenciaSQL )
                resultados =  cursor . buscar ()
                cursor _ Conexión _ cerca ()
                devolver resultados
def  Listado_De_Productos ( self ):
    si  uno mismo . conexión _está_conectado ():
        intentar :
            cursor  =  uno mismo . conexión _cursor ()
            sentenciaSQL  =  "SELECCIONAR * DE Productos"
            cursor _ ejecutar ( sentenciaSQL )
            resultados =  cursor .buscar ()
            cursor _ Conexión _cerrar ()
            devolver  resultados

            excepto  mysql . conector _ Error  como  descripcionDelError :
                print ( "Hubo un error al intentar conctar la Base de Datos" , descripcionDelError )
        excepto  mysql . conector _ Error  como  descripcionDelError :
            print ( "Hubo un error al intentar conctar la Base de Datos" , descripcionDelError )