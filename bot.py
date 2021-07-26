import unittest
import time
import cv2
import pytesseract
import numpy as np
import pyautogui

from colorama import Fore, Style, Back
from time import sleep
from PIL import *
from tqdm import tqdm
from getkey import getkey, keys




def obtencion_datos(f_copia_recibida):
	
	f=f_copia_recibida
	#myScreenshot = pyautogui.screenshot()

	#myScreenshot.save(r'/home/diego/Documentos/Proyecto_aim_b/imgs/captura.png')

	img = cv2.imread('imgs/captura.png')
					
	#Size de img_recortada_puntuacion
	x_puntuacion=1600
	w_puntuacion=210
	y_puntuacion=130
	h_puntuacion=100

	#Size de img_recortada_actividad
	x_actividad=300
	w_actividad=500
	y_actividad=10
	h_actividad=100

	img_recortada_puntuacion =  img[y_puntuacion:y_puntuacion+h_puntuacion, x_puntuacion:x_puntuacion+w_puntuacion]
	img_recortada_actividad = img[y_actividad:y_actividad+h_actividad, x_actividad:x_actividad+w_actividad]
						
	#Se guarda las imagenes en la carpeta img
	cv2.imwrite('imgs/captura_nueva_puntuacion.png', img_recortada_puntuacion)
	cv2.imwrite('imgs/captura_nueva_actividad.png', img_recortada_actividad)
	#cv2.imshow('Cropped image',img_recortada_puntuacion)
	#cv2.imshow('Cropped image',img_recortada_actividad)
	#cv2.waitKey(0)
						
	#Almacenamiento de lo que la libereria pytesseract lea de las imagenes
	puntuacion_capturada = [] 
	puntuacion_capturada.append(pytesseract.image_to_string(Image.open('imgs/captura_nueva_puntuacion.png')))
	actividad = []
	actividad.append(pytesseract.image_to_string(Image.open('imgs/captura_nueva_actividad.png'),lang='eng+spa'))
						
	#print(f'Actividad: {actividad[0]}\nScore: {puntuacion_capturada[0]}')

	#Aqui se obtiene la fecha local 
	tiempo=time.localtime()
	fecha=f'{tiempo[2]}/{tiempo[1]}/{tiempo[0]} - {tiempo[3]}:{tiempo[4]}:{tiempo[5]}'
	#time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
				        

	for score in puntuacion_capturada: 
		scores_convertido=str(score)
		f.write(f'{fecha}\nActividad: {actividad[0]}\nScore: {puntuacion_capturada[0]}\n')

		
	
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

	if opcion == 1:

		duracion = int(input(Fore.BLUE + 'Escribe la cantidad de ejercicios de tu rutina:' + Style.NORMAL))
		
		i=1
		while(i <= duracion):
			
			print(f'Presiona la tecla f para capturar el score ({i}/{duracion})')
			key = getkey()
			
			if key == 'f':
				obtencion_datos(f)
			
			i += 1	
			
		print(Fore.GREEN + 'Entrenamiento completado \nQue tengas un gran dia!')
			

	elif opcion == 2:
		for lineas in f:
			print(Fore.YELLOW + lineas)
					
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