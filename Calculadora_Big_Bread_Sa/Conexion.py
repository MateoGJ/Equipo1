import mysql.connector
import random

class Conectar_BD():
    def __init__(self) -> None:
        self.conexion = mysql.connector.connect(
            host= "localhost",
            port= 3306, 
            user= "root",
            password= 'maximiliano1o1o',
            db= "bd_big_bread",
            auth_plugin='mysql_native_password'
        )

    def Insertar_Producto(self, producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO productos (id_producto, nombre, descripcion, stock, precio, tiempo_de_preparacion) values(%s, %s, %s, %s, %s, %s)"
                data = (
                        #producto.get_id_producto(),
                        random.randint(1,999),
                        producto.get_nombre_producto(),
                        producto.get_descripcion(),
                        producto.get_stock(),
                        producto.get_precio(),
                        producto.get_tiempo_preparacion(),
                        )
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()   
                print("Producto insertado correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)

    def Insertar_Produccion_Diaria(self, produccion_diaria):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO producciones_diarias (id, fecha, id_producto, cantidad_producto) VALUES (%s, %s, %s, %s)"
                data = (
                    random.randint(1, 999),
                    produccion_diaria.get_fecha().strftime("%Y-%m-%d"),
                    produccion_diaria.get_id_producto(),
                    produccion_diaria.get_cantidad_producto(),
                )
                cursor.execute(sentenciaSQL, data)
                sentenciaSQL = "UPDATE productos SET stock = stock + %s WHERE id_producto = %s "
                data = (
                    produccion_diaria.get_cantidad_producto(),
                    produccion_diaria.get_id_producto(),
                )
                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                cursor.close()
                print("Producto insertado correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar con la Base de Datos:", descripcionDelError)

    def insertar_Insumo(self, insumo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO insumos values(%s, %s, %s, %s, %s)"
                data = (
                        random.randint(1,999),
                        insumo.get_nombre_insumo(),
                        insumo.get_unidad_medida(),
                        insumo.get_precio(),
                        insumo.get_stock(),
                        )
                print(sentenciaSQL % data)
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()   
                print("Insumo insertado correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)

    def insertar_Receta(self, receta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO productos_x_insumos values(%s, %s, %s, %s, %s)"
                data = (
                        receta.get_id_producto(),
                        receta.get_id_insumo(),
                        receta.get_cantidad(),
                        receta.get_orden_insumos(),
                        receta.get_procedimiento()
                        )
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()   
                print("Receta insertada correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)

    def update_Producto(self, producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE productos SET nombre = %s, descripcion = %s, stock = %s, precio = %s, tiempo_de_preparacion = %s WHERE id_producto = %s "
                data = (
                        producto.get_nombre_producto(),
                        producto.get_descripcion(),
                        producto.get_stock(),
                        producto.get_precio(),
                        producto.get_tiempo_preparacion(),
                        producto.get_id_producto(),
                        )
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()   
                print("Producto actualizado correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)

    def update_Insumo(self, insumo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE insumos SET nombre_insumo = %s, unidad_medida = %s, precio = %s, stock_actual = %s WHERE id = %s "
                data = (
                        insumo.get_nombre_insumo(),
                        insumo.get_unidad_medida(),
                        insumo.get_precio(),
                        insumo.get_stock(),
                        insumo.get_id_insumo()
                        )
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()   
                print("Producto actualizado correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)

    def update_Produccion_Diaria(self, produccion_diaria):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE producciones_diarias SET id_producto = %s, cantidad_producto = %s WHERE fecha = %s "
                data = (
                        produccion_diaria.get_id_producto(),
                        produccion_diaria.get_cantidad_producto(),
                        produccion_diaria.get_fecha()
                        )
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()   
                print("Producción actualizado correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)

    def update_Receta(self, receta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE productos_x_insumos SET producto_id = %s, insumo_id = %s, cantidad = %s, orden_insumos = %s, procedimiento = %s WHERE producto_id = %s "
                data = (
                        receta.get_id_producto(),
                        receta.get_id_insumo(),
                        receta.get_cantidad(),
                        receta.get_orden_insumos(),
                        receta.get_procedimiento()
                        )
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()   
                print("Producto actualizado correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)

    def delete_Producto(self, id_producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM producciones_diarias WHERE id_producto = %s " % (id_producto)
                cursor.execute(sentenciaSQL)            
                sentenciaSQL = "DELETE FROM productos WHERE id_producto = %s " % (id_producto)
                cursor.execute(sentenciaSQL)
                self.conexion.commit()
                cursor.close()   
                print("Producto eliminado correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)
    
    def delete_Insumo(self, id_insumo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM insumos WHERE id = %s " % (id_insumo)
                cursor.execute(sentenciaSQL)
                self.conexion.commit()
                cursor.close()   
                print("Insumo eliminado correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)

    def delete_Produccion_Diaria(self, id_produccion_diaria):
        if self.conexion.is_connected():
            try: 
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM producciones_diarias WHERE id = %s " % (id_produccion_diaria)
                cursor.execute(sentenciaSQL)
                self.conexion.commit()
                cursor.close()   
                print("Producción eliminada correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)

    def delete_Receta(self, id_producto):
        if self.conexion.is_connected():
            try: 
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM productos_x_insumos WHERE id = %s " % (id_producto)
                cursor.execute(sentenciaSQL)
                self.conexion.commit()
                cursor.close()   
                print("Receta eliminado correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)

    def Listado_De_Productos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM productos"
                cursor.execute(sentenciaSQL)
                resultados= cursor.fetchall()
                cursor.close()
                return resultados
                
            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)

    def listado_Insumos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM insumos"
                cursor.execute(sentenciaSQL)
                resultados= cursor.fetchall()
                cursor.close()
                return resultados
                
            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)

    def Listado_Produccion_Diaria(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = """SELECT * FROM producciones_diarias
                ORDER BY fecha"""
                cursor.execute(sentenciaSQL)
                resultados= cursor.fetchall()
                cursor.close()
                return resultados
                
            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError) 

    def listado_Produccion_Diaria_Fechas(self, fecha_produccion_inicio, fecha_produccion_fin = None):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = """SELECT pd.fecha, p.nombre, sum(pd.cantidad_producto) 
                FROM producciones_diarias pd 
                JOIN productos p on p.id_producto = pd.id_producto """
                clausula1 = "WHERE fecha BETWEEN '%s' AND '%s'" % (fecha_produccion_inicio, fecha_produccion_fin)
                clausula2 = "WHERE fecha = '%s'" % (fecha_produccion_inicio)
                sentenciaSQL = sentenciaSQL + (clausula1 if fecha_produccion_fin is not None else clausula2)
                sentenciaSQL += """
                GROUP BY pd.fecha, p.nombre
                ORDER BY pd.fecha""" 
                cursor.execute(sentenciaSQL)
                resultados= cursor.fetchall()
                cursor.close()
                return resultados
                
            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)   

    def listado_Insumos_Dia(self):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sentenciaSQL = """select pd.fecha, p.nombre, i.nombre_insumo, sum(pi.cantidad * pd.cantidad_producto)
                    from productos_x_insumos pi 
                    join producciones_diarias pd on pd.id_producto = pi.producto_id
                    join productos p on pd.id_producto = p.id_producto
                    join insumos i on i.id = pi.insumo_id 
                    group by pd.fecha, p.nombre, i.nombre_insumo
                    order by pd.fecha, p.nombre, i.nombre_insumo """ 
                    cursor.execute(sentenciaSQL)
                    resultados= cursor.fetchall()
                    cursor.close()
                    return resultados
                    
                except mysql.connector.Error as descripcionDelError:
                    print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)
    
    def listado_Recetas(self, productos):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = """select p.nombre as "producto", i.nombre_insumo, pi.cantidad, pi.orden, p.id_producto, i.id
                from productos_x_insumos pi 
                join productos p on p.id_producto = pi.producto_id  
                join insumos i on i.id = pi.insumo_id where p.id_producto = %s 
                order by p.id_producto, pi.orden LIMIT 0, 1000; """ % (productos)
                cursor.execute(sentenciaSQL)
                resultados= cursor.fetchall()
                cursor.close()
                return resultados
                
            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)        
                
    def delete_Receta(self, producto_id, insumo_id):
        if self.conexion.is_connected():
            try: 
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM productos_x_insumos WHERE producto_id = %s AND insumo_id = %s " % (producto_id, insumo_id)
                cursor.execute(sentenciaSQL)
                self.conexion.commit()
                cursor.close()   
                print("Receta eliminado correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)

    def update_Receta(self, receta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = """UPDATE productos_x_insumos SET insumo_id = %s, cantidad = %s, orden = %s, procedimiento = %s 
                WHERE producto_id = %s """
                data = (
                        receta.get_id_insumo(),
                        receta.get_cantidad(),
                        receta.get_orden_insumos(),
                        receta.get_procedimiento(),
                        receta.get_id_producto()
                        )
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()   
                print("Producto actualizado correctamente")

            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la Base de Datos", descripcionDelError)
