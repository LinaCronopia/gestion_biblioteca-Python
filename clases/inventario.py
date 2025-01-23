class Inventario: 
    def __init__(self):
        self.lista_de_libros = []
    
    def agregar_libro(self, libro):
        self.lista_de_libros.append(libro)
    
    def actualizar_inventario(self, libro, cantidad):
        for lib in self.lista_de_libros:
            if lib.nombre == libro.nombre:
                lib.actualizar_cantidad(cantidad)
    