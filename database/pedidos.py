from database.conexion import getConnection

def putPedido(cliente, fecha):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''INSERT INTO pedidos(id_cliente, fecha)
                VALUES(?,?)''',(cliente, fecha))
    conn.commit()

def deletePedido(idPedido):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''DELETE FROM pedidos WHERE id_pedido = ?''',(idPedido,))
    conn.commit()

def selectPedidos():
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''SELECT * FROM pedidos''')
    pedidos = cur.fetchall()
    return pedidos

def findPedidoById(idPedido):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''SELECT * FROM pedidos WHERE id_pedido = ?''', (idPedido, ))
    pedido = cur.fetchone()
    return pedido

def modifyPedido(idPedido,  nuevoIdCliente, nuevaFecha):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''UPDATE pedidos
                SET id_cliente = ?, fecha = ?
                WHERE id_pedido = ?''', (nuevoIdCliente, nuevaFecha, idPedido))
    
    conn.commit()