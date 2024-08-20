#Clae padre o super clase, clase hija tambien conocidas como subclases
#De la clase padre se hereda a las clases hijas
#Una clase padre no puede acceder a los metodos de la clase hija
#solo son accesibles a partir de clases hijas

#polimorfismo
# (en POO) es la capacidad que tienen ciertos lenguajes para hacer
# que, al enviar el mismo mensaje (o, en otras palabras,
# invocar al mismo método) desde distintos objetos

class Animal:

    def comer(self):
        print('Como mas de tres veces al dia')

    def dormir(self):
        print('Duermo muchas horas')

#La flecha en una apunto hacia la clase de la cual esta heredando
#Para extender de una clase padre se crea la clase hija y entre paraentesis va la clase padre
#Con esto la clase perro podra acceder a los atributos y metodos de la clase padre
class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar'.center(40,'-'))

#sobreescritura del metodo dormir
#Hace referencia a la recreacion de un metodo de la clase padre a la hija
#modificando el comportamiento a las necesidades requeridas
#se recomienda utilizar el mismo nombre
    def dormir(self):
        print('Duermo 15 horas al día')

#polimorfismo se manda a llamar el metodo de la clase con menor gerarquia
#dependiendo de la clase que se este usando
#multiples comportamientos dependiendo con el tipo de dato que se este trabajando
class Gato(Animal):
    pass


#Programa principal
print('Ejemplo de herencia de la clase Animal a clase Perro'.center(50,'-'))
animal1 = Animal()
animal1.dormir()
animal1.comer()

print('\n Clase hija, Soy un Perro')
perro1 = Perro()
perro1.hacer_sonido()
perro1.comer()
perro1.dormir()#metodo sobreescrito de la clase hija.
