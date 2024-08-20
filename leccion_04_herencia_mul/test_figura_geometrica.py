from leccion_04_herencia_mul.Cuadrado import Cuadrado
from leccion_04_herencia_mul.FiguraGeometrica import FiguraGeometrica
from leccion_04_herencia_mul.rectangulo import Rectangulo

#no se puede instanciar una clase abstracta
#figura = FiguraGeometrica()

print('Creación Objeto Cuadrado'.center(40,'-'))
cuadrado1 = Cuadrado(lado = 5,color ='Rojo')
cuadrado1.ancho = -12
cuadrado1.alto = 11
print(cuadrado1)
print(f'Calculo del area de un cuadrado: {cuadrado1.calcular_area()}')

#cuando se trabaja con herencia multiple es importanta saber el orden
#con el cual se mandan a llamar las clases padre

#MRO - Method Resolution Order
#Esta función nos devuelve una tupla con el orden de búsqueda de
# los métodos. Como era de esperar se empieza en la propia clase
# y se va subiendo hasta la clase padre, de izquierda a derecha.
print(Cuadrado.mro())

print('Creación Objeto Rectangulo'.center(40,'-'))
rectangulo1 = Rectangulo(11,8,'Verde')
print(rectangulo1)
print(f'Calculo del area Rectangulo:{rectangulo1.calcular_area()}')

#al agregar el ABC se modifica el metodo resolution order
print(Cuadrado.mro())
