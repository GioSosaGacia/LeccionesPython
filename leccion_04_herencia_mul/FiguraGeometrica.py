#herencia multiple
#Los casos de herencia múltiple en python se dan cuando una clase
# secundaria o hija hereda atributos y metodos de mas de una
# clase principal o padre. Separada por una ,

#ABC = Abstract Base Class se utiliza para convertir a una clase en clase abstracta
# se debe de importar la clase ABC Y EL DECORADOR ABSTRACTMETHOD para definir un metodo abstracto

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self,ancho,alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo ancho: {ancho} ')
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo alto: {alto} ')

    @property
    def ancho(self):
        return self._ancho
#si queremos que un atributo sea de solo lectura no agregamos el metodo set
    @ancho.setter
    def ancho(self,ancho):
        if self._validar_valor(ancho):
             self._ancho = ancho
        else:
            print(f'Valor erroneo: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self,alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')

#Metodo abstracto se agrega despues de los metodos get y set:
    @abstractmethod
    def calcular_area(self):
        pass
        #no contiene implementacion ya que es un metodo abstrtato
        # solo se utiliza para obligar a agregarlo a las clases hijas donde si ahi objetos

    def __str__(self):
        return f'FiguraGeometrica Ancho: {self._ancho}, Alto: {self._alto}'

#encansulando el metodo no se usa fuera de esta clase mas que internamnete
    def _validar_valor(self,valor):
        return True if 0 < valor < 10 else False




#Metodo abstracto no tiene implementacion, pero si lo agregamos a la clase padre, se obliga agregarlo a las clses hijas
#fIGURA GEOMETRica no contiene el metodo de area ya que no sabe que tipo de
# figura geometrica debe de sacar el calculo
#Si afgregamos una clase abstracta toda la clase se hace abstracta
#no se podra crear objetos
#solo objetos de las clases hihas


