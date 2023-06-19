import Conexion
import mysql

class Producto():
    id_producto = 0,
    nombre_producto = "",
    descripcion = "",
    precio = 0,
    tiempo_preparacion = 0

    def __init__(self, id_producto, nombre_producto, descripcion, precio, tiempo_preparacion):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.descripcion = descripcion
        self.precio = precio
        self.tiempo_preparacion = tiempo_preparacion

    def get_id_producto(self):
        return self.id_producto
    def get_nombre_producto(self):
        return self.nombre_producto
    def get_descripcion(self):
        return self.descripcion
    def get_precio(self):
        return self.precio
    def get_tiempo_preparacion(self):
        return self.tiempo_preparacion
    
    def setid_producto(self, id_producto):
        self.id_producto = id_producto
    def setnombre_producto(self,nombre_producto):
        self.nombre_producto = nombre_producto
    def setdescripcion(self,descripcion):
        self.descripcion = descripcion
    def setprecio(self,precio):
        self.precio = precio
    def setgettiempo_preparacion(self,gettiempo_preparacion):
        self.gettiempo_preparacion = gettiempo_preparacion

