
from Conexion import conectar 

Class Producto():
    Id_Producto = 0,
    Nombre_producto = "",
    stock =0,
    Precio = 0,
    Peso_gs= 0,
    Id_Receta =0 
    
    
    def _init_ (self,id_producto,nombre_producto,
                stock, precio,peso_gs,id_receta):
        self.ID_producto = id_producto
        self.Nombre_Producto = nombre_producto
        self.stock = stock
        self.precio = precio
        self.peso_gs = peso_gs
        self.Id_Reseta = id_receta
        
        
        
    
