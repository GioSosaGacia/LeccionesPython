
#para hacer la conexion a la base de dato pirmero debemos importar el modulo del gestor de la base de datos a usar

import pyodbc as db
import pandas as pd

                    #creamos la variable la cual recive el objeto  de tipo conexion que crearemos
                    #creacion del objeto de tipo conexion
                    #estos datos los debo de sacar del sql-server

'''Creamos 4 variables para crear la conexion con del servidor sql-server'''
server = 'DESKTOP-9NNKTB8'
databa = 'test_db'
user = 'Giovanni'
password ='Uppercase1.'


#try:        #conect pasa un diccionario de datos
conexion = db.connect('DRIVER={ODBC Driver 17 for SQL server};'
                          'SERVER='+server+';'
                          'DATABASE='+databa+';'
                          'UID='+user+';'
                          'PWD='+password )
 #   print('Conexion exitosa,puedes continuar con el curso Giovanni')
#except Exception as e:
 #   print(f'Error al intentar conectar la base de datos {e}')'''

#al utilizar with de manera automatica se generan los cambios en la base de datos aplicando el commit o el rollback segun sea el caso
try:
    #autocommit por defaul es false y es como va ya que si esta en true aunque este mal la consulta se guardaran los datos
    #esta linea con el uso de with no se usa conexion.autocommit = False #SI lo cambiamos a true se omite la linea de conexion.commit() pero no es buena practica para el manejo de una transaccion
    with conexion:
        with conexion.cursor() as cursor:
    #se declara en el with cursor = conexion.cursor()
            sentencia = 'INSERT INTO persona(nombre,apellido,email) values(?,?,?)'
            valores = 'Saul','Jaimez','sjaimez@gamil.com'
            cursor.execute(sentencia,valores)

            sentencia = 'Update persona set nombre=?, apellido=?, email=? where id_persona=?'
            valores = ('Giovanni','Garcia','ggarcia@gmail.com',1)
            cursor.execute(sentencia,valores)

   #se omite con el uso de with conexion.commit() #si no hacemos commit no se guardan los cambios en caso de que este bien la consulta
    #se coloca despues de cerrar la conexion print('Termina la transaccion, se hizo commit ')
except Exception as e:
   #tambien se omite ya que lo incluye en automatico el with conexion.rollback()#se aplica cuando ahi un error en la transaccion
    print(f'Ocurrio un error, se hizo rollback de la transacción: {e}')
finally:
    conexion.close()

print('Termina la transaccion, se hizo commit ')
