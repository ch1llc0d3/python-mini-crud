## Tarea Gestión de Productos

# 1. Versión recomendada
Al enviar una tarea, asegúrate de utilizar la siguiente versión:
Python 3.9.7 o superior

# 2. Propósito de la Tarea
Esta tarea tiene como objetivo evaluar tu capacidad para:

    Manejar estructuras de datos complejas en Python, como listas y diccionarios.

    Aplicar métodos avanzados de manipulación de datos.

    Crear un flujo de control robusto utilizando condicionales y bucles.

    Dividir el código en funciones/métodos para mejorar su mantenibilidad.

Objetivos específicos:

    Gestionar una lista de productos que contiene información detallada (nombre, precio, cantidad).

    Realizar operaciones CRUD (crear, leer, actualizar, eliminar) en la lista de productos.

    Persistir los datos de productos en un archivo.


## 3. Problema: Sistema de Gestión de Productos

Imagina que estás desarrollando un sistema básico de gestión de inventario de productos. Este sistema debe permitir a los usuarios realizar las siguientes operaciones:

    Añadir un producto: El usuario debe poder añadir un nuevo producto con nombre, precio y cantidad.

    Ver todos los productos: Mostrar una lista de todos los productos con su respectivo nombre, precio y cantidad.

    Actualizar un producto: Permitir al usuario modificar los detalles de un producto existente (nombre, precio o cantidad).

    Eliminar un producto: Eliminar un producto de la lista basándose en su nombre.

    Guardar los datos en un archivo: Los datos de los productos deben ser persistidos en un archivo productos.txt y cargados al inicio del programa.

 
 Requerimientos Específicos

productos = []

def añadir_producto():
    # Lógica para añadir un producto
    pass

def ver_productos():
    # Lógica para ver todos los productos
    pass

def actualizar_producto():
    # Lógica para actualizar un producto
    pass

def eliminar_producto():
    # Lógica para eliminar un producto
    pass

def guardar_datos():
    # Lógica para guardar los datos en un archivo
    pass
    
def cargar_datos():
    # Lógica para cargar los datos desde un archivo
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

 

## Funcionalidades detalladas

    Añadir producto: Pedir al usuario el nombre del producto, el precio y la cantidad disponible. Estos datos deben ser almacenados en un diccionario y añadidos a la lista de productos.

    Ver productos: Mostrar la lista completa de productos, formateada de manera clara para que se puedan ver el nombre, precio y cantidad de cada uno.

    Actualizar producto: Permitir al usuario seleccionar un producto existente para modificar su nombre, precio o cantidad.

    Eliminar producto: Eliminar un producto de la lista basándose en su nombre.

    Guardar datos: Al finalizar, se debe guardar la lista de productos en un archivo de texto. Cada producto debe ser almacenado en una línea del archivo en formato: nombre, precio, cantidad.

    Cargar datos: Al iniciar el programa, cargar los productos desde el archivo de texto, si existe.

## 4. Requisitos de aprobación

    Debes crear una estructura funcional con los métodos correctamente definidos y separados.

    El sistema debe funcionar correctamente para todas las opciones del menú (añadir, ver, actualizar, eliminar, guardar).

    Debes manejar los errores de entrada del usuario (por ejemplo, si se introduce un valor no numérico para el precio o cantidad).

    La lista de productos debe poder cargarse desde un archivo existente y ser actualizada.

    Los datos deben ser guardados en el archivo productos.txt al finalizar.

## 5. Método de presentación

Envía la URL de tu repositorio de GitHub.
