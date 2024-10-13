import os 

# Lista de productos completa
productos = []


def cargar_datos():
    # Lógica para cargar los datos desde un archivo
    if os.path.exists('productos.txt'):
        with open('productos.txt', 'r') as file:
            for linea in file:
                try:
                    nombre, precio, cantidad = linea.strip().split(',')
                    productos.append({'nombre': nombre, 'precio': float(precio), cantidad: int(cantidad)})
                except ValueError:
                    print(f"Error: linea mal formateada: {linea}")
        print("Datos cargados exitosamente.")
    else:
        print("""    
                ▄  ▗▖▄▀▀▚▖▄  ▗▖    
                █  ▐▌█  ▐▌█  ▐▌    
                ▀▀▀▜▌█  ▐▌▀▀▀▜▌    
                   ▐▌▀▄▄▞▘   ▐▌         
              No se encuentran datos.
              """)
    

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
        productos.append({'nombre': nombre, 'precio': float(precio), 'cantidad': int(cantidad)})
        print(f"Producto {nombre} anhadido correctamente.")
    except ValueError:
            print("""                                      
                        .d88b. 888d888888d888 .d88b. 888d888 
                        d8P  Y8b888P"  888P"  d88""88b888P"   
                        88888888888    888    888  888888     
                        Y8b.    888    888    Y88..88P888     
                        "Y8888 888    888     "Y88P" 888 :  \n    
                                      
                        Los datos introducidos no son validos.
                        """)
    


def ver_productos():
    # Lógica para ver todos los productos
    if not productos:
        print("No tenemos productos en stock.")
    else:
        for i, producto in enumerate(productos, start=1):
            if all(key in producto for key in ['nombre','precio', 'cantidad']):         
                print(f"{i}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")
            else:
                print(f"Error: El producto {producto['nombre']} no tiene cantidad.")


def actualizar_producto():
    # Lógica para actualizar un producto
    ver_productos()
    try:
        indice = int(input("Selecciona el numero del producto que necesitas actualizar: ")) - 1
        if 0 <= indice < len(productos):
            print("1. Actualizar nombre")
            print("2. Actualizar precio")
            print("3. Actualizar cantidad")
            opcion = input("Elige una opcion para modificar los datos: ")

            if opcion == '1':
                nuevo_nombre = input("Escribe un nuevo nombre: ")
                productos[indice]['nombre'] = nuevo_nombre
            elif opcion == '2':
                nuevo_precio = float(input("Escribe un nuevo precio: "))
                productos[indice]['precio'] = nuevo_precio
            elif opcion == '3':                 
                nueva_cantidad = int(input("Escribe una nueva cantidad"))
                productos[indice]['cantidad'] = nueva_cantidad
            else:
                print("Opcion no valida")
        else: 
            print("""                                      
                        .d88b. 888d888888d888 .d88b. 888d888 
                        d8P  Y8b888P"  888P"  d88""88b888P"   
                        88888888888    888    888  888888     
                        Y8b.    888    888    Y88..88P888     
                        "Y8888 888    888     "Y88P" 888 :  \n                 
                        El numero del producto no es valido.
            """)    
    except ValueError:
        print("""                                      
                        .d88b. 888d888888d888 .d88b. 888d888 
                        d8P  Y8b888P"  888P"  d88""88b888P"   
                        88888888888    888    888  888888     
                        Y8b.    888    888    Y88..88P888     
                        "Y8888 888    888     "Y88P" 888 :  \n                 
                        Los datos introducidos no son validos.
            """)
def eliminar_producto():
    # Lógica para eliminar un producto
    ver_productos()
    try:
        indice = int(input("Selecciona el numero del producto que necesitas actualizar: ")) - 1
        if 0 <= indice < len(productos):    
            eliminado = productos.pop(indice)
            print(f"El producto '{eliminado['nombre']}' fue eliminado exitosamente")
        else: 
            print("Numero de producto no valido")
    except ValueError:
        print("""                                      
                        .d88b. 888d888888d888 .d88b. 888d888 
                        d8P  Y8b888P"  888P"  d88""88b888P"   
                        88888888888    888    888  888888     
                        Y8b.    888    888    Y88..88P888     
                        "Y8888 888    888     "Y88P" 888 :  \n                 
                        Los datos introducidos no son validos.
            """)


def menu():
    cargar_datos()
    while True:
        print("1: Añadir producto\n")
        print("2: Ver productos\n")
        print("3: Actualizar producto\n")
        print("4: Eliminar producto\n")
        print("5: Guardar datos y salir\n")

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
            print("Por favor, selecciona una opción válida")

 
menu()