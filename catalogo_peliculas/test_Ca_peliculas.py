from catalogo_peliculas.dominio.Pelicula import Pelicula
from  catalogo_peliculas.servicio.catalogo_peliculas import CatalogoPeliculas as cp
opcion = None

while opcion != 4:
    try:
        print('Opciones:')
        print('1. Agregar Pelicula: ')
        print('2. Listar peliculas: ')
        print('3. Eliminar catalogo de peliculas: ')
        print('4. Salir')
        opcion = int(input('Selecciona una opcion: '))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error {e}')
        #delcaramos de nuevo la opcion no para que siga iterando el menu
        opcion = None
else:
    print('Saliendo...')
