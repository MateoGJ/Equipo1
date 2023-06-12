class produccionDiaria():
    id = 0,
    id_producto = 0,
    fecha = 0,
    cantidad_producto = 0,

    def __init__(self, id, fecha, id_producto, cantidad):
        self.id = id
        self.fecha = fecha
        self.id_producto = id_producto
        self.cantidad_producida = cantidad_producida


    def get_fecha(self):
        return self.fecha
    def get_cantidad_producto(self):
        return self.cantidad_producto
    
    
    def setid_fecha(self, fecha):
        self.fecha = fecha
    def setid_cantidad_producida(self, cantidad_producida):
        self.cantidad_producida = cantidad_producida