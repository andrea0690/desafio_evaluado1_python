precio_subscripcion = int(input('Ingrese el precio de la subscripcion: '))
numero_usuarios = int(input('Ingrese el número de usuarios: '))
gasto_total = float(input('Ingrese el gasto total: '))
utilidades_anterior = float(input('Ingrese el valor de las utilidades del año anterior: '))
razon_utilidades = 0

if utilidades_anterior == 0:
    print("No se puede calcular la razón porque las utilidades del año anterior son cero.")
else:
    razon_utilidades =((precio_subscripcion * numero_usuarios) - gasto_total) /utilidades_anterior
    
    print(f"La razón entre las utilidades actuales y las del año anterior es:{razon_utilidades:.2f}" )