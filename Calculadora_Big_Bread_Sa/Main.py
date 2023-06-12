from Conexion import Conectar_BD
from Producto import Producto

print("*******BIENVENIDO A LA CALCULADORA BIG BRED SA***********")
print("¿Quiere ingresar un producto?")
print("Para ingresar un producto ingrese 1")
print("Para ver el listado de los productos ingrese 2")
ingresaProducto = int(input())
if ingresaProducto == 1:
    con = Conectar_BD()
    nombre_Producto = input("Ingrese el nombre del producto:")
    descripcion = input("Ingrese el descripcion del producto:")
    precio = int(input("Ingrese el precio del producto:"))
    tiempo_Preparacion = input("Ingrese el tiempo de preparacion del producto:")
    producto = Producto(0, nombre_Producto, descripcion, precio, tiempo_Preparacion)
    con.Insertar_Producto(producto)
    
elif  ingresaProducto == 2:
    con = Conectar_BD()
    prod = con.Listado_De_Productos()
    for i in prod:
        print("Nombre: %s, descripcion: %s, precio: %s, tiempo de preparacion: %s" % (i[1], i[2], i[3], i[4]))
