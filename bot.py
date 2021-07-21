import unittest
import time

from colorama import Fore, Style, Back
from time import sleep



def run():
	#Este es un programa que se encarga de registrar las puntuaciones de una rutina de aim
	
	print(Fore.BLUE + """

	Bienvenido!
    (1) Capturar scores de entrenamiento
    (2) Revisar Historial de scores
    (3) Ayuda
    (4) Salir

                           """ + Style.NORMAL)
	opcion = int(input('Seleccione la opcion que le interese realizar:'))
	
	f = open('scores.txt', 'r+')
	scores = [1000,2000,3000,4000,5000,6000]
	if opcion == 1:
		
		tiempo=time.localtime()
		fecha=f'{tiempo[2]}:{tiempo[1]}:{tiempo[0]} - {tiempo[3]}:{tiempo[4]}:{tiempo[5]}'
				
		for score in scores: 
			scores_convertido=str(score)
			texto_a_imprimir=f'{scores_convertido} {fecha} \n'
			f.write(f'{texto_a_imprimir}\n')

		print(Fore.GREEN + 'Que tengas un gran dia!')

	elif opcion == 2:
		for lineas in f:
			print(lineas)
					
	elif opcion == 3:
		print(Fore.GREEN + """
			Este es un programa el cual sirve para dejar de lado el tipico excel e ir subiendo los scores de tus rutinas
			ya que facilita al jugador que sus scores esten mas facil de acceder a ellos
			""")
	elif opcion == 4:
		print(Fore.BLUE + 'Que tengas un gran dia!')
		sleep(2)
		quit()

	else:
		print(Fore.RED + 'Ingrese una opcion valida')
		run()
		

if __name__ == '__main__':
	run()