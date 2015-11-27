#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
#picamera -> API oficial de la camara.
import picamera

with picamera.PiCamera() as camera:
	#la resolucion maxima es 2592x1944 (5Mpx) a 15 fps y 1080p a 30fps
	camera.resolution = (2592, 1944)
	camera.start_preview()
	time.sleep(1)
	camera.stop_preview()
	ajustada = raw_input('¿Está la cámara colocada correctamente? s/n: ')
	while (ajustada != 's'):
	    raw_input('Colócala de nuevo y pulsa cualquier tecla...')
	    camera.start_preview()
	    time.sleep(1)
	    camera.stop_preview()
	    ajustada = raw_input('¿Está ahora bien colocada? s/n: ')

	tiempo_expo = int(raw_input('Elige el tiempo de exposición: '))
	camera.shutter_speed = tiempo_expo
	#iso para ajustar la sensibilidad a la luz de la lente.
	sens_iso = int(raw_input('Elige la sensibilidad de la lente (ISO): '))
	camera.ISO = sens_iso
	#podriamos ajustar el brillo con camera.brightness=0---100
	time.sleep(2)
	nombrearchivo = raw_input('Nombre de la muestra: ')
	camera.capture('ss'+str(tiempo_expo)+'iso'+str(sens_iso)+nombrearchivo + '.bmp')
