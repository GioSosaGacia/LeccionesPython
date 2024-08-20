#Atributo de clase modifica todos loa objetos, no ahi necesidad de crear objetos para acceder al mismo
#Atributo de instancia solo  modifica el objeto que se desea
#Un objeto puede acceder al atributo de clase directamente sin entrar a mandar a llamar la clase


class Aritmetica:

#python usa la flexibilidad de constructores por lo cual podemos declarar mas de 1
#la cuestion es que siempre se tomara el ultimo constructor declarado
    '''def __init__(self,operando1):
        self.operando1 = operando1'''
#Atributo de clase
    atribito_de_clase = 12
    def __init__(self,operando1 = None,operando2 = None):
        self._operando1 = operando1
        self._operando2 = operando2

    @property
    def operando1(self):
        return self._operando1

    @operando1.setter
    def operando1(self,operando1):
        self._operando1 = operando1

    @property
    def operando2(self):
        return self._operando2

    @operando2.setter
    def operando2(self,operando2):
        self._operando2 = operando2

    def sumar(self):
        resultado =  self._operando1 + self._operando2 + Aritmetica.atribito_de_clase
        print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado =  self._operando1 - self._operando2
        print(f'Resultado resta: {resultado}')

    def multiplicar(self):
        resultado =  self._operando1 * self._operando2
        print(f'Resultado multiplicar: {resultado}')

    def dividir(self):
        resultado =  self._operando1 / self._operando2
        print(f'Resultado divición: {resultado}')

aritmrtica1 = Aritmetica(5,7)
aritmrtica1.sumar()
aritmrtica1.restar()
aritmrtica1.dividir()
aritmrtica1.multiplicar()

print(" ")
aritmrtica2 = Aritmetica(12,16)
aritmrtica2.sumar()
aritmrtica2.restar()
aritmrtica2.dividir()
aritmrtica2.multiplicar()


#utilizando el None nos permite usar este modo donde asignamos parametros de uno en uno
print('Tercer objeto')
aritmrtica3 = Aritmetica(2)
aritmrtica3.operando2 = 2
aritmrtica3.sumar()

print('Cuarto objeto')
aritmrtica4 = Aritmetica(10,10)
print(f'El valor del operando 1 = {aritmrtica4.operando1} y el Valor del operando 2 = {aritmrtica4.operando2}')
aritmrtica4.sumar()
