#logging es una libreria que permite rastrear eventos que ocurren al ejecutar un software,
#los eventos se pueden mostrar en consola o se pueden guardar en un archivo, los logs ayudan a entender el comportamiento del programa y detectar errores
#logging cuenta con 5 capas  y por defecto funciona con la capa de warning

#En Python, un handler es un objeto que se encarga de una tarea específica y que tiene una interfaz determinada. Es un recurso a donde vamos a mandar la informacion

import logging as log
#renombrando el paquete a un nombre mas corto
#log = logging
#basicConfig permite especificar el nivel que queremos usar los cuales son 5 y el mas basico es el debug y por "defecto warning"
# configura el controlador predeterminado para escribir los mensajes de depuración en un archivo.

#Depende de cual seleccionemos y de ahi parte en este caso no muetsra el debugg
#format permite dar un formato al mensaje que se arrojara
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',#aque hora ocurrio el error, nivel del error de los 5 que ahi, en que archivo arrojo el mensaje y en que linea paso
                datefmt='%I:%M:%S %p',#modificar la forma en la que semuestra la fecha, hora,minutos,segundos y la p= pm
                handlers=[
                    log.FileHandler('capa_datos.log'),#para vigilar el archivo que se envia a logging y crear el archivo
                    log.StreamHandler()#StreamHandler es una subclase de la clase base Handler que se encarga de enviar mensajes de registro a la consola.
                ])


if __name__ == '__main__':
    log.debug('Mensaje a nivel debbug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel de critical')

