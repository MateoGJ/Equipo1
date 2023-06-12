class Proveedor:
    ID_Proveedor = 0,
    Nombre = "",
    Direccion = "",
    Telefono = 0,
    Correo = "" 

    def __init__(self, id, nombre, direccion, telefono, correo):
        self.ID = id
        self.Nombre = nombre
        self.Direccion = direccion
        self.Telefono = telefono
        self.Correo = correo