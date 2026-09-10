class Prestamo:
    def __init__(self, usuario, lista_de_libros):
        self.usuario = usuario
        self.lista_de_libros = lista_de_libros

    def registrar_prestamo(self):
        self.usuario.registrar_prestamo(self)
        return f"Préstamo registrado con éxito: {self.mostrar_informacion()}"

    def mostrar_informacion(self):
        libros = ", ".join([libro.titulo for libro in self.lista_de_libros])
        return f"Usuario: {self.usuario.nombre}, Libros: {libros}"
