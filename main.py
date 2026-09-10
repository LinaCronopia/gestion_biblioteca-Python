# Funciones para la interfaz de consola

from clases.inventario import Inventario
from clases.libro import Poesia, Prosa
from clases.prestamo import Prestamo
from clases.usuario import Usuario


def registrar_libro():
    tipo = input("Ingrese el tipo de libro: (prosa/poesia) ").strip().lower()
    numero = int(input("Ingrese el número de registro del libro: "))
    titulo = input("Ingrese el título del libro: ")
    anio_publicacion = input("Ingrese el año de publicación: ")
    editorial = input("Ingrese la editorial: ")

    if tipo == "prosa":
        autor = input("Ingrese el autor del libro (prosa): ")
        genero = input("Ingrese el género del libro (prosa): ")
        libro = Prosa(numero, titulo, anio_publicacion, editorial, autor, genero)

    elif tipo == "poesia":
        autor = input("Ingrese el autor del libro (poesía): ")
        pais = input("Ingrese el país del libro (poesía): ")
        libro = Poesia(numero, titulo, anio_publicacion, editorial, autor, pais)

    else:
        print("El tipo de libro no es válido")
        return

    return libro


def registrar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    direccion = input("Ingrese la dirección del usuario: ")
    telefono = input("Ingrese el teléfono del usuario: ")
    usuario = Usuario(nombre, direccion, telefono)

    return usuario


def registrar_prestamo(usuarios, inventario):
    nombre_usuario = input("Nombre del usuario: ")
    usuario = next((u for u in usuarios if u.nombre == nombre_usuario), None)
    if not usuario:
        print("Usuario no encontrado")
        return

    libros = []

    while True:
        titulo_libro = input("Ingrese el nombre del libro (dejar vacío para salir): ")
        if not titulo_libro:
            break
        libro = next(
            (lib for lib in inventario.lista_de_libros if lib.titulo == titulo_libro),
            None,
        )

        if libro:
            libros.append(libro)
        else:
            print("Libro no encontrado")

    if libros:
        prestamo = Prestamo(usuario, libros)
        prestamo.registrar_prestamo()
        print("El préstamo fue realizado con éxito")
    else:
        print("No se ha podido registrar el préstamo")


def mostrar_menu():
    print("\n --- Menú de gestión de la biblioteca --- ")
    print("1. Registrar usuario")
    print("2. Registrar libro")
    print("3. Registrar préstamo")
    print("4. Mostrar información de usuario")
    print("5. Mostrar información de libro")
    print("6. Salir")


def main():
    usuarios = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            usuario = registrar_usuario()
            if usuario:
                usuarios.append(usuario)
                print("Usuario registrado con éxito")

        elif opcion == "2":
            libro = registrar_libro()
            if libro:
                inventario.agregar_libro(libro)
                print("Libro registrado con éxito")

        elif opcion == "3":
            registrar_prestamo(usuarios, inventario)

        elif opcion == "4":
            for usuario in usuarios:
                print(usuario.mostrar_informacion())

        elif opcion == "5":
            for libro in inventario.lista_de_libros:
                print(libro.mostrar_informacion())
                if isinstance(libro, Prosa) or isinstance(libro, Poesia):
                    print(libro.mostrar_caracteristicas())

        elif opcion == "6":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida. Intente nuevamente")


if __name__ == "__main__":
    main()
