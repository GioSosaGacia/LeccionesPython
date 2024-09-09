
#investigar como hacer la conexion con sql server con la clase conexion en python
import pyodbc as dbs
import logging as log
import sys

class Conexion:

    '''Creamos 4 variables de clase para crear la conexion con del servidor sql-server'''


    _server = 'DESKTOP-9NNKTB8'
    _db = 'test_db'
    _user = 'Giovanni'
    _password ='Uppercase1.'
    _cursor = None
    _conexion = None


#try:        #conect pasa un diccionario de datos
   # _conexion = db.connect('DRIVER={ODBC Driver 17 for SQL server};'
    #                      'SERVER='+_server+';'
     #                     'DATABASE='+_db+';'
      #                    'UID='+_user+';'
       #                   'PWD='+_password )

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = dbs.connect('DRIVER={ODBC Driver 17 for SQL server};'
                          'SERVER='+cls._server+';'
                          'DATABASE='+cls._db+';'
                          'UID='+cls._user+';'
                          'PWD='+cls._password )
                log.warning(f'Conexion exitosa:  {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio una exepcion al obtener la conexion: {e}')
                sys.exit()#si existe alguna exepcion termina el programa
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.warning(f'Se abrio correcamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio una exepcion al obtener el cursor: {e}')
                sys.exit()
        else:
            return  cls._cursor

if __name__ == '__maim__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()

