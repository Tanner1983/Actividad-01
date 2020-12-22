#Un profesor de enseñanza básica requiere de una aplicación que permita calcular el promedio de 4 notas.
#Se pide:
#1.	Solicitar nombre, apellido del alumno.
#2.	Solicitar las notas.
#3.	Calcular y mostrar el resultado obtenido y los datos del alumno.

nombre = input('Ingrese Nombre: ')
apellido = input('Ingrese Apellido: ')

nota1 = input('Ingrese nota 1: ')
nota2 = input('Ingrese nota 2: ')
nota3 = input('Ingrese nota 3: ')
nota4 = input('Ingrese nota 4: ')

promedio = (int(nota1) + int(nota2) + int(nota3) + int(nota4))/4


print('Don ' , nombre , ' ' , apellido , ' su promedio de notas es: ' , str(promedio))
