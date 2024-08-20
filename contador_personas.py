#metodo de clase se asocia con la clase y de instancia con los objetos los cuales reciven el parametro de self

class Persona:
    #atributo de clase
    contador_personas = 0

    def __init__(self,nombre,apellido):
        #Incrementamos el valor del atributo de clase ya que aumentara cada que se crea un objeto
        #Para acceder al atributo de clase se debe de acceder a la clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

#metodos de clase existen dos tipos con el decorador @staticmethod o @classmethod
    #Utiliza el nombre de la clase para llamar al metodo
    @staticmethod
    def get_contador_statico_personas():
        print('Contador personas statico')
        return Persona.contador_personas

    #Utiliza el parametro cls para mandar llamar al metodo
    @classmethod
    def get_contador_personas_clase(cls):
        print('Metodo de clase')
        return cls.contador_personas

persona1 = Persona('Giovanni', 'Sosa')
persona1.mostrar_persona()
persona2 = Persona('Angelica','Jaimez')
persona2.mostrar_persona()

#Saber cuantos objetos se han creado
print(f'Objetos creados = {Persona.contador_personas}')
#Imprimir el valor de contador personas con metodo de clase y metodo statico
print(f'Personas: {Persona.get_contador_statico_personas()}')
print(f'Contador objetos metodo de clase: {Persona.get_contador_personas_clase()}')


'''
1:contexto estatico es cuando trabajamos con metodos y atributos de la misma clase 
2:contexto dinamico es cuando creamos objetos una vez definida nuestra clase, objeto dinamico puede acceder al estatico
y el estatico al dinamico no
'''
