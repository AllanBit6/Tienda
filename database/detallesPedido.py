from database.conexion import getConnection

def putDetalle(idPedido, idProducto, cantidad):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''INSERT INTO detallesPedido(id_pedido, id_producto, cantidad)
                VALUES(?,?)''',(idPedido, idProducto, cantidad))
    conn.commit()

def deleteDetalle(idDetalle):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''DELETE FROM detallesPedido WHERE id_detalle = ?''',(idDetalle,))
    conn.commit()

def selectDetalle():
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''SELECT * FROM detallesPedido''')
    clientes = cur.fetchall()
    return clientes

def findDetalleById(idDetalle):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''SELECT * FROM detallesPedido WHERE id_detalle = ?''', (idDetalle, ))
    cliente = cur.fetchone()
    return cliente

def modifyDetalle(idDetalle,  nuevoPedido, nuevoProducto, nuevaCantidad):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''UPDATE detallesPedido
                SET id_pedido = ?, id_producto = ?, cantidad = ?
                WHERE id_pedido = ?''', (nuevoPedido, nuevoProducto, nuevaCantidad, idDetalle))
    
    conn.commit()