#DAO Data Access Object y DAO tiene las operaciones CRUC(Create,Read,Update,Delete) una clase de entidad Persona
#DAO es un patron de diseño
#esta clase es la encargada de recuperar objetos

     #'''
     #este es un docString
     #'''
from capa_datos_persona.conexion import Conexion
from capa_datos_persona.cursor_del_pool import CursorDelPool
from capa_datos_persona.persona import Persona
from capa_datos_persona.logger_base import log


class PersonaDAO: #dao es un patron de diseño
#creacion de las variables de clase
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s, %s, %s)' #utilizamos el parametro posicional
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _DELETE = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        #Al mandar a llamar al cursor de manera indirecta se hace la conexiona la base de datos
        #para cerrar el uso del cursor de manera automatica y no manualmente utilizamos with ya que la cierra en automatico
       # with Conexion.obtenerCursor() as cursor: '''quitamos esta linea ya que se creo la clase cursor del pool donde se hace la conexion de manera manual con el metodo enter y exit

       with CursorDelPool() as cursor: #viene del archivo cursor_del_pool
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall() #creamos la variable registros para recuperarlos con fetchall permite recuperar todos los registros
            #creamos la lista de tipo persona
            personas = []
            #con el for no estamos recuperando el objeto si no una lista
            for registro in registros:#recorremos los registros con un for
                #debido a que estamos trabajando con un registro con ello crearemos los objetos de tipo persona
                persona = Persona(registro[0], registro[1], registro[2], registro[3] )#creando objeto de tipo persona con el indice de una lista
                personas.append(persona)#con append agregamos los objetos de tipo persona a persona
            return personas
#al finalizar se pasa al metodo exit y termina la conexion
    @classmethod
    def insertar(cls,persona):#recivimos un objeto de tipo persona para insertarlo a la base de datos
        #como se requiere de una transaccion, se requiere hacer la conexion
       #with Conexion.obtenerConexion() as conexion: se cambio por la linea de abajo'''
            #si existe la conexion retorna el cursor
           # with conexion.cursor() as cursor:'''

        #se cambio este with por los dos de arriba ya que en esta se hace la conexion de manera manual
        with CursorDelPool() as cursor: #viene del archivo cursor_del_pool
            #creamos una tupla de valores los cuales seran insertados y con el objeto persona mandamos a llamar a los atributos de nombre etc por el metodo get.
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)#corremos la transaccion  y la tupla de valores donde se almacenaran
            log.debug(f'Personas insertada: {persona}')
            return cursor.rowcount #retormanos la cantifdad de registros insertados

    @classmethod
    def actualizar(cls,persona):
       # with Conexion.obtenerConexion() as conexion:
        #    with conexion.cursor() as cursor:
        with CursorDelPool() as cursor: #viene del archivo cursor_del_pool
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'Se actualizo persona: {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls,persona):
       # with Conexion.obtenerConexion() as conexion:
        #    with conexion.cursor() as cursor:
        with CursorDelPool() as cursor: #viene del archivo cursor_del_pool
            valores = (persona.id_persona,)#se le agrega una coma al final ya que es una tupla
            cursor.execute(cls._DELETE,valores)
            log.debug(f'Persona eliminada: {persona}')
            return cursor.rowcount


if __name__ == '__main__':
    #eLIMINAR
    #persona1 = Persona(id_persona=12)
    #personas_eliminadas = PersonaDAO.eliminar(persona1)
    #log.debug(f'Personas eliminadas: {personas_eliminadas}')

     #actualizar
    #persona1 = Persona(10,'Jeiden','Sosa','jsosa@gmail.com')
    #personas_actualizadas =PersonaDAO.actualizar(persona1)
    #log.debug(f'Pernona actualiza: {personas_actualizadas}')

    #Insertar
    #creamos el objeto de tipo persona por varioble y nos por posicional
    #POSIblemete en este ya no se requiera de agregar el atributo id_persona ya que se agrego none a la clase persona de los atributos
    #persona1 = Persona(id_persona='',nombre='Mario',apellido='castañeda',email='mcastañeda@gmail.com' )
    #personas_insertadas = PersonaDAO.insertar(persona1)#retorna la cantidad de personas insetadas
    #log.debug(f'Personas insertadas: {personas_insertadas}')

    #seleccionar
    #creamos el objeto de tipo personas y lo recorremos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)




