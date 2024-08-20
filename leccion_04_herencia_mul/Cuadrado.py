from leccion_04_herencia_mul.Color import Color
from leccion_04_herencia_mul.FiguraGeometrica import FiguraGeometrica

#es indispensable tener un orden al momento de importar varias clases

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):
#super() se utiliza cuando vamos a extender de una clase padre
#pero cuando ahi mas de una clase padre super() no sabe cual de las 2 usar primero
        #super().__init__() = con este nos muestra las clases padre que existem
#cuando existe mas de una clase que seran heredadas a otra hija lo ideal es hacerlo de esta manera:
#Desde la clase + __init__ + atributos
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} - {Color.__str__(self)}'
