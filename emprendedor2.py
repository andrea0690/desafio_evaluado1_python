
precio_subscripcion = int(input('Ingrese el precio de la subscripcion: '))
usuario_normal = int(input('Ingrese el número de usuarios normales: '))
usuarios_premiun = int(input('Ingrese el número de usuarios premiun: '))
gasto_total = int(input('Ingrese el gasto total: '))


subs_premium = precio_subscripcion + (precio_subscripcion * 0.5) 


utilidad_total = ((precio_subscripcion * usuario_normal)+(subs_premium * usuarios_premiun))- gasto_total

print(f'La utilidad total es igual a : {utilidad_total}$')

