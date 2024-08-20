#encapsulamiento protegido y privado
#los metodos set y get solo se utilizan cuando vamos a trabajar fuera de la clase
class Coche:

    def __init__(self,marca,modelo,color):
        self._marca = marca #atributo publico
        self._modelo = modelo #protegido
        self._color = color #privado

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca : {self._marca}
        Modelo: {self._modelo}
        Coloe: {self._color}
''')

    @property # = propiedad de nuestra clase
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self,modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color = color


if __name__ == '__main__':
    coche1 =Coche('Kia','soul','Blanco')
    coche1.color = 'Rojo'
    coche1.marca = 'Jeep'
    coche1.modelo = 'Wangler'
    coche1.conducir()
    print(f'La marca del coche 1 es: {coche1.marca}')

    #Agregar un nuevo atributo a un objeto en especifico con setattr
    #recive el nombre del objeto, el atributo y el valor
    #no se asocio con el metodo conducir ya que no comparten los mismos atributos
    #no modifica los demas objetos
    setattr(coche1,'nuevo_atributo','Valor nuevo atributo')
    coche1.conducir()
    print(coche1.nuevo_atributo)

    coche2 = Coche('wv','Polo','Plata')
    coche2.conducir()

    #Para saber que atributos contiene cada objeto es con __dict__
    print(f'Atributos del objeto 1: {coche1.__dict__}')
