

from laboratorio_usuarios.usuarioDaoL import UsuarioDao
from laboratorio_usuarios.usuarioL import Usuario
from logger_baseL import log

opcion = None
while opcion != 5:
    print('Opciones:')
    print('1. Listar Usuarios')
    print('2. Insertar usuario')
    print('3. Actualizar usuario: ')
    print('4. Eliminar Usuario: ')
    print('5. Salir')
    opcion = int(input('Escribe tu opcion del 1-5: '))
    if opcion == 1:
#definimos la lista de tipo usuario y con usuarioDao interactuamos a nivel objeto y no registros
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.warning(usuario)
    elif opcion == 2:
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(username= username_var,password=password_var)
        usuarios_insertados = UsuarioDao.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion ==3:
        id_usuario_var = int(input('Escribe el id_usuario ha modificar: '))
        username_var = input('Escribe el nuevo user name: ')
        password_var = input('Escribe el nuevo password: ')
        usuario = Usuario(id_usuario_var,username_var,password_var)
        usuarios_actualizados = UsuarioDao.actualizar(usuario)
        log.warning(f'Usuarios actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input('Ingresa el id_usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDao.eliminar(usuario)
        log.warning(f'Usuarios eliminados: {usuarios_eliminados}')
    else:
        log.info('Salimos de la aplicación...')
