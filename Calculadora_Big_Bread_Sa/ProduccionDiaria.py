from Producto import Producto
from datetime import date, datetime
class ProduccionDiaria():
    id_produccion_diaria = 0,
    fecha = date.today(),
    id_producto = 0,
    cantidad_producto = [Producto.nombre_producto, 0]

    def __init__(self, id_produccion_diaria, fecha, id_producto, cantidad_producto):
        self.id_produccion_diaria = id_produccion_diaria
        self.fecha = fecha
        self.id_producto = id_producto
        self.cantidad_producto = cantidad_producto


    def get_id_produccion_diaria(self):
        return self.id_produccion_diaria
    def get_fecha(self):
        return self.fecha
    def get_id_producto(self):
        return self.id_producto
    def get_cantidad_producto(self):
        return self.cantidad_producto
    
    
    def setid_id_produccion_diaria(self, id_produccion_diaria):
        self.id_produccion_diaria = id_produccion_diaria
    def setid_fecha(self, fecha):
        self.fecha = fecha
    def setid_id_producto(self, id_producto):
        self.id_producto = id_producto
    def setid_cantidad_producto(self, cantidad_producto):
        self.cantidad_producto = cantidad_producto