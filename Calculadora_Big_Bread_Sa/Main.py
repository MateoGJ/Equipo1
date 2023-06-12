from Conexion import Conectar_BD
from Producto import Producto
from ProducionDiaria import produccionDiaria

print("*******BIENVENIDO A LA CALCULADORA BIG BRED SA***********")
print("¿Quiere ingresar un producto?")
print("Para ingresar un producto ingrese 1")
print("Para ver el listado de los productos ingrese 2")
# print("Para ver el listado de la producción diaria ingrese 3")
# print("Para ingresar la producción diaria de un producto ingrese 4")
# print("Para ver la producción total en un periodo de tiempo ingrese 5")
# print("Para ver la cantidad de insumos utilizados en un día especifico ingrese 6")
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

# elif  ingresaProducto == 3:
#     con = Conectar_BD()
#     prod_diaria = con.Listado_Produccion_diaria()
#     for i in prod_diaria:
#         print("Fecha: %s, Producto: %s, Cantidad producida: %s" % (i[1], i[2], i[3]))

# elif  ingresaProducto == 4:
#     con = Conectar_BD()
#     fecha = input("Ingrese la fecha:")
#     id_producto = input("Ingrese el producto:")
#     cantidad_producida = int(input("Ingrese la cantidad producida:"))
#     produccion_diaria = produccionDiaria(fecha, id_producto, cantidad_producida)
#     con.Insertar_Produccion_diaria(produccion_diaria)

# elif  ingresaProducto == 5:
#     con = Conectar_BD()

# elif  ingresaProducto == 6:
#     con = Conectar_BD()