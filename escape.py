from math import sqrt


radio = float(input('Ingrese el valor del radio en m : '))
gravedad = float(input('Ingrese el valor de la gravedad en m/s^2: '))


velocidad_escape = sqrt(2 * radio * gravedad)

print(f'El resultado de Velocidad de escape es:\n {velocidad_escape:.1f} m/s')
