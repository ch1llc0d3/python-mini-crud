import os 

# Lista de productos completa
productos = []


def cargar_datos():
    # Lógica para cargar los datos desde un archivo
    if os.path.exists('productos.txt'):
        with open('productos.txt', 'r') as file:
            for linea in file:
                nombre, precio, cantidad = linea.strip().split(',')
                productos.appent({'nombre': nombre, 'precio': float(precio), cantidad: int(cantidad)})
        print("Datos cargados exitosamente.")
    else:
        print("No se encuentran datos.")
    

def guardar_datos():
    # Lógica para guardar los datos en un archivo
    with open('productos.txt', 'w') as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
            print("Datos guardados exitosamente.")

def añadir_producto():
    # Lógica para añadir un producto
    nombre = input("Escribe el nombre del product: ")
    try:
        precio = float(input("Escribe el precio del producto: "))
        cantidad = int(input("Escribe la cantidad del producto: "))
        productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
        print(f"Producto '{nombre} anhadido correctamente.")
    except ValueError:
            print("Error: Los datos introducidos no son validos.")
    

def ver_productos():
    # Lógica para ver todos los productos
    if not productos:
        print("No tenemos productos en stock.")
    else:
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")

def actualizar_producto():
    # Lógica para actualizar un producto
    pass

def eliminar_producto():
    # Lógica para eliminar un producto
    pass




def menu():
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

 
