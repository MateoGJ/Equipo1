create database bd_big_bread;
use bd_big_bread;
create table productos (id_producto int,nombre varchar(45),descripcion varchar(45),
precio int,tiempo_de_reparacion int,
primary key (id_producto));

create table proveedores (id int ,nombre varchar (45),direccion varchar (45),
telefono int,correo varchar (45),
primary key (id));

create table productos_x_insumos (producto_id int,insumo_id int,cantidad int,orden int,procedimiento int,
primary key (producto_id),
foreign key (insumo_id) references producto(id_producto));

create table Insumos (id int,nombre_insumo  varchar(45),unidad_medida varchar (45),
precio int,stock_actual int,proveedor_id int,
primary key (nombre_insumo));

create table producciones_diarias (id int, fecha int, id_producto int, cantidad_producto int,
primary key (id));
