from sqlite3 import *

def getConnection():
   db = connect("tienda.db")
   db.execute("PRAGMA foregin_keys = ON")

   cur = db.cursor()

   #Crear tabla de clientes
   cur.execute('''CREATE TABLE IF NOT EXISTS clientes(
               id_cliente INTEGER PRIMARY KEY AUTOINCREMENT, 
               nombre TEXT NOT NULL,
               correo TEXT NOT NULL UNIQUE)''')
   
   #Crear tabla productos
   cur.execute('''CREATE TABLE IF NOT EXISTS productos(
               id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               precio REAL NOT NULL)''')
   
   #Crear tabla pedidos
   cur.execute('''CREATE TABLE IF NOT EXISTS pedidos(
               id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
               id_cliente INTEGER NOT NULL,
               fecha DATE,
               
               FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente)
               )''')
   
   #Crear tabla detallesPedidos
   cur.execute('''CREATE TABLE IF NOT EXISTS detallesPedido(
               id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
               id_pedido INTEGER NOT NULL,
               id_producto INTEGER NOT NULL,
               cantidad INTEGER NOT NULL,
               
               FOREIGN KEY(id_pedido) REFERENCES pedidos(id_pedido),
               FOREIGN KEY(id_producto) REFERENCES productos(id_productos)
               )''') 
   db.commit()

   return db


