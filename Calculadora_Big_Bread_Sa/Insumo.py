class Insumo:
    id_insumo = 0,
    nombre_insumo = "",
    unidad_medida = "",
    precio = 0,
    stock = 0,
    id_proveedor = 0     
        
    def __init__(self, id_insumo, nombre_insumo, unidad_medida, precio, stock, id_proveedor):
        self.id_insumo = id_insumo
        self.nombre_insumo = nombre_insumo
        self.unidad_medida = unidad_medida
        self.precio = precio
        self.stock = stock
        self.id_proveedor = id_proveedor

    def get_id_insumo(self):
        return self.id_insumo
    def get_nombre_insumo(self):
        return self.nombre_insumo
    def get_unidad_medida(self):
        return self.unidad_medida
    def get_precio(self):
        return self.precio
    def get_stock(self):
        return self.stock
    def get_id_proveedor(self):
        return self.id_proveedor
    
    def set_id_insumo(self, id_insumo):
        self.id_insumo = id_insumo
    def set_nombre_insumo(self, nombre_insumo):
        self.nombre_insumo = nombre_insumo
    def set_unidad_medida(self, unidad_medida):
        self.unidad_medida = unidad_medida
    def set_precio(self, precio):
        self.precio = precio
    def set_stock(self, stock):
        self.stock = stock
    def set_id_proveedor(self, id_proveedor):
        self.id_proveedor = id_proveedor