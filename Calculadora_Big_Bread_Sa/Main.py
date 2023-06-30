from Conexion import Conectar_BD
from Producto import Producto
from Proveedor import Proveedor
from Producto_x_Insumo import Producto_x_Insumo
from Insumo import Insumo
from ProduccionDiaria import ProduccionDiaria
from datetime import datetime

con = Conectar_BD()

def cargar_item_receta(producto_id):
    print("Vamos a cargar los ingredientes ")
    insumos = con.listado_Insumos()
    print(" # - INSUMO ")
    for indice, insumo in enumerate(insumos):
        print(" %s - %s " % (indice, insumo[1]))
    indice_insumo = int(input("Seleccione el insumo: "))
    insumo_id = insumos[indice_insumo][0]
    cantidad = int(input("Ingrese la cantidad requerida:"))
    orden = int(input("Ingrese el orden de los productos(del 1 en adelante...):"))
    procedimiento = 0
    receta = Producto_x_Insumo(producto_id, insumo_id, cantidad, orden, procedimiento)
    con.insertar_Receta(receta)
    cargar_mas_insumos = int(input("Perfecto! ¿Desea cargar otro ingrediente? (1 = SI - 2 = NO)"))
    if cargar_mas_insumos == 1:
        cargar_item_receta(producto_id)
    elif cargar_mas_insumos == 2:
        print("Listo!! receta cargada...") 
   

def listar_productos():
    productos = con.Listado_De_Productos()
    print(" # - PRODUCTO ")
    for indice, producto in enumerate(productos):
        print(" %s - %s " % (indice, producto[1]))
    indice_producto = int(input("Seleccione el producto: "))
    return productos[indice_producto]

def listar_insumos():
    insumos = con.listado_Insumos()
    print(" # - PRODUCTO ")
    for indice, insumo in enumerate(insumos):
        print(" %s - %s " % (indice, insumo[1]))
    indice_insumo = int(input("Seleccione el insumo: "))
    return insumos[indice_insumo]

def listar_producciones_diarias():
    producciones_diarias = con.Listado_Produccion_Diaria()
    print(" # - FECHA - PRODUCTO")
    for indice, produccion_diaria in enumerate(producciones_diarias):
        print(" %s - %s - %s" % (indice, produccion_diaria[1], produccion_diaria[2]))
    indice_produccion_diaria = int(input("Seleccione la producción: "))
    return producciones_diarias[indice_produccion_diaria]

def listar_recetas():
    productos = listar_productos()
    recetas = con.listado_Recetas(productos[0])
    print(" # - INGREDIENTES - CANTIDAD - ORDEN ")
    for indice, receta in enumerate(recetas):
        print(" %s - %s - %s - %s" % (indice, receta[1], receta[2], receta[3]))
    ingrediente = int(input("Seleccione el ingrediente: "))
    return recetas[ingrediente]

