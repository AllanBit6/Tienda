from database.detallesPedido import *

def agregarDetalle(id_pedido, id_producto, cantidad):

    if id_pedido != 0 and id_producto != 0 and cantidad != 0:
        putDetalle(id_pedido, id_producto, cantidad)
        print("Detalle agregado con exito")
    else:
        print("Campos vacios, por favor de verificar")

def eliminarDetalle(id):
    try:
        findDetalleById(id)
        deleteDetalle(id)
        print("Detalle eliminado con exito")
    except:
        print("Detalle no encontrado en la base de datos")

def editarDetalle(id, pedido, producto, cantidad):
    try:
        findDetalleById(id)
        modifyDetalle(id, pedido, producto, cantidad)
        print("Detalle actualizado con exito")
    except:
        print("Detalle no encontrado en la base de datos")

def listarDetalles():
    try:
        detalles = selectDetalle()

        for detalle in detalles:
            print(detalle)
    except:
        print("Lista de detalles vacia")

def buscarDetalleporId(id):
    try:
        cliente = findDetalleById(id)
        print(cliente)
    except:
        print("Detalle no encontrado en la base de datos")
