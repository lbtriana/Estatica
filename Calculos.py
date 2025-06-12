import numpy as np
import math
import random as rd
import pandas as pd

#=========================Functions to generate the variables============================

#Function to calculate variables associated with forces
def calcular_fuerzas(num_fuerzas=16, rango=(10,300)):
    rangos = (rango[0], rango[1])

    fuerzas=[]
    
    for i in range(num_fuerzas):
        fuerza = rd.randint(rangos[0], rangos[1])
        fuerzas.append(fuerza)

    if fuerzas[0] <= fuerzas[1]:
        fuerzas[0] = rd.randint(rangos[0]+1, rangos[1])
        fuerzas[1] = rd.randint(rangos[0], fuerzas[0]-1)
    return fuerzas

#Function to calculate variables associated with angles
def calcular_angulos(num_angulos=16):
    rangos = [(5, 85), (91, 180), (181, 270), (271, 360)]
    
    angulos = []
    
    for i in range(num_angulos):
        rango = rangos[i % len(rangos)]
        angulo = rd.randint(rango[0], rango[1])
        angulos.append(angulo)
    
    if angulos[0] >= angulos[4]:
        angulos[4] = rd.randint(rangos[0][0]+1, rangos[0][1])
        angulos[0] = rd.randint(rangos[0][0], angulos[4]-1)

    return angulos

#Functions to calculate variables associated with position
def calcular_coordenadas():
    while True:
        coordenadas = [rd.randint(-100, 100) for _ in range(9)]#x_0,y_0,z_0,x_1,y_1,z_1
        if coordenadas[0] < coordenadas[3] and coordenadas[1] < coordenadas[4] and coordenadas[2] < coordenadas[5]:
            return coordenadas

#Functions to calculate variables associated with dimensions
def calcular_dimensiones(num_dimensiones = 28):
    values = [(1, 10), (-10, -1), (-10, 10)]
    
    dimensiones = []
    
    for i in range(num_dimensiones):
        value = values[i % len(values)]
        dimension = rd.randint(value[0], value[1])
        dimensiones.append(dimension)

    if dimensiones[9] <= dimensiones[6]:
        dimensiones[9] = rd.randint(values[0][0]+1, values[0][1])
        dimensiones[6] = rd.randint(values[0][0], dimensiones[9]-1)

    while dimensiones[0] == dimensiones[6] or dimensiones[3] == dimensiones[6]:
        dimensiones[6] = rd.randint(values[0][0], values[0][1])

    if dimensiones[2] == 0:
        dimensiones[2] = dimensiones[2]+1
    
    return dimensiones

#Functions to calculate variables associated with moments
def calcular_momentos():
    momentos=[]
    momentos = [rd.randint(10,100) for _ in range(6)]
    return momentos

#=========================
# Class Calculations Contains Functions for Variable-Based Calculations
class Calculations:
    #Function to calculate cosine
    def cosine(angle):
        cos=math.cos(math.radians(angle))
        return cos
    
    #Function to calculate sine
    def sine(angle):
        sin=math.sin(math.radians(angle))
        return sin
    
    #Function to calculate tangent
    def tangent(angle):
        tan=math.tan(math.radians(angle))
        return tan
    
    #Function to calculate magnitude in 2D
    def magnitude(fx,fy):
        magnitude=math.sqrt(fx**2 + fy**2)
        return magnitude
    
    #Function to calculate magnitude in 3D
    def magnitude3D(fx,fy,fz):
        magnitude3D=math.sqrt(fx**2 + fy**2 + fz**2)
        return magnitude3D
    
    #Function to calculate the angle using fx and fy components
    def define_angle(fx,fy):
        if fx == 0 and fy == 0:
            return 0  
        if fx == 0:
            return 90 if fy > 0 else 270
        if fy == 0:
            return 0 if fx > 0 else 180
        if fx>0 and fy>0: #Primer cuadrante
            angle = math.degrees(math.atan(abs(fy)/abs(fx)))
        if fx<0 and fy>0: #Segundo cuadrante
            angle = 180-math.degrees(math.atan(abs(fy)/abs(fx)))
        if fx<0 and fy<0: #Tercer cuadrante
            angle = 180+math.degrees(math.atan(abs(fy)/abs(fx)))
        if fx>0 and fy<0: #Cuarto cuadrante
            angle = 360-math.degrees(math.atan(abs(fy)/abs(fx)))
        return angle
    
    #Function to calculate the angle with arccosine
    def arccosine(fc,mag):
        arccosine = math.degrees(math.acos(fc/mag))
        return arccosine
    
    #Function to calculate the angle with arctangent
    def arctangent(angle):
        arctangent = math.degrees(math.atan(angle))
        return arctangent