def principal():
    print("*******BIENVENIDO A LA CALCULADORA BIG BREAD SA***********")
    print("¿¿Que desea hacer hoy??")
    print("Ingresar, eliminar, modificar un producto: 1")
    print("Ingresar, eliminar, modificar un insumo: 2")
    print("Ingresar, eliminar, modificar la producción diaria: 3")
    print("Ingresar, eliminar, modificar un receta: 4")
    print("Listado de los productos: 5")
    print("Listado de producción total en un día especifico: 6")
    print("Listado de producción total en un periodo de tiempo: 7")
    print("Listado de la cantidad de insumos utilizados en un día: 8")
    print("SALIR: 0")
    ingresaProducto = int(input())
    if ingresaProducto == 0:
        return
    if ingresaProducto == 1:
        print("¿¿Que acción desea realizar??") 
        print("Ingresar un producto: 1")
        print("Eliminar un producto: 2")
        print("Modificar un producto: 3")
        accion = int(input())
        if accion == 1:
            nombre_Producto = input("Ingrese el nombre del producto:")
            descripcion = input("Ingrese el descripción del producto:")
            stock = int(input("Ingrese el stock del producto:"))
            precio = int(input("Ingrese el precio del producto:"))
            tiempo_Preparacion = input("Ingrese el tiempo de preparación del producto:")
            producto = Producto(0, nombre_Producto, descripcion, stock, precio, tiempo_Preparacion)
            con.Insertar_Producto(producto)

        
        elif accion == 2:
            producto = listar_productos()
            con.delete_Producto(producto[0])
            
        
        elif accion == 3:
            producto = listar_productos()
            nombre = input("Nombre (%s): " % (producto[1])) or producto[1]
            descripcion = input("Descripción (%s): " % (producto[2])) or producto[2]
            stock = input("Stock (%s): " % (producto[3])) or producto[3]
            precio = input("Precio (%s): " % (producto[4])) or producto[4]
            tiempo_preparacion = input("Tiempo preparación (%s): " % (producto[5])) or producto[5]
            record = Producto(producto[0], nombre, descripcion, stock, precio, tiempo_preparacion)
            con.update_Producto(record)

        
        else:
            print("¡¡Opción incorrecta!! Intente de nuevo...")
            ingresaProducto == 1
        
        
    elif  ingresaProducto == 2:
        
        print("¿¿Que acción desea realizar??") 
        print("Ingresar un insumo: 1")
        print("Eliminar un insumo: 2")
        print("Modificar un insumo: 3")
        accion = int(input())
        if accion == 1:
            proveedores = con.listado_Proveedores()
            nombre_insumo = input("Ingrese el nombre del insumo:")
            unidad_medida = input("Ingrese la unidad medida del insumo:")
            precio = int(input("Ingrese el precio del insumo:"))
            stock = input("Ingrese el stock actual del insumo:")
            print("---- Lista de proveedores ----")
            print(" ID - NOMBRE PROVEEDOR")
            for index, proveedor in enumerate(proveedores):
                    print("%s - %s" % (index, proveedor[1]))
            id_proveedor = int(input("Seleccione el proveedor actual del insumo:"))
            proveedor_seleccionado = proveedores[id_proveedor]
            insumo = Insumo(0, nombre_insumo, unidad_medida, precio, stock, proveedor_seleccionado[0])
            con.insertar_Insumo(insumo)
        
        elif accion == 2:
            insumo = listar_insumos()
            con.delete_Insumo(insumo[0])
        
        elif accion == 3:
            proveedores = con.listado_Proveedores()
            insumo = listar_insumos()
            nombre = input("Nombre (%s): " % (insumo[1])) or insumo[1]
            unidad = input("Unidad de medida (%s): " % (insumo[2])) or insumo[2]
            precio = input("Precio (%s): " % (insumo[3])) or insumo[3]
            stock = input("Stock (%s): " % (insumo[4])) or insumo[4]            
            print("Proveedor actual (%s) " % (insumo[5]))
            for index, proveedor in enumerate(proveedores):
                    print("%s - %s" % (index, proveedor[1]))
            id_proveedor = int(input("Seleccione el proveedor actual del insumo:"))
            proveedor_seleccionado = proveedores[id_proveedor]
            record = Insumo(insumo[0], nombre, unidad, precio, stock, proveedor_seleccionado[0] or insumo[5])
            con.update_Insumo(record)
        
        else:
            print("¡¡Opción incorrecta!! Intente de nuevo...")
            principal()
        

    elif ingresaProducto == 3:
        
        print("¿¿Que acción desea realizar??")
        print("Ingresar una producción diaria: 1")
        print("Eliminar una producción diaria: 2")
        print("Modificar una producción diaria: 3")
        accion = int(input())
        if accion == 1:
            
            productos = con.Listado_De_Productos()
            fecha = input("Ingrese la fecha de producción (formato dd/mm/aaaa): ")
            fecha_produccion = datetime.strptime(fecha, "%d/%m/%Y")

            id_producto = 0  
            cantidad_producto = 0  

            produccion_diaria = ProduccionDiaria(0, fecha_produccion, id_producto, cantidad_producto)
            con.Insertar_Produccion_Diaria(produccion_diaria)

            def Ingresar_productos_fecha():
                producto = listar_productos()
                cantidad_producto = int(input("Ingrese la cantidad del producto: "))
                produccion_diaria = ProduccionDiaria(0, fecha_produccion, producto, cantidad_producto)
                con.Insertar_Produccion_Diaria(produccion_diaria)
                cargar_mas_productos = int(input("Perfecto! ¿Desea cargar otro producto? (1 = SI - 2 = NO)"))
                if cargar_mas_productos == 1:
                    Ingresar_productos_fecha()
                elif cargar_mas_productos == 2:
                    print("Listo!! producción del día cargada...") 
                    principal()  

            Ingresar_productos_fecha()
        
        
        elif accion == 2:
            produccion_diaria = listar_producciones_diarias()
            con.delete_Produccion_Diaria(produccion_diaria[0])

        
        elif accion == 3:
            
            produccion_diaria = listar_producciones_diarias()
            fecha_produccion_inicio = produccion_diaria[1]
            lis_prod_diaria = con.listado_Produccion_Diaria_Fechas(fecha_produccion_inicio)
            print("Producto (%s) " % (produccion_diaria[2]))
            producto_id = listar_productos()
            cantidad_producto = int(input("Cantidad (%s): " % (produccion_diaria[3]))) or produccion_diaria[3]
            record = ProduccionDiaria(produccion_diaria[0], fecha_produccion_inicio, producto_id[0], cantidad_producto)
            con.update_Produccion_Diaria(record)
        
        else:
            print("¡¡Opción incorrecta!! Intente de nuevo...")
            principal()
        

    elif  ingresaProducto == 4:
        
        print("¿¿Que acción desea realizar??")
        print("Ingresar una receta: 1")
        print("Eliminar una receta: 2")
        print("Modificar una receta: 3")
        accion = int(input())
        if accion == 1:
            print("Para que producto desea crear una receta??")
            producto = listar_productos()
            cargar_item_receta(producto[0])
                     

        
        elif accion == 2:
            producto = listar_productos()
            con.delete_Receta(producto[0])

        
        elif accion == 3:
            insumo = listar_recetas()
            insumo = input("Ingrediente (%s): " % (insumo[1])) or insumo[1]
            cantidad = input("Cantidad (%s): " % (insumo[2])) or insumo[2]
            orden_insumos = input("Orden (%s): " % (insumo[3])) or insumo[3]
            procedimiento = 0
            record = Producto_x_Insumo(insumo[0], insumo, cantidad, orden_insumos, procedimiento)
            con.update_Receta(record)

        elif accion == 4:
            listar_recetas()
            
        else:
            print("¡¡Opción incorrecta!! Intente de nuevo...")
            principal()

    elif  ingresaProducto == 5:
        
        prod = con.Listado_De_Productos()
        print(" NOMBRE - STOCK - PRECIO - TIEMPO DE PREPARACIÓN ")
        for i in prod:
            print(" %s - %s - %s - %s " % (i[1], i[3], i[4], i[5]))


    elif  ingresaProducto == 6:
        
        productos_cantidad = {}
        fecha_inicio = input("Ingrese la fecha de produccion (formato dd/mm/aaaa): ")
        fecha_produccion_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        # 05/08/2023
        # 01/07/2020
        # 05/05/2023
        lis_prod_diaria = con.listado_Produccion_Diaria_Fechas(fecha_produccion_inicio)
        total_cantidad_producida = 0

        for index, produccion_diaria in enumerate (lis_prod_diaria):
            cantidad_producida = produccion_diaria[2]
            total_cantidad_producida += cantidad_producida
            cantidad_producto = productos_cantidad.get(produccion_diaria[1], 0); #si no está ya cargado, devuelve el 0.
            cantidad_producto += produccion_diaria[2]
            productos_cantidad[produccion_diaria[1]] = cantidad_producto

        print("PRODUCTO - CANTIDAD")
        for productoKey in productos_cantidad.keys():
            print("%s - %s" % (productoKey, productos_cantidad[productoKey]))
        print("La cantidad total producida es: %s" % total_cantidad_producida)
            
        
    elif ingresaProducto == 7:
        
        fecha_inicio = input("Ingrese la fecha de inicio (formato dd/mm/aaaa): ")
        fecha_produccion_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_fin = input("Ingrese la fecha de fin (formato dd/mm/aaaa): ")
        fecha_produccion_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")

        prod_diaria = con.listado_Produccion_Diaria_Fechas(fecha_produccion_inicio, fecha_produccion_fin)

        total_cantidad_producida = 0
        cantidad_producto = 0
        productos_cantidad = {}
        productos = con.Listado_De_Productos()
        lis_prod_diaria = con.Listado_Produccion_Diaria()
        
        print(" # -  FECHA  - PRODUCTO - CANTIDAD")

        for index, produccion_diaria in enumerate(prod_diaria):
            print(" %s - %s - %s - %s" % (index, produccion_diaria[0], produccion_diaria[1], produccion_diaria[2]))
            total_cantidad_producida += produccion_diaria[2]
            cantidad_producto = productos_cantidad.get(produccion_diaria[1], 0); #si no está ya cargado, devuelve el 0.
            cantidad_producto += produccion_diaria[2]
            productos_cantidad[produccion_diaria[1]] = cantidad_producto

        print("PRODUCTO - CANTIDAD")
        for productoKey in productos_cantidad.keys():
            print("%s - %s" % (productoKey, productos_cantidad[productoKey]))
            


        print("Cantidad total de productos realizada desde el %s hasta el %s es: %s " % (fecha_inicio, fecha_fin, total_cantidad_producida))
        
        # 01/01/2010
        # 01/01/2026

    elif  ingresaProducto == 8:
        fecha_produccion = listar_producciones_diarias()
        insumos_usados = con.listado_Insumos_Dia(fecha_produccion[1])
        print(" # - PRODUCTO - INSUMO - CANTIDAD")
        for index, insumo in enumerate(insumos_usados):
            print("%s - %s - %s - %s" % (index, insumo[0], insumo[1], insumo[2]))

    else:
        print("¡Opción incorrecta!")
        
    principal()

principal()