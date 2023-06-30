from Conexion import Conectar_BD
from Producto import Producto
from Producto_x_Insumo import Producto_x_Insumo
from Insumo import Insumo
from ProduccionDiaria import ProduccionDiaria
from datetime import datetime
import os

class MainApp():
    def __init__(self):
        self.con = Conectar_BD()

    def producto_crud(self):
        os.system('clear')
        print("¿¿Que acción desea realizar??") 
        print("------------------------------") 
        print("Ingresar un producto: 1")
        print("Eliminar un producto: 2")
        print("Modificar un producto: 3")
        accion = int(input())
        if accion == 1:
            nombre_Producto = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese el descripción del producto: ")
            stock = int(input("Ingrese el stock del producto: "))
            precio = int(input("Ingrese el precio del producto: "))
            tiempo_Preparacion = input("Ingrese el tiempo de preparación del producto: ")
            producto = Producto(0, nombre_Producto, descripcion, stock, precio, tiempo_Preparacion)
            self.con.Insertar_Producto(producto)

        
        elif accion == 2:
            producto = self.listar_productos()
            self.con.delete_Producto(producto[0])
        
        elif accion == 3:
            producto = self.listar_productos()
            nombre = input("Nombre (%s): " % (producto[1])) or producto[1]
            descripcion = input("Descripción (%s): " % (producto[2])) or producto[2]
            stock = input("Stock (%s): " % (producto[3])) or producto[3]
            precio = input("Precio (%s): " % (producto[4])) or producto[4]
            tiempo_preparacion = input("Tiempo preparación (%s): " % (producto[5])) or producto[5]
            record = Producto(producto[0], nombre, descripcion, stock, precio, tiempo_preparacion)
            self.con.update_Producto(record)

        else:
            print("¡¡Opción incorrecta!! Intente de nuevo...")
            self.producto_crud()

    def insumo_crud(self):
        os.system('clear')
        print("¿¿Que acción desea realizar??") 
        print("Ingresar un insumo: 1")
        print("Eliminar un insumo: 2")
        print("Modificar un insumo: 3")
        accion = int(input())
        if accion == 1:
            nombre_insumo = input("Ingrese el nombre del insumo:")
            unidad_medida = input("Ingrese la unidad medida del insumo:")
            precio = int(input("Ingrese el precio del insumo:"))
            stock = input("Ingrese el stock actual del insumo:")
            insumo = Insumo(0, nombre_insumo, unidad_medida, precio, stock)
            self.con.insertar_Insumo(insumo)
        
        elif accion == 2:
            insumo = self.listar_insumos()
            self.con.delete_Insumo(insumo[0])
        
        elif accion == 3:
            insumo = self.listar_insumos()
            nombre = input("Nombre (%s): " % (insumo[1])) or insumo[1]
            unidad = input("Unidad de medida (%s): " % (insumo[2])) or insumo[2]
            precio = input("Precio (%s): " % (insumo[3])) or insumo[3]
            stock = input("Stock (%s): " % (insumo[4])) or insumo[4]            
            record = Insumo(insumo[0], nombre, unidad, precio, stock)
            self.con.update_Insumo(record)
        
        else:
            print("¡¡Opción incorrecta!! Intente de nuevo...")
            self.insumo_crud()
 
    def produccion_diaria_crud(self):
        os.system('clear')
        print("¿¿Que acción desea realizar??")
        print("Ingresar una producción diaria: 1")
        print("Eliminar una producción diaria: 2")
        print("Modificar una producción diaria: 3")
        accion = int(input())

        if accion == 1:
            
            fecha = input("Ingrese la fecha de producción (formato dd/mm/aaaa): ")
            fecha_produccion = datetime.strptime(fecha, "%d/%m/%Y")
            producto = self.listar_productos()
            cantidad_producto = int(input("Ingrese la cantidad del producto: "))

            produccion_diaria = ProduccionDiaria(0, fecha_produccion, producto[0], cantidad_producto)
            self.con.Insertar_Produccion_Diaria(produccion_diaria)
        
        elif accion == 2:
            produccion_diaria = self.listar_producciones_diarias()
            self.con.delete_Produccion_Diaria(produccion_diaria[0])

        
        elif accion == 3:
            
            produccion_diaria = self.listar_producciones_diarias()
            fecha_produccion_inicio = produccion_diaria[1]
            lis_prod_diaria = self.con.listado_Produccion_Diaria_Fechas(fecha_produccion_inicio)
            print("Producto (%s) " % (produccion_diaria[2]))
            producto_id = self.listar_productos()
            cantidad_producto = int(input("Cantidad (%s): " % (produccion_diaria[3]))) or produccion_diaria[3]
            record = ProduccionDiaria(produccion_diaria[0], fecha_produccion_inicio, producto_id[0], cantidad_producto)
            self.con.update_Produccion_Diaria(record)
        
        else:
            print("¡¡Opción incorrecta!! Intente de nuevo...")
            self.produccion_diaria_crud()
 
    def receta_crud(self):
        os.system('clear')
        print("¿¿Que acción desea realizar??")
        print("Ingresar una receta: 1")
        print("Eliminar una receta: 2")
        print("Modificar una receta: 3")
        accion = int(input())

        if accion == 1:
            os.system('clear')
            print("Para que producto desea crear una receta??")
            producto = self.listar_productos()
            self.cargar_item_receta(producto[0])
        
        elif accion == 2:
            item = self.listar_recetas()
            self.con.delete_Receta(item[4], item[5])

        
        elif accion == 3:
            item = self.listar_recetas()
            cantidad = input("Cantidad (%s): " % (item[2])) or item[2]
            orden_insumos = input("Orden (%s): " % (item[3])) or item[3]
            procedimiento = 0
            record = Producto_x_Insumo(item[4], item[5], cantidad, orden_insumos, procedimiento)
            self.con.update_Receta(record)
        
        else:
            print("¡¡Opción incorrecta!! Intente de nuevo...")
            self.receta_crud()

    def cargar_item_receta(self, producto_id):
        os.system('clear')
        print("Vamos a cargar los ingredientes ")
        insumos = self.con.listado_Insumos()
        print(" # - INSUMO ")
        for indice, insumo in enumerate(insumos):
            print(" %s - %s " % (indice, insumo[1]))
        indice_insumo = int(input("Seleccione el insumo: "))
        insumo_id = insumos[indice_insumo][0]
        cantidad = int(input("Ingrese la cantidad requerida:"))
        orden = int(input("Ingrese el orden de los productos(del 1 en adelante...):"))
        procedimiento = 0
        receta = Producto_x_Insumo(producto_id, insumo_id, cantidad, orden, procedimiento)
        self.con.insertar_Receta(receta)
        cargar_mas_insumos = int(input("Perfecto! ¿Desea cargar otro ingrediente? (1 = SI - 2 = NO)"))
        if cargar_mas_insumos == 1:
            os.system('clear')
            self.cargar_item_receta(producto_id)
        elif cargar_mas_insumos == 2:
            print("Listo!! receta cargada...") 
    
    def listar_productos(self):
        productos = self.con.Listado_De_Productos()
        print(" # - PRODUCTO ")
        for indice, producto in enumerate(productos):
            print(" %s - %s " % (indice, producto[1]))
        indice_producto = int(input("Seleccione el producto: "))
        return productos[indice_producto]

    def listar_insumos(self):
        insumos = self.con.listado_Insumos()
        print(" # - PRODUCTO ")
        for indice, insumo in enumerate(insumos):
            print(" %s - %s " % (indice, insumo[1]))
        indice_insumo = int(input("Seleccione el insumo: "))
        return insumos[indice_insumo]

    def listar_producciones_diarias(self):
        producciones_diarias = self.con.Listado_Produccion_Diaria()
        print(" # - FECHA - PRODUCTO")
        for indice, produccion_diaria in enumerate(producciones_diarias):
            print(" %s - %s - %s" % (indice, produccion_diaria[1], produccion_diaria[2]))
        indice_produccion_diaria = int(input("Seleccione la producción: "))
        return producciones_diarias[indice_produccion_diaria]

    def listar_recetas(self):
        productos = self.listar_productos()
        recetas = self.con.listado_Recetas(productos[0])
        print(" # - INGREDIENTES - CANTIDAD - ORDEN ")
        for indice, receta in enumerate(recetas):
            print(" %s - %s - %s - %s" % (indice, receta[1], receta[2], receta[3]))
        ingrediente = int(input("Seleccione el ingrediente: "))
        return recetas[ingrediente]

    def productos_listado(self):
        os.system('clear')
        prod = self.con.Listado_De_Productos()
        print("NOMBRE \t STOCK \t PRECIO \t TIEMPO DE PREPARACIÓN ")
        print("-------------------------------------------------")
        for i in prod:
            print(" %s \t %s \t %s \t %s" % (i[1], i[3], i[4], i[5]))
        input("\nPresione ENTER para continuar")
        os.system('clear')


    def produccion_total_por_dia(self):
        os.system('clear')
        productos_cantidad = {}
        fecha_inicio = input("Ingrese la fecha de produccion (formato dd/mm/aaaa): ")
        fecha_produccion_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        lis_prod_diaria = self.con.listado_Produccion_Diaria_Fechas(fecha_produccion_inicio)
        total_cantidad_producida = 0

        for index, produccion_diaria in enumerate (lis_prod_diaria):
            cantidad_producida = produccion_diaria[2]
            total_cantidad_producida += cantidad_producida
            cantidad_producto = productos_cantidad.get(produccion_diaria[1], 0); #si no está ya cargado, devuelve el 0.
            cantidad_producto += produccion_diaria[2]
            productos_cantidad[produccion_diaria[1]] = cantidad_producto

        print("PRODUCTO \t CANTIDAD")
        for productoKey in productos_cantidad.keys():
            print("%s \t %s" % (productoKey, productos_cantidad[productoKey]))
        print("La cantidad total producida es: %s" % total_cantidad_producida)
        input("\nPresione ENTER para continuar")
        os.system('clear')
                
 
    def produccion_total_por_periodo(self):
        os.system('clear')
        fecha_inicio = input("Ingrese la fecha de inicio (formato dd/mm/aaaa): ")
        fecha_produccion_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_fin = input("Ingrese la fecha de fin (formato dd/mm/aaaa): ")
        fecha_produccion_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")

        prod_diaria = self.con.listado_Produccion_Diaria_Fechas(fecha_produccion_inicio, fecha_produccion_fin)

        total_cantidad_producida = 0
        cantidad_producto = 0
        productos_cantidad = {}
        print(" # \t FECHA \t PRODUCTO \ CANTIDAD")

        for index, produccion_diaria in enumerate(prod_diaria):
            print(" %s \t %s \t %s \t %s" % (index, produccion_diaria[0], produccion_diaria[1], produccion_diaria[2]))
            total_cantidad_producida += produccion_diaria[2]
            cantidad_producto = productos_cantidad.get(produccion_diaria[1], 0); #si no está ya cargado, devuelve el 0.
            cantidad_producto += produccion_diaria[2]
            productos_cantidad[produccion_diaria[1]] = cantidad_producto

        print("\n\nTOTAL PRODUCTO \t TOTAL CANTIDAD")
        for productoKey in productos_cantidad.keys():
            print("%s \t %s" % (productoKey, productos_cantidad[productoKey]))
            
        print("Cantidad total de productos realizada desde el %s hasta el %s es: %s " % (fecha_inicio, fecha_fin, total_cantidad_producida))
        input("\nPresione ENTER para continuar")
        os.system('clear')

    def insumos_utilizados(self):
        os.system('clear')
        insumos_usados  = self.con.listado_Insumos_Dia()
        print(" FECHA \t PRODUCTO \t INSUMO \t CANTIDAD")
        for index, insumo in enumerate(insumos_usados):
            print("%s \t %s \t %s \t %s" % (insumo[0], insumo[1], insumo[2], insumo[3]))
        input("\nPresione ENTER para continuar")
        os.system('clear')


    def run(self):
        try:
            print("*******BIENVENIDO A LA CALCULADORA BIG BREAD SA***********")
            print("-----------------------------------------------------------")
            print("¿¿Que desea hacer hoy??")
            print("1.- PRODUCTO")
            print("2.- INSUMO")
            print("3.- PRODUCCION DIARIA")
            print("4.- RECETA")
            print("5.- Listado de los productos")
            print("6.- Listado de producción total en un día especifico")
            print("7.- Listado de producción total en un periodo de tiempo")
            print("8.- Listado de la cantidad de insumos utilizados por día")
            print("SALIR: 0")

            menu = int(input())
            if menu == 0:
                return
            if menu == 1:
                self.producto_crud()
            elif menu == 2:
                self.insumo_crud()
            elif menu == 3:
                self.produccion_diaria_crud()
            elif menu == 4:
                self.receta_crud() 
            elif menu == 5:
                self.productos_listado()
            elif menu == 6:
                self.produccion_total_por_dia()
            elif menu == 7:
                self.produccion_total_por_periodo()
            elif  menu == 8:
                self.insumos_utilizados()
            else:
                print("¡Opción incorrecta!")
                
            #os.system('clear')
            self.run()

        except Exception as e:
            os.system('clear')
            print(e),
            print("Ocurrio un error: (%s)" % str(e))
            self.run()

os.system('clear')
app = MainApp()
app.run()