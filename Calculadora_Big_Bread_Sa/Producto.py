import Conexion
import mysql

class Producto():
    id_producto = 0,
    nombre_producto = "",
    descripcion = "",
    stock = 0,
    precio = 0,
    tiempo_preparacion = 0

    def __init__(self, id_producto, nombre_producto, descripcion, stock, precio, tiempo_preparacion):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.descripcion = descripcion
        self.stock = stock
        self.precio = precio
        self.tiempo_preparacion = tiempo_preparacion

    def get_id_producto(self):
        return self.id_producto
    def get_nombre_producto(self):
        return self.nombre_producto
    def get_descripcion(self):
        return self.descripcion
    def get_stock(self):
        return self.stock
    def get_precio(self):
        return self.precio
    def get_tiempo_preparacion(self):
        return self.tiempo_preparacion
    
    def set_id_producto(self, id_producto):
        self.id_producto = id_producto
    def set_nombre_producto(self,nombre_producto):
        self.nombre_producto = nombre_producto
    def set_descripcion(self,descripcion):
        self.descripcion = descripcion
    def set_stock(self,stock):
        self.stock = stock          
    def set_precio(self,precio):
        self.precio = precio
    def set_tiempo_preparacion(self,tiempo_preparacion):
        self.tiempo_preparacion = tiempo_preparacion

