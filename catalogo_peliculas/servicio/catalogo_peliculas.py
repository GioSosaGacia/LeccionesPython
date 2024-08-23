import os

class CatalogoPeliculas:
    #variable de clase
    ruta_archivo = 'peliculas.txt'

    #classmethod tiene axceso directo a los metodos y variables de clase, los metodos estaticos no acceden de manera directa al contexto de clase
    @classmethod
    def agregar_pelicula(cls,pelicula):
        with open(cls.ruta_archivo,'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8' ) as archivo:
            print('Listado de peliculas: '.center(50,'-'))
            print(archivo.read())

#Para eliminar un archivo se requiere de importar la clase impor os (operating system)
    #Ya que contiene el metodo remove para eliminar archivos
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')
