# coding=utf-8
# Calculadora de parámetros de antenas. 
# @author Matias Serino Marin
import math
salir = False

while(salir != True):

	print("Calculadora de longitud de antenas");

	velOndaVacio =  299792458
	velOndaAire = 284802835.1

	a = int(input("Seleccione medio: 1 = aire, 2 = vacío"))

	if(a == 1):
		velocidad = velOndaAire
	if(a == 2):
		velocidad = velOndaVacio
	

	frec = int(input("Ingrese frecuencia en hertz:"))
	velocidad = float(velocidad)
	longOnda = velocidad / frec
	longOndaSobreCuatro = longOnda / 4
	longOndaSobreDos = longOnda / 2

	print("Longitud de onda: ")
	print(longOnda)
	print("Lambda sobre 4:")
	print(longOndaSobreCuatro)
	print("Lambda sobre 2:")
	print(longOndaSobreDos)

	opcion = int(input("Si desea salir presione 1, sino, cualquier numero"))
	if(opcion == 1):
		salir = True

	else:
		salir = False




	
