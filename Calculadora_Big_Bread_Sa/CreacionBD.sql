DROP DATABASE bd_big_bread;

CREATE DATABASE bd_big_bread;

USE bd_big_bread;

CREATE TABLE productos (
  id_producto int,
  nombre varchar(45),
  descripcion varchar(45),
  stock int,
  precio int,
  tiempo_de_preparacion int,
  PRIMARY KEY (id_producto)
);

CREATE TABLE insumos (
  id int,
  nombre_insumo varchar(45),
  unidad_medida varchar (45),
  precio int,
  stock_actual int,

  PRIMARY KEY (nombre_insumo)
);

CREATE TABLE productos_x_insumos (
  producto_id int,
  insumo_id int,
  cantidad int,
  orden int,
  procedimiento int,

  PRIMARY KEY (producto_id,insumo_id)
  -- FOREIGN KEY (producto_id) REFERENCES productos (id_producto),
  -- FOREIGN KEY (insumo_id) REFERENCES insumos (id)
);

CREATE TABLE producciones_diarias (
  id int,
  fecha date,
  id_producto int,
  cantidad_producto int,
  PRIMARY KEY (id)
);
