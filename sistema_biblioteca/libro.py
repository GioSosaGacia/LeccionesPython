class Libro:

    contador_libros = 0

    def __init__(self,titulo,autor,genero):
        Libro.contador_libros += 1
        self._id = Libro.contador_libros
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    @property
    def titulo(self):
        return self._titulo
    def autor(self):
        return self._autor
    def genero(self):
        return self._genero

