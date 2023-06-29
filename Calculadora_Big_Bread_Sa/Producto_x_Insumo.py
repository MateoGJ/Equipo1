class Producto_x_Insumo():
    id_producto = 0,
    id_insumo = 0,
    cantidad = 0,
    orden_insumos = 0,
    procedimiento = 0,
    

    def __init__(self, id_Producto, id_insumo, cantidad, orden_insumos, procedimiento):
        self.id_producto = id_Producto
        self.id_insumo = id_insumo
        self.cantidad = cantidad
        self.orden_insumos = orden_insumos
        self.procedimiento = procedimiento

    def get_id_producto(self):
        return self.id_producto
    def get_id_insumo(self):
        return self.id_insumo
    def get_cantidad(self):
        return self.cantidad
    def get_orden_insumos(self):
        return self.orden_insumos
    def get_procedimiento(self):
        return self.procedimiento
    
    def set_id_producto(self, id_producto):
        self.id_producto = id_producto
    def set_id_insumo(self, id_insumo):
        self.id_insumo = id_insumo
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    def set_orden_insumos(self, orden_insumos):
        self.orden_insumos = orden_insumos
    def set_procedimiento(self, procedimiento):
        self.procedimiento = procedimiento