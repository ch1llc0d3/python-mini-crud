import os 


# Item
class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad 
        
class RegistroProducto: 
    def __init__(self):
        self.productos = []
        self.cargar_datos()

    # Mensajes de error reutilizables 
    def mensaje_error(mensaje):
        print("""                                      
                .d88b. 888d888888d888 .d88b. 888d888 
                d8P  Y8b888P"  888P"  d88""88b888P"   
                88888888888    888    888  888888     
                Y8b.    888    888    Y88..88P888     
                "Y8888 888    888     "Y88P" 888 :  \n    
                {mensaje}
            """)

    #cargar datos
    def cargar_datos(self):
        # Lógica para cargar los datos desde un archivo
        if os.path.exists('productos.txt'):
            with open('productos.txt', 'r') as file:
                for linea in file:
                    try:
                        id, nombre, precio, cantidad = linea.strip().split(',')
                        self.productos.append(Producto(int(id), nombre, float(precio), int(cantidad)))
                    except ValueError:
                        print(f"Error: linea mal formateada: {linea}")
            print("Datos cargados exitosamente.")
        else:
            print("No se encuentran datos...")
            

    # Guardar datos en un archivo
    def guardar_datos(self):
        # Lógica para guardar los datos en un archivo
        with open('productos.txt', 'w') as file:
            for producto in self.productos:
                file.write(f"{producto.id},{producto.name},{producto.precio},{producto.cantidad}\n")
                print("Datos guardados exitosamente.")

    # add producto
    def añadir_producto(self):
        # Lógica para añadir un producto
        nombre = input("Escribe el nombre del product: ")
        try:
            precio = float(input("Escribe el precio del producto: "))
            cantidad = int(input("Escribe la cantidad del producto: "))
            nuevo_id = len(self.productos) + 1
            producto = Producto(nuevo_id, nombre, precio, cantidad)
            self.productos.append(producto)
            print(f"Producto {nombre} anhadido correctamente.")
        except ValueError:
                self.mensaje_error("Los datos introducidos no son validos...")
        


    def ver_productos(self):
        # Lógica para ver todos los productos
        if not self.productos:
            print("No tenemos productos en stock.")
        else:
            print("Lista de productos:")
            for producto in self.productos:
                print(f"ID: {producto.id} - Nombre {producto.nombre} - Precio: {producto.precio} - Cantidad: {producto.cantidad}")


    def actualizar_producto(self):
        # Lógica para actualizar un producto
        self.ver_productos()
        try:
            id_product = int(input("Selecciona el ID del producto a actualizar: "))
            producto = next((p for p in self.productos if p.id == id_product), None)
            if producto:
                print("1. Actualizar nombre")
                print("2. Actualizar precio")
                print("3. Actualizar cantidad")
                opcion = input("Elige una opcion para modificar los datos: ")

                if opcion == '1':
                    producto.nombre = input("Escribe un nuevo nombre: ")
                elif opcion == '2':
                    producto.precio = float(input("Escribe un nuevo precio: "))
                elif opcion == '3':                 
                    producto.cantidad = int(input("Escribe una nueva cantidad"))
                else:
                    print("Opcion no valida")
            else: 
                self.mensaje_error("Numero de producto no valido...")
        except ValueError:
            self.mensaje_error("Los datos introducidos no son validos...")


    def eliminar_producto(self):
        # Lógica para eliminar un producto
        self.ver_productos()
        try:
            id_product = int(input("Selecciona el ID del producto a eliminar: "))
            producto = next((p for p in self.productos if p.id == id_product), None)
            if producto:
                self.productos.remove(producto)
                print(f"El producto '{producto.nombre}' fue eliminado exitosamente")
            else: 
                self.mensaje_error("Numero de producto no valido...")
        except ValueError:
            self.mensaje_error("Datos introducidos no son validos...")


    # Menu Principal
    def menu(self):
        self.cargar_datos()
        while True:
            print("\n--- Menu Principal ---")
            print("1: Añadir producto\n")
            print("2: Ver productos\n")
            print("3: Actualizar producto\n")
            print("4: Eliminar producto\n")
            print("5: Guardar datos y salir\n")

            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                self.añadir_producto()
            elif opcion == '2':
                self.ver_productos()
            elif opcion == '3':
                self.actualizar_producto()
            elif opcion == '4':
                self.eliminar_producto()
            elif opcion == '5':
                self.guardar_datos()
                print("Nos vemos pronto")
                break
            else:
                print("Por favor, selecciona una opción válida")

    
# Ejecucion del programa 
registro = RegistroProducto()
registro.menu()