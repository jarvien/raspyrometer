#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
#import os
from PIL import Image
from PIL import ImageFont, ImageDraw
from vectores import *

#abrimos la imagen con identificador im
nombre_img = raw_input('Introduce el nombre del archivo bmp sin la extensión: ')
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
#establecer los rangos en x e y para el recuadro a cortar.
left = ancho/4
top = alto/4
right = 3 * ancho/4
bottom = 3 * alto/4
recorte = im.crop((left, top, right, bottom))
draw = ImageDraw.Draw(recorte)
font = ImageFont.truetype("./sans_seriff.ttf", 50);
draw.text((0, 0),"Máximo de temperatura",(255,255,255),font=font)
recorte.show()
coords = (0,0, 100,100)
grosor = 10
rect = ImageDraw.Draw(im)
for i in range(grosor):
    rect.rectangle(coords, outline = "blue")
    coords = (coords[0]+1,coords[1]+1, coords[2]+1,coords[3]+1)

im.show()
