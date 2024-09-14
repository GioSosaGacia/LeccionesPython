'''
DAO Data Accces Object
CRUD Create-Read-Update-Delete
'''
from cursor_del_poolL import CursorDelPool
from laboratorio_usuarios.usuarioL import Usuario
from logger_baseL import log

class UsuarioDao:

    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERT = 'INSERT INTO usuario(username,password) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMAR = ' DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            #definimos una lista la cual almacenara los objetos de tipo usuario
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls,usuario):
        with CursorDelPool() as cursor:
            #tupla de valores la cual sustituira cada uno de los valores posicionales de qwery insert
            valores = (usuario.username,usuario.password)
            cursor.execute(cls._INSERT,valores)
            log.warning(f'Usuario insertado: {usuario}')
            return cursor.rowcount #conteo de registros

    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
    #tupla de valores la cual sustituira cada uno de los valores posicionales
            valores = (usuario.username,usuario.password,usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls,usuario):
        with CursorDelPool() as cursor:
    #tupla de valores la cual sustituira cada uno de los valores posicionales
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMAR,valores)
            log.debug(f'Usuario eliminado: {usuario}')
            return cursor.rowcount

if __name__ == '__main__':
     #Insertar
    #creamos el objeto de tipo persona por varioble y nos por posicional
    #POSIblemete en este ya no se requiera de agregar el atributo id_persona ya que se agrego none a la clase persona de los atributos
    usuario1 = Usuario(id_usuario='',username='Mario',password='castañeda')
    usuarios_insertados = UsuarioDao.insertar(usuario1) #retorna la cantidad de usuarios insertadas
    log.debug(f'Usuarios insertados: {usuarios_insertados}')

    #seleccionar
    #usuarios = UsuarioDao.seleccionar()
    #for usuario in usuarios:
     #   log.debug(usuario)
