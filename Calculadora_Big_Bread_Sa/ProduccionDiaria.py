from Producto import Producto
from datetime import date
from datetime import datetime
class ProduccionDiaria():
    id = 0
    fecha = None
    id_producto = 0
    cantidad_producto = 0

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
    
    def set_id_produccion_diaria(self, id_produccion_diaria):
        self.id_produccion_diaria = id_produccion_diaria
    
    def set_fecha(self, fecha):
        if isinstance(fecha, str):
            fecha = datetime.strptime(fecha, "%d/%m/%Y")
        self.fecha = fecha
    
    def set_id_producto(self, id_producto):
        self.id_producto = id_producto
    
    def set_cantidad_producto(self, cantidad_producto):
        self.cantidad_producto = cantidad_producto