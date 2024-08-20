#
#
class Empleado:

    contador_empleados = 0

    def __init__(self,nombre,departamento):
        Empleado.contador_empleados += 1
        self.id = Empleado.contador_empleados
        self.nombre = nombre
        self.departamento = departamento

    @classmethod
    def total_empleados(cls):
        return cls.contador_empleados

