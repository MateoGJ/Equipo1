class ProduccionDiaria:
    ID = 0,
    ID_Producto = 0,
    Fecha = 0,
    Cantidad_Producto = 0,

    def __init__(self, id, fecha, id_producto, cantidad):
        self.ID = id
        self.Fecha = fecha
        self.ID_Producto = id_producto
        self.Cantidad = cantidad