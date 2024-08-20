from sistema_empleados.empleado import Empleado
from sistema_empleados.empresa import Empresa

print('Sistema empleados'.center(40,'-'))

#crear una instancia de una empresa
empresa1 = Empresa('Global Mentoring')


#Contratar algunos empleados
empresa1.contratar_empleado('Giovanni','Sistemas')
empresa1.contratar_empleado('Maria','Produccion')
empresa1.contratar_empleado('Hector','Sistemas')
empresa1.contratar_empleado('Aneliz','Enfermeria')

#Obtener el total de objetos de tipo empleado
print(f'Total de empleados:{Empleado.contador_empleados}')

#Obtener numero de empleados en el departamento de sistemas:
print(f'Empleados en el departamento de Sistemas:'
      f'{empresa1.obtener_numero_empleado_departamento("Sistemas")}')

#Mostrar los empleados de la empresa 1
print('Total de empleados'.center(50,'-'))
empresa1.obtener_total_empleados()
