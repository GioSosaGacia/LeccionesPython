#open permite abrir un archivo ya existente, o crear el archivo en caso de que
# no exista, leer o escribir inf a un archivo
#open recive dos argumentos el archivo y lo que se hará

#PARA hacer el uso de acentos debemos agregar la funcion encoding = 'UTF-8'
try:
    archivo = open('prueba.txt','w',encoding='UTF-8') #w = write permite escribir un archivo
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adios...')
except Exception as e:
    print(e)
#podemos utilizar finally para cerrar un archivo ya que finally se ejecuta si ahi o no un error
finally:
    archivo.close() #una vez cerrado el archivo ya no se puede escribir o leer
    print('Fin del archivo')
