from sistema_biblioteca.biblioteca import Biblioteca
from sistema_biblioteca.libro import Libro

#Crear una Biblioteca
biblioteca = Biblioteca('Bienvenidos a la Biblioteca General de la UDG')
print(f'Nombre: {biblioteca._nombre}')

#Agregar libros a la biblioteca
biblioteca.agregar_libro('SQL','Giovanni','Informatica')
biblioteca.agregar_libro('Primeros auxilios','Ana','Salud')
biblioteca.agregar_libro('Python','Juan','Informatica')
biblioteca.agregar_libro('Anatomia de Gray','Nick','Saluc')
biblioteca.agregar_libro('SQL-Lite','Giovanni','Informatica')
biblioteca.agregar_libro('MySQL','Giovanni','Informatica')

#Contador de libros
print(f'Total de libros en stock: {Libro.contador_libros}')

#Mostrar libros:
biblioteca.mostrar_todos_los_libros()
#Mostrar libros por autor
biblioteca.buscar_libro_por_autor()
#Mostrar libros por genero
biblioteca.buscar_libro_por_genero()


##Ejemplo con los metodos creados por ubaldo
'''
libro1 = Libro('SQL','Giovanni','Informatica')
biblioteca.agregar_libro(libro1)

#Buscar libro por autor}}:
autor = 'Giovanni'
print(f'\nLibros de {autor}')
biblioteca.search_book_by_autor(autor)

#buscar libro por genero:
genero = 'Informatica'
print(f'\nLibros de {genero}')
biblioteca.search_book_by_autor(genero)

#mostar todos los libros
biblioteca.mostrar_todos_los_libros
'''
