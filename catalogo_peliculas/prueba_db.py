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

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+db+';UID='+user+';PWD='+password
                              )
    print('Conexion exitosa,puedes continuar con el curso Giovanni')
except Exception as e:
    print(f'Error al intentar conectar la base de datos {e}')

#Returns a list of installed drivers.
#print(pyodbc.drivers())



'''
#Crear el cursor para almacenar la informción en memoria
cursor = conexion.cursor()
                #la informacion que vaya generando o extrayendo de SQL lo guardaremos en memoria
                #INFORMATION_SCHEMA se utiliza para acceder a la información de metadatos de la base de datos. Esta información incluye:
                # Nombre de la base de datos o tabla, Tipo de datos de una columna, Privilegios de acceso.
query_tablas = 'select * from information_schema.table'
query_columnas = 'select * from information_schema.columns'

#guardando las consultas como dataframes
df_tablas = pd.read_sql(query_tablas,conexion)
df_columnas = pd.read_sql(query_columnas,conexion)

#nos aseguramos de cerrar el cursor'''





'''
#para hacer la conexion a la base de dato pirmero debemos importar el modulo del gestor de la base de datos a usar

import pyodbc
import pandas as pd

                    #creamos la variable la cual recive el objeto  de tipo conexion que crearemos
                    #creacion del objeto de tipo conexion
                    #estos datos los debo de sacar del sql-server

Creamos 4 variables para crear la conexion con del servidor sql-server
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

'''
try:
    with conexion:
        #vamos a crear el cursor el cual nos permitira crear sentencias sql
        #cursor = conexion.cursor()
        with conexion.cursor() as cursor: #este with cierra el cursor
            sentencia = 'select * from persona where id_persona IN (1,2,3,4)'
            #id_persona = input('Proporciona el valor: ')
                #execute permite ejecutar la sentencia
            cursor.execute(sentencia)
                #El método recupera todas las filas (o todas las restantes) de un conjunto de resultados de una consulta y devuelve una lista de tuplas
            registros = cursor.fetchall() #fetchall retorna una lista, permite recuperar todos los registros fetchone retorna solo un registro
            for i in registros:
                print(f'{i}')

#cerrar la conexion a la base de datos, ya que tenemos abierto un objeto cursor
#cursor.close() al utilizar with ya no se requiere de cerrar el cursor, en automatico se cierra con with
except Exception as e:
     print(f'Ocurrio un error: {e}')
finally:
     conexion.close()



#Returns a list of installed drivers.
#print(pyodbc.drivers())


#%s = En Python, el marcador de posición %s sirve para indicar el tipo de variable que se quiere imprimir en una cadena.
# Para usar %s, se debe colocar el valor real después del operador %
'''
