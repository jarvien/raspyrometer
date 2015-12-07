#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import picamera

def TomarFoto(shutt, sens, nombre):
    with picamera.PiCamera() as camera:
        camera.resolution = (2592, 1944)
        camera.shutter_speed = shutt
        camera.ISO = sens
        time.sleep(1)
        camera.capture('ss'+str(shutt)+'iso'+str(sens)+str(nombre)+'.bmp')

tiempo_expo = []
sens_iso = int(raw_input('Elige la sensibilidad de la lente (ISO): '))

tiempo_expo.append(  int(raw_input('Elige el tiempo de exposición: '))  )


nombrearchivo = raw_input('Nombre de la muestra: ')

TomarFoto(tiempo_expo, sens_iso, nombrearchivo)
