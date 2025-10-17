create database camila;
use camila;
create table productos (id_producto int primary key,nombre varchar (150), descripcion varchar (300), precio_sin_iva int, tipo varchar (20) , cod_producto int);
create table pedidos (id_pedido int primary key, descripcion varchar (300),fecha date);
CREATE TABLE pedido_producto (
  id_pedprod INT,
  id_producto INT,
  id_pedido INT,
  precio INT,
  PRIMARY KEY (id_pedprod),
  CONSTRAINT fk_id_producto -- Se cambió el nombre de la restricción a un nombre más descriptivo
  FOREIGN KEY (id_producto) REFERENCES productos(id_producto), -- Se añadió la columna de referencia en la tabla 'productos'
  CONSTRAINT fk_id_pedido -- Se cambió el nombre de la restricción a un nombre más descriptivo
  FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido)
);
INSERT INTO productos (id_producto, nombre, descripcion, precio_sin_iva, cod_producto) VALUES 
(101, 'Laptop', 'i7, 16GB RAM', 1500000, '001'),
(102, 'Monitor', 'Alta resolución', 350000, '002'),
(103, 'Mouse', 'Inalámbrico USB', 250000, '003'),
(104, 'Teclado', 'Retroiluminado RGB', 750000, '004'),
(105, 'Camara', 'Full HD 1080p', 450000, '005');
select * from productos;
INSERT INTO pedidos (id_pedido, descripcion, fecha) VALUES
(1, 'Pedido Cliente A', '2024-05-10'),
(2, 'Pedido Cliente B', '2024-05-11'),
(3, 'Pedido Cliente C', '2024-05-11'),
(4, 'Pedido Cliente D', '2024-05-12'),
(5, 'Pedido Cliente E', '2024-05-13');
select * from pedidos;
INSERT INTO pedido_producto (id_pedprod, id_pedido, id_producto, precio) VALUES
(1001, 1, 101, 2000000),
(1002, 2, 103, 400000),
(1003, 3, 102, 300000),
(1004, 4, 104, 800000),
(1005, 5, 101, 500000);
select * from pedido_producto;
select sum(precio) as preciototalpedidos from pedido_producto; 
select min(precio_sin_iva) as preciosinivamasbajo from productos;