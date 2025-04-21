from database.productos import *

def agregarProducto(nombre, precio):

    if nombre != "" and isinstance(precio, int):
        putProducto(nombre, precio)
        print("Producto agregado con exito")
    else:
        print("Campos vacios, por favor de verificar")

def eliminarProducto(id):
    try:
        findProductoById(id)
        deleteProducto(id)
        print("Producto eliminado con exito")
    except:
        print("Producto no encontrado en la base de datos")

def editarProducto(id, nombre, precio):
    try:
        findProductoById(id)
        modifyProducto(id, nombre, precio)
        print("Producto actualizado con exito")
    except:
        print("Producto no encontrado en la base de datos")

def listarProductos():
    try:
        productos = selectProductos()

        for producto in productos:
            print(producto)
    except:
        print("Lista de productos vacia")

def buscarProductoPorId(id):
    try:
        producto = findProductoById(id)
        print(producto)
    except:
        print("Productos no encontrado en la base de datos")
