#eSTE ARCHIVO LO QUE HACE ES ADMINISTRAR EL CURSOR

#with es conocido como resourse manager
#administra los objetos de conexion y el cursor para las sentencias a la base de datos
#donde el cursor se obtiene a traves de una conexion valida a traves del pool

from logger_base import log
from capa_datos_persona.conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

#resourse manager de manera manual lo iniciamos con __enter__ inicia la llamada a un recurso
#cuando termina el with se implementa el exit
#cuando inicia el bloque with se manda a llamar el metodo __enter__ para obtener la conexion
    def __enter__(self):
        log.debug(f'Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

#__exit__ esel metodo que se manda a llamar cuando termina el bloque with
     #exc_type = tio de la exepcion , exc_val = valor de la exepcion , exc_tb= traceback o detalle de la exepcion)
    #se ejecuta despues de haber ejecutado una sentencia sql
    def __exit__(self,tipo_exepcion, valor_exepcion, detalle_exepcion):
        log.debug(f'Se ejecuta metodo __exit__ ')
        if valor_exepcion:#si existe una exepcion hace rollback
            self._conexion.rollback()
            log.error(f'Ocurrio una exepcion, se hace rollback: {valor_exepcion }{tipo_exepcion} {detalle_exepcion}')
        else:
            self._conexion.commit() #si todo sale bien hace commit y guarda los cambion se las sentencias ejecutadas
            log.debug('Commit de la transaccion')
        self._cursor.close()#si todo sale bien cerramos y liberamos la conexion
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    #usamos with cuando lo implementamos de manera manual el resource manager o el with
    with CursorDelPool() as cursor: #se hace la conexion
        log.debug('Dentro del bloque with')
        cursor.execute('Select * From persona')
        log.debug(cursor.fetchall())

#fetchall recupera todos loa registros
