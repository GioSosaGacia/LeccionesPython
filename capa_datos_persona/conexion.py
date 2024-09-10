import psycopg2 as bd #psycopg2 tambien nos da acceso al pool de conexiones
import logging as log
import sys
from psycopg2 import pool #para utilizar el pool lo importamos desde el psycopg2

class Conexion:

    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = '1993'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1     #3N 3L POOL DE CONEXIONES siempre se debe de declarar un minimo y maximo de conexiones
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls): #crea el objeto donde estan las conexiones 1 a 5
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user =  cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.warning(f'Creación de pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.warning(f'Ocurrio un error al obtenerl el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    #estas variables no se utulizaran son antes del pool
    #_conexion = None
    #_cursor = None

    @classmethod
    #obtener conexion proporsiona una de las 5 conexiones disponibles
    def obtenerConexion(cls): #obtener pool si aun no existe crea un objeto de conexion y si ya exist lo regresa para no estas duplicando objetos de conexion
        conexion = cls.obtenerPool().getconn() #getconn se encarga de regresar un objeto de conexion a la base de datos
        log.warning(f'Conexion obtenida del pool: {conexion}')
        return conexion

    #lIberar un objeto de conexion cuando se deje de utilIzar
    @classmethod
    def liberarConexion(cls,conexion):
        #OBTENER Pool no existe lo crea y si no lo retorna
        cls.obtenerPool().putconn(conexion) #putconn cierra la conexion que ya no se esta utilizando
        log.warning(f'Regresando la conexion al pool: {conexion}')

    @classmethod
    #cierra todas las conexiones dentro del pool de conexiones def obtenerPool
    def cerrarConexiones(cls):
        #OBTENER Pool no existe lo crea y si no lo retorna
        cls.obtenerPool().closeall()#

if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    #si agrego una conexion de mas marca error pool exhausted
    conexion6 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion6)
    conexion7 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion7)
    conexion8 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion8)
    conexion9 = Conexion.obtenerConexion()
    conexion10 = Conexion.obtenerConexion()

   #antes del pool
        #si conexion is None entonces se creara el objeto conexion
        #si exista ya no se crea
    '''def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
    #anteriormente me marcaba error  y consistia en que al usar log.debug no lo leia e incluso en info tampoco, por defaul inicia del warning
                #log.debug(f'Conexion exitosa: {cls._conexion}')
                log.warning(f'Conexion exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio un error al hacer la conexion: {e}')
                sys.exit()
        else:
            #si ya existe retorna la conexion
            return cls._conexion'''

    #@classmethod
    #def obtenerCursor(cls):
     #   pass

    '''
    #antes del pool
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:    #el objeto cursor se obtiene del objeto conexion
                cls._cursor = cls.obtenerConexion().cursor()
                log.warning(f'Se abrio correctamente la conexion: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio un error en el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor'''

#if __name__ == '__main__':
    #conexion1 = Conexion.obtenerConexion()
    #Conexion.obtenerCursor()
