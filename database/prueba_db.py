#para hacer la conexion a la base de dato pirmero debemos importar el modulo del gestor de la base de datos a usar

import pyodbc
import pandas as pd

                    #creamos la variable la cual recive el objeto  de tipo conexion que crearemos
                    #creacion del objeto de tipo conexion
                    #estos datos los debo de sacar del sql-server

'''Creamos 4 variables para crear la conexion con del servidor sql-server'''
server = 'DESKTOP-9NNKTB8'
db = 'test_db'
user = 'Giovanni'
password ='Uppercase1.'


#try:        #conect pasa un diccionario de datos
conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};'
                          'SERVER='+server+';'
                          'DATABASE='+db+';'
                          'UID='+user+';'
                          'PWD='+password )
 #   print('Conexion exitosa,puedes continuar con el curso Giovanni')
#except Exception as e:
 #   print(f'Error al intentar conectar la base de datos {e}')'''


try:
    with conexion:
        #vamos a crear el cursor el cual nos permitira crear sentencias sql
        #cursor = conexion.cursor()
        with conexion.cursor() as cursor: #este with cierra el cursor
            #select
            #sentencia = 'select * from persona where id_persona IN (1,2,3,4)'
            #id_persona = input('Proporciona el valor: ')
                #execute permite ejecutar la sentencia
            #cursor.execute(sentencia)
                #El método recupera todas las filas (o todas las restantes) de un conjunto de resultados de una consulta y devuelve una lista de tuplas
            #registros = cursor.fetchall() #fetchall retorna una lista, permite recuperar todos los registros fetchone retorna solo un registro
            #for i in registros:
                #print(f'{i}')

            #insert
            #Nota: fila. Nosotros vamos a especificar los valores como signos de interrogación (?, ?) para indicarle que los valores reales serán
            # pasados como una tupla ( 'My Way', 15 ) en el segundo parámetro de la llamada a execute().
            #sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(?,?,?)'
            #para agregar varios valores debemos de hacer una tupla de tuplas y utilizar el executemany
            #valores = (('Clara','Canales','ccanales@gmail.com'),
             #          ('Juan','Velazco','jvelazco@gmail.com'),
              #         ('Olivia','Rara','orara@gmail.com'),
               #        ('Miguel','Perez','mperez@gmail.com')) #pasamos una tupla de valores

            #update
            #sentencia = 'Update persona Set nombre = ?, apellido = ?, email = ? where id_persona = ? '
            #valores = ('Juan','Garcia','jgarcia@gmail.com',1) #para actualizar varios registros es = a insertar varios

            #delete
            #sentencia = 'delete from persona where id_persona IN ? '
            #entrada = input('Proporciona los valores a eliminar separados por una coma(,): ')
            #valores = (tuple(entrada.split(',')),)
            sentencia = 'delete from persona where id_persona = ? '
            valores = (4,)
            cursor.execute(sentencia,valores)
            #conexion.commit() #commit guarda los cambios es la base de datos, al usar with el commit se ejecuta en automatico, no ahi necesidad de colocarlo
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')


#cerrar la conexion a la base de datos, ya que tenemos abierto un objeto cursor
#cursor.close() al utilizar with ya no se requiere de cerrar el cursor, en automatico se cierra con with
except Exception as e:
     print(f'Ocurrio un error: {e}')
finally:
     conexion.close()



#Returns a list of installed drivers.
#print(pyodbc.drivers())


#%s = En Python, el marcador de posición %s sirve para indicar el tipo de variable que se quiere imprimir en una cadena.
# Para usar %s, se debe colocar el valor real después del operador % en este caso se utiliza ?
