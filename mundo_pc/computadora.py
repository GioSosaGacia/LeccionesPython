from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado


class Computadora:

    contador_computadoras = 0

    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

#el metodo __str__ manda a llamar al metodo str de cada clase las cuales ya
#estan asociadas a traves de self
    def __str__(self):
        #usamos una cadena multilinea
        return f'''Computadora: {self.nombre}:{self.id_computadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}'''

#codigo principal creando objetos de cada una de las clases:
if __name__ == '__main__':
    teclado1 = Teclado('Lenovo','USB')
    raton1 = Raton('Hp','USB')
    monitor1 = Monitor('Lenovo','15 pulgadas')
    computadora1 = Computadora('Lenovo',teclado1,raton1,monitor1)

#Al utilizar print rn automatico se manda a llamar el metodo str de las demas clases
    print(computadora1)

    teclado2 = Teclado('Gamer','USB')
    raton2 = Raton('Gamer','USB')
    monitor2 = Monitor('Gamer','30 pulgadas')
    computadora2 = Computadora('Gamer',teclado2,raton2,monitor2)
    print(computadora2)

