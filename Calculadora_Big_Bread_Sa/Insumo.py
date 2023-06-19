class Insumo:
    id_insumo = 0,
    nombre_insumo = "",
    unidad_medida = "",
    precio = 0,
    stock_actual = 0,
    id_proveedor = 0     
        
    def __init__(self, id_insumo, nombre_insumo, unidad_medida, precio, stock_actual, id_proveedor):
        self.id_insumo = id_insumo
        self.nombre_insumo = nombre_insumo
        self.unidad_medida = unidad_medida
        self.precio = precio
        self.stock_actual = stock_actual
        self.id_proveedor = id_proveedor