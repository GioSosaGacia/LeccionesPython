import psycopg2 as bd
import logging as log
import sys

class Conexion:

    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = '1993'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    @classmethod
        #si conexion is None entonces se creara el objeto conexion
        #si exista ya no se crea
    def obtenerConexion(cls):
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
            return cls._conexion

    @classmethod
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
            return cls._cursor

if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
