fonasa = 0


nombre = input('Ingrese su nombre: ')
apellido = input('ingrese su apellido: ')
cargo =  input('Ingrese su cargo: ')

sueldoBase = input('Ingrese su sueldo base: ')
sueldoBase=int(sueldoBase)

fonasa = sueldoBase * 0.07
isapre = sueldoBase * 0.10
seguro = sueldoBase * 0.03

comision = input('Ingrese Comision (si no tiene ingrese 0): ')
adelanto = input('Ingrese adelanto (si no tiene ingrese 0): ')

dscto = int(fonasa) + int(isapre) + int(seguro) + int(comision) + int(adelanto)
liquido = int(sueldoBase) - int(dscto)


print('Se realizaran los siguientes descuentos')
print(' Fonasa: ' + str(fonasa) + '\n Isapre: ' + str(isapre) + '\n Seguro: ' + str(seguro) + '\n Comision: ' + str(comision) + '\n adelanto: ' + str(adelanto))

print('Don ' + nombre + ' ' + apellido + '  Cargo: ' + cargo)
print('Sueldo Base: ' + str(sueldoBase))
print('-----------------')
print('Total descuento: ' + str(dscto))
print('-----------------')
print('Sueldo liquido: ' + str(liquido))
print('-----------------')
