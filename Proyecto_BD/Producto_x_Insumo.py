class Producto_x_Insumo():
    ID_Insumo = 0,
    ID_Producto = 0,
    Cantidad = 0,
    Orden_insumos = 0,
    Procedimiento = "",
    

    def __init__(self, id_insumo, id_Producto, insumo, cantidad, orden_insumos, procedimiento):
        self.ID_Insumo = id_insumo
        self.ID_Producto = id_Producto
        self.Insumo = insumo
        self.Cantidad = cantidad
        self.Orden_insumos = orden_insumos
        self.Procedimiento = procedimiento