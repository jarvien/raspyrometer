#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from PIL import Image
from PIL import ImageFont, ImageDraw
from vectores import *

#abrimos la imagen con identificador im
nombre_img = raw_input('Introduce el nombre del archivo bmp sin la extensión: ')
#forzamos que sea en formato bmp
im = Image.open(nombre_img +".bmp")
#veamos su información
print(im.format, im.size, im.mode)
#check para ver que está en bmp
while im.format != 'BMP':
    im = Image.open(raw_input('La imagen debe estar en formato BMP. Inténtalo de nuevo: '))
    print(im.format, im.size, im.mode)

#guardamos ancho y alto en píxeles.
ancho = im.width
alto = im.height
#puede ser interesante guardar los canales por separado para ver si alguno es más lineal con la temperatura.
rojo = list(im.getdata(0))
verde = list(im.getdata(1))
azul = list(im.getdata(2))
print ('Rango de color RGB: ', im.getextrema())
#Para analizar vamos a considerar la suma de intensidades RGB.
#Usamos SumarVectores que utiliza una librería de numpy para facilitar cálculos.
SumaRGB = SumarVectores(rojo, verde)
SumaRGB = SumarVectores(SumaRGB, azul)
mapeo_rgb = MapearEntorno(SumaRGB, ancho, alto)

#veamos cuál es la matriz 3x3 con intensidad máxima en toda la imagen.
max_total = max(mapeo_rgb)
print ('Máximo RGB: ', max_total)
#al sacar las coordenadas del máximo, cuidado: hemos de restar los bordes.
pos_max_total = Coordenadas2d(mapeo_rgb.index(max_total), ancho-2, alto-2)
#esas coordenadas van de 0 a n-1, pero visualmente van de 1 a n luego:
print ('Posición: ', pos_max_total[0]+2, pos_max_total[1]+2)
#si queremos ver las veces que repite el máximo. debería ser sólo 1...
#print (mapeo_rgb.count(max_total))
mapeo_rojo = MapearEntorno(rojo, ancho, alto)
max_rojo = max(mapeo_rojo)
print ('Máximo rojo: ', max_rojo)
pos_max_rojo = Coordenadas2d(mapeo_rgb.index(max_rojo), ancho-2, alto-2)
print ('Posición: ', pos_max_rojo[0]+2, pos_max_rojo[1]+2)

mapeo_verde = MapearEntorno(verde, ancho, alto)
max_verde = max(mapeo_verde)
print ('Máximo verde: ', max_verde)
pos_max_verde = Coordenadas2d(mapeo_rgb.index(max_verde), ancho-2, alto-2)
print ('Posición: ', pos_max_verde[0]+2, pos_max_verde[1]+2)

mapeo_azul = MapearEntorno(azul, ancho, alto)
max_azul = max(mapeo_azul)
print ('Máximo azul: ', max_azul)
pos_max_azul = Coordenadas2d(mapeo_rgb.index(max_azul), ancho-2, alto-2)
print ('Posición: ', pos_max_azul[0]+2, pos_max_azul[1]+2)

#vamos a fijarnos en la zona que nos interesa.
xmin, ymin, xmax, ymax = RangoRecorte(pos_max_total[0]+1, pos_max_total[1]+1, ancho, alto)
#establecer los rangos en x e y para el recuadro a cortar.
recorte = im.crop((xmin, ymin, xmax, ymax))
recorte.show()
coords = (xmin,ymin, xmax,ymax)
grosor = 5
rect = ImageDraw.Draw(im)
for i in range(grosor):
    rect.rectangle(coords, outline = "blue")
    coords = (coords[0]+1,coords[1]+1, coords[2]+1,coords[3]+1)
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("./sans_seriff.ttf", 20);
draw.text((xmin-1, ymin-1),"Zona mas caliente",(255,255,255),font=font)
#para sacar imagen por pantalla: im.show()
im.show()

arch = open(nombre_img+'.txt', 'w')
arch.write("Intensidad máxima del rojo\tIntensidad máxima del verde\tIntensidad máxima del azul\tIntensidad promedio máxima total\n")
arch.write(str(float(max_rojo)/9)+"\t"+str(float(max_verde)/9)+"\t"+str(float(max_azul)/9)+"\t"+str(float(max_total)/27))

arch.close
