from Conexion import Conectar_BD
from Producto import Producto
from Insumo import Insumo
from ProduccionDiaria import ProduccionDiaria
from datetime import date, datetime

print("*******BIENVENIDO A LA CALCULADORA BIG BREAD SA***********")
print("¿¿Que desea hacer hoy??")
print("Ingresar, eliminar, modificar un producto: 1")
print("Ingresar, eliminar, modificar un insumo: 2")
print("Ingresar, eliminar, modificar la producción diaria: 3")
print("Ingresar, eliminar, modificar un ¿receta?: 4")
print("Listado de los productos: 5")
print("Listado de producción total en un día especifico: 6")
print("Listado de producción total en un periodo de tiempo: 7")
print("Listado de la cantidad de insumos utilizados en un día: 8")
ingresaProducto = int(input())
if ingresaProducto == 1:
    print("¿¿Que acción desea realizar??") 
    print("Ingresar un producto: 1")
    print("Eliminar un producto: 2")
    print("Modificar un producto: 3")
    accion = int(input())
    if accion == 1:
        con = Conectar_BD()
        nombre_Producto = input("Ingrese el nombre del producto:")
        descripcion = input("Ingrese el descripción del producto:")
        precio = int(input("Ingrese el precio del producto:"))
        tiempo_Preparacion = input("Ingrese el tiempo de preparación del producto:")
        producto = Producto(0, nombre_Producto, descripcion, precio, tiempo_Preparacion)
        con.Insertar_Producto(producto)
    
    elif accion == 2:
        con = Conectar_BD()
    
    elif accion == 3:
        con = Conectar_BD()
    
    else:
        print("¡¡Opción incorrecta!! Intente de nuevo...")
        ingresaProducto == 1
    
    
elif  ingresaProducto == 2:
    con = Conectar_BD()
    print("¿¿Que acción desea realizar??") 
    print("Ingresar un insumo: 1")
    print("Eliminar un insumo: 2")
    print("Modificar un insumo: 3")
    accion = int(input())
    if accion == 1:
        con = Conectar_BD()
        nombre_insumo = input("Ingrese el nombre del insumo:")
        unidad_medida = input("Ingrese el unidad_medida del insumo:")
        precio = int(input("Ingrese el precio del insumo:"))
        stock_actual = input("Ingrese el stock_actual del insumo:")
        id_proveedor = input("Ingrese el proveedor actual del insumo:")
        insumo = Insumo(0, nombre_insumo, unidad_medida, precio, stock_actual, id_proveedor)
        con.Insertar_Insumo(insumo)
    
    elif accion == 2:
        con = Conectar_BD()
    
    elif accion == 3:
        con = Conectar_BD()
    
    else:
        print("¡¡Opción incorrecta!! Intente de nuevo...")
        ingresaProducto == 2
    

elif  ingresaProducto == 3:
    con = Conectar_BD()
    print("¿¿Que acción desea realizar??") 
    print("Ingresar una producción diaria: 1")
    print("Eliminar una producción diaria: 2")
    print("Modificar una producción diaria: 3")
    accion = int(input())
    produccion_diaria = con.Listado_Produccion_Diaria()
    if accion == 1:
        con = Conectar_BD()
        productos = con.Listado_De_Productos()
        print("Ingrese la fecha de producción (formato dd/mm/aaaa):")  

        day = int(input('Ingrese dia: '))
        month = int(input('Ingrese mes: '))        
        year = int(input('Ingrese año: '))

        fecha = date(year, month, day)
        print(fecha)
        
        def Ingresar_productos_fecha ():
            for index, producto in enumerate (productos):
                print("%s - %s" % (index, producto[1]))
            indice_producto = int(input("Seleccione el producto: "))
            producto_seleccionado = productos [indice_producto] 
            global producto_id
            global cantidad_producto
            producto_id = producto_seleccionado [0]  
            cantidad_producto = int(input("Ingrese la cantidad del producto: "))
            print("Perfecto! Desea cargar otro producto?? (1 = SI - 2 = NO)")
            cargar_mas_productos = int(input())  
            if  cargar_mas_productos == 1:
                Ingresar_productos_fecha()
            elif cargar_mas_productos == 2:
                global produccion_diaria 
                produccion_diaria = ProduccionDiaria(0, fecha, producto_id, cantidad_producto)
                con.Insertar_Produccion_Diaria(produccion_diaria)
        Ingresar_productos_fecha()
     
    
    elif accion == 2:
        con = Conectar_BD()
    
    elif accion == 3:
        con = Conectar_BD()
    
    else:
        print("¡¡Opción incorrecta!! Intente de nuevo...")
        ingresaProducto == 2
    

elif  ingresaProducto == 4:
    con = Conectar_BD()
    fecha = input("Ingrese la fecha:")
    id_producto = input("Ingrese el producto:")
    cantidad_producida = int(input("Ingrese la cantidad producida:"))
    produccion_diaria = ProduccionDiaria(fecha, id_producto, cantidad_producida)
    con.Insertar_Produccion_diaria(produccion_diaria)

elif  ingresaProducto == 5:
    con = Conectar_BD()
    prod = con.Listado_De_Productos()
    for i in prod:
        print("Nombre: %s, descripcion: %s, precio: %s, tiempo de preparacion: %s" % (i[1], i[2], i[3], i[4]))


elif  ingresaProducto == 6:
    con = Conectar_BD()
    prod_diaria = con.Listado_Produccion_Diaria()
    for index, produccion_diaria in enumerate (prod_diaria):
        print("%s - %s" % (index, produccion_diaria[1]))
    indice_fecha = int(input("Seleccione la fecha: "))
    fecha_seleccionado = prod_diaria [indice_fecha] 
    fecha_id = fecha_seleccionado [0]
    for i in prod_diaria:
        print("Producto: %s, Cantidad producida: %s" % (i[2], i[3]))
    for cantidad_producto in prod_diaria:
        prod_total_diaria = (i)
    print(f"Produccion total del día: {prod_total_diaria}")
        
    
elif  ingresaProducto == 7:
    con = Conectar_BD()
    insumos = con.Listado_De_Insumos()
    for index, insumo in enumerate (insumos):
        print("%s - %s" % (index, insumo[1]))
    indice_fecha = int(input("Seleccione la fecha: "))
    fecha_seleccionado = insumos [indice_fecha] 
    fecha_id = fecha_seleccionado [0]
    for i in insumos:
        print("Producto: %s, Cantidad utilizada: %s" % (i[2], i[3]))

elif  ingresaProducto == 8:
    con = Conectar_BD()
else:
    print("¡Opción incorrecta!")