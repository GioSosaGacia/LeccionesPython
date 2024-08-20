#clase contiene atributos y  metodos
#atrubutos son las caracteristicas de nuestros objetos
#metodos son las acciones que pueden realizar nuestros objetos
#Instanciar una clase es la creacion de objetos

#Una clase se define en Mayuscula
#Un constructor es un metodo que se utiliza para crear un objeto
#self nos permite acceder a los atributos y metodos de nuestra clase

#encapsulamiento protegido _ y privado __ ambos necesitan los metodos set y get por cada atributo

#clase padre
class Persona:

     def __init__(self,nombre, edad):
         self.nombre = nombre
         self.edad  = edad

#str es sobreescritura donde un metodo de una clase padre lo volvemos a definir en una clase hija
     def __str__(self):
         return f'Persona: {self.nombre} Edad: {self.edad} '


#clase hija que hereda de la clase padre
class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        #super permite acceder a los metodos de la clase padre y estos agregarlos a la clase __init__ de empleado
        super().__init__(nombre,edad)
        self.sueldo = sueldo

#en este apartado se "sobreescribe el metodo" con str de persona a empleado con super(), despues a ello
    # solo se debe de agregrae el argumento restante
    def __str__(self):
        return f'{super().__str__()}, Empleado-Sueldo: {self.sueldo}'

empleado1 = Empleado('Mireya',59,5000)
print(empleado1.nombre)


#Direccion de memoria de los objetos creados con el usode id ' el objeto creado
print(f'Memoria objeto: {id(empleado1)}')
print(f'Memoria objeto: {hex(id(empleado1))}')

