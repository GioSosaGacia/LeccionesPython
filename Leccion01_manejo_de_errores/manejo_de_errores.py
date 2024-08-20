#El trybloque le permite probar un bloque de código para detectar errores.
#El exceptbloque le permite gestionar el error.
#Exception es una de las clases padre para el manejo de errores
from Leccion01_manejo_de_errores.numerosEdenticosException import NumerosIdenticosException

#si vamos a utilizar variables fuera del try  no se declaran dentro del try
resultado = None

try:
#variables que solo se utilizan dentro del bloque try (variabkes locales
    a = int(input('Ingresa un valor A:'))
    b = int(input('Ingresa un valor B:'))
    if a == b:
    #raise nos permite lanzar o arrojar una excepcion
        raise  NumerosIdenticosException('Numeros identicos')
#dentro del try va la condicion
    resultado = a/b
#en el bloque de Exception puede haber mas de un bloque de manejo de excepciones para ser mas especificos con cada tipo de error
#se recomiendo usar las clases espeficias o hijas al inicio y la padre al final
#ya que si colocamos la padre al inicio con la Exception seria la primera que elegiria
except ZeroDivisionError as e:
    print(f'Ocurrio un error: {e}, {type(e)}')#type nos permite ver que tipo de excepcion se arrojo
except TypeError as e:
    print(f'Ocurrio un error: {e}, {type(e)}')
except ValueError as e:
    print(f'Ocurrio un error VE: {e}, {type(e)}')
except Exception as e: #al final va la clase de mayor gerarquia
    print(f'Ocurrio un error: {e}, {type(e)}')
#se utiliza/ejecuta en cazo de no haber lanzado ninguna exception
else:
    print('No se arrojo ninguna exception')
#siempre se ejecuta si ahi o no alguna exception
finally:
    print(f'Ejecucion del bloque finally ')


#despues del bloque try si todo sale bien se manda a imprimir el resultado
print(f'Resultado: {resultado}')
print('Continuamos...')
