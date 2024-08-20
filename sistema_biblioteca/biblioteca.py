from sistema_biblioteca.libro import Libro

class Biblioteca:

    def __init__(self,nombre):
        self._nombre = nombre
        self._libros = []

    def agregar_libro(self,titulo,autor,genero):
        libro = Libro(titulo,autor,genero)
        self._libros.append(libro)

    #Metodo del ejemplo de ubaldo
    def agregar_book(self,libro):
        self._libros.append(libro)

    def buscar_libro_por_autor(self):
        autor = input('Selecciona el autor: ')
        print(f'Autor del libro: {autor}')
        for libro in self._libros:
            if libro._autor.lower() == autor.lower():
                print(f'Descripcion libro: {libro._titulo}')

#Buscar libro autor del video ubaldo
    def search_book_by_autor(self,autor):
        for libro in self._libros:
            if libro._autor.lower() == autor.lower():
                self.mostrar_un_libro(libro)

#Buscar libro gener0 del video ubaldo
    def search_book_by_gender(self,genero):
        for libro in self._libros:
            if libro._genero.lower() == genero.lower():
                self.mostrar_un_libro(libro)


    def buscar_libro_por_genero(self):
        genero = input('Selecciona el Genero: ')
        print(f'Genero del libro: {genero}')
        for libro in self._libros:
            if libro._genero.lower() == genero.lower():
                print(f'Descripcion libro: {libro._titulo}')


    def mostrar_todos_los_libros(self):
        print(f'\n Total de libros en la biblioteca: {self._nombre}')
        for libro in self._libros:
            print(f'''Id:{libro._id}
            Titulo: {libro._titulo}
            Autor: {libro._autor} 
            Genero: {libro._genero}''')

#mostrar todos los libros de la biblioteca ubaldo
    def show_all_the_books(self,libro):
        print(f'\n Todos los libros de la biblioteca: {self._nombre}')
        for libro in self._libros:
            self.mostrar_un_libro(libro)


#ejemplo de mpostrar libro ubaldo
    def mostrar_un_libro(self,libro):
        print(f'Libro -> Titulo: {libro._titulo}, Autor: {libro._autor},'
              f'Genero: {libro._genero}')

    @property
    def nombre(self):
        return self._nombre
    @property
    def libros(self):
        return self._libros




