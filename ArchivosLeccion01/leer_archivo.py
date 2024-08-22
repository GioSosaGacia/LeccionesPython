'''
"r" read abre un archivo para leer y si no existe marca error
"a" agregar/añadir abre un archivo para agregar  mas inf de la que ya contiene, si no existe el archivo lo crea
"w" escritura abre un archivo para escritura y si este no existe lo crea
"x"  crear un archivo, y si no existe envia una exception
t on b text and binary
"w+" para escribir y leer informacion o r+ ist the same
'''

#Para que abra el archivo, si estamos dentro de la misma carpeta no es nesesario agregar la ruta/caso contrario agrear ruta
#archivo = open('c://Python//POO//Leccion03//ArchivosLeccion01//prueba.txt','r', encoding='UTF-8')
#en mac so lo requiere una sola diagonal ya que es inversa
archivo = open('prueba.txt','r', encoding='UTF-8')
#print(archivo.read())

'''
#LEER algunos caracteres del archivo especificando la cantidad
print(archivo.read(9))

#leer lineas completas
print(archivo.readline())'''

#Iterar el  archivo
#for linea in archivo:
  #  print(linea)

#Leer todas las lineas con un solo metodo
#print(archivo.readlines()) #retorna una lista con el comtenido del archivo

#acceder a una sola linea que ya que es una lista
#print(archivo.readlines()[2])

#creamos un nuevo archivo
#a- anexar informacion si no existe el archivo lo crea
archivo2 = open('copia.txt', 'a', encoding='UTF-8')
archivo2.write(archivo.read()) #escribe y leer lo que tiene el archivo al archivo2

archivo.close()
archivo2.close()
print('Se copio y creo nuevo archivo de manera exitosa')

#read() solo se una una vez ya se si se imprime dos veces seguidas solo aplicara el primer read ya no ahi mas que leer en el segundo read
