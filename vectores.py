#!/usr/bin/env python
# -*- coding: utf-8 -*-
def Coordenadas2d(valor, ancho, alto):
    #Para pasar de 1d a 2d, hacemos divisón entera de la pos1d entre el ancho
    y = int(float(valor/ancho))
    #para sacar x, 2 alternativas:
    #usamos álgebra modular: x = valor % ancho; o despejamos:
    x = valor - ancho*y
    return x,y

def Cooordenadas1d(p, ancho):
    #la conversión inversa es aún más sencilla, basta con hacer: x + ancho*y
    return p[0] + ancho*p[1]

def SumarEntorno(color, pos, ancho):
    #sumamos los valores de una matrix 3x3.
    return (color[pos + 1] + color[pos - 1] + color[pos] + color[pos + 1 + ancho] + color[pos - 1 + ancho] + color[pos + ancho] + color[pos + 1 - ancho] + color[pos -1 - ancho] + color[pos - ancho])

def SumarVectores(v1, v2):
    #función para sumar vectores valiéndonos de numpy.
    #resulta más eficiente (utiliza menos flops) que cualquier otra alternativa.
    import numpy as np
    v1 = np.array(v1)
    v2 = np.array(v2)
    return (v1 + v2)

def MapearEntorno(vector, ancho, alto):
    i=0
    #inicializamos un vector de ceros y ya que los bordes no nos importan:
    #le restaremos un píxel alrededor.
    VectorMapeo = [0] * (ancho-2) * (alto-2)
    for y in range(1, alto-1):
        for x in range(1, ancho-1):
            p = [x, y]
            VectorMapeo[i] = SumarEntorno(vector, Cooordenadas1d(p, ancho), ancho)
            i+=1
    return VectorMapeo
#Esta función nos permite coger la zona más caliente de la imagen.
#Hemos de tener cuidado si el máximo está en alguno de los bordes.
def RangoRecorte(posx, posy, ancho, alto):
    #en principio cogemos un entorno de 100x100 alrededor del máximo.
    xmin = posx - 50
    xmax = posx + 50
    ymin = posy - 50
    ymax = posy + 50
    if (xmax > ancho - 1):
        #si ese entorno se sale de la imagen, corregimos de forma que entre.
        dif = xmax - ancho
        xmax = xmax - dif
        xmin = xmin - dif
    if (xmin < 0):
        #misma idea para xmin, esta vez la condición es que sea < 0.
        dif = abs(xmin)
        xmin = 0
        xmax = xmax + dif
    if (ymax > alto - 1):
        #análogamente para ymax
        dif = ymax - alto
        ymax = ymax - dif
        ymin = ymin - dif
    if (ymin < 0):
        #ahora ymin
        dif = abs(ymin)
        ymin = 0
        ymax = ymax + dif
    #devolvemos los valores. si el máximo no está en ninguna de esas situaciones,
    #no habrá entrado en ninguno de los ifs.
    return (xmin, ymin, xmax, ymax)
