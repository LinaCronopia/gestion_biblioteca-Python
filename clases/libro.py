class Libro:
    def __init__(self, numero, titulo, anio_publicacion, editorial):
        self.numero = numero
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.editorial = editorial

    def actualizar_registro(self, numero=None, titulo=None, anio_publicacion=None, editorial=None):
        if numero:
            self.numero = numero
        if titulo:
            self.titulo = titulo
        if anio_publicacion:
            self.anio_publicacion = anio_publicacion
        if editorial:
            self.editorial = editorial
    
    def mostrar_informacion(self):
        return f"Número: {self.numero}, Título: {self.titulo}, Año de publicación: {self.anio_publicacion}, Editorial: {self.editorial}"

class Prosa(Libro):
    def __init__(self, numero, titulo, anio_publicacion, editorial, autor, genero):
        super().__init__(numero, titulo, anio_publicacion, editorial)
        self.autor = autor
        self.genero = genero

    def mostrar_caracteristicas(self):
        return f"Autor: {self.autor}, Género: {self.genero}"

class Poesia(Libro):
    def __init__(self, numero, titulo, anio_publicacion, editorial, autor, pais):
        super().__init__(numero, titulo, anio_publicacion, editorial)
        self.autor = autor
        self.pais = pais
    
    def mostrar_caracteristicas(self):
        return f"Autor: {self.autor}, País: {self.pais}"