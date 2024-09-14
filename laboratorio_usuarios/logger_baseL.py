#logging es una libreria que permite rastrear eventos que ocurren al ejecutar un software,
#los eventos se pueden mostrar en consola o se pueden guardar en un archivo, los logs ayudan a entender el comportamiento del programa y detectar errores
#logging cuenta con 5 capas  y por defecto funciona con la capa de warning

import logging as log

#basicConfig permite especificar el nivel que queremos usar los cuales son 5 y el mas basico es el debug y por "defecto warning"
# configura el controlador predeterminado para escribir los mensajes de depuración en un archivo

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',#aque hora ocurrio el error, nivel del error de los 5 que ahi, en que archivo arrojo el mensaje y en que linea paso y el mensaje del error
                datefmt='%I:%M:%S %p',#modificar la forma en la que semuestra la fecha hora,minutos,segundos y la p= pm)
                handlers=[
                    log.FileHandler('laboratorio_usuarios.log'),#para vigilar el archivo que se envia a logging y crear el archivo
                    log.StreamHandler()#StreamHandler es una subclase de la clase base Handler que se encarga de enviar mensajes de registro a la consola.
                ])

if __name__ == '__main__':
    log.debug('Error a nivel debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel de critical')


'''
El módulo logging también proporciona atributos que se pueden usar en la cadena de formato para incluir más información en los mensajes de registro, como:
%(asctime)s: La hora en que se registró el mensaje
%(name)s: El nombre del registrador
%(levelname)s: El nivel de registro
%(message)s: El mensaje de registro en sí
%(filename)s: El nombre del archivo del módulo en el que se creó el registrador
%(lineno)d: El número de línea del módulo en el que se creó el registrador
%(funcName)s: El nombre de la función en la que se creó el registrador 
https://docs.python.org/3/library/logging.html
'''
