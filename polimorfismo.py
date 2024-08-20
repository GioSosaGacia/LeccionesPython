#poliformismo: en el archivo de herencia ahi informacion sobre el tema
#polimorfismo
'''
El polimorfismo es la capacidad de objetos de diferentes clases para responder al mismo mensaje.
 En otras palabras, dos objetos de diferentes clases pueden tener métodos con el mismo nombre,
 y ambos métodos pueden ser llamados con el mismo código, dando respuestas diferentes.
'''

# (en POO) es la capacidad que tienen ciertos lenguajes para hacer
# que, al enviar el mismo mensaje (o, en otras palabras,
# invocar al mismo método) desde distintos objetos

#Polimorfismo
#Se comporta de multiples maneras dependiendo del tipo de dato con el que estamos trabajando
#al igual si existe la sobreescritura

class Animal:
    def hacer_sonido(self):
        print('Hago un pitido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

#funcion polimorfica / Duck-Typing

#Recive distintos tipos de datos de cualquier clase relacionada
#If it walks like a duck and it quacks like a duck, then it must be a duck
#Lo que se podría traducir al español como. Si camina como un pato y habla
# como un pato, entonces tiene que ser un pato.
def hacer_sonido_animal(animal):
    #depende lo que reciva es lo que hará
    animal.hacer_sonido()


print('***Ejemplo Polimorfismo***')
print('Clase padre Animal')
animal1 = Animal()
hacer_sonido_animal(animal1)

#definimos un obejto de la clase perro de la clase hija:
print('\n Clase hija Perro')
perro1 = Perro()
hacer_sonido_animal(perro1)

#Definimos un objeto de la clase hija gato
print('\nClase hija Gato')
gato1 = Gato()
hacer_sonido_animal(gato1)


#la clase object es la clase padre de todas las clases de forma directa
# e indirecta __str__ nos permite imprimir el estado de nuestro objetos
#__eq__ compara si dos objetos son iguales
