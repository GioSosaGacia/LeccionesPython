#Personalizar nuestras propias clases de excepciones personalizadas

class NumerosIdenticosException(Exception):

    def __init__(self,mensaje):
    #message es un atributo de la clase padre que se esta heredando de Exception
        self.message = mensaje



