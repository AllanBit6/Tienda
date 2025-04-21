from database.pedidos import *

def agregarPedido(idCliente, fecha):

    if isinstance(idCliente, int) and idCliente >= 0:
        putPedido(idCliente, fecha)
        print("Pedido agregado con exito")
    else:
        print("Campos vacios, por favor de verificar")

def eliminarPedido(id):
    try:
        findPedidoById(id)
        deletePedido(id)
        print("Pedido eliminado con exito")
    except:
        print("Pedido no encontrado en la base de datos")

def editarPedido(id, idCliente, fecha):
    try:
        findPedidoById(id)
        modifyPedido(id, idCliente, fecha)
        print("Pedido actualizado con exito")
    except:
        print("Pedido no encontrado en la base de datos")

def listarPedidos():
    try:
        pedidos = selectPedidos()

        for pedido in pedidos:
            print(pedido)
    except:
        print("Lista de pedidos vacia")

def buscarPedidoPorId(id):
    try:
        pedido = findPedidoById(id)
        print(pedido)
    except:
        print("Pedido no encontrado en la base de datos")