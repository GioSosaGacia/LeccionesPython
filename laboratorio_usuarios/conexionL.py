
from psycopg2 import pool
from logger_baseL import log
import sys

class Conexion:

    _DATABASE = 'test_db'
    _PASSWORD = '1993'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _USERNAME ='postgres'
    _MIN_CON = 1     #3N 3L POOL DE CONEXIONES siempre se debe de declarar un minimo y maximo de conexiones
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MAX_CON,cls._MAX_CON, #estas dos variables van al inico de la conexion
                                                      host = cls._HOST,
                                                      user =  cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.warning(f'Conexion del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.warning(f'Ocurrio un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        #OBTENER Pool no existe lo crea y si no lo retorna
        cls.obtenerPool().putconn(conexion) #putconn cierra la conexion que ya no se esta utilizando
        log.warning(f'Regresando la conexion al pool: {conexion}')

    @classmethod
    #cierra todas las conexiones dentro del pool de conexiones def obtenerPool
    def cerrarConexiones(cls):
        #OBTENER Pool no existe lo crea y si no lo retorna
        cls.obtenerPool().closeall()


conexion1 = Conexion.obtenerConexion()
conexion1 = Conexion.liberarConexion(conexion1)

