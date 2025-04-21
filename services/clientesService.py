from database.clientes import *

def agregarCliente(nombre, correo):

    if nombre != "" and correo != "":
        putCliente(nombre, correo)
        print("Cliente agregado con exito")
    else:
        print("Campos vacios, por favor de verificar")

def eliminarCliente(id):
    try:
        findClienteById(id)
        deleteCliente(id)
        print("Cliente eliminado con exito")
    except:
        print("Cliente no encontrado en la base de datos")

def editarCliente(id, nombre, email):
    try:
        findClienteById(id)
        modifyClient(id, nombre, email)
        print("Cliente actualizado con exito")
    except:
        print("Usuario no encontrado en la base de datos")

def listarClientes():
    try:
        clientes = selectClientes()

        for cliente in clientes:
            print(cliente)
    except:
        print("Lista de clientes vacia")

def buscarClienteporId(id):
    try:
        cliente = findClienteById(id)
        print(cliente)
    except:
        print("Cliente no encontrado en la base de datos")
