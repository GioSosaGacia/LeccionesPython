#no debe de extnder de otra clase solo debe de usar los metodos enter y
# exit los cuales estan dentro de la clase object
#esta clase de manejo de archivos tambien la podemos utilizar para abrir un cerrar una base de datos


class ManejoArchivos:

    def __init__(self,nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Entrando al recurso'.center(50,'-'))
        self.nombre = open(self.nombre,'r',encoding='UTF-8')
        return self.nombre

#recibe mas parametros
#traceback(traza) toda la lista de errores si es que ocurrio alguno
#no es necesario utilizar todos los parametros pero si se deben de declarar si no marca error
    def __exit__(self,tipo_execion,valor_excepcion,traza_error):
        print('Cerramos el recurso'.center(50,'-'))
        #preguntar si el archivo esta apuntando a un objeto y si es asi esta abierto
        if self.nombre:
            #si esta abierto entonces lo cerramos
            self.nombre.close()

#El metodo enter lo podemos utilizar para la conexión a la base de datos y el exit para terminar tal conexión

