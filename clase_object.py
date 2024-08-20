#por defaul se hereda de la clase object
class Persona():
    #init inicializa atributos de la clase
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    #sobreescribir el metodo str permite imprimir el valor de los atributos
    def __str__(self):
        return f'''Persona:
        Nombre = {self.nombre}
        Apellido = {self.apellido}
        #super permite acceder al comportamiento oculto de la clase padre 
        Dir. Mem = {super.__str__(self)}'''

persona1 = Persona('Giovanni','Sosa')
#Si no utilizamos el metodo str solo mandara a imprimir el objeto en memoria
print(persona1) #METODO __str__ se llama de manera automatica utilizando el metodo print

