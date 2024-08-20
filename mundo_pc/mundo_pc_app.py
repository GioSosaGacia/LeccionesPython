from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

print('Mundo PC')

teclado1 = Teclado('Lenovo','USB')
raton1 = Raton('Hp','USB')
monitor1 = Monitor('Lenovo','15 pulgadas')
computadora1 = Computadora('Lenovo',teclado1,raton1,monitor1)


teclado2 = Teclado('Gamer','USB')
raton2 = Raton('Gamer','USB')
monitor2 = Monitor('Gamer','30 pulgadas')
computadora2 = Computadora('Gamer',teclado2,raton2,monitor2)

#Crear lista de computadoras:
computadoras1 = [computadora1,computadora2]
#CREAR UNA ORDEN
orden1 = Orden(computadoras1)
#print(orden1)
orden2 = Orden(computadoras1)
print(orden2)

#metodo agregar computadorá
teclado3 = Teclado('Dell','USB')
raton3 = Raton('Dell','USB')
monitor3 = Monitor('Dell','30 pulgadas')
computadora3 = Computadora('Dell',teclado2,raton2,monitor2)
orden1.agregar_computadora(computadora3)
print(orden1)


