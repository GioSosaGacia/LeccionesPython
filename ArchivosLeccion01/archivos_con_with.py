#con with se manera automatica abre y cierra el archivo
#a esto se le llama context manager o administrador de recursos
#wit usa dos metodos internos  __enter__ para abrir y __exit__ para cerrar
from ArchivosLeccion01.ManejoArchivos01 import ManejoArchivos

#with manda a llamar al metodo enter y exit
#with open('prueba.txt','r',encoding='UTF-8') as archivo:
with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
