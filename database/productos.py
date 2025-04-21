from database.conexion import getConnection

def putProducto(nombreProducto, precioProducto):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''INSERT INTO productos(nombre, precio)
                VALUES(?,?)''',(nombreProducto, precioProducto))
    conn.commit()

def deleteProducto(idProducto):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''DELETE FROM productos WHERE id_producto = ?''',(idProducto,))
    conn.commit()

def selectProductos():
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''SELECT * FROM productos''')
    productos = cur.fetchall()
    return productos

def findProductoById(idProducto):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''SELECT * FROM productos WHERE id_producto = ?''', (idProducto, ))
    producto = cur.fetchone()
    return producto

def modifyProducto(idProducto,  nuevoNombre, nuevoPrecio):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''UPDATE productos
                SET nombre = ?, precio = ?
                WHERE id_producto = ?''', (nuevoNombre, nuevoPrecio, idProducto))
    
    conn.commit()