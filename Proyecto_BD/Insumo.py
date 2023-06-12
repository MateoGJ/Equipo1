class Insumo:
    ID_Insumo = 0,
    Nombre = "",
    Unidad_medida = "",
    Precio = 0,
    Stock_actual = 0,
    ID_Proveedor = 0     
        
    def __init__(self, id, nombre, unidad_medida, precio, stock_actual,id_Proveedor):
        self.ID = id
        self.Nombre = nombre
        self.Unidad_medida = unidad_medida
        self.Precio = precio
        self.Stock_actual = stock_actual
        self.ID_Proveedor = id_Proveedor