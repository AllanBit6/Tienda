from database.conexion import getConnection

def putCliente(nombreCliente, emailCliente):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''INSERT INTO clientes(nombre, correo)
                VALUES(?,?)''',(nombreCliente, emailCliente))
    conn.commit()

def deleteCliente(idCliente):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''DELETE FROM clientes WHERE id_cliente = ?''',(idCliente,))
    conn.commit()

def selectClientes():
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''SELECT * FROM clientes''')
    clientes = cur.fetchall()
    return clientes

def findClienteById(idCliente):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''SELECT * FROM clientes WHERE id_cliente = ?''', (idCliente, ))
    cliente = cur.fetchone()
    return cliente

def modifyClient(idCliente,  nuevoNombre, nuevoEmail):
    conn = getConnection()
    cur = conn.cursor()

    cur.execute('''UPDATE clientes
                SET nombre = ?, email = ?
                WHERE id_cliente = ?''', (nuevoNombre, nuevoEmail, idCliente))
    
    conn.commit()