import streamlit as st
import numpy as np
import random as rd
import pandas as pd
import math as math
from Calculos import *
from Texts import *

#class Questionary stores the information of each exercises
class Questionary:
    def __init__(self, code, no_pregunta,complexity,topic, subtopic,version,pregunta,no_answers,a1_name,a2_name,a3_name,answer1,answer2,answer3,ayuda1,ayuda2,ayuda3,respuesta_P1,respuesta_P2,respuesta_P3,calculos):
        self.code = code ##### Topic, Subtopic, Complexity (1. Fácil, 2. Medio, 3. Díficil), No de la pregunta, Versión
        self.no_pregunta = no_pregunta
        self.complexity = complexity
        self.topic = topic
        self.subtopic = subtopic
        self.version = version
        self.pregunta_func=pregunta
        self.pregunta = ""
        self.no_answers = no_answers
        self.a1_name = a1_name
        self.a2_name = a2_name
        self.a3_name = a3_name
        self.answer1_func=answer1
        self.answer1 = ""
        self.answer2_func=answer2
        self.answer2 = ""
        self.answer3_func=answer3
        self.answer3 = ""
        self.ayuda1 = ayuda1
        self.ayuda2 = ayuda2
        self.ayuda3 = ayuda3
        self.respuestaP1_func=respuesta_P1
        self.respuesta_P1 = ""
        self.respuestaP2_func=respuesta_P2
        self.respuesta_P2 = ""
        self.respuestaP3_func=respuesta_P3
        self.respuesta_P3 = ""
        self.calculos = calculos
        self.generate_values()


    #Function to generate the values of the variables and relates them to the parameters of the class
    def generate_values(self):
        self.fuerzas = calcular_fuerzas()
        self.angulos = calcular_angulos()
        self.coordenadas = calcular_coordenadas()
        self.dimensiones = calcular_dimensiones()
        self.momentos = calcular_momentos()
        self.calculos = self.operations()

        self.pregunta = self.pregunta_func(self.fuerzas, self.angulos, self.calculos, self.coordenadas, self.dimensiones, self.momentos)
        self.answer1 = self.answer1_func(self.fuerzas, self.angulos, self.calculos, self.coordenadas, self.dimensiones, self.momentos)
        self.answer2 = self.answer2_func(self.fuerzas, self.angulos, self.calculos, self.coordenadas, self.dimensiones, self.momentos)
        self.answer3 = self.answer3_func(self.fuerzas, self.angulos, self.calculos, self.coordenadas, self.dimensiones, self.momentos)
        self.respuesta_P1 = self.respuestaP1_func(self.fuerzas, self.angulos, self.calculos, self.coordenadas, self.dimensiones, self.momentos)
        self.respuesta_P2 = self.respuestaP2_func(self.fuerzas, self.angulos, self.calculos, self.coordenadas, self.dimensiones, self.momentos)
        self.respuesta_P3 = self.respuestaP3_func(self.fuerzas, self.angulos, self.calculos, self.coordenadas, self.dimensiones, self.momentos)
        return  

    def regenerate_values(self):
        self.generate_values()
        return

    def operations(self):
        operations_dict = {}

        for i in range(16):  # For each version
            angle = self.angulos[i]
            force = self.fuerzas[i]
            
            #Trigonometry according to the angle
            cos_value = Calculations.cosine(angle)
            sin_value = Calculations.sine(angle)
            tan_value = Calculations.tangent(angle)
            
            # Add values to the dictionary
            operations_dict[f'cos{i+1}'] = cos_value
            operations_dict[f'sin{i+1}'] = sin_value
            operations_dict[f'tan{i+1}'] = tan_value
            operations_dict[f'mag{i+1}_u'] = Calculations.magnitude(cos_value, sin_value)
            operations_dict[f'mag{i+1}_f'] = Calculations.magnitude(force * cos_value, force * sin_value)
        
        return operations_dict
    
   
    #Function to filter the questions according to the user's selection
    def filtrar_preguntas(preguntas, topic=None, subtopic=None, complexity=None):
        preguntas_filtradas = [
            pregunta for pregunta in preguntas
            if (topic is None or pregunta.topic == topic) and
               (subtopic is None or pregunta.subtopic == subtopic) and
               (complexity is None or pregunta.complexity == complexity)
        ]
        return preguntas_filtradas

#List of questions
preguntas = [

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Vectores 2D        ---------------------------------------------------
    #-------------------------------------------------     Nivel fácil        ---------------------------------------------------
    #-------------------------------------------------     Code: 111####      ---------------------------------------------------
    
    Questionary(#1_1
        code = 1110011,
        no_pregunta = 1,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es ángulo que forma el vector fuerza F1 con el eje X positivo y con el eje Y positivo medidos en sentido antihorario?. Considere $\\alpha_x = {a[0]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = AX,
        a2_name = AY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(a[0], 2),
        answer2 = lambda f, a, calc, c, d, m: np.round(90-a[0], 2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A1,
        ayuda2 = A2,
        ayuda3 = A3,
        respuesta_P1 = lambda fa, a, calc, c, d, m: f"El ángulo con respecto al eje X ($\\alpha_x$) es ${a[0]:.0f}°$ y con respecto al eje Y ($\\alpha_y$) es ${90-a[0]:.0f}°$",
        respuesta_P2 = lambda fa, a, calc, c, d, m: f"",
        respuesta_P3 = lambda fa, a, calc, c, d, m: f"",
        calculos = 'operations'
        ),

    Questionary(#1_2
        code = 1110012,
        no_pregunta = 1,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es ángulo que forma el vector fuerza F1 con el eje X positivo y con el eje Y positivo medidos en sentido antihorario?. Considere $\\alpha_x = {a[1]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = AX,
        a2_name = AY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(a[1], 2),
        answer2 = lambda f, a, calc, c, d, m: np.round(a[1]-90, 2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A1,
        ayuda2 = A2,
        ayuda3 = A3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"El ángulo con respecto al eje X ($\\alpha_x$) es ${a[1]:.0f}°$ y con respecto al eje Y ($\\alpha_y$) es ${a[1]-90:.0f}°$",
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    Questionary(#1_3
        code = 1110013,
        no_pregunta = 1,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es ángulo que forma el vector fuerza F1 con el eje X positivo y con el eje Y positivo medidos en sentido antihorario?. Considere $\\alpha_x = {a[2]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = AX,
        a2_name = AY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(a[2], 2),
        answer2 = lambda f, a, calc, c, d, m: np.round(a[2]-90, 2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A1,
        ayuda2 = A2,
        ayuda3 = A3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"El ángulo con respecto al eje X ($\\alpha_x$) es ${a[2]:.0f}°$ y con respecto al eje Y ($\\alpha_y$) es ${a[2]-90:.0f}°$",
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#1_4
        code = 1110014,
        no_pregunta = 1,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es ángulo que forma el vector fuerza F1 con el eje X positivo y con el eje Y positivo medidos en sentido antihorario?. Considere $\\alpha_x = {a[3]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = AX,
        a2_name = AY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(a[3], 2),
        answer2 = lambda f, a, calc, c, d, m: np.round(a[3]-90, 2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A1,
        ayuda2 = A2,
        ayuda3 = A3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"El ángulo con respecto al eje X ($\\alpha_x$) es ${a[3]:.0f}°$ y con respecto al eje Y ($\\alpha_y$) es ${a[3]-90:.0f}°$",
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 1110021,
        no_pregunta = 2,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es la componente del vector F1 con respecto al eje X ${{(F1_x)}}$ y con respecto al eje Y ${{(F1_y)}}$?. Considere $\\text{{F1}}={f[0]:.0f}\\text{{ kN}}$ y $\\alpha_x = {a[0]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = FX,
        a2_name = FY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['cos1'],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['sin1'],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A4,
        ayuda2 = A5,
        ayuda3 = A6,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P2(f, calc, 1),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_2
        code = 1110022,
        no_pregunta = 2,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es la componente del vector F1 con respecto al eje X ${{(F1_x)}}$ y con respecto al eje Y ${{(F1_y)}}$?. Considere $\\text{{F1}}={f[0]:.0f}\\text{{ kN}}$ y $\\alpha_x = {a[1]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = FX,
        a2_name = FY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['cos2'],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['sin2'],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A4,
        ayuda2 = A5,
        ayuda3 = A6,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P2(f, calc, 2),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 

    Questionary(#2_3
        code = 1110023,
        no_pregunta = 2,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es la componente del vector F1 con respecto al eje X ${{(F1_x)}}$ y con respecto al eje Y ${{(F1_y)}}$?. Considere $\\text{{F1}}={f[0]:.0f}\\text{{ kN}}$ y $\\alpha_x = {a[2]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = FX,
        a2_name = FY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['cos3'],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['sin3'],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A4,
        ayuda2 = A5,
        ayuda3 = A6,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P2(f, calc, 3),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_4
        code = 1110024,
        no_pregunta = 2,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es la componente del vector F1 con respecto al eje X ${{(F1_x)}}$ y con respecto al eje Y ${{(F1_y)}}$?. Considere $\\text{{F1}}={f[0]:.0f}\\text{{ kN}}$ y $\\alpha_x = {a[3]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = FX,
        a2_name = FY,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(f[0]*calc['cos4'],2),
        answer2=lambda f, a, calc, c, d, m: np.round(f[0]*calc['sin4'],2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A4,
        ayuda2 = A5,
        ayuda3 = A6,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P2(f, calc, 4),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 1110031,
        no_pregunta = 3,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Encuentre la pendiente de la línea definida por los puntos A (punto inicial) y B (punto final). Las coordenadas $(X, Y)$ del punto A son $({c[0]:.0f},{c[1]:.0f})$ y las del punto B son $({c[3]:.0f},{c[4]:.0f})$.",
        no_answers = 1,
        a1_name = "Pendiente",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: (c[4]-c[1])/(c[3]-c[0]),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1= A7,
        ayuda2= A8,
        ayuda3= A9,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P3(c[0], c[1], c[3], c[4]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_2
        code = 1110032,
        no_pregunta = 3,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"Encuentre la pendiente de la línea definida por los puntos A (punto inicial) y B (punto final). Las coordenadas $(X,Y)$ del punto A son $({c[3]:.0f},{c[4]:.0f})$ y las del punto B son $({c[0]:.0f},{c[1]:.0f})$.",
        no_answers = 1,
        a1_name = "Pendiente",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: (c[1]-c[4])/(c[0]-c[3]),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A8,
        ayuda3 = A9,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P3(c[3], c[4], c[0], c[1]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_3
        code = 1110033,
        no_pregunta = 3,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"Encuentre la pendiente de la línea definida por los puntos A (punto inicial) y B (punto final). Las coordenadas $(X,Y)$ del punto A son $({c[3]:.0f},{c[1]:.0f})$ y las del punto B son $({c[0]:.0f},{c[4]:.0f})$.",
        no_answers = 1,
        a1_name = "Pendiente",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: (c[4]-c[1])/(c[0]-c[3]),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A8,
        ayuda3 = A9,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P3(c[3], c[1], c[0], c[4]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_4
        code = 1110034,
        no_pregunta = 3,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"Encuentre la pendiente de la línea definida por los puntos A (punto inicial) y B (punto final). Las coordenadas $(X,Y)$ del punto A son $({c[0]:.0f},{c[4]:.0f})$ y las del punto B son $({c[3]:.0f},{c[1]:.0f})$.",
        no_answers = 1,
        a1_name = "Pendiente",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: (c[1]-c[4])/(c[3]-c[0]),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A8,
        ayuda3 = A9,
        respuesta_P1=lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P3(c[0], c[4], c[3], c[1]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_1
        code = 1110041,
        no_pregunta = 4,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Si el vector $\\overrightarrow{{F1}}$ está definido por dos puntos en el espacio A (punto inicial) y B (punto final), ¿cuál es la magnitud de $\\overrightarrow{{F1}}$ (|$\\overrightarrow{{F1}}$|)?. Las coordenadas $(X,Y)$ del punto A son $({c[0]:.0f}, {c[1]:.0f})$ y las del punto B son $({c[3]:.0f}, {c[4]:.0f})$.",
        no_answers = 1,
        a1_name = "Magnitud $\\overrightarrow{{F1}}$ (|$\\overrightarrow{{F1}}$|)",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A8,
        ayuda3= A10,
        respuesta_P1 = lambda f, a, calc, c, d, m:rta_EQ_V2D_F_P4(c[0], c[1], c[3], c[4]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_2
        code = 1110042,
        no_pregunta = 4,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"Si el vector $\\overrightarrow{{F1}}$ está definido por dos puntos en el espacio A (punto inicial) y B (punto final), ¿cuál es la magnitud de $\\overrightarrow{{F1}}$ (|$\\overrightarrow{{F1}}$|)?. Las coordenadas $(X,Y)$ del punto A son $({c[3]:.0f}, {c[4]:.0f})$ y las del punto B son $({c[0]:.0f}, {c[1]:.0f})$.",
        no_answers = 1,
        a1_name = "Magnitud $\\overrightarrow{{F1}}$ (|$\\overrightarrow{{F1}}$|)",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2),2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A8,
        ayuda3= A10,
        respuesta_P1 = lambda f, a, calc, c, d, m:rta_EQ_V2D_F_P4(c[3], c[4], c[0], c[1]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_3
        code = 1110043,
        no_pregunta = 4,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"Si el vector $\\overrightarrow{{F1}}$ está definido por dos puntos en el espacio A (punto inicial) y B (punto final), ¿cuál es la magnitud de $\\overrightarrow{{F1}}$ (|$\\overrightarrow{{F1}}$|)?. Las coordenadas $(X,Y)$ del punto A son $({c[3]:.0f}, {c[1]:.0f})$ y las del punto B son $({c[0]:.0f}, {c[4]:.0f})$.",
        no_answers = 1,
        a1_name = "Magnitud $\\overrightarrow{{F1}}$ (|$\\overrightarrow{{F1}}$|)",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(math.sqrt((c[0]-c[3])**2+(c[4]-c[1])**2),2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A8,
        ayuda3 = A10,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_F_P4(c[3], c[1], c[0], c[4]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_4
        code = 1110044,
        no_pregunta = 4,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"Si el vector F1 está definido por dos puntos en el espacio A (punto inicial) y B (punto final), ¿cuál es la magnitud de $\\overrightarrow{{F1}}$ (|$\\overrightarrow{{F1}}$|)?. Las coordenadas $(X,Y)$ del punto A son $({c[0]:.0f}, {c[4]:.0f})$ y las del punto B son $({c[3]:.0f}, {c[1]:.0f})$.",
        no_answers = 1,
        a1_name = "Magnitud $\\overrightarrow{{F1}}$ (|$\\overrightarrow{{F1}}$|)",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A8,
        ayuda3 = A10,
        respuesta_P1 = lambda f, a, calc, c, d, m:rta_EQ_V2D_F_P4(c[0], c[4], c[3], c[1]),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#5_1
        code = 1110051,
        no_pregunta = 5,
        complexity = F,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud y la dirección respecto al eje X positivo del vector cartesiano $[({c[0]:.0f}) \\hat{{i}} + ({c[1]:.0f}) \\hat{{j}}] N$.",
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(c[0],c[1]),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(c[0],c[1]),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A11,
        ayuda2 = A12,
        ayuda3 = A13,
        respuesta_P1 = lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la magnitud:}}$

        ${{\hspace{{4mm}} F = \\sqrt{{Fx^2+Fy^2}} = {Calculations.magnitude(c[0],c[1]):.2f}}} \\text{{N}}$

        $\\textbf{{\\small 2. Cálculo del ángulo:}}$

        ${{\hspace{{4mm}} \\alpha ={Calculations.define_angle(c[0],c[1]):.2f}}}°$

        El cálculo del ángulo respecto al eje x positivo depende del cuadrante en el que se encuentra el vector:

        -Primer cuadrante:  $tan^{-1}\\left(\\dfrac{{componente \\hspace{{1mm}} \\hat{{j}} }} {{componente \\hspace{{1mm}} \\hat{{i}} }}\\right)$  

        -Segundo cuadrante: $180 - tan^{-1}\\left(\\dfrac{{componente \\hspace{{1mm}} \\hat{{j}} }}{{componente \\hspace{{1mm}} \\hat{{i}} }}\\right)$  

        -Tercer cuadrante:  $180 + tan^{-1}\\left(\\dfrac{{componente \\hspace{{1mm}} \\hat{{j}} }}{{componente \\hspace{{1mm}} \\hat{{i}} }}\\right)$  

        -Cuarto cuadrante:  $360 - tan^{-1}\\left(\\dfrac{{componente \\hspace{{1mm}} \\hat{{j}} }}{{componente \\hspace{{1mm}} \\hat{{i}} }}\\right)$ 
        
        """,     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),


    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Vectores 2D        ---------------------------------------------------
    #-------------------------------------------------     Nivel medio        ---------------------------------------------------
    #-------------------------------------------------     Code: 112####      ---------------------------------------------------

    Questionary(#1_1
        code = 1120011,
        no_pregunta = 1,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Si se conoce que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[0]:.0f}$°, $\\alpha_2={a[4]:.0f}$°, determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ de los vectores fuerza.",
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[0]*calc['cos1']+f[1]*calc['cos5'],f[0]*calc['sin1']+f[1]*calc['sin5']),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(f[0]*calc['cos1']+f[1]*calc['cos5'],f[0]*calc['sin1']+f[1]*calc['sin5']),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_M_P1(f[0], f[0], f[1], f[1], calc, 1, 5),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),

    Questionary(#1_2
        code = 1120012,
        no_pregunta = 1,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"Si se conoce que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[0]:.0f}$°, $\\alpha_2={a[4]:.0f}$°, determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ de los vectores fuerza.",
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[0]*calc['cos1']+f[1]*calc['cos5'],f[0]*calc['sin1']+f[1]*calc['sin5']),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(-f[0]*calc['cos1']-f[1]*calc['cos5'],f[0]*calc['sin1']+f[1]*calc['sin5']),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_M_P1(-f[0], f[0], -f[1], f[1], calc, 1, 5),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),
    
    Questionary(#1_3
        code = 1120013,
        no_pregunta = 1,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"Si se conoce que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[0]:.0f}$°, $\\alpha_2={a[4]:.0f}$°, determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ de los vectores fuerza.",
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[0]*calc['cos1']+f[1]*calc['cos5'],f[0]*calc['sin1']+f[1]*calc['sin5']),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(-f[0]*calc['cos1']-f[1]*calc['cos5'],-f[0]*calc['sin1']-f[1]*calc['sin5']),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_M_P1(-f[0], -f[0], -f[1], -f[1], calc, 1, 5),     
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),
    
    Questionary(#1_4
        code = 1120014,
        no_pregunta = 1,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"Si se conoce que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[0]:.0f}$°, $\\alpha_2={a[4]:.0f}$°, determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ de los vectores fuerza.",
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[0]*calc['cos1']+f[1]*calc['cos5'],f[0]*calc['sin1']+f[1]*calc['sin5']),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(f[0]*calc['cos1']+f[1]*calc['cos5'],-f[0]*calc['sin1']-f[1]*calc['sin5']),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_M_P1(f[0], -f[0], f[1], -f[1], calc, 1, 5),   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",  
        calculos='operations',
        ),

    Questionary(#2_1
        code = 1120021,
        no_pregunta = 2,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ si se sabe que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[4]:.0f}$°, $\\alpha_2={a[0]:.0f}$°.",  
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(-f[0]*calc['sin5']-f[1]*calc['cos1'],f[0]*calc['cos5']-f[1]*calc['sin1']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(-f[0]*calc['sin5']-f[1]*calc['cos1'],f[0]*calc['cos5']-f[1]*calc['sin1']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m:rta_EQ_V2D_M_P2(-f[0], f[0], -f[1], -f[1], calc, 1, 5),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),

    Questionary(#2_2
        code = 1120022,
        no_pregunta = 2,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ si se sabe que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[4]:.0f}$°, $\\alpha_2={a[0]:.0f}$°.",  
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[0]*calc['sin5']-f[1]*calc['cos1'],f[0]*calc['cos5']+f[1]*calc['sin1']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(f[0]*calc['sin5']-f[1]*calc['cos1'],f[0]*calc['cos5']+f[1]*calc['sin1']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m:rta_EQ_V2D_M_P2(f[0], f[0], -f[1], f[1], calc, 1, 5),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),

    Questionary(#2_3
        code = 1120023,
        no_pregunta = 2,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ si se sabe que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[4]:.0f}$°, $\\alpha_2={a[0]:.0f}$°.",  
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[0]*calc['sin5']-f[1]*calc['cos1'],-f[0]*calc['cos5']-f[1]*calc['sin1']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(f[0]*calc['sin5']-f[1]*calc['cos1'],-f[0]*calc['cos5']-f[1]*calc['sin1']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m:rta_EQ_V2D_M_P2(f[0], -f[0], -f[1], -f[1], calc, 1, 5),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),
    
    Questionary(#2_4
        code = 1120024,
        no_pregunta = 2,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud y la dirección respecto al eje X positivo de la fuerza resultante $(F_R)$ si se sabe que $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $\\alpha_1={a[4]:.0f}$°, $\\alpha_2={a[0]:.0f}$°.",  
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(-f[0]*calc['sin5']-f[1]*calc['cos1'],-f[0]*calc['cos5']+f[1]*calc['sin1']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(-f[0]*calc['sin5']-f[1]*calc['cos1'],-f[0]*calc['cos5']+f[1]*calc['sin1']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A14,
        ayuda2 = A15,
        ayuda3 = A16,
        respuesta_P1 = lambda f, a, calc, c, d, m:rta_EQ_V2D_M_P2(-f[0], -f[0], -f[1], f[1], calc, 1, 5),
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),

    Questionary(#3_1
        code = 1120031,
        no_pregunta = 3,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"El cofre mostrado en la figura es desplazado mediante dos cuerdas. Si se sabe que $F1={f[0]:.0f} \\text{{ kN}}$, $\\alpha_1 = {a[0]:.0f}°$ y $\\alpha_2 = {a[4]:.0f}°$, determine las magnitudes de $F2$ y de la fuerza resultante $(F_R)$ de tal forma que esta se dirija a lo largo del eje X.",
        no_answers = 2,
        a1_name = "Magnitud $F2$ [kN]",
        a2_name = "Magnitud $F_R$ [kN]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((f[0]*calc['sin1'])/calc['sin5']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['cos1']+((f[0]*calc['sin1'])/calc['sin5'])*calc['cos5'],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A17,
        ayuda2 = A18,
        ayuda3 = A19,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Se sugiere para la solución del ejercicio el siguiente método:

        $\\textbf{{\\small 1. Descomposición de los vectores F1 y F2:}}$

        ${{\hspace{{4mm}} F1_x = F1*cos(\\alpha_1) = {f[0]*calc['cos1']:.2f} \\text{{ kN}} }}$  
        ${{\hspace{{4mm}} F1_y = F1*sen(\\alpha_1) = {f[0]*calc['sin1']:.2f} \\text{{ kN}} }}$  
        ${{\hspace{{4mm}} F2_x = F2*cos(\\alpha_2)}}$  
        ${{\hspace{{4mm}} F2_y = -F2*sen(\\alpha_2)}}$  

        $\\textbf{{\\small 2. Sumatoria de fuerzas en Y:}}\\text{{Esta sumatoria equivale a 0, dado que, la fuerza resultante actúa únicamente en el eje X. A partir de esta ecuación se despeja la magnitud de F2:}}$

        ${{\hspace{{4mm}}\\sum{{F_y}} = F1_y + F2_y = 0}}$  

        ${{\hspace{{4mm}} |F2| = \\dfrac{{F1*sen(\\alpha_1)}}{{sen(\\alpha_2)}} ={(f[0]*calc['sin1'])/calc['sin5']:.2f} \\text{{ kN}} }}$  

        $\\textbf{{\\small 3. Sumatoria de fuerzas en X:}}\\text{{El valor de esta sumatoria equivale a la magnitud de la fuerza resultante, dado que, solo actúa en este eje.}}$
        
        ${{\hspace{{4mm}}\\sum{{F_X}} = F1_x + F2_x = F_R}}$  
        ${{\hspace{{4mm}}\\sum{{F_X}} = F_R = {f[0]*calc['cos1']+((f[0]*calc['sin1'])/calc['sin5'])*calc['cos5']:.2f} \\text{{ kN}} }}$  
       """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_2
        code = 1120032,
        no_pregunta = 3,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"El cofre mostrado en la figura es desplazado mediante dos cuerdas. Si se sabe que $F2={f[0]:.0f} \\text{{ kN}}$, $\\alpha_1 = {a[0]:.0f}°$ y $\\alpha_2 = {a[4]:.0f}°$, determine las magnitudes de $F1$ y de la fuerza resultante $(F_R)$ de tal forma que esta se dirija a lo largo del eje X.",
        no_answers = 2,
        a1_name = "Magnitud $F1$ [kN]",
        a2_name = "Magnitud $F_R$ [kN]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((f[0]*calc['sin5'])/calc['sin1']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[1]*calc['cos2']+((f[0]*calc['sin5'])/calc['sin1'])*calc['cos5'],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A17,
        ayuda2 = A18,
        ayuda3 = A19,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Se sugiere para la solución del ejercicio el siguiente método:

        $\\textbf{{\\small 1. Descomposición de los vectores F1 y F2:}}$

        ${{\hspace{{4mm}} F1_x = F1*cos(\\alpha_1)}}$  
        ${{\hspace{{4mm}} F1_y = F1*sen(\\alpha_1)}}$  
        ${{\hspace{{4mm}} F2_x = F2*cos(\\alpha_2) = {f[0]*calc['cos1']:.2f} \\text{{ kN}} }}$  
        ${{\hspace{{4mm}} F2_y = -F2*sen(\\alpha_2) = {f[0]*calc['sin1']:.2f} \\text{{ kN}} }}$  

        $\\textbf{{\\small 2. Sumatoria de fuerzas en Y:}}\\text{{Esta sumatoria equivale a 0, dado que, la fuerza resultante actúa únicamente en el eje X. A partir de esta ecuación se despeja la magnitud de F1:}}$

        ${{\hspace{{4mm}}\\sum{{F_y}} = F1_y + F2_y = 0}}$  

        ${{\hspace{{4mm}} |F2| = \\dfrac{{F2*sen(\\alpha_2)}}{{sen(\\alpha_1)}} ={(f[0]*calc['sin5'])/calc['sin1']:.2f} \\text{{ kN}} }}$  

        $\\textbf{{\\small 3. Sumatoria de fuerzas en X:}}\\text{{El valor de esta sumatoria equivale a la magnitud de la fuerza resultante, dado que, solo actúa en este eje.}}$
        
        ${{\hspace{{4mm}}\\sum{{F_X}} = F1_x + F2_x = F_R }}$  
        ${{\hspace{{4mm}}\\sum{{F_X}} = F_R = {f[0]*calc['cos1']+((f[0]*calc['sin1'])/calc['sin5'])*calc['cos5']:.2f} \\text{{ kN}} }}$  
       """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_1
        code = 1120041,
        no_pregunta = 4,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Para el descenso del globo aerostático mostrado en la figura se requiere una fuerza vertical de $FR={f[0]:.0f} \\text{{ kN}}$. Determine las magnitudes de $F1$ y $F2$ si $\\alpha_1 = {a[0]:.0f}°$ y $\\alpha_2 = {a[4]:.0f}°$.",
        no_answers = 2,
        a1_name = "Magnitud $F1$ [kN]",
        a2_name = "Magnitud $F2$ [kN]",
        a3_name = "",
        answer1 =lambda f, a, calc, c, d, m: np.round((f[0]*calc['tan5'])/(calc['sin1']+calc['cos1']*calc['tan5']),2),
        answer2 =lambda f, a, calc, c, d, m: np.round(((((-f[0]*calc['tan5'])/(calc['sin1']+calc['cos1']*calc['tan5']))*calc['cos1'])+f[0])/calc['cos5'],2),
        answer3 =lambda f, a, calc, c, d, m: 0,
        ayuda1 = A17,
        ayuda2 = A20,
        ayuda3 = A12,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Se sugiere para la solución del ejercicio el siguiente método:

        $\\textbf{{\\small 1. Sumatoria de fuerzas en X y Y:}}$

        Se analiza de acuerdo con lo requerido en el enunciado a que equivale cada sumatoria.

        $\\underline{{Ecuación \\hspace{{2mm}} 1}}$  

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_x}} = F1_x + F2_x = -F1*sen(\\alpha_1) + F2*sen(\\alpha_2) = 0}}$

        $\\underline{{Ecuación \\hspace{{2mm}} 2}}$  

        ${{\hspace{{4mm}} \\sum{{F_y}} = -F_R }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = F1_y + F2_y = -F1*cos(\\alpha_1)-F2*cos(\\alpha_2) = -F_R}}$
        

        $\\textbf{{\\small 2. Despejar las magnitudes:}}$

        Para simplificar el proceso de despeje, se busca formar una tangente. Al hacer esto, se reduce el número de términos en las ecuaciones. Dado lo anterior, se despeja F2 de la Ecuación 2 y se reemplaza en la Ecuación 1 para despejar F1. Con el valor de F1 obtenido, se halla F2.

        De la ecuación 2 se despeja F2:  

        ${{\hspace{{4mm}} F2 = \\dfrac{{-F1*cos(\\alpha_1)+F_R}}{{cos(\\alpha_2)}}}}$

        Se reemplaza F2 en la ecuación 1:

        ${{\hspace{{4mm}} -F1*sen(\\alpha_1) + \\left(\\dfrac{{-F1*cos(\\alpha_1)+F_R}}{{cos(\\alpha_2)}}\\right)*sen(\\alpha_2) = 0}}$

        ${{\hspace{{4mm}} -F1*sen(\\alpha_1)-F1*cos(\\alpha_1)*tan(\\alpha_2)+F_R*tan(\\alpha_2)=0}}$

        ${{\hspace{{4mm}} -F_R*tan(\\alpha_2)=F1(sen(\\alpha_1)+cos(\\alpha_1)*tan(\\alpha_2))}}$

        ${{\hspace{{4mm}} F1=\\dfrac{{F_R*tan(\\alpha_2)}}{{sen(\\alpha_1)+cos(\\alpha_1)*tan(\\alpha_2)}}}}$  

        ${{\hspace{{4mm}} F1={(f[0]*calc['tan5'])/(calc['sin1']+calc['cos1']*calc['tan5']):.2f}}} \\text{{ kN}}$

        Con el valor de F1 se calcula F2:  

        ${{\hspace{{4mm}} F2 = {((((-f[0]*calc['tan5'])/(calc['sin1']+calc['cos1']*calc['tan5']))*calc['cos1'])+f[0])/calc['cos5']:.2f}}} \\text{{ kN}}$
       """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_2
        code = 1120042,
        no_pregunta = 4,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"Para el descenso del globo aerostático mostrado en la figura se requiere una fuerza vertical de $FR={f[0]:.0f} \\text{{ kN}}$. Determine la magnitud de $F1$ y el ángulo $\\alpha_1$, si $F2 = {f[1]:.0f} \\text{{ kN}}$ y $\\alpha_2 = {a[4]:.0f}°$.",
        no_answers = 2,
        a1_name = "Magnitud $F1$ [kN]",
        a2_name = "Ángulo $\\alpha_1$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[0]-f[1]*calc['cos5'])/Calculations.cosine(Calculations.define_angle(f[0]-(f[1]*calc['cos5']), f[1]*calc['sin5'])),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(f[0]-(f[1]*calc['cos5']), f[1]*calc['sin5']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A17,
        ayuda2 = A20,
        ayuda3 = A21,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Se sugiere para la solución del ejercicio el siguiente método:

        $\\textbf{{\\small 1. Sumatoria de fuerzas en X y Y:}}$

        Se analiza de acuerdo con lo requerido en el enunciado a que equivale cada sumatoria.

        $\\underline{{Ecuación \\hspace{{2mm}} 1}}$  

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_x}} = F1_x + F2_x = -F1*sen(\\alpha_1) + F2*sen(\\alpha_2) = 0}}$

        $\\underline{{Ecuación \\hspace{{2mm}} 2}}$  

        ${{\hspace{{4mm}} \\sum{{F_y}} = F_R }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = F1_y + F2_y = -F1*cos(\\alpha_1)-F2*cos(\\alpha_2) = -F_R}}$
        
        $\\textbf{{\\small 2. Despeje del ángulo:}}$

        Para simplificar el proceso de despeje, se busca formar una tangente. Al hacer esto, se obtiene una expresión para hallar el ángulo desconocido.

        De la ecuación 2 se despeja F1:

        ${{\hspace{{4mm}} F1 = \\dfrac{{-F2*cos(\\alpha_2)-FR}}{{cos(\\alpha_1)}}}}$

        Se reemplaza F1 en la ecuación 1:

        ${{\hspace{{4mm}} F1 = -\\left(\\dfrac{{-F2*cos(\\alpha_2)-FR}}{{cos(\\alpha_1)}}\\right)*sen(\\alpha_1)+F2*sen(\\alpha_2) = 0}}$

        ${{\hspace{{4mm}} F1 = -({{-F2*cos(\\alpha_2)+FR}})*tan(\\alpha_1)=-F2*sen(\\alpha_2)}}$

        ${{\hspace{{4mm}} \\alpha_1 = tan^{-1}\\left(\\dfrac{{-F2*sen(\\alpha_2)}}{{F2*cos(\\alpha_2)+FR}}\\right)}}$    

        ${{\hspace{{4mm}} \\alpha_1 ={Calculations.define_angle(f[0]-(f[1]*calc['cos5']), f[1]*calc['sin5']):.2f} °}}$

        $\\textbf{{\\small 3. Despejar la magnitud:}}$

        Se puede retomar la ecuación de F1 mostrada en el paso anterior o despejarla de la ecuación 1:

        ${{\hspace{{4mm}} F1 = \\dfrac{{F2*sen(\\alpha_2)+F_R}}{{sen(\\alpha_1)}}}}$  
        ${{\hspace{{4mm}} F1 = {(f[0]-f[1]*calc['cos5'])/Calculations.cosine(Calculations.define_angle(f[0]-(f[1]*calc['cos5']), f[1]*calc['sin5'])):.2f} \\text{{ kN}}}}$
       """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#5_1
        code = 1120051,
        no_pregunta = 5,
        complexity = M,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud y dirección respecto al eje X positivo de la fuerza resultante de los vectores cartesianos $F_1=[({c[0]:.0f}) \\hat{{i}} + ({c[1]:.0f}) \\hat{{j}}] N$, $F_2=[({c[2]:.0f}) \\hat{{i}} + ({c[3]:.0f}) \\hat{{j}}] N$ y $F_3=[({c[4]:.0f}) \\hat{{i}} + ({c[5]:.0f}) \\hat{{j}}] N$",
        no_answers = 2,
        a1_name = Mag,
        a2_name = Dir,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(c[0]+c[2]+c[4],c[1]+c[3]+c[5]),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.define_angle(c[0]+c[2]+c[4],c[1]+c[3]+c[5]),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A11,
        ayuda2 = A15,
        ayuda3 = A13,
        respuesta_P1 = lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de las componentes X y Y de la fuerza resultante:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = F1_x + F2_x + F3_x = ({c[0]}) \\hat{{i}} + ({c[2]}) \\hat{{i}} + ({c[4]}) \\hat{{i}} = {c[0]+c[2]+c[4]:.2f} \\text{{ N}} }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{RY}} = F1_y + F2_y + F3_y = ({c[1]}) \\hat{{j}} + ({c[3]}) \\hat{{j}} + ({c[5]}) \\hat{{j}} ={c[1]+c[3]+c[5]:.2f} \\text{{ N}} }}$  

        $\\textbf{{\\small 2. Cálculo de la magnitud:}}$

        ${{\hspace{{4mm}} |F_R|=\\sqrt{{F_{{RX}}^2+F_{{RY}}^2}} = {Calculations.magnitude(c[0]+c[2]+c[4],c[1]+c[3]+c[5]):.2f} }} \\text{{ N}}$

        $\\textbf{{\\small 3. Cálculo de la dirección:}}$

        ${{\hspace{{4mm}} \\alpha ={Calculations.define_angle(c[0]+c[2]+c[4],c[1]+c[3]+c[5]):.2f}}}°$

        El cálculo del ángulo respecto al eje x positivo depende del cuadrante en el que se encuentra el vector:

        -Primer cuadrante:  $tan^{-1}\\left(\\dfrac{{componente \\hspace{{1mm}} \\hat{{j}} }} {{componente \\hspace{{1mm}} \\hat{{i}} }}\\right)$  

        -Segundo cuadrante: $180 - tan^{-1}\\left(\\dfrac{{componente \\hspace{{1mm}} \\hat{{j}} }}{{componente \\hspace{{1mm}} \\hat{{i}} }}\\right)$  

        -Tercer cuadrante:  $180 + tan^{-1}\\left(\\dfrac{{componente \\hspace{{1mm}} \\hat{{j}} }}{{componente \\hspace{{1mm}} \\hat{{i}} }}\\right)$  

        -Cuarto cuadrante:  $360 - tan^{-1}\\left(\\dfrac{{componente \\hspace{{1mm}} \\hat{{j}} }}{{componente \\hspace{{1mm}} \\hat{{i}} }}\\right)$ 
        
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Vectores 2D        ---------------------------------------------------
    #-------------------------------------------------    Nivel díficil       ---------------------------------------------------
    #-------------------------------------------------     Code: 113####      ---------------------------------------------------

    Questionary(#1_1
        code = 1130011,
        no_pregunta = 1,
        complexity = D,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las componentes de la fuerza $F$ a lo largo de los ejes $u-u$ y $v-v$, si se sabe que $|\\overrightarrow{{F}}|={f[0]:.0f} \\text{{ kN}}$, $\\alpha_1={a[0]:.0f}°$ y $\\alpha_2={a[4]:.0f}°$.",
        no_answers = 2,
        a1_name = "Componente $u$ [kN]",
        a2_name = "Componente $v$ [kN]",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round((f[0]*calc['sin1'])/Calculations.sine(180-a[0]-a[4]),2),
        answer2=lambda f, a, calc, c, d, m: np.round((f[0]*calc['sin5'])/Calculations.sine(180-a[0]-a[4]),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A22,
        ayuda2 = A23,
        ayuda3 = A24,
        respuesta_P1 = lambda f, a, calc, c, d, m: T1,     
        respuesta_P2 = lambda f, a, calc, c, d, m: rta_EQ_V2D_D_P1(f, a, calc),
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 1130021,
        no_pregunta = 2,
        complexity = D,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Si la componente de la fuerza a lo largo del eje $u-u$ debe ser ${f[0]:.0f} \\text{{ kN}}$. Determine la magnitud de F y su componente a lo largo del eje $v-v$ si se sabe que $\\alpha_1={a[0]:.0f}°$ y $\\alpha_2={a[4]:.0f}°$.",
        no_answers = 2,
        a1_name = Mag,
        a2_name = "Componente $v$ [kN]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[0]*Calculations.sine(180-a[0]-a[4]))/calc['sin1'],2),
        answer2 = lambda f, a, calc, c, d, m: np.round((f[0]*calc['sin5'])/calc['sin1'],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A22,
        ayuda2 = A23,
        ayuda3 = A25,
        respuesta_P1 = lambda f, a, calc, c, d, m: T1, 
        respuesta_P2 = lambda f, a, calc, c, d, m: rta_EQ_V2D_D_P2(f, a, calc),
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),
    
    Questionary(#3_1
        code = 1130031,
        no_pregunta = 3,
        complexity = D,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle las componentes X y Y de la fuerza F si la componente $F_u$ es ${f[0]:.0f} \\text{{ kN}}$. Considere que $\\alpha_u={a[0]:.0f}°$, $\\alpha_v={a[8]:.0f}°$ y $\\alpha_Y={a[4]:.0f}°$.",
        no_answers = 2,
        a1_name = "Componente en X [kN]",
        a2_name = "Componente en Y [kN]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((f[0]*Calculations.sine(180-a[0]-a[8]))/calc['sin9'])*calc['sin5'],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((f[0]*Calculations.sine(180-a[0]-a[8]))/calc['sin9'])*calc['cos5'],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A22,
        ayuda2 = A23,
        ayuda3 = A25,
        respuesta_P1 = lambda f, a, calc, c, d, m: T1, 
        respuesta_P2 = lambda f, a, calc, c, d, m: rta_EQ_V2D_D_P3(f, a, calc),
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),
    
    Questionary(#4_1
        code = 1130041,
        no_pregunta = 4,
        complexity = D,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Para remolcar el bote se requiere una fuerza horizontal, a lo largo del eje X positivo, de ${f[0]:.0f}\\text{{ kN}}$. Determine las magnitudes de $F1$, $F2$ y el ángulo $\\alpha_2$ de forma que $F2$ sea mínima. Considere que $F1$ se ejerce a ${a[0]:.0f}$° del eje X ($\\alpha_1$).",
        no_answers = 3,
        a1_name = "Magnitud $F1$ [kN]",
        a2_name = "Magnitud $F2$ [kN]",
        a3_name = "Ángulo $\\alpha_2$",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*Calculations.sine(180-90-a[0]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*Calculations.sine(a[0]),2),
        answer3 = lambda f, a, calc, c, d, m: 180-90-a[0],
        ayuda1 = A27,
        ayuda2 = A28,
        ayuda3 = A29,
        respuesta_P1 = lambda f, a, calc, c, d, m: T2, 
        respuesta_P2 = lambda f, a, calc, c, d, m: rta_EQ_V2D_D_P4(f, a, calc),
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),

    Questionary(#5_1
        code = 1130051,
        no_pregunta = 5,
        complexity = D,
        topic = EQ,
        subtopic = V2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud mínima de la fuerza resultante de las tres fuerzas ($FR$) y la fuerza $F2$ que las genera. Considere que $F1$ es ${f[0]:.0f}\\text{{ kN}}$, $F3$ es ${f[1]:.0f}\\text{{ kN}}$ y $\\alpha_1$ es ${85-Calculations.define_angle(f[1],f[0]):.2f}$°",
        no_answers = 2,
        a1_name = "Magnitud $FR$ [kN]",
        a2_name = "Magnitud $F2$ [kN]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[1],f[0])*Calculations.sine(85),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude(f[1],f[0])*Calculations.sine(180-90-85),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A30,
        ayuda2 = A31,
        ayuda3 = A32,
        respuesta_P1 = lambda f, a, calc, c, d, m: rta_EQ_V2D_D_P5_P1(f[1], f[0], a),
        respuesta_P2 = lambda f, a, calc, c, d, m: rta_EQ_V2D_D_P5_P2(f[1], f[0], a),
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),

    
    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------       Vectores 3D       ---------------------------------------------------
    #-------------------------------------------------       Nivel fácil       ---------------------------------------------------
    #-------------------------------------------------     Code: 121####       ---------------------------------------------------

    Questionary(#1_1
        code = 1210011,
        no_pregunta = 1,
        complexity = F,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle las componentes del vector $F={f[0]:.0f} \\text{{ N}}$, si $\\theta_1 = {a[0]:.0f}\\degree$ y $\\theta_2 = {a[4]:.0f}\\degree$.",
        no_answers = 3,
        a1_name = Ci,
        a2_name = Cj,
        a3_name = Ck,
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['sin1']*calc['sin5'],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['sin1']*calc['cos5'],2),
        answer3 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['cos1'],2),
        ayuda1 = A33,
        ayuda2 = A34,
        ayuda3 = A35,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta el procedimiento sugerido para hallar las componentes:
        
        $\\textbf{{\\small 1. Cálculo de las componentes X y Y:}}$

        Se recomienda primero proyectar el vector F en el plano XY y luego utilizar la trigonometría para determinar sus componentes.

        ${{\\text{{Componente en X: }} F*sen(\\theta_1)*sen(\\theta_2) = [{f[0]*calc['sin1']*calc['sin5']:.2f} \\hat{{ i}}] N}}$     
        ${{\\text{{Componente en Y: }} F*sen(\\theta_1)*cos(\\theta_2) = [{f[0]*calc['sin1']*calc['cos5']:.2f} \\hat{{ j}}] N}}$       

        $\\textbf{{\\small 2. Cálculo de la componente Z (k):}}$

        El ángulo $\\theta_1$ permite encontrar directamente la componente en Z.

        ${{\\text{{Componente en Z: }} F*cos(\\theta_1) = [{f[0]*calc['cos1']:.2f} \\hat{{ k}}] N}}$

        De acuerdo con lo anterior el vector cartesiano de $\\overrightarrow{{F1}}$ es $[{f[0]*calc['sin1']*calc['sin5']:.2f} \\hat{{i}} + {f[0]*calc['sin1']*calc['cos5']:.2f} \\hat{{j}} + {f[0]*calc['cos1']:.2f} \\hat{{k}}] N$.       
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 1210021,
        no_pregunta = 2,
        complexity = F,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine los ángulos directores coordenados del vector $F={f[0]:.0f} \\text{{ N}}$, si $\\theta_1 = {a[0]:.0f}\\degree$ y $\\theta_2 = {a[4]:.0f}\\degree$.",
        no_answers = 3,
        a1_name = A3X,
        a2_name = A3Y,
        a3_name = A3Z,
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*calc['sin1']*calc['sin5'],f[0]),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*calc['sin1']*calc['cos5'],f[0]),2),
        answer3=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*calc['cos1'],f[0]),2),
        ayuda1 = A36,
        ayuda2 = A37 ,
        ayuda3 = A38,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para determinar los ángulos directores del vector, se calcula el arcocoseno de cada una de sus componentes divididas por la magnitud del vector F.
        
        $\\textbf{{\\small 1. Cálculo de las componentes X, Y y Z:}}$

        ${{\hspace{{4mm}}\\text{{Componente en X: }}}} F*sen(\\theta_1)*sen(\\theta_2) = {f[0]*calc['sin1']*calc['sin5']:.2f} \\text{{ N}}$     
        ${{\hspace{{4mm}}\\text{{Componente en Y: }}}} F*sen(\\theta_1)*cos(\\theta_2) = {f[0]*calc['sin1']*calc['cos5']:.2f} \\text{{ N}}$      
        ${{\hspace{{4mm}} \\text{{Componente en Z: }}}} F*cos(\\theta_1) = {f[0]*calc['cos1']:.2f} \\text{{ N}}$    

        $\\textbf{{\\small 2. Cálculo de los ángulos directores coordenados:}}$

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a X: }} \\alpha = cos^{-1}\\left(\\dfrac{{F_X}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(f[0]*calc['sin1']*calc['sin5'],f[0]):.2f}°}}$    
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Y: }} \\beta = cos^{-1}\\left(\\dfrac{{F_Y}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(f[0]*calc['sin1']*calc['cos5'],f[0]):.2f}°}}$    
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Z: }} \\gamma = cos^{-1}\\left(\\dfrac{{F_Z}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(f[0]*calc['cos1'],f[0]):.2f}°}}$    
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 1210031,
        no_pregunta = 3,
        complexity = F,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud del vector $\\overrightarrow{{F}}$ si $F_x = {f[0]:.0f}\\text{{ N}}$, $F_y = {f[1]:.0f}\\text{{ N}}$ y $F_z = {f[2]:.0f}\\text{{ N}}$.",
        no_answers = 1,
        a1_name = "Magnitud [N]]",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D(f[0],f[1],f[2]),2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A39,
        ayuda2 = A40,
        ayuda3="",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución del ejercicio:

        $\\textbf{{\\small 1. Definir el vector cartesiano:}}$

        El vector cartesiano de $\\overrightarrow{{F}}$ es $[{f[0]:.0f}\\hspace{{1mm}}\\hat{{i}}+{f[1]:.0f}\\hspace{{1mm}}\\hat{{j}}-{f[2]:.0f}\\hspace{{1mm}}\\hat{{k}}]N$. Recuerde que las componentes $\\hat{{i}}, \\hat{{j}}, \\hat{{k}}$ se extienden a lo largo de los ejes X, Y y Z, respectivamente. 
        
        $\\textbf{{\\small 2. Cálculo de la magnitud:}}$

        La magnitud se calcula como $\\sqrt{{F_x^2 + F_y^2 + F_z^2}}$ = $|\\overrightarrow{{F}}|={Calculations.magnitude3D(f[0],f[1],f[2]):.2f}\\text{{ N}}$       
        """,  
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#4_1
        code = 1210041,
        no_pregunta = 4,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vectores 3D",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine los ángulos directores del vector F si $F_x = {f[0]:.0f}\\text{{ N}}$, $F_y = {f[1]:.0f}\\text{{ N}}$ y $F_z = {f[2]:.0f}\\text{{ N}}$.",
        no_answers = 3,
        a1_name = "Ángulo respecto a X $(\\alpha)$ [°]",
        a2_name = "Ángulo respecto a Y $(\\beta)$ [°]",
        a3_name = "Ángulo respecto a Z $(\\gamma)$ [°]",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0],Calculations.magnitude3D(f[0],f[1],f[2])),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[1],Calculations.magnitude3D(f[0],f[1],f[2])),2),
        answer3=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[2],Calculations.magnitude3D(f[0],f[1],f[2])),2),
        ayuda1 = A36,
        ayuda2 = A39,
        ayuda3 = A40,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para determinar los ángulos directores del vector, se calcula el arcocoseno de cada una de sus componentes divididas por la magnitud del vector $\\overrightarrow{{F}}$.
        
        $\\textbf{{\\small 1. Cálculo de la magnitud:}}$

         La magnitud se calcula como $\\sqrt{{F_x^2 + F_y^2 + F_z^2}}=$ $|\\overrightarrow{{F}}|={Calculations.magnitude3D(f[0],f[1],f[2]):.2f}\\text{{ N}}$

        $\\textbf{{\\small 2. Cálculo de los ángulos directores coordenados:}}$

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a X: }} \\alpha = cos^{-1}\\left(\\dfrac{{F_X}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(f[0],Calculations.magnitude3D(f[0],f[1],f[2])):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Y: }} \\beta = cos^{-1}\\left(\\dfrac{{F_Y}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(f[1],Calculations.magnitude3D(f[0],f[1],f[2])):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Z: }} \\gamma = cos^{-1}\\left(\\dfrac{{F_Z}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(f[2],Calculations.magnitude3D(f[0],f[1],f[2])):.2f}°}}$
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#5_1
        code = 1210051,
        no_pregunta = 5,
        complexity = F,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle las componentes del vector $\\overrightarrow{{F}}$ si su magnitud es ${f[0]:.0f} \\text{{ N}}$ y sus ángulos coordenados son $\\alpha_x = {a[0]:.0f}°$, $\\beta_y = {a[5]:.0f}°$ y $\\gamma_z = {a[4]:.0f}°$  ",
        no_answers = 3,
        a1_name = Ci,
        a2_name = Cj,
        a3_name = Ck,
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*Calculations.cosine(a[0]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*Calculations.cosine(a[5]),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(f[0]*Calculations.cosine(a[4]),2),
        ayuda1 = "Los ángulos directores relacionan directamente al vector F con cada uno de los ejes.",
        ayuda2 = A42,
        ayuda3 = "Calcule las componentes de cada eje como la multiplicación de la fuerza por el coseno del ángulo que forma con dicho eje.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para calcular las componentes se multiplica la magnitud del vector F con el coseno del ángulo que forma la fuerza con el eje.
        
        $\\textbf{{\\small 1. Cálculo de las componentes:}}$

        ${{\hspace{{4mm}} \\text{{Componente en X: }} F_x = F*cos(\\alpha_x)={f[0]*Calculations.cosine(a[0]):.2f} \\text{{ N}}}}$
        ${{\hspace{{4mm}} \\text{{Componente en Y: }} F_y = F*cos(\\beta_y)={f[0]*Calculations.cosine(a[5]):.2f} \\text{{ N}}}}$
        ${{\hspace{{4mm}} \\text{{Componente en Z: }} F_z = F*cos(\\gamma_z)={f[0]*Calculations.cosine(a[4]):.2f} \\text{{ N}}}}$
        
        De acuerdo con lo anterior el vector cartesiano de F es:  $\\overrightarrow{{F}} = [({f[0]*Calculations.cosine(a[0]):.2f})\\hspace{{1mm}}\\hat{{i}} + ({f[0]*Calculations.cosine(a[5]):.2f})\\hspace{{1mm}}\\hat{{j}} + ({f[0]*Calculations.cosine(a[4]):.2f}) \\hspace{{1mm}}\\hat{{k}} ] N$.
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------       Vectores 3D       --------------------------------------------------
    #-------------------------------------------------       Nivel medio       --------------------------------------------------
    #-------------------------------------------------     Code: 122####       ---------------------------------------------------

    Questionary(#1_1
        code = 1220011,
        no_pregunta = 1,
        complexity = M,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle la magnitud de la fuerza resultante ($FR$) entre los vectores $F1$ y $F2$. Suponga que $F1 = {f[0]:.0f} \\text{{ N}}$, $F2 = {f[1]:.0f} \\text{{ N}}$, $\\theta_1 = {Calculations.arccosine(f[0]*(5/13)*Calculations.sine(a[0]),f[0]):.3f}\\degree$, $\\theta_2 = {Calculations.arccosine(f[0]*(5/13)*Calculations.cosine(a[0]),f[0]):.3f}\\degree$ y $\\theta_3 = {a[4]:.3f}\\degree$.",
        no_answers = 1,
        a1_name = "Magnitud $FR$ $[N]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D(f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*Calculations.sine(a[4]),f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*Calculations.cosine(a[4]),-f[0]*(12/13)+f[1]*(3/5)),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A41,
        ayuda2 = A42,
        ayuda3 = A40,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución del ejercicio:
        
        $\\textbf{{\\small 1. Cálculo de las componentes de la fuerza resultante FR en X, Y y Z:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_x = F1*cos(\\theta_1) + F2*\\dfrac{{4}}{{5}}*sen(\\theta_3) = {f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*calc['sin5']:.2f} \\text{{ N}}}}$
        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_y = F1*cos(\\theta_2) + F2*\\dfrac{{4}}{{5}}*cos(\\theta_3) = {f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*calc['cos5']:.2f} \\text{{ N}}}}$
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_z = -F1*\\dfrac{{12}}{{13}} + F2*\\dfrac{{3}}{{5}} = {-f[0]*(12/13)+f[1]*(3/5):.2f} \\text{{ N}} }}$
        
        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante FR es:  $\\overrightarrow{{FR}} = [({f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*calc['sin5']:.2f})\\hspace{{1mm}}\\hat{{i}} + ({f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*calc['cos5']:.2f})\\hspace{{1mm}}\\hat{{j}} + ({-f[0]*(12/13)+f[1]*(3/5):.2f}) \\hspace{{1mm}}\\hat{{k}}] \\text{{ N}}$ .
        
        $\\textbf{{\\small 2. Cálculo de la magnitud de la fuerza resultante FR:}}$

        ${{\hspace{{4mm}} |\\overrightarrow{{FR}}|= \\sqrt{{FR_x^2 + FR_y^2 + FR_z^2}} = {Calculations.magnitude3D(f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*calc['sin5'],f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*calc['cos5'],-f[0]*(12/13)+f[1]*(3/5)):.2f} \\text{{ N}}}}$       
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations',
        ),

    Questionary(#2_1
        code = 1220021,
        no_pregunta = 2,
        complexity = M,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle los ángulos directores coordenados de la fuerza resultante ($FR$) entre los vectores $F1$ y $F2$. Suponga que $F1 = {f[0]:.0f} \\text{{ N}}$, $F2 = {f[1]:.0f} \\text{{ N}}$, $\\theta_1 = {Calculations.arccosine(f[0]*(5/13)*Calculations.sine(a[0]),f[0]):.3f}\\degree$, $\\theta_2 = {Calculations.arccosine(f[0]*(5/13)*Calculations.cosine(a[0]),f[0]):.3f}\\degree$ y $\\theta_3 = {a[4]:.3f}\\degree$.",
        no_answers = 3,
        a1_name = A3X,
        a2_name = A3Y,
        a3_name = A3Z,
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*calc['sin5'],Calculations.magnitude3D(f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*calc['sin5'],f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*calc['cos5'],-f[0]*(12/13)+f[1]*(3/5))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*calc['cos5'],Calculations.magnitude3D(f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*calc['sin5'],f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*calc['cos5'],-f[0]*(12/13)+f[1]*(3/5))),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(-f[0]*(12/13)+f[1]*(3/5),Calculations.magnitude3D(f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*calc['sin5'],f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*calc['cos5'],-f[0]*(12/13)+f[1]*(3/5))),2),
        ayuda1 = A36,
        ayuda2 = A37,
        ayuda3 = A38,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para determinar los ángulos directores del vector, se calcula el arcocoseno de cada una de sus componentes divididas por la magnitud del vector F.
        
        $\\textbf{{\\small 1. Cálculo de las componentes de la fuerza resultante FR en X, Y y Z:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_x = F1*cos(\\theta_1) + F2*\\dfrac{{4}}{{5}}*sen(\\theta_3) = {f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*calc['sin5']:.2f} \\text{{ N}}}}$
        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_y = F1*cos(\\theta_2) + F2*\\dfrac{{4}}{{5}}*cos(\\theta_3) = {f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*calc['cos5']:.2f} \\text{{ N}}}}$
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_z = -F1*\\dfrac{{12}}{{13}} + F2*\\dfrac{{3}}{{5}} = {-f[0]*(12/13)+f[1]*(3/5):.2f} \\text{{ N}} }}$
        
        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante FR es:  $\\overrightarrow{{FR}} = [({f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*calc['sin5']:.2f})\\hspace{{1mm}}\\hat{{i}} + ({f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*calc['cos5']:.2f})\\hspace{{1mm}}\\hat{{j}} + ({-f[0]*(12/13)+f[1]*(3/5):.2f}) \\hspace{{1mm}}\\hat{{k}}] \\text{{ N}}$ .
        
        $\\textbf{{\\small 2. Cálculo de la magnitud de la fuerza resultante FR:}}$

        ${{\hspace{{4mm}} |\\overrightarrow{{FR}}|= \\sqrt{{FR_x^2 + FR_y^2 + FR_z^2}} = {Calculations.magnitude3D(f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*calc['sin5'],f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*calc['cos5'],-f[0]*(12/13)+f[1]*(3/5)):.2f} \\text{{ N}}}}$       
        
        $\\textbf{{\\small 3. Cálculo de los ángulos directores coordenados:}}$

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a X: }} \\alpha = cos^{-1}\\left(\\dfrac{{FR_x}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*calc['sin5'],Calculations.magnitude3D(f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*calc['sin5'],f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*calc['cos5'],-f[0]*(12/13)+f[1]*(3/5))):.2f}°}}$

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Y: }} \\beta = cos^{-1}\\left(\\dfrac{{FR_y}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*calc['cos5'],Calculations.magnitude3D(f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*calc['sin5'],f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*calc['cos5'],-f[0]*(12/13)+f[1]*(3/5))):.2f}°}}$

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Z: }} \\gamma = cos^{-1}\\left(\\dfrac{{FR_z}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(-f[0]*(12/13)+f[1]*(3/5),Calculations.magnitude3D(f[0]*(f[0]*(5/13)*Calculations.sine(a[0])/f[0])+f[1]*(4/5)*calc['sin5'],f[0]*(f[0]*(5/13)*Calculations.cosine(a[0])/f[0])+f[1]*(4/5)*calc['cos5'],-f[0]*(12/13)+f[1]*(3/5))):.2f}°}}$
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#3_1
        code = 1220031,
        no_pregunta = 3,
        complexity = M,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de $F1$ y $F2$ para que la componente X de la fuerza resultante sea ${f[0]:.2f} \\text{{ N}}$ y la componente Z sea ${f[0]*0.7:.2f} \\text{{ N}}$ cuando $\\theta_1 = {Calculations.arccosine(f[0]*(5/13)*Calculations.sine(a[0]),f[0]):.3f}\\degree$, $\\theta_2 = {Calculations.arccosine(f[0]*(5/13)*Calculations.cosine(a[0]),f[0]):.3f}\\degree$ y $\\theta_3 = {a[4]:.3f}\\degree$.",
        no_answers = 2,
        a1_name = "Magnitud $F1$ $[N]$",
        a2_name = "Magnitud $F2$ $[N]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[0]-f[0]*0.7*(4/3)*calc['sin5'])/(Calculations.cosine((Calculations.arccosine(f[0]*(5/13)*Calculations.sine(a[0]),f[0])))+(4/3)*(12/13)*calc['sin5']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((f[0]*0.7+(12/13)*((f[0]-f[0]*0.7*(4/3)*calc['sin5'])/(Calculations.cosine(Calculations.arccosine(f[0]*(5/13)*Calculations.sine(a[0]),f[0]))+(4/3)*(12/13)*calc['sin5'])))*(5/3),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A44,
        ayuda2 = A37,
        ayuda3 = A38,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Sistema de ecuaciones - Sumatoria de fuerzas en X y Z:}}$

        $\\underline{{Ecuación \\hspace {{1mm}} 1}}$  
        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_x = F1*cos(\\theta_1) + F2*\\dfrac{{4}}{{5}}*sen(\\theta_3)}}$         
        ${{\hspace{{4mm}}  {f[0]:.2f} = F1*cos(\\theta_1) + F2*\\dfrac{{4}}{{5}}*sen(\\theta_3)}}$       

        $\\underline{{Ecuación \\hspace {{1mm}} 2}}$       
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_z = -F1*\\dfrac{{12}}{{13}} + F2*\\dfrac{{3}}{{5}} }}$  

        ${{\hspace{{4mm}} {f[0]*0.7:.2f} = -F1*\\dfrac{{12}}{{13}} + F2*\\dfrac{{3}}{{5}} }}$           

        $\\textbf{{\\small 2. Despejar las magnitudes F1 y F2:}}$

        De la ecuación 2 se despeja $F2$ en términos de $F1$:

        ${{\hspace{{4mm}} FR_Z + F1*\\dfrac{{12}}{{13}} = F2*\\dfrac{{3}}{{5}} }}$            

        ${{\hspace{{4mm}} F2 = \\dfrac{{5}}{{3}}*\\left(FR_Z + F1*\\dfrac{{12}}{{13}}\\right) }}$

        Se reemplaza $F2$ en la ecuación 1:

        ${{\hspace{{4mm}} FR_X = F1*cos(\\theta_1) + \\left(\\dfrac{{5}}{{3}}*\\left(FR_Z + F1*\\dfrac{{12}}{{13}}\\right)\\right)*\\dfrac{{4}}{{5}}*sen(\\theta_3)}}$           
        ${{\hspace{{4mm}} FR_X - F1*cos(\\theta_1) = \\left(\\dfrac{{4}}{{3}}*\\left(FR_Z + F1*\\dfrac{{12}}{{13}}\\right)\\right)*sen(\\theta_3)}}$          
        ${{\hspace{{4mm}} FR_X - F1*cos(\\theta_1) = \\dfrac{{4}}{{3}}*FR_Z*sen(\\theta_3) + \\dfrac{{4}}{{3}}*sen(\\theta_3)*F1*\\dfrac{{12}}{{13}} }}$      
        ${{\hspace{{4mm}} FR_X - \\dfrac{{4}}{{3}}*FR_Z*sen(\\theta_3) = \\dfrac{{4}}{{3}}*sen(\\theta_3)*F1*\\dfrac{{12}}{{13}} + F1*cos(\\theta_1) }}$    
        ${{\hspace{{4mm}} F1\\left(\dfrac{{4}}{{3}}*sen(\\theta_3)*\\dfrac{{12}}{{13}} + cos(\\theta_1) \\right) =  FR_X - \\dfrac{{4}}{{3}}*FR_Z*sen(\\theta_3)}}$   
           
        ${{\hspace{{4mm}} F1 = \\dfrac{{FR_X - \\dfrac{{4}}{{3}}*FR_Z*sen(\\theta_3)}}{{\dfrac{{4}}{{3}}*sen(\\theta_3)*\\dfrac{{12}}{{13}} + cos(\\theta_1) }}}}$    
       
        Reemplazando en las ecuaciones de $F1$ y $F2$ se obtiene: 

        $F1 = {(f[0]-f[0]*0.7*(4/3)*calc['sin5'])/(Calculations.cosine((Calculations.arccosine(f[0]*(5/13)*Calculations.sine(a[0]),f[0])))+(4/3)*(12/13)*calc['sin5']):.2f} \\text{{N}}$    
        $F2 = {(f[0]*0.7+(12/13)*((f[0]-f[0]*0.7*(4/3)*calc['sin5'])/(Calculations.cosine(Calculations.arccosine(f[0]*(5/13)*Calculations.sine(a[0]),f[0]))+(4/3)*(12/13)*calc['sin5'])))*(5/3):.2f} \\text{{N}}$    
       """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#4_1
        code = 1220041,
        no_pregunta = 4,
        complexity = M,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle la magnitud de la fuerza resultante ($FR$) entre los vectores $F_1=[({c[0]:.0f})\\hspace{{1mm}}\\hat{{i}} + ({c[1]:.0f}) \\hspace{{1mm}}\\hat{{j}} + ({c[2]:.0f}) \\hspace{{1mm}}\\hat{{k}}] N$, $F_2=[({c[3]:.0f})\\hspace{{1mm}}\\hat{{i}} + ({c[4]:.0f}) \\hspace{{1mm}}\\hat{{j}} + ({c[5]:.0f}) \\hspace{{1mm}}\\hat{{k}}] N$.",
        no_answers = 1,
        a1_name = "Magnitud $FR$ [N]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5]),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A42,
        ayuda2 = A40,
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de las componentes X, Y y Z de la fuerza resultante (FR):}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_{{x}} = F1_x + F2_x = ({c[0]}) i + ({c[3]}) i = {c[0]+c[3]:.2f} \\text{{ N}} }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_{{y}} = F1_y + F2_y = ({c[1]}) j + ({c[4]}) j = {c[1]+c[4]:.2f} \\text{{ N}} }}$  
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_{{z}} = F1_z + F2_z = ({c[2]}) k + ({c[5]}) k = {c[2]+c[5]:.2f} \\text{{ N}} }}$  

        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante $FR$ es:  $\\overrightarrow{{FR}} = ({c[0]+c[3]:.2f}) \\hspace{{1mm}}\\hat{{i}} + ({c[1]+c[4]:.2f}) \\hspace{{1mm}}\\hat{{j}} + ({c[2]+c[5]:.2f}) \\hspace{{1mm}}\\hat{{k}}$.

        $\\textbf{{\\small 2. Cálculo de la magnitud:}}$

        ${{\hspace{{4mm}} |\\overrightarrow{{FR}}| = \\sqrt{{FR_x^2 + FR_y^2 + FR_z^2}} = {Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5]):.2f} \\text{{ N}} }}$       
       """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#5_1
        code = 1220051,
        no_pregunta = 5,
        complexity = M,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle los ángulos directores coordenados de la fuerza resultante ($FR$) entre los vectores $F_1=[({c[0]:.0f}) \\hspace{{1mm}}\\hat{{i}} + ({c[1]:.0f}) \\hspace{{1mm}}\\hat{{j}} + ({c[2]:.0f}) \\hspace{{1mm}}\\hat{{k}}] N$, $F_2=[({c[3]:.0f}) \\hspace{{1mm}}\\hat{{i}} + ({c[4]:.0f}) \\hspace{{1mm}}\\hat{{j}} + ({c[5]:.0f}) \\hspace{{1mm}}\\hat{{k}}] N $.",
        no_answers = 3,
        a1_name = A3X,
        a2_name = A3Y,
        a3_name = A3Z,
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine((c[0]+c[3]),Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5])),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine((c[1]+c[4]),Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5])),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine((c[2]+c[5]),Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5])),2),
        ayuda1 = A42,
        ayuda2 = A36,
        ayuda3 = A40,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para determinar los ángulos directores del vector, se calcula el arcocoseno de cada una de sus componentes divididas por la magnitud del vector F.
        
        $\\textbf{{\\small 1. Cálculo de las componentes X, Y y Z de la fuerza resultante (FR):}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_x = F1_x + F2_x = ({c[0]}) \\hspace{{1mm}}\\hat{{i}} + ({c[3]}) \\hspace{{1mm}}\\hat{{i}} = {c[0]+c[3]:.2f} \\text{{ N}} }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_y = F1_y + F2_y = ({c[1]}) \\hspace{{1mm}}\\hat{{j}} + ({c[4]}) \\hspace{{1mm}}\\hat{{j}} = {c[1]+c[4]:.2f} \\text{{ N}} }}$  
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_z = F1_z + F2_z = ({c[2]}) \\hspace{{1mm}}\\hat{{k}} + ({c[5]}) \\hspace{{1mm}}\\hat{{k}} = {c[2]+c[5]:.2f} \\text{{ N}} }}$  

        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante $FR$ es:  $\\overrightarrow{{FR}} = ({c[0]+c[3]:.2f}) \\hspace{{1mm}}\\hat{{i}} + ({c[1]+c[4]:.2f}) \\hspace{{1mm}}\\hat{{j}} + ({c[2]+c[5]:.2f}) \\hspace{{1mm}}\\hat{{k}}$.

        $\\textbf{{\\small 2. Cálculo de los ángulos directores coordenados:}}$

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a X: }} \\alpha = cos^{-1}\\left(\\dfrac{{FR_x}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine((c[0]+c[3]),Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5])):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Y: }} \\beta = cos^{-1}\\left(\\dfrac{{FR_y}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine((c[1]+c[4]),Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5])):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Z: }} \\gamma = cos^{-1}\\left(\\dfrac{{FR_z}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine((c[2]+c[5]),Calculations.magnitude3D(c[0]+c[3],c[1]+c[4],c[2]+c[5])):.2f}°}}$
       """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------       Vectores 3D       --------------------------------------------------
    #-------------------------------------------------       Nivel díficil       --------------------------------------------------
    #-------------------------------------------------     Code: 123##        ---------------------------------------------------

    Questionary(#1_1
        code = 1230011,
        no_pregunta = 1,
        complexity = D,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de $F1$ para que la componente Z de la fuerza resultante sea ${f[5]*0.7:.2f}$ $\\text{{ N}}$. Suponga que $F2 = {f[5]*8:.0f} \\text{{ N}}$ y se ubica en las coordenadas $X,Y,Z$ $(-{d[0]:.0f}, -{d[3]:.0f}, {d[6]:.0f})$, $F3 = {f[2]:.0f} \\text{{ N}}$, $F4 = {f[3]:.0f} \\text{{ N}}$, $\\theta_1 = {a[0]:.0f}\\degree$ y $\\theta_2 = {a[4]:.0f}\\degree$.",
        no_answers = 1,
        a1_name = "Magnitud $F1$ $[N]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[5]*8*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5)-f[5]*0.7)/calc['sin1'],2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A44,
        ayuda2 = A37,
        ayuda3 = A38,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Sumatoria de fuerzas en Z:}}$

        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_z = -F1*sen(\\theta_1)+F2*\\left(\\dfrac{{z}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)-F4*(4/5)}}$     

        $\\textbf{{\\small 2. Despejar la magnitudes de F1:}}$

        ${{\hspace{{4mm}} F1*sen(\\theta_1) = F2*\\left(\\dfrac{{z}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)-F4*(4/5)- FR_z }}$        
        ${{\hspace{{4mm}} F1 = \\dfrac{{F2*\\left(\\dfrac{{z}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)-F4*(4/5)- FR_z}}{{sen(\\theta_1)}} }}$

        $F1 = {(f[5]*8*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5)-f[5]*0.7)/calc['sin1']:.2f} \\text{{ N}}$
       """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#2_1
        code = 1230021,
        no_pregunta = 2,
        complexity = D,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle la magnitud de la fuerza resultante ($FR$). Suponga que $F1 = {f[0]:.0f} \\text{{ N}}$, $F2 = {f[1]:.0f} \\text{{ N}}$ y se extiende desde el origen hasta las coordenadas $X,Y,Z$ $(-{d[0]:.0f}, -{d[3]:.0f}, {d[6]:.0f})$, $F3 = {f[2]:.0f} \\text{{ N}}$, $F4 = {f[3]:.0f} \\text{{ N}}$, $\\theta_1 = {a[0]:.0f}\\degree$ y $\\theta_2 = {a[4]:.0f}\\degree$.",
        no_answers = 1,
        a1_name = "Magnitud $FR$ $[N]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*d[3]/Calculations.magnitude3D(d[0],d[3],d[6])+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5)),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A41,
        ayuda2 = A42,
        ayuda3 = A43,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución del ejercicio:
        
        $\\textbf{{\\small 1. Cálculo de las componentes de la fuerza resultante FR en X, Y y Z:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_x = -F1*cos(\\theta_1)-F2*\\left(\\dfrac{{x}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)-F3*sen(\\theta_2) = {-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5']:.2f} \\text{{ N}}}}$
        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_y = -F2*\\left(\\dfrac{{y}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)+F3*cos(\\theta_2)+F4*\\dfrac{{3}}{{5}} = {-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5):.2f} \\text{{ N}}}}$
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_z = -F1*sen(\\theta_1)+F2*\\left(\\dfrac{{z}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)-F4*\\dfrac{{4}}{{5}} = {-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5):.2f} \\text{{ N}}}}$
        
        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante FR es:  $\\overrightarrow{{F}} = [({-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5']:.2f})\\hspace{{1mm}}\\hat{{i}} + ({-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5):.2f}) \\hspace{{1mm}}\\hat{{j}} +  ({-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5):.2f}) \\hspace{{1mm}}\\hat{{k}}] \\text{{ N}}$.
        
        $\\textbf{{\\small 2. Cálculo de la magnitud de la fuerza resultante FR:}}$

        ${{\hspace{{4mm}} |\\overrightarrow{{FR}}|= \\sqrt{{FR_x^2 + FR_y^2 + FR_z^2}} = {Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5)):.2f} \\text{{ N}}}}$       
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#3_1
        code = 1230031,
        no_pregunta = 3,
        complexity = D,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle los ángulos directores coordenados de la fuerza resultante ($FR$).Suponga que $F1 = {f[0]:.0f} \\text{{ N}}$, $F2 = {f[1]:.0f} \\text{{ N}}$ y se extiende desde el origen hasta las coordenadas $X,Y,Z$ $(-{d[0]:.0f}, -{d[3]:.0f}, {d[6]:.0f})$, $F3 = {f[2]:.0f} \\text{{ N}}$, $F4 = {f[3]:.0f} \\text{{ N}}$, $\\theta_1 = {a[0]:.0f}\\degree$ y $\\theta_2 = {a[4]:.0f}\\degree$.",
        no_answers = 3,
        a1_name = A3X,
        a2_name = A3Y,
        a3_name = A3Z,
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*d[3]/Calculations.magnitude3D(d[0],d[3],d[6])+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*d[3]/Calculations.magnitude3D(d[0],d[3],d[6])+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5))),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5),Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*d[3]/Calculations.magnitude3D(d[0],d[3],d[6])+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5))),2),
        ayuda1 = A41,
        ayuda2 = A36,
        ayuda3 = A40,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para determinar los ángulos directores del vector, se calcula el arcocoseno de cada una de sus componentes divididas por la magnitud del vector F.
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_x = -F1*cos(\\theta_1)-F2*\\left(\\dfrac{{x}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)-F3*sen(\\theta_2) = {-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5']:.2f} \\text{{ N}}}}$
        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_y = -F2*\\left(\\dfrac{{y}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)+F3*cos(\\theta_2)+F4*\\dfrac{{3}}{{5}} = {-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5):.2f} \\text{{ N}}}}$
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_z = -F1*sen(\\theta_1)+F2*\\left(\\dfrac{{z}}{{\\sqrt{{x^2+y^2+z^2}}}}\\right)-F4*\\dfrac{{4}}{{5}} = {-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5):.2f} \\text{{ N}}}}$
      
        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante $FR$ es:  $\\overrightarrow{{F}} = [({-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5']:.2f})\\hspace{{1mm}} \\hat{{i}} + ({-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5):.2f}) \\hspace{{1mm}} \\hat{{j}} +  ({-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5):.2f}) \\hspace{{1mm}} \\hat{{i}}] \\text{{ N}}$.
       
        $\\textbf{{\\small 2. Cálculo de la magnitud de la fuerza resultante FR:}}$

        ${{\hspace{{4mm}} |\\overrightarrow{{FR}}|= \\sqrt{{FR_x^2 + FR_y^2 + FR_z^2}} = {Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5)):.2f} \\text{{ N}}}}$       
        
        $\\textbf{{\\small 3. Cálculo de los ángulos directores coordenados:}}$

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a X: }} \\alpha = cos^{-1}\\left(\\dfrac{{FR_x}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*d[3]/Calculations.magnitude3D(d[0],d[3],d[6])+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5))):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Y: }} \\beta = cos^{-1}\\left(\\dfrac{{FR_y}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(-f[1]*(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]))+f[2]*calc['cos5']+f[3]*(3/5),Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*d[3]/Calculations.magnitude3D(d[0],d[3],d[6])+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5))):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Z: }} \\gamma = cos^{-1}\\left(\\dfrac{{FR_z}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5),Calculations.magnitude3D(-f[0]*calc['cos1']-f[1]*(d[0]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[2]*calc['sin5'],-f[1]*d[3]/Calculations.magnitude3D(d[0],d[3],d[6])+f[2]*calc['cos5']+f[3]*(3/5),-f[0]*calc['sin1']+f[1]*(d[6]/Calculations.magnitude3D(d[0],d[3],d[6]))-f[3]*(4/5))):.2f}°}}$
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#4_1
        code = 1230041,
        no_pregunta = 4,
        complexity = D,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle las componentes en X, Y y Z de la fuerza resultante ($FR$) entre los vectores que inician en el origen: $F1 = {f[0]:.0f} \\text{{ N}}$ que termina en $({d[0]},{d[1]},{d[2]})$, $F2 = {f[1]:.0f} \\text{{ N}}$ que termina en $({d[3]},{d[4]},{d[5]})$ y $F3 = {f[2]:.0f} \\text{{ N}}$ que termina en $({d[6]},{d[7]},{d[8]}).$",
        no_answers = 3,
        a1_name = Ci,
        a2_name = Cj,
        a3_name = Ck,
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])),2),
        ayuda1 = A43,
        ayuda2 = A45,
        ayuda3 = A46,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de las componentes X, Y y Z de la fuerza resultante (FR):}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_{{x}} = F1_x + F2_x + F3_x = F1*\\dfrac{{X_1}}{{\\sqrt{{X_1^2 + Y_1^2 + Z_1^2}}}} + F2*\\dfrac{{X_2}}{{\\sqrt{{X_2^2 + Y_2^2 + Z_2^2}}}} + F3*\\dfrac{{X_3}}{{\\sqrt{{X_3^2 + Y_3^2 + Z_3^2}}}} = {f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f} \\text{{ N}} }}$  
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_{{y}} = F1_y + F2_y + F3_y = F1*\\dfrac{{Y_1}}{{\\sqrt{{X_1^2 + Y_1^2 + Z_1^2}}}} + F2*\\dfrac{{Y_2}}{{\\sqrt{{X_2^2 + Y_2^2 + Z_2^2}}}} + F3*\\dfrac{{Y_3}}{{\\sqrt{{X_3^2 + Y_3^2 + Z_3^2}}}}  = {f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f} \\text{{ N}} }}$  
        
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_{{z}} = F1_z + F2_z + F3_z = F1*\\dfrac{{Z_1}}{{\\sqrt{{X_1^2 + Y_1^2 + Z_1^2}}}} + F2*\\dfrac{{Z_2}}{{\\sqrt{{X_2^2 + Y_2^2 + Z_2^2}}}} + F3*\\dfrac{{Z_3}}{{\\sqrt{{X_3^2 + Y_3^2 + Z_3^2}}}}  = {f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f} \\text{{ N}} }}$  

        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante $FR$ es:  $\\overrightarrow{{FR}} = [({f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f}) \\hspace{{1mm}}\\hat{{i}} + ({f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f}) \\hspace{{1mm}}\\hat{{j}} + ({f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f}) \\hspace{{1mm}}\\hat{{k}}] \\text{{ N}}$.
       """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#5_1
        code = 1230051,
        no_pregunta = 5,
        complexity = D,
        topic = EQ,
        subtopic = V3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Halle los ángulos directores coordenados de la fuerza resultante ($FR$) entre los vectores que inician en el origen: $F1 = {f[0]:.0f} \\text{{ N}}$ que termina en $({d[0]},{d[1]},{d[2]})$, $F2 = {f[1]:.0f} \\text{{ N}}$ que termina en $({d[3]},{d[4]},{d[5]})$ y $F3 = {f[2]:.0f} \\text{{ N}}$ que termina en $({d[6]},{d[7]},{d[8]}).$",
        no_answers = 3,
        a1_name = A3X,
        a2_name = A3Y,
        a3_name = A3Z,
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),Calculations.magnitude3D(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),Calculations.magnitude3D(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])))),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])),Calculations.magnitude3D(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])))),2),
        ayuda1 = A45,
        ayuda2 = A36,
        ayuda3 = A40,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para determinar los ángulos directores del vector, se calcula el arcocoseno de cada una de sus componentes divididas por la magnitud del vector F.
        
        $\\textbf{{\\small 1. Cálculo de las componentes X, Y y Z de la fuerza resultante (FR):}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = FR_{{x}} = F1_x + F2_x + F3_x = F1*\\dfrac{{X_1}}{{\\sqrt{{X_1^2 + Y_1^2 + Z_1^2}}}} + F2*\\dfrac{{X_2}}{{\\sqrt{{X_2^2 + Y_2^2 + Z_2^2}}}} + F3*\\dfrac{{X_3}}{{\\sqrt{{X_3^2 + Y_3^2 + Z_3^2}}}} = {f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f} \\text{{ N}} }}$  

        ${{\hspace{{4mm}} \\sum{{F_y}} = FR_{{y}} = F1_y + F2_y + F3_y = F1*\\dfrac{{Y_1}}{{\\sqrt{{X_1^2 + Y_1^2 + Z_1^2}}}} + F2*\\dfrac{{Y_2}}{{\\sqrt{{X_2^2 + Y_2^2 + Z_2^2}}}} + F3*\\dfrac{{Y_3}}{{\\sqrt{{X_3^2 + Y_3^2 + Z_3^2}}}}  = {f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f} \\text{{ N}} }}$  
        
        ${{\hspace{{4mm}} \\sum{{F_z}} = FR_{{z}} = F1_z + F2_z + F3_z = F1*\\dfrac{{Z_1}}{{\\sqrt{{X_1^2 + Y_1^2 + Z_1^2}}}} + F2*\\dfrac{{Z_2}}{{\\sqrt{{X_2^2 + Y_2^2 + Z_2^2}}}} + F3*\\dfrac{{Z_3}}{{\\sqrt{{X_3^2 + Y_3^2 + Z_3^2}}}}  = {f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f} \\text{{ N}} }}$  

        De acuerdo con lo anterior el vector cartesiano de la fuerza resultante $FR$ es:  $\\overrightarrow{{FR}} = [({f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f}) \\hspace{{1mm}}\\hat{{i}} + ({f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f}) \\hspace{{1mm}}\\hat{{j}} + ({f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])):.2f}) \\hspace{{1mm}}\\hat{{k}}] \\text{{ N}}$.
       
        $\\textbf{{\\small 2. Cálculo de la magnitud fuerza resultante:}}$

        ${{\hspace{{4mm}} |\\overrightarrow{{FR}}| = \\sqrt{{FR_{{x}}^2+FR_{{y}}^2+FR_{{z}}^2}} = {Calculations.magnitude3D(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8]))):.2f} \\text{{ N}}}}$

        $\\textbf{{\\small 3. Cálculo de los ángulos directores coordenados:}}$

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a X: }} \\alpha = cos^{-1}\\left(\\dfrac{{FR_x}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),Calculations.magnitude3D(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])))):.2f}°}}$

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Y: }} \\beta = cos^{-1}\\left(\\dfrac{{FR_y}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),Calculations.magnitude3D(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])))):.2f}°}}$
        
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Z: }} \\gamma = cos^{-1}\\left(\\dfrac{{FR_z}}{{|\\overrightarrow{{FR}}|}}\\right) = {Calculations.arccosine(f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])),Calculations.magnitude3D(f[0]*(d[0]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[3]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[6]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[1]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[4]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[7]/Calculations.magnitude3D(d[6],d[7],d[8])),f[0]*(d[2]/Calculations.magnitude3D(d[0],d[1],d[2]))+f[1]*(d[5]/Calculations.magnitude3D(d[3],d[4],d[5]))+f[2]*(d[8]/Calculations.magnitude3D(d[6],d[7],d[8])))):.2f}°}}$
       """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Vector unitario     ---------------------------------------------------
    #-------------------------------------------------       Nivel fácil       ---------------------------------------------------
    #-------------------------------------------------     Code: 131##        ---------------------------------------------------

    Questionary(#1_1
        code = 1310011,
        no_pregunta = 1,
        complexity = F,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es el coseno del ángulo que forma el vector $F1$ con el eje X y con el eje Y?. Estos se conocen como los cosenos direccionales. Considere $\\alpha_x = {a[0]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = "Coseno del ángulo con X",
        a2_name = "Coseno del ángulo con Y",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: calc['cos1'],
        answer2 = lambda f, a, calc, c, d, m: calc['sin1'],
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A47,
        ayuda2 = A1,
        ayuda3 = A48,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El coseno del ángulo con respecto al eje X es ${calc['cos1']:.2f}$, y con respecto al eje Y es ${calc['sin1']:.2f}$:
        
        ${{\hspace{{4mm}}\\cos(\\alpha_x) \\text{{ = cos(}}}}{a[0]:.0f}{{\\text{{°) = }}}}{calc['cos1']:.2f}$  
        ${{\hspace{{4mm}}\\cos(\\alpha_y) \\text{{ = cos(}}}}{90-a[0]:.0f}{{\\text{{°) = }}}}{calc['sin1']:.2f}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    Questionary(#1_2
        code = 1310012,
        no_pregunta = 1,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es el coseno del ángulo que forma el vector F1 con el eje X y con el eje Y?. Estos se conocen como los cosenos direccionales. Considere $\\alpha_x = {a[1]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = "Coseno del ángulo con X",
        a2_name = "Coseno del ángulo con Y",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: calc['cos2'],
        answer2=lambda f, a, calc, c, d, m: calc['sin2'],
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1=A47,
        ayuda2= A1,
        ayuda3= A48,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El coseno del ángulo con respecto al eje X es ${calc['cos2']:.2f}$, y con respecto al eje Y es ${calc['sin2']:.2f}$:
        
        ${{\hspace{{4mm}}\\cos(\\alpha_x) \\text{{ = cos(}}}}{a[1]:.0f}{{\\text{{°) = }}}}{calc['cos2']:.2f}$  
        ${{\hspace{{4mm}}\\cos(\\alpha_y) \\text{{ = cos(}}}}{a[1]-90:.0f}{{\\text{{°) = }}}}{calc['sin2']:.2f}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#1_3
        code = 1310013,
        no_pregunta = 1,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es el coseno del ángulo que forma el vector F1 con el eje X y con el eje Y?. Estos se conocen como los cosenos direccionales. Considere $\\alpha_x = {a[2]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = "Coseno del ángulo con X",
        a2_name = "Coseno del ángulo con Y",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: calc['cos3'],
        answer2=lambda f, a, calc, c, d, m: calc['sin3'],
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A47,
        ayuda2 = A1,
        ayuda3 = A48,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El coseno del ángulo con respecto al eje X es ${calc['cos3']:.2f}$, y con respecto al eje Y es ${calc['sin3']:.2f}$:

        ${{\hspace{{4mm}}\\cos(\\alpha_x) \\text{{ = cos(}}}}{a[2]:.0f}{{\\text{{°) = }}}}{calc['cos3']:.2f}$  
        ${{\hspace{{4mm}}\\cos(\\alpha_y) \\text{{ = cos(}}}}{a[2]-90:.0f}{{\\text{{°) = }}}}{calc['sin3']:.2f}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#1_4
        code = 1310014,
        no_pregunta = 1,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es el coseno del ángulo que forma el vector F1 con el eje X y con el eje Y?. Estos se conocen como los cosenos direccionales. Considere $\\alpha_x = {a[3]:.0f}\\degree$.",
        no_answers = 2,
        a1_name = "Coseno del ángulo con X",
        a2_name = "Coseno del ángulo con Y",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: calc['cos4'],
        answer2=lambda f, a, calc, c, d, m: calc['sin4'],
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A47,
        ayuda2 = A1,
        ayuda3 = A48,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El coseno del ángulo con respecto al eje X es ${calc['cos4']:.2f}$, y con respecto al eje Y es ${calc['sin4']:.2f}$:

        ${{\hspace{{4mm}}\\cos(\\alpha_x) \\text{{ = cos(}}}}{a[3]:.0f}{{\\text{{°) = }}}}{calc['cos4']:.2f}$  
        ${{\hspace{{4mm}}\\cos(\\alpha_y) \\text{{ = cos(}}}}{a[3]-90:.0f}{{\\text{{°) = }}}}{calc['sin4']:.2f}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 1310021,
        no_pregunta = 2,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule la norma (magnitud) de un vector que es la suma de dos vectores con magnitudes igual a los cosenos direccionales. Considere $\\alpha_x = {a[0]:.0f}\\degree$.",
        no_answers = 1,
        a1_name = "Norma",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(calc['mag1_u'],2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A49,
        ayuda2 = A50,
        ayuda3 = A51,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}\\cos(\\alpha_x) \\text{{ = cos(}}}}{a[0]:.0f}{{\\text{{°) = }}}}{calc['cos1']:.2f}$  
        ${{\hspace{{4mm}}\\cos(\\alpha_y) \\text{{ = cos(}}}}{90-a[0]:.0f}{{\\text{{°) = }}}}{calc['sin1']:.2f}$

        $\\textbf{{\\small 2. Cálculo de la norma del vector resultante:}}$
        
        ${{\hspace{{4mm}} |F1| = \\sqrt{{(cos(\\alpha_x))^2 + (cos(\\alpha_y))^2)}} = }} {calc['mag1_u']:.2f}$

        Este resultado significa que se puede construir un vector unitario $u = {calc['cos1']:.2f}\\hspace{{1mm}}\\hat{{i}} + {calc['sin1']:.2f}\\hspace{{1mm}}\\hat{{j}}$, con una magnitud de 1, que representa la dirección del vector.
        """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_2
        code = 1310022,
        no_pregunta = 2,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule la norma (magnitud) de un vector que es la suma de dos vectores con magnitudes igual a los cosenos direccionales. Considere $\\alpha_x = {a[1]:.0f}\\degree$.",
        no_answers = 1,
        a1_name = "Norma",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(calc['mag2_u'],2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1="En un triángulo con un ángulo recto, de lados a y b, la longitud de la hipotenusa se calcula como: $\\sqrt{a^2+b^2}$",
        ayuda2= "Considere que a y b corresponden a los cosenos direccionales",
        ayuda3= "La norma será: $|u| = \\sqrt{(cos(\\alpha_x))^2 + (cos(\\alpha_y))^2)}$.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}\\cos(\\alpha_x) \\text{{ = cos(}}}}{a[1]:.0f}{{\\text{{°) = }}}}{calc['cos2']:.2f}$  
        ${{\hspace{{4mm}}\\cos(\\alpha_y) \\text{{ = cos(}}}}{a[1]-90:.0f}{{\\text{{°) = }}}}{calc['sin2']:.2f}$

        $\\textbf{{\\small 2. Cálculo de la norma del vector resultante:}}$
        
        ${{\hspace{{4mm}} |F1| = \\sqrt{{(cos(\\alpha_x))^2 + (cos(\\alpha_y))^2)}} = }} {calc['mag2_u']:.2f}$

        Este resultado significa que se puede construir un vector unitario $u = {calc['cos2']:.2f} \\hspace{{1mm}}\\hat{{i}} + {calc['sin2']:.2f} \\hspace{{1mm}}\\hat{{j}}$, con una magnitud de 1, que representa la dirección del vector.
        """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_3
        code = 1310023,
        no_pregunta = 2,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule la norma (magnitud) de un vector que es la suma de dos vectores con magnitudes igual a los cosenos direccionales. Considere $\\alpha_x = {a[2]:.0f}\\degree$.",
        no_answers = 1,
        a1_name = "Norma",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(calc['mag3_u'],2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1=A49,
        ayuda2=A50,
        ayuda3=A51,
        respuesta_P1=lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}\\cos(\\alpha_x) \\text{{ = cos(}}}}{a[2]:.0f}{{\\text{{°) = }}}}{calc['cos3']:.2f}$  
        ${{\hspace{{4mm}}\\cos(\\alpha_y) \\text{{ = cos(}}}}{a[2]-90:.0f}{{\\text{{°) = }}}}{calc['sin3']:.2f}$

        $\\textbf{{\\small 2. Cálculo de la norma del vector resultante:}}$
        
        ${{\hspace{{4mm}} |F1| = \\sqrt{{(cos(\\alpha_x))^2 + (cos(\\alpha_y))^2)}} = }} {calc['mag3_u']:.2f}$

        Este resultado significa que se puede construir un vector unitario $u = {calc['cos3']:.2f} \\hspace{{1mm}}\\hat{{i}} {calc['sin3']:.2f} \\hspace{{1mm}}\\hat{{j}}$, con una magnitud de 1, que representa la dirección del vector.
        """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_4
        code = 1310024,
        no_pregunta = 2,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule la norma (magnitud) de un vector que es la suma de dos vectores con magnitudes igual a los cosenos direccionales. Considere $\\alpha_x = {a[3]:.0f}\\degree$.",
        no_answers = 1,
        a1_name = "Norma",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(calc['mag4_u'],2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A49,
        ayuda2 = A50,
        ayuda3 = A51,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}\\cos(\\alpha_x) \\text{{ = cos(}}}}{a[3]:.0f}{{\\text{{°) = }}}}{calc['cos4']:.2f}$  
        ${{\hspace{{4mm}}\\cos(\\alpha_y) \\text{{ = cos(}}}}{a[3]-90:.0f}{{\\text{{°) = }}}}{calc['sin4']:.2f}$

        $\\textbf{{\\small 2. Cálculo de la norma del vector resultante:}}$
        
        ${{\hspace{{4mm}} |F1| = \\sqrt{{(cos(\\alpha_x))^2 + (cos(\\alpha_y))^2)}} = }} {calc['mag4_u']:.2f}$

        Este resultado significa que se puede construir un vector unitario $u = {calc['cos4']:.2f} \\hspace{{1mm}}\\hat{{i}} {calc['sin4']:.2f} \\hspace{{1mm}}\\hat{{j}} $, con una magnitud de 1, que representa la dirección del vector.
        """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 1310031,
        no_pregunta = 3,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuales son los cosenos direccionales de un vector $F1$ definido por dos puntos A (punto inicial) y B (punto final)?. Las coordenadas $X,Y$ del punto A son $({c[0]:.0f} , {c[1]:.0f})$ y las del punto B son $({c[3]:.0f} , {c[4]:.0f})$.",
        no_answers = 2,
        a1_name = "$cos_x$",
        a2_name = "$cos_y$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((c[3]-c[0])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((c[4]-c[1])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A7,
        ayuda2 = A52,
        ayuda3 = A53,
        respuesta_P1 = lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la diferencia de coordenadas en X y Y:}}$

        ${{\hspace{{4mm}}dx \\text{{ = }}}} {c[3]:.0f} {{\\text{{ - (}}}} {c[0]:.2f} {{\\text{{) = }}}} {c[3]-c[0]:.0f}$  
        ${{\hspace{{4mm}}dy \\text{{ = }}}} {c[4]:.0f} {{\\text{{ - (}}}} {c[1]:.2f} {{\\text{{) = }}}} {c[4]-c[1]:.0f}$ 

        $\\textbf{{\\small 2. Cálculo de la longitud AB:}}$
        
        ${{\hspace{{4mm}} |AB| = \\sqrt{{(cos(dx))^2 + (cos(dy))^2}} = }} {math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$

        $\\textbf{{\\small 3. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}cos_x \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[3]-c[0]:.0f}}} {{{math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[3]-c[0])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$   

        ${{\hspace{{4mm}}cos_y \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[4]-c[1]:.0f}}} {{{math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[4]-c[1])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$ 
        
        Este resultado significa que se puede construir un vector unitario $u = {(c[3]-c[0])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f} \\hspace{{1mm}}\\hat{{i}} + {(c[4]-c[1])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f} \\hspace{{1mm}}\\hat{{j}}$, con una magnitud de 1, que representa la dirección del vector.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#3_2
        code = 1310032,
        no_pregunta = 3,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuales son los cosenos direccionales de un vector $F1$ definido por dos puntos A (punto inicial) y B (punto final)?. Las coordenadas del punto A $X,Y$ son $({c[3]:.0f} , {c[4]:.0f})$ y las del punto B son $({c[0]:.0f} , {c[1]:.0f})$.",
        no_answers = 2,
        a1_name = "$cos_x$",
        a2_name = "$cos_y$",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round((c[0]-c[3])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer2=lambda f, a, calc, c, d, m: np.round((c[1]-c[4])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1= A7,
        ayuda2= A52,
        ayuda3= A53,
        respuesta_P1=lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la diferencia de coordenadas en X y Y:}}$

        ${{\hspace{{4mm}}dx \\text{{ = }}}} {c[0]:.0f} {{\\text{{ - (}}}} {c[3]:.2f} {{\\text{{) = }}}} {c[0]-c[3]:.0f}$  
        ${{\hspace{{4mm}}dy \\text{{ = }}}} {c[1]:.0f} {{\\text{{ - (}}}} {c[4]:.2f} {{\\text{{) = }}}} {c[1]-c[4]:.0f}$ 

        $\\textbf{{\\small 2. Cálculo de la longitud AB:}}$
        
        ${{\hspace{{4mm}} |AB| = \\sqrt{{(cos(dx))^2 + (cos(dy))^2}} = }} {math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$

        $\\textbf{{\\small 3. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}cos_x \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[0]-c[3]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[0]-c[3])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$   
          
        ${{\hspace{{4mm}}cos_y \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[1]-c[4]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[1]-c[4])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$ 
        
        Este resultado significa que se puede construir un vector unitario $u = {(c[0]-c[3])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f} \\hspace{{1mm}}\\hat{{i}} {(c[1]-c[4])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f} \\hspace{{1mm}}\\hat{{j}}$, con una magnitud de 1, que representa la dirección del vector.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#3_3
        code = 1310033,
        no_pregunta = 3,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 3,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuales son los cosenos direccionales de un vector $F1$ definido por dos puntos A (punto inicial) y B (punto final)?. Las coordenadas $X,Y$ del punto A son $({c[3]:.0f} , {c[1]:.0f})$ y las del punto B son $({c[0]:.0f} , {c[4]:.0f})$.",
        no_answers = 2,
        a1_name = "$cos_x$",
        a2_name = "$cos_y$",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round((c[0]-c[3])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer2=lambda f, a, calc, c, d, m: np.round((c[4]-c[1])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1= A7,
        ayuda2= A52,
        ayuda3= A53,
        respuesta_P1=lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la diferencia de coordenadas en X y Y:}}$

        ${{\hspace{{4mm}}dx \\text{{ = }}}} {c[0]:.0f} {{\\text{{ - (}}}} {c[3]:.2f} {{\\text{{) = }}}} {c[0]-c[3]:.0f}$  
        ${{\hspace{{4mm}}dy \\text{{ = }}}} {c[4]:.0f} {{\\text{{ - (}}}} {c[1]:.2f} {{\\text{{) = }}}} {c[4]-c[1]:.0f}$ 

        $\\textbf{{\\small 2. Cálculo de la longitud AB:}}$
        
        ${{\hspace{{4mm}} |AB| = \\sqrt{{(cos(dx))^2 + (cos(dy))^2}} = }} {math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$

        $\\textbf{{\\small 3. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}cos_x \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[0]-c[3]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[0]-c[3])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$   
          
        ${{\hspace{{4mm}}cos_y \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[4]-c[1]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[4]-c[1])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$ 
        
        Este resultado significa que se puede construir un vector unitario $u = {(c[0]-c[3])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f} \\hspace{{1mm}}\\hat{{i}} + {(c[4]-c[1])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f} \\hspace{{1mm}}\\hat{{j}}$, con una magnitud de 1, que representa la dirección del vector.
        """,    
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_4
        code = 1310034,
        no_pregunta = 3,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuales son los cosenos direccionales de un vector $F1$ definido por dos puntos A (punto inicial) y B (punto final)?. Las $X,Y$ del punto A son $({c[0]:.0f} , {c[4]:.0f})$ y las del punto B son $({c[3]:.0f} , {c[1]:.0f})$.",
        no_answers = 2,
        a1_name = "$cos_x$",
        a2_name = "$cos_y$",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round((c[3]-c[0])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer2=lambda f, a, calc, c, d, m: np.round((c[1]-c[4])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1= A7,
        ayuda2= A52,
        ayuda3= A53,
        respuesta_P1=lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la diferencia de coordenadas en X y Y:}}$

        ${{\hspace{{4mm}}dx \\text{{ = }}}} {c[3]:.0f} {{\\text{{ - (}}}} {c[0]:.2f} {{\\text{{) = }}}} {c[3]-c[0]:.0f}$  
        ${{\hspace{{4mm}}dy \\text{{ = }}}} {c[1]:.0f} {{\\text{{ - (}}}} {c[4]:.2f} {{\\text{{) = }}}} {c[1]-c[4]:.0f}$ 

        $\\textbf{{\\small 2. Cálculo de la longitud AB:}}$
        
        ${{\hspace{{4mm}} |AB| = \\sqrt{{(cos(dx))^2 + (cos(dy))^2}} = }} {math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$

        $\\textbf{{\\small 3. Cálculo de los cosenos direccionales:}}$

        ${{\hspace{{4mm}}cos_x \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[3]-c[0]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[3]-c[0])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$   
          
        ${{\hspace{{4mm}}cos_y \\text{{ = }} \\dfrac{{dy}}{{AB}} \\text{{ = }}}} {{\\dfrac{{{c[1]-c[4]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {(c[1]-c[4])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$ 
        
        Este resultado significa que se puede construir un vector unitario $u = {(c[3]-c[0])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f} \\hspace{{1mm}}\\hat{{i}} {(c[1]-c[4])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f} \\hspace{{1mm}}\\hat{{j}}$, con una magnitud de 1, que representa la dirección del vector.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations'
        ),

    Questionary(#4_4
        code = 1310044,
        no_pregunta = 4,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 4,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el vector catersiano de $F1={f[0]} \\text{{  kN}}$ definido por los puntos A (punto inicial) y B (punto final)?. Las coordenadas $X,Y$ del punto A son $({c[0]:.0f} , {c[4]:.0f})$ y las del punto B son $({c[3]:.0f} , {c[1]:.0f})$.",
        no_answers = 2,
        a1_name = "Componente en X $(\\hat{{i}})$",
        a2_name = "Componente en Y $(\\hat{{j}})$",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(f[0]*((c[3]-c[0])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2))),2),
        answer2=lambda f, a, calc, c, d, m: np.round(f[0]*((c[1]-c[4])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2))),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1= A7,
        ayuda2= A52,
        ayuda3= A54,
        respuesta_P1 = lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la diferencia de coordenadas en X y Y:}}$

        ${{\hspace{{4mm}}dx \\text{{ = }}}} {c[3]:.0f} {{\\text{{ - (}}}} {c[0]:.2f} {{\\text{{) = }}}} {c[3]-c[0]:.0f}$  
        ${{\hspace{{4mm}}dy \\text{{ = }}}} {c[1]:.0f} {{\\text{{ - (}}}} {c[4]:.2f} {{\\text{{) = }}}} {c[1]-c[4]:.0f}$ 

        $\\textbf{{\\small 2. Cálculo de la longitud AB:}}$
        
        ${{\hspace{{4mm}} |AB| = \\sqrt{{dx^2 + dy^2}} = }} {math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2):.2f}$

        $\\textbf{{\\small 3. Cálculo de las componentes en X y Y:}}$

        ${{\hspace{{4mm}}\\text{{componente i = }} \\overrightarrow{{F1}}*\\dfrac{{dx}}{{AB}} \\text{{ = }}}} {f[0]:.0f}*{{\\dfrac{{{c[3]-c[0]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {f[0]*((c[3]-c[0])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f}$   
          
        ${{\hspace{{4mm}}\\text{{componente j = }} \\overrightarrow{{F1}}*\\dfrac{{dy}}{{AB}} \\text{{ = }}}} {f[0]:.0f}*{{\\dfrac{{{c[1]-c[4]:.0f}}} {{{math.sqrt((c[1]-c[4])**2+(c[3]-c[0])**2):.2f}}} }} {{\\text{{ = }}}} {f[0]*((c[1]-c[4])/math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2)):.2f}$ 
        
        De acuerdo con lo anterior el vector cartesiano de $F1$ es igual a $[{f[0]*((c[3]-c[0])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2))):.2f} \\hspace{{1mm}}\\hat{{i}} {f[0]*((c[1]-c[4])/(math.sqrt((c[4]-c[1])**2+(c[3]-c[0])**2))):.2f} \\hspace{{1mm}}\\hat{{j}}]\\text{{ kN}}$.
        """,  
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",  
        calculos='operations'
        ),

    Questionary(#5_1
        code = 1310051,
        no_pregunta = 5,
        complexity ="Fácil",
        topic = "Equilibrio de partículas",
        subtopic ="Vector unitario",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine los ángulos directores coordenados del vector cartesiano $[({c[0]:.0f}) i + ({c[1]:.0f}) j + ({c[2]:.0f}) k] N$.",
        no_answers = 3,
        a1_name = "Ángulo respecto a X $(\\alpha)$ [°]",
        a2_name = "Ángulo respecto a Y $(\\beta)$ [°]",
        a3_name = "Ángulo respecto a Z $(\\gamma)$ [°]",
        answer1=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(c[0],Calculations.magnitude3D(c[0],c[1],c[2])),2),
        answer2=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(c[1],Calculations.magnitude3D(c[0],c[1],c[2])),2),
        answer3=lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(c[2],Calculations.magnitude3D(c[0],c[1],c[2])),2),
        ayuda1 = A42,
        ayuda2= A55,  
        ayuda3= A40,
        respuesta_P1=lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la magnitud del vector cartesiano:}}$

        ${{\hspace{{4mm}} |\\overrightarrow{{F}}| = \\sqrt{{F_X^2 + F_Y^2 + F_Z^2}} = \\sqrt{{({c[0]})^2 + ({c[1]})^2 + ({c[2]})^2}} = {Calculations.magnitude3D(c[0],c[1],c[2]):.2f} \\text{{N}}}}$

        $\\textbf{{\\small 2. Cálculo de los ángulos:}}$

        Para el cálculo de los ángulos se determina el coseno inverso de cada una de las componentes del vector unitario en la dirección del vector $\\overrightarrow{{F}}$.

        ${{\hspace{{4mm}} \\text{{Ángulo respecto a X: }} \\alpha = cos^{-1}\\left(\\dfrac{{F_X}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(c[0],Calculations.magnitude3D(c[0],c[1],c[2])):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Y: }} \\beta = cos^{-1}\\left(\\dfrac{{F_Y}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(c[1],Calculations.magnitude3D(c[0],c[1],c[2])):.2f}°}}$
        ${{\hspace{{4mm}} \\text{{Ángulo respecto a Z: }} \\gamma = cos^{-1}\\left(\\dfrac{{F_Z}}{{|\\overrightarrow{{F}}|}}\\right)={Calculations.arccosine(c[2],Calculations.magnitude3D(c[0],c[1],c[2])):.2f}°}}$
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),
    
    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Vector unitario    ---------------------------------------------------
    #-------------------------------------------------       Nivel medio      ---------------------------------------------------
    #-------------------------------------------------       Code: 132####    ---------------------------------------------------

    Questionary(#1_1
        code = 1320011,
        no_pregunta = 1,
        complexity = M,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine los cosenos direccionales de la fuerza resultante $FR$ del siguientes sistema de vectores, use el vector unitario.  Considere $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $F3={f[2]:.0f} \\text{{ kN}}$, $F4={f[3]:.0f} \\text{{ kN}}$, $X_1={d[0]:.0f} \\text{{ m}}$, $Y_1={d[3]:.0f} \\text{{ m}}$, $X_2={d[6]:.0f} \\text{{ m}}$ y $Y_2={d[9]:.0f}\\text{{ m}}$.",
        no_answers = 2,
        a1_name = CosX,
        a2_name = CosY,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round((-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2])/Calculations.magnitude(-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2],-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]),2),
        answer2=lambda f, a, calc, c, d, m: np.round((-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3])/Calculations.magnitude(-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2],-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A56,
        ayuda2 = A57,
        ayuda3 = A58,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Los cosenos direccionales corresponden a las componentes del vector divididas por la magnitud del vector. A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Sumatoria de fuerzas en X:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = F1_x + F2_x + F3_x + F4_x}}$ 

        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = -F1 \\cdot \\dfrac{{(X1-0)}}{{\\sqrt{{(X_1-0)^2 + (Y_1-0)^2}}}}- F2 \\cdot \\dfrac{{(X2-0)}}{{\\sqrt{{(X_2-0)^2 + (Y_2-0)^2}} + F3}} }}$    
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = {-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2]:.2f} \\text{{ kN}}}}$

        $\\textbf{{\\small 2. Sumatoria de fuerzas en Y:}}$

        ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{RY}} = F1_y + F2_y + F3_y + F4_y}}$      
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{RY}} = -F1 \\cdot \\dfrac{{(Y1-0)}}{{\\sqrt{{(X_1-0)^2 + (Y_1-0)^2}}}}- F2 \\cdot \\dfrac{{(Y2-0)}}{{\\sqrt{{(X_2-0)^2 + (Y_2-0)^2}} - F4}} }}$       
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{RY}} = {-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]:.2f} \\text{{ kN}} }}$

        $\\textbf{{\\small 3. Cálculo de la magnitud:}}$

        ${{\hspace{{4mm}} |\\overrightarrow{{F_R}}|=\\sqrt{{F_{{RX}}^2+F_{{RY}}^2}} = {Calculations.magnitude(-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2],-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]):.2f} \\text{{ kN}}}}$
        
        $\\textbf{{\\small 4. Cosenos direccionales de la fuerza resultante FR:}}$

        ${{\hspace{{4mm}} Cos_x  = \\dfrac{{F_{{RX}}}}{{|\\overrightarrow{{F_R}}|}} = \\dfrac{{{-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2]:.2f}}}{{{Calculations.magnitude(-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2],-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]):.2f}}} = {(-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2])/Calculations.magnitude(-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2],-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]):.2f} }}$

        ${{\hspace{{4mm}} Cos_y  = \\dfrac{{F_{{RY}}}}{{|\\overrightarrow{{F_R}}|}} = \\dfrac{{{-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]:.2f}}}{{{Calculations.magnitude(-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2],-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]):.2f}}} = {(-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3])/Calculations.magnitude(-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2],-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]):.2f} }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    Questionary(#2_1
        code = 1320021,
        no_pregunta = 2,
        complexity = M,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza resultante $FR$ del siguiente sistema de vectores, use el vector unitario.  Considere $F1={f[0]:.0f} \\text{{ kN}}$, $F2={f[1]:.0f} \\text{{ kN}}$, $F3={f[2]:.0f} \\text{{ kN}}$, $F4={f[3]:.0f} \\text{{ kN}}$, $X_1={d[0]:.0f} \\text{{ m}}$, $Y_1={d[3]:.0f} \\text{{ m}}$, $X_2={d[6]:.0f} \\text{{ m}}$ y $Y_2={d[9]:.0f} \\text{{ m}}$.",
        no_answers = 1,
        a1_name = Mag,
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: Calculations.magnitude(-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2],-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A59,
        ayuda2 = A57,
        ayuda3 = A15,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Sumatoria de fuerzas en X:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = F1_x + F2_x + F3_x + F4_x}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = -F1 \\cdot \\dfrac{{(X1-0)}}{{\\sqrt{{(X_1-0)^2 + (Y_1-0)^2}}}}- F2 \\cdot \\dfrac{{(X2-0)}}{{\\sqrt{{(X_2-0)^2 + (Y_2-0)^2}} + F3}} }}$
       
         ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = {-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2]:.2f} \\text{{ kN}} }}$

        $\\textbf{{\\small 2. Sumatoria de fuerzas en Y:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = F1_y + F2_y + F3_y + F4_y}}$
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = -F1 \\cdot \\dfrac{{(Y1-0)}}{{\\sqrt{{(X_1-0)^2 + (Y_1-0)^2}}}}- F2 \\cdot \\dfrac{{(Y2-0)}}{{\\sqrt{{(X_2-0)^2 + (Y_2-0)^2}} - F4}} }}$
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = {-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]:.2f} \\text{{ kN}} }}$
       
        $\\textbf{{\\small 3. Cálculo de la magnitud:}}$

        ${{\hspace{{4mm}} |F_R|=\\sqrt{{F_{{RX}}^2+F_{{RY}}^2}} = {Calculations.magnitude(-f[0]*(d[0]/Calculations.magnitude(d[0],d[3]))-f[1]*(d[6]/Calculations.magnitude(d[6],d[9]))+f[2],-f[0]*(d[3]/Calculations.magnitude(d[0],d[3]))+f[1]*(d[9]/Calculations.magnitude(d[6],d[9]))-f[3]):.2f} \\text{{ kN}} }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 1320031,
        no_pregunta = 3,
        complexity = M,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule el vector unitario del cable AD, evaluado desde A hacia D. Considere que $D_X={d[0]:.0f} \\text{{ m}}$, $D_Y={d[3]:.0f} \\text{{ m}}$ y $A_Z={d[6]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = Ci,
        a2_name = Cj,
        a3_name = Ck,
        answer1=lambda f, a, calc, c, d, m: np.round(-d[0]/Calculations.magnitude3D(d[0],d[3],d[6]),2),
        answer2=lambda f, a, calc, c, d, m: np.round(d[3]/Calculations.magnitude3D(d[0],d[3],d[6]),2),
        answer3=lambda f, a, calc, c, d, m: np.round(-d[6]/Calculations.magnitude3D(d[0],d[3],d[6]),2),
        ayuda1 = A57,
        ayuda2 = A60,
        ayuda3 = A61,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la componente X del vector unitario:}}$

        ${{\hspace{{4mm}} u_x = \\dfrac{{-D_X-0}}{{\\sqrt{{(-D_X-0)^2 + (D_Y-0)^2 + (0-A_Z)^2}} }} }}$     
        ${{\hspace{{4mm}} u_x = {-d[0]/Calculations.magnitude3D(d[0],d[3],d[6]):.2f}}}$
        
        $\\textbf{{\\small 2. Cálculo de la componente Y del vector unitario:}}$

        ${{\hspace{{4mm}} u_y = \\dfrac{{D_Y-0}}{{\\sqrt{{(-D_X-0)^2 + (D_Y-0)^2 + (0-A_Z)^2}} }} }}$      
        ${{\hspace{{4mm}} u_y = {d[3]/Calculations.magnitude3D(d[0],d[3],d[6]):.2f}}}$
       
        $\\textbf{{\\small 3. Cálculo de la componente Z del vector unitario:}}$

        ${{\hspace{{4mm}} u_z = \\dfrac{{0-A_Z}}{{\\sqrt{{(-D_X-0)^2 + (D_Y-0)^2 + (0-A_Z)^2}} }} }}$     
        ${{\hspace{{4mm}} u_z = {-d[6]/Calculations.magnitude3D(d[0],d[3],d[6]):.2f} }}$
        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
 
    Questionary(#4_1
        code = 1320041,
        no_pregunta = 4,
        complexity = M,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"La componente en Y del vector unitario del cable AD, evaluado desde A hacia D, es equivalente a $\\dfrac{{{d[6]:.0f}}}{{{d[9]:.0f}}}$. ¿Cuál es la distancia $D_Y$ si $D_X={d[0]:.0f} \\text{{ m}}$ y $A_Z={d[3]:.0f} \\text{{ m}}$?. Además, ¿cuál es la componente en Y de la fuerza, si la fuerza a lo largo del cable es ${f[0]:.0f} \\text{{ kN}}?$.",
        no_answers = 2,
        a1_name = "Distancia $D_Y$",
        a2_name = "Componente en y ($F_y$)",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(math.sqrt(((d[6]/d[9])**2*(d[0]**2+d[3]**2))/(1-(d[6]/d[9])**2)),2),
        answer2=lambda f, a, calc, c, d, m: np.round((d[6]/d[9])*f[0],2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A65,
        ayuda2 = A66,
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Despeje de la distancia:}}$    

        Para despejar la distancia $D_Y$ se plantea la ecuación de la componente Y $\\hat{{j}}$ del vector unitario:

        ${{\hspace{{4mm}} \\lambda_{{uy}} = \\dfrac{{D_Y}}{{\\sqrt{{(D_X-0)^2 + (D_Y-0)^2 + (0-A_Z)^2}} }} }}$   

        ${{\hspace{{4mm}} \\sqrt{{(D_X-0)^2 + (D_Y-0)^2 + (0-A_Z)^2}} = \\dfrac{{D_Y}}{{\\lambda_{{uy}}}} }}$

        ${{\hspace{{4mm}} (D_X-0)^2 + (D_Y-0)^2 + (0-A_Z)^2 = \\left(\\dfrac{{D_Y}}{{\\lambda_{{uy}}}}\\right)^2 }}$ 

        ${{\hspace{{4mm}} (D_X-0)^2 + (0-A_Z)^2 = \\left(\\dfrac{{D_Y}}{{\\lambda_{{uy}}}}\\right)^2 - (D_Y-0)^2}}$ 

        ${{\hspace{{4mm}} (D_X-0)^2 + (0-A_Z)^2 = (D_Y-0)^2*\\left(\\dfrac{{1}}{{(\\lambda_{{uy}})^2}}-1\\right)}}$    

        ${{\hspace{{4mm}} ((D_X-0)^2 + (0-A_Z)^2)*\\lambda_{{uy}})^2 = (D_Y-0)^2 - \\lambda_{{uy}})^2*D_Y^2 }}$  

        ${{\hspace{{4mm}} ((D_X-0)^2 + (0-A_Z)^2)*\\lambda_{{uy}})^2 = D_Y^2*(1-\\lambda_{{uy}})^2)}}$    

        ${{\hspace{{4mm}} D_Y = \\sqrt{{\\dfrac{{((D_X-0)^2 + (0-A_Z)^2)*\\lambda_{{uy}}^2}}{{(1-\\lambda_{{uy}})^2}} }}}}$    

        ${{\hspace{{4mm}} D_Y = {math.sqrt(((d[6]/d[9])**2*(d[0]**2+d[3]**2))/(1-(d[6]/d[9])**2)):.2f} \\text{{ m}}}}$    
        
        $\\textbf{{\\small 2. Cálculo de la componente Y de la fuerza que actúa en el cable AD:}}$

        ${{\hspace{{4mm}} F_y = F*\\lambda_{{uy}} }}$   
        ${{\hspace{{4mm}} F_y = {(d[6]/d[9])*f[0]:.2f} \\text{{kN}} }}$        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#5_1 
        code = 1320051, 
        no_pregunta = 5, 
        complexity = M, 
        topic = EQ, 
        subtopic = VU, 
        version = 1, 
        pregunta = lambda f, a, calc, c, d, m: f"Halle el vector cartesiano de la fuerza resultante ($FR$) entre los vectores que inician en el origen:  $F1 = {f[0]:.0f} \\text{{ N}}$ que termina en $({c[0]},{c[1]},{c[2]})$ y $F2 = {f[1]:.0f} \\text{{ N}}$ que termina en $({c[3]},{c[4]},{c[5]})$.", 
        no_answers = 3, 
        a1_name = Ci, 
        a2_name = Cj, 
        a3_name = Ck, 
        answer1=lambda f, a, calc, c, d, m: np.round(f[0]*(c[0]/Calculations.magnitude3D(c[0],c[1],c[2]))+f[1]*(c[3]/Calculations.magnitude3D(c[3],c[4],c[5])), 2), 
        answer2=lambda f, a, calc, c, d, m: np.round(f[0]*(c[1]/Calculations.magnitude3D(c[0],c[1],c[2]))+f[1]*(c[4]/Calculations.magnitude3D(c[3],c[4],c[5])), 2), 
        answer3=lambda f, a, calc, c, d, m: np.round(f[0]*(c[2]/Calculations.magnitude3D(c[0],c[1],c[2]))+f[1]*(c[5]/Calculations.magnitude3D(c[3],c[4],c[5])), 2), 
        ayuda1 = A62, 
        ayuda2 = A63, 
        ayuda3 = A57, 
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo del vector cartesiano de las fuerzas F1 y F2:}}$

        $\\underline{{Vector \\hspace{{1mm}} cartesiano \\hspace{{1mm}} F1}}$ 

        ${{\hspace{{4mm}} \\overrightarrow{{F1}} = \\dfrac{{(X_2-X_1) i + (Y_2-Y_1) j + (Z_2-Z_1) k}}{{\\sqrt{{(X_2-X_1)^2 + (Y_2-Y_1)^2 + (Z_2-Z_1)^2}} }} }}$

        ${{\hspace{{4mm}} \\overrightarrow{{F1}} = \\dfrac{{({c[0]:.0f}-0) \\hat{{i}} + ({c[1]:.0f}-0) \\hat{{j}} + ({c[2]:.0f}-0) \\hat{{k}}}}{{\\sqrt{{({c[0]:.0f}-0)^2 + ({c[1]:.0f}-0)^2 + ({c[2]:.0f}-0)^2}} }} }}$

        ${{\hspace{{4mm}} \\overrightarrow{{F1}} = ({f[0]*c[0]/Calculations.magnitude3D(c[0],c[1],c[2]):.2f}) \\hat{{i}} + ({f[0]*c[1]/Calculations.magnitude3D(c[0],c[1],c[2]):.2f}) \\hat{{j}} + ({f[0]*c[2]/Calculations.magnitude3D(c[0],c[1],c[2]):.2f}) \\hat{{k}}}}$

        $\\underline{{Vector \\hspace{{1mm}} cartesiano \\hspace{{1mm}} F2}}$ 

        ${{\hspace{{4mm}} \\overrightarrow{{F2}} = \\dfrac{{(X_2-X_1) i + (Y_2-Y_1) j + (Z_2-Z_1) k}}{{\\sqrt{{(X_2-X_1)^2 + (Y_2-Y_1)^2 + (Z_2-Z_1)^2}} }} }}$

        ${{\hspace{{4mm}} \\overrightarrow{{F2}} = \\dfrac{{({c[3]:.0f}-0) \\hat{{i}} + ({c[4]:.0f}-0) \\hat{{j}} + ({c[5]:.0f}-0) \\hat{{k}}}}{{\\sqrt{{({c[3]:.0f}-0)^2 + ({c[4]:.0f}-0)^2 + ({c[5]:.0f}-0)^2}} }} }}$

        ${{\hspace{{4mm}} \\overrightarrow{{F2}} = ({f[1]*(c[3]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f}) \\hat{{i}} + ({f[1]*(c[4]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f}) \\hat{{j}} + ({f[1]*(c[5]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f}) \\hat{{k}}}}$

        $\\textbf{{\\small 2. Cálculo del vector cartesiano de la fuerza resultante FR:}}$       
        ${{\hspace{{4mm}} \\overrightarrow{{F_R}} = FR_X \\hat{{i}} + FR_Y \\hat{{j}} + FR_Z \\hat{{k}}}}$    
        ${{\hspace{{4mm}} \\overrightarrow{{F_R}} = (F1_X + F2_X) \\hat{{i}} + (F1_Y + F2_Y) \\hat{{j}} + (F1_Z + F2_Z) \\hat{{k}}}}$    
        ${{\hspace{{4mm}} \\overrightarrow{{F_R}} = ({f[0]*c[0]/Calculations.magnitude3D(c[0],c[1],c[2]):.2f} + {f[1]*(c[3]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f}) \\hat{{i}} + ({f[0]*c[1]/Calculations.magnitude3D(c[0],c[1],c[2]):.2f} + {f[1]*(c[4]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f} ) \\hat{{j}} + ({f[0]*c[2]/Calculations.magnitude3D(c[0],c[1],c[2]):.2f} + {f[1]*(c[5]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f}) \\hat{{k}}}}$  
        ${{\hspace{{4mm}} \\overrightarrow{{F_R}} = ({(f[0]*c[0]/Calculations.magnitude3D(c[0],c[1],c[2]))+(f[1]*c[3]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f}) \\hat{{i}} + ({f[0]*(c[1]/Calculations.magnitude3D(c[0],c[1],c[2]))+(f[1]*c[4]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f}) \\hat{{j}} + ({(f[0]*c[2]/Calculations.magnitude3D(c[0],c[1],c[2]))+(f[1]*c[5]/Calculations.magnitude3D(c[3],c[4],c[5])):.2f}) \\hat{{k}}}}$
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"", 
        respuesta_P3 = lambda f, a, calc, c, d, m: f"", 
        calculos='operations' 
        ),

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Vector unitario     ---------------------------------------------------
    #-------------------------------------------------       Nivel díficil      ---------------------------------------------------
    #-------------------------------------------------       Code: 133##      ---------------------------------------------------

    Questionary(#1_1
        code = 1330011,
        no_pregunta = 1,
        complexity = D,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule el vector cartesiano de la fuerza resultante ($FR$) de las fuerzas que actuán en los cables mostrados en la figura. Considere que la fuerzas que actúan en los cables $AB$, $AC$ y $AD$ son: ${f[0]:.0f}$ $kN$, ${f[1]:.0f}$ $kN$ y ${f[2]:.0f}$ $kN$, respectivamente. También considere que $A_Z={d[0]:.0f}$ $m$, $B_X={d[3]:.0f}$ $m$, $B_Y={d[6]:.0f}$ $m$, $C_X={d[9]:.0f}$ $m$, $C_Y={d[12]:.0f}$ $m$, $D_X={d[15]:.0f}$ $m$ y $D_Y={d[18]:.0f}$ $m$.",
        no_answers = 3,
        a1_name = Ci,
        a2_name = Cj,
        a3_name = Ck,
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])-f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(-f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])-f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])-f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]),2),
        ayuda1 = A64,
        ayuda2 = A62,
        ayuda3 = A63,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para hallar el vector cartesiano de la fuerza resultante ($FR$), se realiza la sumatoria de las fuerzas en $X$, $Y$, $Z$, para lo cual se usa el vector unitario de cada uno de los cables.

        $\\textbf{{\\small 1. Cálculo del vector unitario de los cables AB, AC y AD (Evaluados desde A a los puntos B, C, D):}}$

        ${{\hspace{{4mm}} \\lambda_{{AB}} = \\dfrac{{\\overrightarrow{{AB}}}}{{|\\overrightarrow{{AB}}|}} = \\dfrac{{(B_X-0) i + (-B_Y-0) j + (0 - A_Z) k}}{{\\sqrt{{((B_X-0)^2 + (-B_Y-0)^2 + (0 - A_Z)^2}}}} }}$   

        ${{\hspace{{4mm}} \\lambda_{{AB}} = ({d[3]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f}) \\hat{{i}} + (-{d[6]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f}) \\hat{{j}} +(-{d[0]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f}) \\hat{{k}}}}$

        ${{\hspace{{4mm}} \\lambda_{{AC}} = \\dfrac{{\\overrightarrow{{AC}}}}{{|\\overrightarrow{{AC}}|}} = \\dfrac{{(C_X-0) i + (C_Y-0) j + (0 - A_Z) k}}{{\\sqrt{{((C_X-0)^2 + (C_Y-0)^2 + (0 - A_Z)^2}}}} }}$ 

        ${{\hspace{{4mm}} \\lambda_{{AC}} = ({d[9]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f}) \\hat{{i}} + ({d[12]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f}) \\hat{{j}} + (-{d[0]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f}) \\hat{{k}}}}$

        ${{\hspace{{4mm}} \\lambda_{{AD}} = \\dfrac{{\\overrightarrow{{AD}}}}{{|\\overrightarrow{{AD}}|}} = \\dfrac{{(-D_X-0) i + (D_Y-0) j + (0 - A_Z) k}}{{\\sqrt{{((-D_X-0)^2 + (D_Y-0)^2 + (0 - A_Z)^2}}}} }}$
        
        ${{\hspace{{4mm}} \\lambda_{{AD}} = (-{d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}) \\hat{{i}} + ({d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}) \\hat{{j}} + (-{d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}) \\hat{{k}}}}$
    
        
        $\\textbf{{\\small 2. Sumatoria de fuerzas en X, Y, Z:}}$

        ${{\hspace{{4mm}} \\sum_X = FR_X = F_{{AB}}*\\left(\\dfrac{{B_X}}{{\\sqrt{{(B_X)^2 + (-B_Y)^2 + (-A_Z)^2}}}}\\right) + F_{{AC}}*\\left(\\dfrac{{C_X}}{{\\sqrt{{(C_X)^2 + (C_Y)^2 + (-A_Z)^2}}}}\\right) + F_{{AD}}*\\left(\\dfrac{{-D_X}}{{\\sqrt{{(-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}}}\\right)}}$    
        ${{\hspace{{4mm}} \\sum_X = FR_X = ({f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f}) + ({f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f}) + ({-f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f})}}$    
        ${{\hspace{{4mm}} \\sum_X = FR_X = {f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])-f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} \\text{{ kN}}}}$
        
        ${{\hspace{{4mm}} \\sum_Y = FR_Y = F_{{AB}}*\\left(\\dfrac{{-B_Y}}{{\\sqrt{{(B_X)^2 + (-B_Y)^2 + (-A_Z)^2}}}}\\right) + F_{{AC}}*\\left(\\dfrac{{C_Y}}{{\\sqrt{{(C_X)^2 + (C_Y)^2 + (-A_Z)^2}}}}\\right) + F_{{AD}}*\\left(\\dfrac{{D_Y}}{{\\sqrt{{(-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}}}\\right)}}$   
        ${{\hspace{{4mm}} \\sum_Y = FR_Y = ({-f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f}) + ({f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f}) + ({f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f})}}$    
        ${{\hspace{{4mm}} \\sum_Y = FR_Y = {-f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} \\text{{ kN}} }}$

        ${{\hspace{{4mm}} \\sum_Z = FR_Z = F_{{AB}}*\\left(\\dfrac{{-A_Z}}{{\\sqrt{{(B_X)^2 + (-B_Y)^2 + (-A_Z)^2}}}}\\right) + F_{{AC}}*\\left(\\dfrac{{-A_Z}}{{\\sqrt{{(C_X)^2 + (C_Y)^2 + (-A_Z)^2}}}}\\right) + F_{{AD}}*\\left(\\dfrac{{-A_Z}}{{\\sqrt{{(-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}}}\\right)}}$    
        ${{\hspace{{4mm}} \\sum_Z = FR_Z = ({-f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f}) + ({-f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f}) + ({-f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f})}}$    
        ${{\hspace{{4mm}} \\sum_Z = FR_Z ={-f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])-f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])-f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} \\text{{ kN}}}}$  
        
        De acuerdo con el anterior procedimiento el vector cartesiano de la fuerza resultante ($FR$) es: $[({f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])-f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f})$ $\\hat{{i}}$ + $({-f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f})$ $\\hat{{j}}$ + $({-f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])-f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])-f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}$ $\\hat{{k}})]$ $kN$. 
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    Questionary(#2_1
        code = 1330021,
        no_pregunta = 2,
        complexity = D,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine los ángulos directores coordenados de la fuerza resultante ($F_R$) de las fuerzas que actuán en los cables mostrados en la figura. Considere que la fuerzas que actúan en los cables AB, AC y AD son: {f[0]:.0f} kN, {f[1]:.0f} kN y {f[2]:.0f} kN, respectivamente. También considere que $A_Z={d[0]:.0f}$, $B_X={d[3]:.0f}$, $B_Y={d[6]:.0f}$, $C_X={d[9]:.0f}$, $C_Y={d[12]:.0f}$, $D_X={d[15]:.0f}$ y $D_Y={d[18]:.0f}$.",
        no_answers = 3,
        a1_name = A3X,
        a2_name = A3Y,
        a3_name = A3Z,
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]))),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine(f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]),Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]))),2),
        ayuda1 = A36,
        ayuda2 = A62,
        ayuda3 = A57,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para hallar los ángulos directores coordeados, primero se halla el vector cartesiano de la fuerza resultante ($F_R$) y su magnitud. Luego, se calculan los arcocosenos de las componentes del vector divididas entre su magnitud:

        $\\textbf{{\\small 1. Cálculo del vector unitario de los cables AB, AC y AD (Evaluados desde A a los puntos B, C, D):}}$

        ${{\hspace{{4mm}} \\Lambda_{{AB}} = \\dfrac{{\\overrightarrow{{AB}}}}{{|\\overrightarrow{{AB}}|}} = \\dfrac{{(B_X-0) i + (-B_Y-0) j + (0 - A_Z) k}}{{\\sqrt((B_X-0)^2 + (-B_Y-0)^2 + (0 - A_Z)^2}} }}$
        ${{\hspace{{4mm}} \\Lambda_{{AC}} = \\dfrac{{\\overrightarrow{{AC}}}}{{|\\overrightarrow{{AC}}|}} = \\dfrac{{(C_X-0) i + (C_Y-0) j + (0 - A_Z) k}}{{\\sqrt((C_X-0)^2 + (C_Y-0)^2 + (0 - A_Z)^2}} }}$
        ${{\hspace{{4mm}} \\Lambda_{{AD}} = \\dfrac{{\\overrightarrow{{AD}}}}{{|\\overrightarrow{{AD}}|}} = \\dfrac{{(-D_X-0) i + (D_Y-0) j + (0 - A_Z) k}}{{\\sqrt((-D_X-0)^2 + (D_Y-0)^2 + (0 - A_Z)^2}} }}$
    
        
        $\\textbf{{\\small 2. Sumatoria de fuerzas en X, Y, Z:}}$

        ${{\hspace{{4mm}} \\sum_X = F_R_X = F_{{AB}}*\\left(\\dfrac{{B_X}}{{\\sqrt((B_X)^2 + (-B_Y)^2 + (-A_Z)^2}}\\right) + F_{{AC}}*\\left(\\dfrac{{C_X}}{{\\sqrt((C_X)^2 + (C_Y)^2 + (-A_Z)^2}}\\right) + F_{{AD}}*\\left(\\dfrac{{-D_X}}{{\\sqrt((-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}\\right)}}$
        ${{\hspace{{4mm}} \\sum_X = F_R_X = {f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f} + {f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f} + {f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}$
        ${{\hspace{{4mm}} \\sum_X = F_R_X = {f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} }}$
        
        ${{\hspace{{4mm}} \\sum_Y = F_R_Y = F_{{AB}}*\\left(\\dfrac{{-B_Y}}{{\\sqrt((B_X)^2 + (-B_Y)^2 + (-A_Z)^2}}\\right) + F_{{AC}}*\\left(\\dfrac{{C_Y}}{{\\sqrt((C_X)^2 + (C_Y)^2 + (-A_Z)^2}}\\right) + F_{{AD}}*\\left(\\dfrac{{D_Y}}{{\\sqrt((-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}\\right)}}$
        ${{\hspace{{4mm}} \\sum_Y = F_R_Y = {f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f} + {f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f} + {f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}
        ${{\hspace{{4mm}} \\sum_Y = F_R_Y = {f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}$
        
        ${{\hspace{{4mm}} \\sum_Z = F_R_Z = F_{{AB}}*\\left(\\dfrac{{-A_Z}}{{\\sqrt((B_X)^2 + (-B_Y)^2 + (-A_Z)^2}}\\right) + F_{{AC}}*\\left(\\dfrac{{-A_Z}}{{\\sqrt((C_X)^2 + (C_Y)^2 + (-A_Z)^2}}\\right) + F_{{AD}}*\\left(\\dfrac{{-A_Z}}{{\\sqrt((-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}\\right)}}$
        ${{\hspace{{4mm}} \\sum_Z = F_R_Z = {f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0]):.2f} + {f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0]):.2f} + {f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}
        ${{\hspace{{4mm}} \\sum_Z = F_R_Z ={f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}
        
        De acuerdo con el anterior procedimiento el vector cartesiano de la fuerza resultante ($F_R$) es: {f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} i + {f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} j + {f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f} k. 
        
        $\\textbf{{\\small 3. Calcular los ángulos con respecto a X, Y, Z:}}$
        ${{\hspace{{4mm}} Ángulo con respecto a X = \\alpha = cos^{-1}\\left(\\dfrac{{\\overrightarrow{{F_R_X}}}}{{|\\overrightarrow{{F_R|}}\\right)}} }}$
        ${{\hspace{{4mm}} Ángulo con respecto a X = \\alpha = cos^{-1}\\left(\\dfrac{{{f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}{{{Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0])):.2f}}}\\right)}}$
        ${{\hspace{{4mm}} Ángulo con respecto a X = \\alpha = {Calculations.arccosine(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]))):.2f}}}$
       
        ${{\hspace{{4mm}} Ángulo con respecto a Y = \\beta = cos^{-1}\\left(\\dfrac{{\\overrightarrow{{F_R_Y}}}}{{|\\overrightarrow{{F_R|}}\\right)}} }}$
        ${{\hspace{{4mm}} Ángulo con respecto a Y = \\beta = cos^{-1}\\left(\\dfrac{{{f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}{{{Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0])):.2f}}}\\right)}}$
        ${{\hspace{{4mm}} Ángulo con respecto a Y = \\beta = {Calculations.arccosine(f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]))):.2f} }}$

        ${{\hspace{{4mm}} Ángulo con respecto a Z = \\gamma = cos^{-1}\\left(\\dfrac{{\\overrightarrow{{F_R_Z}}}}{{|\\overrightarrow{{F_R|}}\\right)}} }}$
        ${{\hspace{{4mm}} Ángulo con respecto a Z = \\gamma = cos^{-1}\\left(\\dfrac{{{f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]):.2f}}}{{{Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0])):.2f}}}\\right)}}$
        ${{\hspace{{4mm}} Ángulo con respecto a Z = \\gamma = {Calculations.arccosine(f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]),Calculations.magnitude3D(f[0]*d[3]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[9]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[15]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[6]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[12]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[18]/Calculations.magnitude3D(d[15],d[18],d[0]),f[0]*d[0]/Calculations.magnitude3D(d[3],d[6],d[0])+f[1]*d[0]/Calculations.magnitude3D(d[9],d[12],d[0])+f[2]*d[0]/Calculations.magnitude3D(d[15],d[18],d[0]))):.2f} }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 1330031,
        no_pregunta = 3,
        complexity = D,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"En el cable AD actúa una fuerza de {f[0]:.0f} N. Si la longitud del cable es {Calculations.magnitude3D(d[0],d[3],d[6]):.2f} m, $A_Z = {d[6]:.0f}$ y la componente $y$ de la fuerza es $F_y = {f[0]*d[3]/Calculations.magnitude3D(d[0],d[3],d[6]):.2f}$ N. Determine la distancia $D_X$ y $D_Y$.",
        no_answers = 2,
        a1_name = "Distancia $D_X$",
        a2_name = "Distancia $D_Y$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: d[0],
        answer2 = lambda f, a, calc, c, d, m: d[3],
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A66,
        ayuda2 = "Despeje de la anterior ecuación la distancia en Y ($D_Y$)",
        ayuda3 = "Para hallar la distancia en X ($D_X$) plantee la ecuación de la longitud del cable y despeje. ¿Qué representa la longitud del cable?.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para hallar las distancias $D_X$ y $D_Y$, primero se plantea la ecuación de la componente $y$ de la fuerza y a partir de ella se despeja la distancia en $y$. Luego se plantea la ecuación de la longitud de la cuerda y se despeja la distancia en $x$.
        
        $\\textbf{{\\small 1. Despeje de la distancia $D_Y$:}}$

        ${{\hspace{{4mm}} F_y = |\\overrightarrow{{F}}|*dfrac{{D_Y}}{{\\sqrt{{(-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}}} = |\\overrightarrow{{F}}|*dfrac{{D_Y}}{{Longitud del cable}} }}$
        ${{\hspace{{4mm}} D_Y = \\dfrac{{F_y*Longitud del cable}}{{|\\overrightarrow{{F}}|}}}}$
        ${{\hspace{{4mm}} D_Y = \\dfrac{{{f[0]*d[3]/Calculations.magnitude3D(d[0],d[3],d[6]):.2f}*{Calculations.magnitude3D(d[0],d[3],d[6]):.2f}}}{{{f[0]:.2f}}}}}$
        ${{\hspace{{4mm}} D_Y = {d[3]:.0f}}}$

        $\\textbf{{\\small 2. Despeje de la distancia $D_X$:}}$
        
        ${{\hspace{{4mm}} \\text{{Longitud de la cuerda}} = \\sqrt{{(-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}}}$
        ${{\hspace{{4mm}} (\\text{{Longitud de la cuerda}})^2 = (-D_X)^2 + (D_Y)^2 + (-A_Z)^2}}$
        ${{\hspace{{4mm}} (\\text{{Longitud de la cuerda}})^2 - (D_Y)^2 - (-A_Z)^2= (-D_X)^2}}$
        ${{\hspace{{4mm}} D_X = \\sqrt{{\\text{{Longitud de la cuerda}}-- (D_Y)^2 - (-A_Z)^2}}}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 

    Questionary(#4_1
        code = 1330041,
        no_pregunta = 4,
        complexity = D,
        topic = EQ,
        subtopic = VU,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Considere una cuerda en la que actúa una fuerza $\\overrightarrow{{F}}$ = ({f[0]*d[0]/Calculations.magnitude3D(d[0], d[3], d[6]):.2f} i + {f[0]*d[3]/Calculations.magnitude3D(d[0], d[3], d[6]):.2f} j + {f[0]*d[6]/Calculations.magnitude3D(d[0], d[3], d[6]):.2f}) k N  con origen en 0 i + 0 j + 0 k. Si la longitud de la cuerda es {Calculations.magnitude3D(d[0],d[3],d[6]):.2f} determine las distancias en X, Y y Z de la cuerda.",
        no_answers = 2,
        a1_name = "Distancia en X ($D_X$)",
        a2_name = "Distancia en Y ($D_Y$)",
        a3_name = "Distancia en Z ($D_Z$)",
        answer1 = lambda f, a, calc, c, d, m: d[0],
        answer2 = lambda f, a, calc, c, d, m: d[3],
        answer3 = lambda f, a, calc, c, d, m: d[6],
        ayuda1 = A67,
        ayuda2 = A68,
        ayuda3 = A69,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para hallar las distancias en X, Y y Z, se plantean las ecuaciones de cada una de las componentes de la fuerza como la multiplicación de la magnitud de la fuerza y el vector unitario en dicha componente.
        
        $\\textbf{{\\small 1. Despeje de la distancia en X ($D_X$):}}$

        ${{\hspace{{4mm}} F_x = |\\overrightarrow{{F}}|*dfrac{{D_X}}{{\\sqrt{{(D_X)^2 + (D_Y)^2 + (D_Z)^2}}}} = |\\overrightarrow{{F}}|*dfrac{{D_X}}{{Longitud de la cuerda}} }}$
        ${{\hspace{{4mm}} D_X = \\dfrac{{F_x*Longitud del cable}}{{|\\overrightarrow{{F}}|}}}}$
        ${{\hspace{{4mm}} D_X = \\dfrac{{{f[0]*d[0]/Calculations.magnitude3D(d[0],d[3],d[6]):.2f}*{Calculations.magnitude3D(d[0],d[3],d[6]):.2f}}}{{{f[0]:.2f}}}}}$
        ${{\hspace{{4mm}} D_X = {d[0]:.0f} }}$

        $\\textbf{{\\small 2. Despeje de la distancia en Y ($D_Y$):}}$

        ${{\hspace{{4mm}} F_y = |\\overrightarrow{{F}}|*dfrac{{D_Y}}{{\\sqrt{{(D_X)^2 + (D_Y)^2 + (D_Z)^2}}}} = |\\overrightarrow{{F}}|*dfrac{{D_Y}}{{Longitud de la cuerda}} }}$
        ${{\hspace{{4mm}} D_Y = \\dfrac{{F_y*Longitud del cable}}{{|\\overrightarrow{{F}}|}}}}$
        ${{\hspace{{4mm}} D_Y = \\dfrac{{{f[0]*d[3]/Calculations.magnitude3D(d[0],d[3],d[6]):.2f}*{Calculations.magnitude3D(d[0],d[3],d[6]):.2f}}}{{{f[0]:.2f}}}}}$
        ${{\hspace{{4mm}} D_Y = {d[3]:.0f} }}$

        $\\textbf{{\\small 1. Despeje de la distancia en Z ($D_Z$):}}$

        ${{\hspace{{4mm}} F_z = |\\overrightarrow{{F}}|*dfrac{{D_Z}}{{\\sqrt{{(D_X)^2 + (D_Y)^2 + (D_Z)^2}}}} = |\\overrightarrow{{F}}|*dfrac{{D_Z}}{{Longitud de la cuerda}} }}$
        ${{\hspace{{4mm}} D_Z = \\dfrac{{F_x*Longitud del cable}}{{|\\overrightarrow{{F}}|}}}}$
        ${{\hspace{{4mm}} D_Z = \\dfrac{{{f[0]*d[6]/Calculations.magnitude3D(d[0],d[3],d[6]):.2f}*{Calculations.magnitude3D(d[0],d[3],d[6]):.2f}}}{{{f[0]:.2f}}}}}$
        ${{\hspace{{4mm}} D_Z = {d[6]:.0f} }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),  

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Equilibrio 2D      ---------------------------------------------------
    #-------------------------------------------------       Nivel fácil      ---------------------------------------------------
    #-------------------------------------------------       Code: 141##      ---------------------------------------------------

    Questionary(#1_1
        code = 1410011,
        no_pregunta = 1,
        complexity = F,
        topic = EQ,
        subtopic = E2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las magnitudes de las fuerzas $F1$ y $F2$ para que la partícula esté en equilibrio. Considere $F3 = {f[0]:.0f} \\text{{ kN}}$, $\\alpha_1={a[0]:.0f}°$ y $\\alpha_2={a[4]:.0f}°$.",
        no_answers = 2,
        a1_name = "Magnitud $F1$ $[kN]$",
        a2_name = "Magnitud $F2$ $[kN]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((-(f[0]*calc['tan5']/(calc['sin1']+calc['cos1']*calc['tan5']))*calc['cos1']+f[0])/calc['cos5']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((f[0]*calc['tan5']/(calc['sin1']+calc['cos1']*calc['tan5'])),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A70,
        ayuda2 = A71,
        ayuda3 = A72,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
         Se sugiere para la solución del ejercicio el siguiente método:

        $\\textbf{{\\small 1. Sumatoria de fuerzas en X y Y:}}$

        $\\underline{{Ecuación \\hspace{{1mm}} 1}}$  

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_x}} = F1_x + F2_x + F3= -F1*cos(\\alpha_2) - F2*cos(\\alpha_1) +F3 = 0}}$

        $\\underline{{Ecuación \\hspace{{1mm}} 2}}$  

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = F1_y + F2_y = F1*sen(\\alpha_2)-F2*sen(\\alpha_1) = 0}}$
        

        $\\textbf{{\\small 2. Despejar las magnitudes:}}$

        Para simplificar el proceso de despeje, se busca formar una tangente. Al hacer esto, se reduce el número de términos en las ecuaciones. Dado lo anterior, se despeja $F1$ de la Ecuación 1 y se reemplaza en la Ecuación 2 para despejar $F2$. Con el valor de $F2$ obtenido, se halla $F1$.

        De la ecuación 1 se despeja $F1$:  

        ${{\hspace{{4mm}} F1 = \\dfrac{{-F2*cos(\\alpha_1)+F3}}{{cos(\\alpha_2)}}}}$

        Se reemplaza $F1$ en la ecuación 2:

        ${{\hspace{{4mm}} \\left(\\dfrac{{-F2*cos(\\alpha_1)+F3}}{{cos(\\alpha_2)}}\\right)*sen(\\alpha_2)-F2*sen(\\alpha_1) = 0}}$

        ${{\hspace{{4mm}} -F2*cos(\\alpha_1)*tan(\\alpha_2) + F3*tan(\\alpha_2) - F2*sen(\\alpha_1) = 0}}$

        ${{\hspace{{4mm}} F3*tan(\\alpha_2) = F2*sen(\\alpha_1) + F2*cos(\\alpha_1)*tan(\\alpha_2)}}$

        ${{\hspace{{4mm}} F3*tan(\\alpha_2) = F2(sen(\\alpha_1) + cos(\\alpha_1)*tan(\\alpha_2))}}$ 

        ${{\hspace{{4mm}} F2 = \\dfrac{{F3*tan(\\alpha_2)}}{{sen(\\alpha_1) + cos(\\alpha_1)*tan(\\alpha_2)}}}}$ 

        ${{\hspace{{4mm}} F2 = {(f[0]*calc['tan5']/(calc['sin1']+calc['cos1']*calc['tan5'])):.2f}}} \\text{{kN}}$

        Con el valor de $F2$ se calcula $F1$:  

        ${{\hspace{{4mm}} F1 = {((-(f[0]*calc['tan5']/(calc['sin1']+calc['cos1']*calc['tan5']))*calc['cos1']+f[0])/calc['cos5']):.2f}}} \\text{{kN}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 

    Questionary(#2_1
        code = 1410021,
        no_pregunta = 2,
        complexity = F,
        topic = EQ,
        subtopic = E2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las magnitudes de la $F1$ y el ángulo $\\alpha_2$ para que la partícula esté en equilibrio. Considere $F2 = {f[1]:.0f} \\text{{ kN}}$, $F3 = {f[0]:.0f} \\text{{ kN}}$ y $\\alpha_1={a[0]:.0f}°$.",
        no_answers = 2,
        a1_name = "Magnitud $F1$ $[kN]$",
        a2_name = "Ángulo $\\alpha_2$ $[°]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[1]*calc['sin1']/Calculations.sine(Calculations.arctangent((f[1]*calc['sin1'])/(-f[1]*calc['cos1']+f[0]))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((Calculations.arctangent((f[1]*calc['sin1'])/(-f[1]*calc['cos1']+f[0]))),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A70,
        ayuda2 = A71,
        ayuda3 = A72,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Se sugiere para la solución del ejercicio el siguiente método:

        $\\textbf{{\\small 1. Sumatoria de fuerzas en X y Y:}}$

        $\\underline{{Ecuación 1}}$  

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_x}} = F1_x + F2_x + F3= -F1*cos(\\alpha_2) - F2*cos(\\alpha_1) +F3 = 0}}$

        $\\underline{{Ecuación 2}}$  

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = F1_y + F2_y = F1*sen(\\alpha_2)-F2*sen(\\alpha_1) = 0}}$
        

        $\\textbf{{\\small 2. Despeje de la magnitud de F1 y el ángulo:}}$

        Para simplificar el proceso de despeje, se busca formar una tangente. Al hacer esto, se reduce el número de términos en las ecuaciones. Dado lo anteior, se despeja $F1$ de la Ecuación 1 y se reemplaza en la Ecuación 2 para despejar el ángulo $\\alpha_2$. Con el valor de $\\alpha_2$ obtenido, se halla $F1$.

        De la ecuación 1 se despeja $F1$:  

        ${{\hspace{{4mm}} F1 = \\dfrac{{-F2*cos(\\alpha_1)+F3}}{{cos(\\alpha_2)}}}}$

        Se reemplaza $F1$ en la ecuación 2:

        ${{\hspace{{4mm}} \\left(\\dfrac{{-F2*cos(\\alpha_1)+F3}}{{cos(\\alpha_2)}}\\right)*sen(\\alpha_2)-F2*sen(\\alpha_1) = 0}}$

        ${{\hspace{{4mm}} -F2*cos(\\alpha_1)*tan(\\alpha_2) + F3*tan(\\alpha_2) - F2*sen(\\alpha_1) = 0}}$
       
        ${{\hspace{{4mm}} tan(\\alpha_2)(-F2*cos(\\alpha_1) + F3) = F2*sen(\\alpha_1)}}$
        
        ${{\hspace{{4mm}} tan(\\alpha_2) = \\dfrac{{F2*sen(\\alpha_1)}}{{-F2*cos(\\alpha_1) + F3}}}}$
        
        ${{\hspace{{4mm}} \\alpha_2 = tan^{{-1}}\\left(\\dfrac{{F2*sen(\\alpha_1)}}{{-F2*cos(\\alpha_1) + F3}}\\right)}}$
        
        ${{\hspace{{4mm}} \\alpha_2 = {Calculations.arctangent((f[1]*calc['sin1'])/(-f[1]*calc['cos1']+f[0])):.2f}}}°$

        Con el valor de $F2$ se calcula $F1$:  

        ${{\hspace{{4mm}} F1 = {f[1]*calc['sin1']/Calculations.sine(Calculations.arctangent((f[1]*calc['sin1'])/(-f[1]*calc['cos1']+f[0]))):.2f}}} \\text{{ kN}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),  

    Questionary(#3_1
        code = 1410031,
        no_pregunta = 3,
        complexity = F,
        topic = EQ,
        subtopic = E2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el valor de $F$ para el siguiente sistema. Considere $W = {f[0]:.0f} N$.",
        no_answers = 1,
        a1_name = "Fuerza $F$ $[N]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]/2,2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A73,
        ayuda2 = A74,
        ayuda3 = A75,
        respuesta_P1 = lambda f, a, calc, c, d, m: T3,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Sumatoria de fuerzas en Y:}}$

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{F_y}} = W - 2F = 0}}$     
        ${{\hspace{{4mm}} 2F = W}}$     
        ${{\hspace{{4mm}} F = \\dfrac{{W}}{{2}}}}$ 

        ${{\hspace{{4mm}} F = {f[0]/2:.2f}}} N$ 
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 

    Questionary(#4_1
        code = 1410041,
        no_pregunta = 4,
        complexity = F,
        topic = EQ,
        subtopic = E2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es la fuerza de fricción necesaria para evitar que el bloque de peso $W={f[0]:.0f}$ $N$ se desplace a lo largo del plano inclinado a ${a[0]:.0f}$° de la horizontal.",
        no_answers = 1,
        a1_name = "Fuerza de fricción ($f_r$) $[N]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['sin1'],2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "Defina un sistema de coordenadas arbitrario, donde el eje X' sea paralelo al plano inclinado y el eje Y' esté a 90° con respecto a la superficie del plano.",
        ayuda2 = A76,
        ayuda3 = A75,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Diagrama de cuerpo libre de la polea y sistema de coordenadas arbitrario:}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Sumatoria de fuerzas en Y:}}$

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{F_y}} = f_r - W*sen(\\alpha_1) = 0}}$     
        ${{\hspace{{4mm}} f_r = W*sen(\\alpha_1)}}$       
        ${{\hspace{{4mm}} F = {f[0]*calc['sin1']:.2f}}} N$ 
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),  
    
    Questionary(#5_1
        code = 1410051,
        no_pregunta = 5,
        complexity = F,
        topic = EQ,
        subtopic = E2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Considere una partícula sobre la que actúan las fuerzas $F_1=[({c[0]:.0f}) i + ({c[1]:.0f}) j] N$ y $F_2=[({c[2]:.0f}) i + ({c[3]:.0f}) j] N$. Determine el vector cartesiano de la fuerza que debe aplicarse para que la partícula esté en equilibrio.",
        no_answers = 2,
        a1_name = Ci,
        a2_name = Cj,
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(-(c[0]+c[2]),2),
        answer2=lambda f, a, calc, c, d, m: np.round(-(c[1]+c[3]),2),
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A71,
        ayuda2 = A77,
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m:f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Sumatoria de fuerzas en X:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0}}$     
        ${{\hspace{{4mm}} \\sum{{F_x}} = F1_x + F2_x + F3_x}}$     
        ${{\hspace{{4mm}} F3_x = -F1_x - F2_x }}$     
        ${{\hspace{{4mm}} F3_x = {-(c[0]+c[2]):.2f}}} \\text{{N}}$      
       
        $\\textbf{{\\small 2. Sumatoria de fuerzas en Y:}}$

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0}}$     
        ${{\hspace{{4mm}} \\sum{{F_y}} = F1_y + F2_y + F3_y}}$     
        ${{\hspace{{4mm}} F3_y = -F1_y - F2_y }}$     
        ${{\hspace{{4mm}} F3_x = {-(c[1]+c[3]):.2f}}} \\text{{N}}$   

        De acuerdo con lo anterior, el vector cartesiano de la fuerza que debe aplicar es [${-(c[0]+c[2]):.2f}$ $\\hat{{i}}$ + ${-(c[1]+c[3]):.2f}$ $\\hat{{j}}$] $N$.
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),
    
    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Equilibrio 2D      ---------------------------------------------------
    #-------------------------------------------------       Nivel medio      ---------------------------------------------------
    #-------------------------------------------------       Code: 142##      ---------------------------------------------------

    Questionary(#1_1
        code = 1420011,
        no_pregunta = 1,
        complexity = M,
        topic = EQ,
        subtopic = E2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el valor de F para el siguiente sistema. Considere $W = {f[0]:.0f} N$",
        no_answers = 1,
        a1_name = "Fuerza $F$ $[N]$",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(f[0]/8,2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = A78,
        ayuda2 = A74,
        ayuda3 = A75,
        respuesta_P1 = lambda f, a, calc, c, d, m:T3, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Equilibrio en la polea 1:}}$

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$    
        ${{\hspace{{4mm}} \\sum{{F_y}} = 2T_1 - W = 0}}$     
        ${{\hspace{{4mm}} 2T_1 = W}}$     
        ${{\hspace{{4mm}} T_1 = \\dfrac{{W}}{{2}}}}$  

        ${{\hspace{{4mm}} T_1 = {f[0]/2:.2f}}} N$   

        $\\textbf{{\\small 3. Equilibrio en la polea 2:}}$ 

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$    
        ${{\hspace{{4mm}} \\sum{{F_y}} = 2T_2 - T_1 = 0}}$    
        ${{\hspace{{4mm}} 2T_2 = T_1}}$      
        ${{\hspace{{4mm}} T_2 = \\dfrac{{T_1}}{{2}}}}$  

        ${{\hspace{{4mm}} T_2 = \\dfrac{{W}}{{4}}}}$    

        ${{\hspace{{4mm}} T_2 = {f[0]/4:.2f}}} N$      

        $\\textbf{{\\small 4. Equilibrio en la polea 3:}}$

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = 2T_3 - T_2 = 0}}$        
        ${{\hspace{{4mm}} 2T_3 = T_2}}$      
        ${{\hspace{{4mm}} T_3 = \\dfrac{{T_2}}{{2}}}}$ 

        ${{\hspace{{4mm}} T_3 = \\dfrac{{W}}{{8}}}}$   

        ${{\hspace{{4mm}} T_3 = {f[0]/8:.2f}}} N$   

        $\\textbf{{\\small 5. Definición de la fuerza F:}}$

        Dado que la cuerda en la que actúa la tensión $T_3$ es la misma en la que actúa $F$, la fuerza F es equivalente a $T_3$, es decir, ${f[0]/8:.2f}$ $N$.
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------     Equilibrio 2D      ---------------------------------------------------
    #-------------------------------------------------       Nivel díficil    ---------------------------------------------------
    #-------------------------------------------------       Code: 143##      ---------------------------------------------------

    Questionary(#1_1
        code = 1430011,
        no_pregunta = 1,
        complexity = D,
        topic = EQ,
        subtopic = E2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Esta sección de la aplicación está en implementación. ¡Pronto estará disponible!",
        no_answers = 3,
        a1_name = "",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: 0,
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = "",
        ayuda2 = "",
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m:"", 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),

    #========================================================MOMENTO============================================================
    #--------------------------------------------     Momento en un punto en 2D      --------------------------------------------
    #-------------------------------------------------       Nivel fácil      ---------------------------------------------------
    #-------------------------------------------------       Code: 21100##    ---------------------------------------------------

    Questionary(#1_1
        code = 2110011,
        no_pregunta = 1,
        complexity = F,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el momento en el punto A de la fuerza $F_1$ y $F_2$. Considere que $F_1 = {f[0]:.0f} \\text{{ kN}}$, $F_2 = {f[1]:.0f} \\text{{ kN}}$, $\\alpha_1 = {a[0]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ m}}$,  $X_2 = {d[3]:.0f}  \\text{{ m}}$ y $X_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Momento en A de la fuerza F1 [$kN \\cdot m$]",
        a2_name = "Momento en A de la fuerza F2 [$kN \\cdot m$]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(-f[0]*d[0],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-f[1]*calc['sin1']*(d[0]+d[3]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP2,      
        ayuda3 = MP3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector posición $\\overrightarrow{{r}}$. A continuación, se presenta la solución sugerida para el ejercicio:  

        $\\textbf{{\\small 1. Descomposición de las fuerzas F1 y F2:}}$

        $\\underline{{Fuerza \\hspace{{2mm}} F_1 :}}$ La fuerza $F_1$ solo tiene componente en Y y es igual a su magnitud. 

        $\\underline{{Fuerza  \\hspace{{2mm}} F_2 :}}$ 

        ${{\hspace{{4mm}} F_2x = |\\overrightarrow{{F_2}}| \\cdot \\cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ kN }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ kN}}}}}}$     
        ${{\hspace{{4mm}} F_2y = |\\overrightarrow{{F_2}}| \\cdot \\sin(\\alpha_1) = {f[1]:.0f}{{\\text{{ kN }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ kN}}}}}}$    

        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        En este caso, los vectores posición solo tienen componente en la dirección X, y son equivalentes a la magnitud de las distancias de A al punto de acción de la fuerza:      
        
        ${{\hspace{{4mm}} r_1 \\text{{ = }} X_1 = {d[0]:.0f}{{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} r_2 \\text{{ = }} X_1 + X_2 = {(d[0]+d[3]):.0f}{{ \\text{{ m}}}}}}$     

        Ahora solo es necesario operar utilizando la ecuación de momento según las componentes necesarias y denotando el signo acorde a la regla de la mano de derecha: 

        $\\textbf{{\\small 3. Cálculo del momento en el punto A:}}$ 

        $\\underline{{Momento \\hspace{{2mm}} de \\hspace{{2mm}} la \\hspace{{2mm}} fuerza \\hspace{{2mm}} F1:}}$

        Teniendo en cuenta que el vector posición y la fuerza $F_1$ ya son perpendiculares entre sí, y que, por la regla de la mano de derecha el momento es negativo (en sentido horario):

        ${{\hspace{{4mm}} M_1 = - |\\overrightarrow{{r_1}}| \\cdot |\\overrightarrow{{F_1}}| = -{d[0]:.0f}{{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[0]:.0f}{{\\text{{ kN }}}}}}$     
        ${{\hspace{{4mm}} M_1 = {-f[0]*d[0]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$     

        $\\underline{{Momento \\hspace{{2mm}} de \\hspace{{2mm}} la \\hspace{{2mm}} fuerza \\hspace{{2mm}} F2:}}$

        En el momento de la fuerza F2, la componente de la fuerza que es perpendicular al vector posición es $F2_y$, y por la regla de la mano de derecha el momento es negativo: 

        ${{\hspace{{4mm}} M_2 = \\overrightarrow{{r_2}} X \\overrightarrow{{F_2}} = -r_2 \\cdot\\hspace{{1mm}} F_2y = - {(d[3]+d[0]):.0f}{{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['sin1']:.2f}{{\\text{{ kN}}}}}}$      
        ${{\hspace{{4mm}} M_2 = {-(f[1]*calc['sin1']*(d[0]+d[3])):.2f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$  
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 2110021,
        no_pregunta = 2,
        complexity = F,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de las fuerzas $F_1$ y $F_2$, si en el punto D el momento que ejerce la fuerza $F1$ es ${m[0]:.0f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}$, y el momento que ejerce la fuerza $F2$ es ${m[1]:.0f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}$. Considere que $\\alpha_1 = {a[0]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ m}}$,  $X_2 = {d[3]:.0f}  \\text{{ m}}$ y $X_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Fuerza $F_1 [kN]$",
        a2_name = "Fuerza $F_2 [kN]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((m[0])/(d[3]+d[6]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((m[1])/(d[6]*calc['sin1']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP2,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector posición $\\overrightarrow{{r}}$. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Determinación del vector posición asociado a cada fuerza: }}$ 
        
        En este caso, los vectores posición solo tienen componente en la dirección X y son equivalentes a la magnitud de las distancias de D al punto de acción de la fuerza. 

        ${{\hspace{{4mm}} r_1 = X_2 + X_3 = {d[3] + d[6]:.0f}{{\\text{{ m}}}}}}$       
        ${{\hspace{{4mm}} r_2 = X_3 = {(d[6]):.0f}{{\\text{{ m}}}}}}$      
        
        $\\textbf{{\\small 2. Descomposición de las fuerzas F1 y F2: }}$
       
        $\\underline{{Fuerza \\hspace{{2mm}} F1 :}}$ La fuerza F1 solo tiene componente en Y y es igual a su magnitud. 

        $\\underline{{Fuerza \\hspace{{2mm}} F2 :}}$ 

        ${{\hspace{{4mm}} F2_x = |\\overrightarrow{{F2}}| \\cdot cos(\\alpha_1)}}$       
        ${{\hspace{{4mm}} F2_y = |\\overrightarrow{{F2}}| \\cdot sen(\\alpha_1)}}$       
        
        $\\textbf{{\\small 3. Cálculo de las fuerzas F1 y F2: }}$ 

        $\\underline{{Fuerza  \\hspace{{2mm}} F_1 :}}$ 
        
        Se define la ecuación de momento en D de la fuerza $F_1$ y por la regla de la mano de derecha el momento es positivo (en sentido antihorario).
        
        ${{\hspace{{4mm}} M_1D  = \\overrightarrow{{r_1}} X \\overrightarrow{{F_1}} = r_1x \\cdot F1_y}}$ 

        ${{\hspace{{4mm}} F_1 = \\dfrac{{M_{{1D}}}}{{r_1x}}}}$  

        ${{\hspace{{4mm}} F_1 = ( \\dfrac{{{m[0]:.0f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}{{{d[3]+d[6]:.0f}{{\\text{{ m}}}}}} ) }}$      

        ${{\hspace{{4mm}} F_1  = {(m[0])/(d[3]+d[6]):.2f}{{\\text{{ kN}}}}}}$      
        
        $\\underline{{Fuerza  \\hspace{{2mm}} F_2 :}}$ 
        
        Se desarrolla el mismo procedimiento que con la fuerza $F_1$, se define la ecuación de momento en D de la fuerza F2 y se verifica su sentido con la regla de la mano de derecha el momento es positivo (en sentido antihorario).
        
        ${{\hspace{{4mm}} M2_D  = \\overrightarrow{{r2}} X \\overrightarrow{{F2}} = |\\overrightarrow{{r2}}| \\cdot |\\overrightarrow{{F2}}| \\cdot sen(\\alpha_1)}}$   

        ${{\hspace{{4mm}} F_2 = \\dfrac{{M_{{2D}}}}{{r_2 \\cdot sen(\\alpha_1)}}}}$      

        ${{\hspace{{4mm}} F_2 = ( \\dfrac{{{m[1]:.0f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}{{{d[6]*calc['sin1']:.2f}{{\\text{{ m}}}}}} ) }}$      

        ${{\hspace{{4mm}} F_2  = {(m[1])/(d[6]*calc['sin1']):.2f}{{\\text{{ kN}}}}}}$      
        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 2110031,
        no_pregunta = 3,
        complexity = F,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el momento en el punto B de la fuerza $F1$ y $F2$, y el momento en C de la fuerza $F2$. Considere que $F_1 = {f[0]:.0f} \\text{{ kN}}$, $F_2 = {f[1]:.0f} \\text{{ kN}}$, $\\alpha_1 = {a[0]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ m}}$,  $X_2 = {d[3]:.0f}  \\text{{ m}}$ y $X_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Momento en B de la fuerza $F1$ [$kN \\cdot m$]",
        a2_name = "Momento en B de la fuerza $F2$ [$kN \\cdot m$]",
        a3_name = "Momento en C de la fuerza $F2$ [$kN \\cdot m$]",
        answer1 = lambda f, a, calc, c, d, m: np.round(-f[0]*d[3],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-f[1]*calc['cos1']*(d[0]),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(-(f[1]*calc['cos1']*(d[0]+d[3])),2),
        ayuda1 = MP1,
        ayuda2 = MP2,      
        ayuda3 = MP3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector posición $\\overrightarrow{{r}}$. A continuación, se presenta la solución sugerida para el ejercicio:  

        $\\textbf{{\\small 1. Descomposición de las fuerzas F1 y F2:}}$

        $\\underline{{Fuerza \\hspace{{2mm}} F1:}}$ La fuerza $F1$ solo tiene componente en Y y es igual a su magnitud. 

        $\\underline{{Fuerza \\hspace{{2mm}} F2:}}$ 
        
        ${{\hspace{{4mm}} F_{{2x}} = |\\overrightarrow{{F_2}}| \\cdot sen(\\alpha_1) = {f[1]:.0f}{{\\text{{ kN }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ kN}}}}}}$       
        ${{\hspace{{4mm}} F_{{2y}} = |\\overrightarrow{{F_2}}| \\cdot cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ kN }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ kN}}}}}}$          
        
        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

       En este caso, los vectores posición solo tienen componente en la dirección X y son equivalentes a la magnitud de las distancias de D al punto de acción de la fuerza: 

        ${{\hspace{{4mm}} r_{{1B}} = X_2 = {d[3]:.0f}{{ \\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} r_{{2B}} = X_1 = {d[0]:.0f}{{ \\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} r_{{2C}} = X_1 + X_2 = {d[0] +d[3]:.0f}{{ \\text{{ m}}}}}}$       

        $\\textbf{{\\small 3. Cálculo de los momentos: }}$ 

        $\\underline{{Momento \\hspace{{2mm}} en \\hspace{{2mm}} B \\hspace{{2mm}} de \\hspace{{2mm}} la \\hspace{{2mm}} fuerza \\hspace{{2mm}} F_1:}}$ 

        Se tiene en cuenta que el vector posición y la fuerza $F_1$ son perpendiculares entre sí, y que, por la regla de la mano de derecha el momento es negativo (en sentido horario): 

        ${{\hspace{{4mm}} M_{{1B}} = -|\\overrightarrow{{r_{{1B}}}}| \\cdot |\\overrightarrow{{F1}}| = -{d[3]:.0f}{{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[0]:.0f}{{\\text{{ kN}}}}}}$       
        ${{\hspace{{4mm}} M_{{1B}} = {-f[0]*d[3]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$     

        $\\underline{{Momento \\hspace{{2mm}} en \\hspace{{2mm}} B \\hspace{{2mm}} de \\hspace{{2mm}} la \\hspace{{2mm}} fuerza \\hspace{{2mm}} F_2:}}$ 

        La componente de la fuerza $F_2$ que genera momento en el punto B es $F2_y$, la cual es perpendicular al vector posición $r_{{2B}}. Por la regla de la mano de derecha, el momento es negativo (en sentido horario): 

        ${{\hspace{{4mm}} M_{{2B}} = \\overrightarrow{{r_{{2B}}}} X \\overrightarrow{{F_2}} = r{{2B}} \\cdot\\hspace{{1mm}} F_{{2y}} = -{(d[0]):.0f}{{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['cos1']:.2f}{{\\text{{ kN}}}}}}$      
        ${{\hspace{{4mm}} M_{{2B}} = {-(f[1]*calc['cos1']*(d[0])):.2f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$    
        
        $\\underline{{Momento \\hspace{{2mm}} en \\hspace{{2mm}} C \\hspace{{2mm}} de \\hspace{{2mm}} la \\hspace{{2mm}} fuerza \\hspace{{2mm}} F_2 :}}$ 

       De manera simular al punto B, el momento en C de la fuerza $F_2$ es generado por la componente perpendicular al vector posición, es decir, $F2_y$. Según la regla de la mano de derecha, el momento es negativo (en sentido horario):  
        
        ${{\hspace{{4mm}} M_{{2C}} = \\overrightarrow{{r_{{2C}}}} X \\overrightarrow{{F_2}} = r_{{2C}} \\cdot\\hspace{{1mm}} F_{{2y}} = -{(d[0]+d[3]):.0f}{{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['cos1']:.2f}{{\\text{{ kN}}}}}}$      
        ${{\hspace{{4mm}} M_{{2C}} = {-(f[1]*calc['cos1']*(d[0]+d[3])):.2f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$    
        
        Asimismo, es importante aclarar que la fuerza $F_1$ no genera momento en el punto C, dado que, su línea de acción de esta fuerza cruza con el punto C.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_1
        code = 2110041,
        no_pregunta = 4,
        complexity = F,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza $F1$ y la distancia $X1$, si en el punto B el momento de $F_1$ es ${-m[0]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}$, y el momento de $F_2$ es ${-m[1]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}$. Considere que $\\alpha_1 = {a[0]:.0f}°$, $F_2 = {f[1]:.0f} \\text{{ kN}}$,  $X_2 = {d[3]:.0f}  \\text{{ m}}$ y $X_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Fuerza $F_1 [kN]$",
        a2_name = "Distancia $X_1 [m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((m[0])/d[3]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((m[1])/(f[1]*calc['cos1']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP2,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector posición $\\overrightarrow{{r}}$. A continuación, se presenta la solución sugerida para el ejercicio:
        
        Para hallar la fuerza $F_1$ se define la ecuación del momento que esta ejerce en el punto B. Por otra parte, la distancia $X_1$ se calcula mediante la ecuación del momento que ejerce la fuerza $F_2$ en el punto B.
        
        $\\textbf{{\\small 1. Determinación del vector posición asociado a cada fuerza: }}$ 
        
        En este caso, los vectores posición solo tiene componente en X y son equivalentes a la magnitud de las distancias de B al punto de acción de la fuerza. 

        ${{\hspace{{4mm}} r_1 = X_2 = {d[3]:.0f}{{\\text{{ m}}}}}}$    
        ${{\hspace{{4mm}} r_2 = X_1}}$
        
        $\\textbf{{\\small 2. Descomposición de las fuerzas F1 y F2: }}$
       
        $\\underline{{Fuerza \\hspace{{2mm}} F1 :}}$ La fuerza $F_1$ solo tiene componente en Y y es igual a su magnitud. 

        $\\underline{{Fuerza \\hspace{{2mm}} F2 :}}$ 

        ${{\hspace{{4mm}} F_{{2x}} = |\\overrightarrow{{F_2}}| \\cdot sen(\\alpha_1) = {f[1]:.0f}{{\\text{{ kN }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ kN}}}}}}$      
        ${{\hspace{{4mm}} F_{{2y}} = |\\overrightarrow{{F_2}}| \\cdot \\cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ kN }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ kN}}}}}}$     
        
        $\\textbf{{\\small 3. Cálculo de la fuerza F1: }}$ 
        
        Se define la ecuación de momento en B de la fuerza F1. De acuedo con la regla de la mano de derecha el momento es negativo (sentido horario).
        
        ${{\hspace{{4mm}} M_{{1B}}  = \\overrightarrow{{r_1}} X \\overrightarrow{{F_1}} = - r_1 \\cdot |\\overrightarrow{{F_1}}| }}$ 

        ${{\hspace{{4mm}} F1 = -\\dfrac{{M_{{1d}}}}{{r_1}}}}$ 

        ${{\hspace{{4mm}} F1 = -( \\dfrac{{{-m[0]:.0f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}{{{d[3]:.0f}{{\\text{{ m}}}}}} ) }}$    

        ${{\hspace{{4mm}} F1  = {(m[0])/d[3]:.2f}{{\\text{{ kN}}}}}}$     
        
        $\\textbf{{\\small 4. Cálculo de la distancia X1: }}$ 
        
       Se define la ecuación de momento en B de la fuerza $F_2$. Según la regla de la mano de derecha el momento es negativo (sentido horario).
        
        ${{\hspace{{4mm}} M_{{2B}}  = \\overrightarrow{{r_2}} X \\overrightarrow{{F_2}} = -r_2 \\cdot |\\overrightarrow{{F_2}}| \\cdot \\cos(\\alpha_1)}}$     

        ${{\hspace{{4mm}} X_1 = r2 = - \\dfrac{{M_{{2B}}}}{{F_2 \\cdot \\cos(\\alpha_1)}}}}$      

        ${{\hspace{{4mm}} X_1 = -( \\dfrac{{{-m[1]:.0f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}{{{f[1]*calc['cos1']:.2f}{{ \\text{{ kN}}}}}} ) }}$  

        ${{\hspace{{4mm}} X_1  = {(m[1])/(f[1]*calc['cos1']):.2f}{{\\text{{ m}}}}}}$    
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#5_1
        code = 2110051,
        no_pregunta = 5,
        complexity = F,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule el momento alrededor del origen $\\textit{{O}}$ generado por la fuerza $\\overrightarrow{{F}} = [ {m[0]:.0f}\\hat{{i}} +  {m[3]:.0f} \\hat{{j}} ] {{ \\text{{ kN}}}}$ que actúa en un punto $A$. Evalúe el momento considerando los siguientes vectores de posición:  $ \\overrightarrow{{r_a}} = [ {d[0]:.0f}\\hat{{i}} + {d[3]:.0f}\\hat{{j}} ]{{ \\text{{ m}}}}$ ; $\\overrightarrow{{r_b}} = [ {d[6]:.0f} \\hat{{i}} + {d[9]:.0f}\\hat{{j}} ]{{ \\text{{ m}}}}$.",
        no_answers = 2,
        a1_name = "Momento usando $\\overrightarrow{{r_a}}$ $[kN \\cdot m]$",
        a2_name = "Momento usando $\\overrightarrow{{r_b}}$ $[kN \\cdot m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(d[0]*m[3]-d[3]*m[0],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(d[6]*m[3]-d[9]*m[0],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP3,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. A continuación, se presenta la solución sugerida:  

        En el ejercicio planteado, es importante notar que se proporcionan las componentes de la Fuerza y del Vector posición, lo que permite resolver el problema mediante el producto cruz. Sin embargo, como el análisis se realiza en dos dimensiones, el momento resultante tendrá una única componente en la dirección $\\hat{{k}}$, perpendicular al plano. Su obtención se realiza multiplicando las componentes perpendiculares entre sí del Vector Fuerza y del vector Posición, tal que:
        
        ${{\hspace{{4mm}} M = \\overrightarrow{{r_x}} \\cdot \\overrightarrow{{F_y}} - \\overrightarrow{{r_y}} \\cdot \\overrightarrow{{F_x}}}}$
        
        A partir de lo anterior, se puede determinar fácilmente el momento asociado a cada Vector posición dado en el enunciado:
        
        $\\textbf{{\\small 1. Momento usando el vector de posición a:}}$
        
        ${{\hspace{{4mm}} M = \\overrightarrow{{r_x}} \\cdot \\overrightarrow{{F_y}} - \\overrightarrow{{r_y}} \\cdot \\overrightarrow{{F_x}} = ( {d[0]:.0f}{{ \\text{{ m}}}} \\cdot {m[3]:.0f}{{ \\text{{ kN }}}} ) - ( {d[3]:.0f}{{ \\text{{ m}}}} \\cdot {m[0]:.0f}{{ \\text{{ kN}}}} ) }}$     
        ${{\hspace{{4mm}} M = {d[0]*m[3]-d[3]*m[0]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$    
        
        $\\textbf{{\\small 2. Momento usando el vector de posición b:}}$
        
        ${{\hspace{{4mm}} M = \\overrightarrow{{r_x}} \\cdot \\overrightarrow{{F_y}} - \\overrightarrow{{r_y}} \\cdot \\overrightarrow{{F_x}} = ( {d[6]:.0f}{{ \\text{{ m}}}} \\cdot {m[3]:.0f}{{ \\text{{ kN}}}} ) - ( {d[9]:.0f}{{ \\text{{ m}}}} \\cdot {m[0]:.0f}{{ \\text{{ kN}}}} ) }}$     
        ${{\hspace{{4mm}} M = {d[6]*m[3]-d[9]*m[0]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$            
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    
    #=========================================================== MOMENTO ========================================================
    #--------------------------------------------     Momento en un punto en 2D      --------------------------------------------
    #-------------------------------------------------       Nivel medio      ---------------------------------------------------
    #-------------------------------------------------       Code: 2120011    ---------------------------------------------------

    Questionary(#1_1
        code = 2120011,
        no_pregunta = 1,
        complexity = M,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el momento en el punto A generado por las tres fuerzas. Considere que $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$, $F_3 = {f[2]:.0f} \\text{{ N}}$, $\\alpha_1 = {a[0]:.0f}°$, $\\alpha_2 = {a[4]:.0f}°$,  $\\beta = {a[8]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ m}}$ y $X_2 = {d[3]:.0f}  \\text{{ m}}$.",
        no_answers = 1,
        a1_name = "Momento en A [$N \\cdot m$]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[1]*calc['sin1']*(d[0]))+(-f[2]*calc['cos5']*(d[3]*calc['sin9'])+(-f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9'])))),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento en el punto A corresponde a la sumatoria del momento generado en A por cada una de las fuerzas.
        
        $\\textbf{{\\small 1. Descomposición de las fuerzas:}}$

        $\\underline{{Fuerza  \\hspace{{2mm}} F1 :}}$ La fuerza F1 solo tiene componente en Y y es igual a su magnitud. 

        $\\underline{{Fuerza  \\hspace{{2mm}} F2 :}}$ 

        ${{\hspace{{4mm}} F2_x = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ N}}}}}}$     
        ${{\hspace{{4mm}} F2_y = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_1) = {f[1]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ N}}}}}}$     

        $\\underline{{Fuerza  \\hspace{{2mm}} F3 :}}$ 
        
        ${{\hspace{{4mm}} F3_x = |\\overrightarrow{{F3}}| \\cdot \\cos(\\alpha_2) = {f[2]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['cos5']:.2f} = {f[2]*calc['cos5']:.2f}{{ \\text{{ N}}}}}}$      
        ${{\hspace{{4mm}} F3_y = |\\overrightarrow{{F3}}| \\cdot \\sin(\\alpha_2) = {f[2]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['sin5']:.2f} = {f[2]*calc['sin5']:.2f}{{ \\text{{ N}}}}}}$     

        $\\textbf{{\\small 2. Determinación del vector posición:}}$ 

        $\\underline{{Vector \\hspace{{2mm}} Posición  \\hspace{{2mm}} r1: }}$
        
        $r_1$ es igual a 0, dado que, la línea de acción de la fuerza $F_1$ cruza el punto A.

        $\\underline{{Vector \\hspace{{2mm}} Posición  \\hspace{{2mm}} r2: }}$         

        En este caso, el vector posición $\\overrightarrow{{r2}}$ solo tiene componente en dirección X y es equivalente a la magnitud de la distancia de A al punto de acción de la fuerza. Considerando: 

        ${{\hspace{{4mm}} r_2 =  X_1 = {d[0]:.0f}{{ \\text{{ m}}}}}}$     
        
        $\\underline{{Vector \\hspace{{2mm}} Posición \\hspace{{2mm}} r3: }}$ 

        ${{\hspace{{4mm}} r_{{3x}} = X_1 + X_2 \\cdot \\cos(\\beta) = {d[0]+(d[3]*calc['cos9']):.2f}{{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} r_{{3y}} = x_2 \\cdot \\sin(\\beta) = {d[3]*calc['sin9']:.2f}{{ \\text{{ m}}}}}}$     

        $\\textbf{{\\small 3. Sumatoria de momento en A: }}$ 

        $\\underline{{Momento \\hspace{{2mm}} en \\hspace{{2mm}} A \\hspace{{2mm}} de \\hspace{{2mm}} la \\hspace{{2mm}} fuerza \\hspace{{2mm}} F1:}}$ 

        Dado que, la fuerza F1 se aplica directamente en el punto A, no se genera momento: 

        ${{\hspace{{4mm}} M_1 = 0 {{\\text{{ N}} \\cdot\\text{{ m}}}} }}$    

        $\\underline{{Momento \\hspace{{2mm}} en \\hspace{{2mm}} A \\hspace{{2mm}} de \\hspace{{2mm}} la \\hspace{{2mm}} fuerza \\hspace{{2mm}} F2:}}$ 

        La componente en Y de la fuerza F2 genera el momento en el punto A. De acuerdo con la regla de la mano de derecha el momento es positivo. 

        ${{\hspace{{4mm}} M_2 = \\overrightarrow{{r_2}} X \\overrightarrow{{F_2}} = r_2 \\cdot\\hspace{{1mm}} F_{{2y}} = {(d[0]):.0f}{{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['sin1']:.2f}{{\\text{{ N}}}}}}$     
        ${{\hspace{{4mm}} M_2 = {(f[1]*calc['sin1']*(d[0])):.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$    
        
        $\\underline{{Momento \\hspace{{2mm}} en \\hspace{{2mm}} A \\hspace{{2mm}} de \\hspace{{2mm}} la \\hspace{{2mm}} fuerza \\hspace{{2mm}} F3:}}$

        Las componentes X y Y de la fuerza F3 generan momento en el punto A:

        ${{\hspace{{4mm}} \\sum{{M_3}} = -r3_y \\cdot\\ F3_x + (-r3_y \\cdot\\hspace{{1mm}} F3_x)}}$    
        ${{\hspace{{4mm}} \\sum{{M_3}} = -{(d[3]*calc['sin9']):.2f}{{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[2]*calc['cos5']:.2f}{{\\text{{ N}}}} + (-{d[0]+(d[3]*calc['cos9']):.2f}{{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[2]*calc['sin5']:.2f}{{\\text{{ N}}}})}}$           
        ${{\hspace{{4mm}} \\sum{{M_3}} = {-((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}  }}$

        Finalmente, se calcula la sumatoria de momentos en el punto A:

        ${{\hspace{{4mm}} \\sum{{M_A}} = M_1 + M_2 + M_3 = {(f[1]*calc['sin1']*(d[0]))+(-f[2]*calc['cos5']*(d[3]*calc['sin9'])+(-f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}  }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 
    
    Questionary(#2_1
        code = 2120021,
        no_pregunta = 2,
        complexity = M,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el valor de $F_1$ para que el momento que este genera en B sea igual al momento en B generado por $F_3$. Considere que $F_2 = {f[1]:.0f} \\text{{ N}}$, $F_3 = {f[2]:.0f} \\text{{ N}}$, $\\alpha_1 = {a[0]:.0f}°$, $\\alpha_2 = {a[4]:.0f}°$,  $\\beta = {a[8]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ m}}$ y $X_2 = {d[3]:.0f}  \\text{{ m}}$.",
        no_answers = 1,
        a1_name = "Fuerza $F1 [N]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[2]*(d[3]/d[0])*Calculations.sine(a[4]+a[8]),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP2,      
        ayuda3 = MP3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para resolver este ejercicio, primero se calcula el momento en B generado por la fuerza $F_3$, y luego, se iguala a la ecuación de momento generado por $F_1$:
        
        $\\textbf{{\\small 1. Momento de la fuerza F3: }}$ 

        Para el cálculo del momento que genera la fuerza $F_3$ en el punto B se realiza la suma del momento que producen sus componentes. En la sumatoria se tiene en cuenta la dirección del momento de acuerdo con la regla de la mano derecha.
        
        ${{\hspace{{4mm}} M_3 = (-r_{{3y}} \\cdot\\hspace{{1mm}} F_{{3x}}) + (-r_{{3x}} \\cdot\\hspace{{1mm}} F_{{3y}})  = {-(f[2]*calc['cos5']*(d[3]*calc['sin9'])):.2f}{{\\text{{ N}} \\cdot\\text{{ m }}}}{-(f[2]*calc['sin5']*((d[3]*calc['cos9']))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} M_3 = {-((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*((d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$ 
   
        $\\textbf{{\\small 2. Cálculo de la fuerza F1: }}$
        
        Para hallar la fuerza $F_1$, se iguala la ecuación del momento generado por la fuerza $F_1$ en el punto B con el momento generado por $F_3$ en el mismo punto.

        ${{\hspace{{4mm}} M1 = -r1  \\cdot F1}}$              
        ${{\hspace{{4mm}} M1 = -r1  \\cdot F1 = M3}}$     
        ${{\hspace{{4mm}} {-d[0]:.0f}{{ \\text{{ m}}}} \\cdot F1 = {-((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*((d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} F1 = {(f[2]*(d[3]/d[0])*Calculations.sine(a[4]+a[8])):.2f}{{ \\text{{ N}}}}}}$     
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 

    Questionary(#3_1
        code = 2120031,
        no_pregunta = 3,
        complexity = M,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Encuentre la magnitud y dirección de una cuarta fuerza $F_4$ aplicada verticalmente a ${(d[0]*(3/5)):.2f} \\text{{ m}}$ desde A sobre el tramo AB, de manera que el momento generado por las cuatro fuerzas sea igual en los puntos A y B. Considere que $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$, $F_3 = {f[2]:.0f} \\text{{ N}}$, $\\alpha_1 = {a[0]:.0f}°$, $\\alpha_2 = {a[4]:.0f}°$,  $\\beta = {a[8]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ m}}$ y $X_2 = {d[3]:.0f}  \\text{{ m}}$.",
        no_answers = 1,
        a1_name = "Fuerza $F_4 [N]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[2]*calc['sin5']-f[0]-f[1]*calc['sin1'],2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP2,      
        ayuda3 = MP3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para resolver este problema, se igualan los momentos generados por las cuatro fuerzas en los puntos A y B. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Descomposición de las fuerzas del problema:}}$

        $\\underline{{Fuerza \\hspace{{2mm}} F1:}}$ La fuerza $F_1$ solo tiene componente en Y y es igual a su magnitud. 
        
        $\\underline{{Fuerza \\hspace{{2mm}} F2:}}$ 

        ${{\hspace{{4mm}} F_{{2x}} = |\\overrightarrow{{F_2}}| \\cdot \\cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ N}}}}}}$      
        ${{\hspace{{4mm}} F_{{2y}} = |\\overrightarrow{{F_2}}| \\cdot sen(\\alpha_1) = {f[1]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ N}}}}}}$       

        $\\underline{{Fuerza \\hspace{{2mm}} F3:}}$ 
        
        ${{\hspace{{4mm}} F_{{3x}} = |\\overrightarrow{{F_3}}| \\cdot \\cos(\\alpha_2) = {f[2]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['cos5']:.2f} = {f[2]*calc['cos5']:.2f}{{ \\text{{ N}}}}}}$     
        ${{\hspace{{4mm}} F_{{3y}} = |\\overrightarrow{{F_3}}| \\cdot \\sin(\\alpha_2) = {f[2]:.0f}{{\\text{{ N }} \\cdot\\hspace{{1mm}}}}{calc['sin5']:.2f} = {f[2]*calc['sin5']:.2f}{{ \\text{{ N}}}}}}$      
        
        $\\underline{{Fuerza \\hspace{{2mm}} F4:}}$ En este ejercicio se asume que la fuerza tiene dirección positiva en Y. Si el resultado muestra que la fuerza es negativa, significa que la suposición es incorrecta y la fuerza tiene dirección negativa en Y.
    
        $\\textbf{{\\small 2. Sumatoria de Momentos en los puntos A y B:}}$ 
        
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} momentos \\hspace{{2mm}} en \\hspace{{2mm}} A:}}$ 

        En el punto A, las fuerzas $F_4$, $F_3$ y la componente en Y de la fuerza $F_2$ generan momento.
        
        ${{\hspace{{4mm}} M_A = F_4 \\cdot  {(d[0]*(3/5)):.2f} \\text{{ m}} + |\\overrightarrow{{F_2}}| \\cdot \\sin(\\alpha_1) \\cdot X_1 - |\\overrightarrow{{F_3}}| \\cdot \\cos(\\alpha_2) \\cdot x_2 \\cdot \\sin(\\beta) - |\\overrightarrow{{F_3}}| \\cdot \\cos(\\alpha_2) \\cdot (X_1 + X_2 \\cdot \\cos(\\beta))}}$     
        ${{\hspace{{4mm}} M_A = F_4 \\cdot  {(d[0]*(3/5)):.2f} \\text{{ m}} + {f[1]*calc['sin1']:.2f}{{\\text{{ N}}}} \\cdot\\hspace{{1mm}} {(d[0]):.0f}{{ \\text{{ m}}}} - {f[2]*calc['cos5']:.2f}{{\\text{{ N}}}} \\cdot \\hspace{{1mm}} {(d[3]*calc['sin9']):.2f}{{ \\text{{ m}}}} - {f[2]*calc['sin5']:.2f}{{\\text{{ N}}}} \\cdot\\hspace{{1mm}}{d[0]+(d[3]*calc['cos9']):.2f}{{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} M_A = F_4 \\cdot  {(d[0]*(3/5)):.2f} \\text{{ m}} + {(f[1]*calc['sin1']*(d[0])):.2f}{{\\text{{ N}} \\cdot \\text{{m}}}} - {((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$    
        ${{\hspace{{4mm}} M_A = F_4 \\cdot  {(d[0]*(3/5)):.2f} \\text{{ m}} + ( {((f[1]*calc['sin1']*(d[0]))-((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9']))))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}} ) }}$    
        
       $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} momentos \\hspace{{2mm}} en \\hspace{{2mm}} B:}}$ 
        
        En el punto B, las fuerzas $F_4$, $F_3$ y $F_1$ generan momento.
        
        ${{\hspace{{4mm}} M_B = -F_4 \\cdot  ( X_1 - {(d[0]*(3/5)):.2f}) \\text{{ m}} - |\\overrightarrow{{F_1}}| \\cdot X_1 - |\\overrightarrow{{F_3}}| \\cdot \\cos(\\alpha_2) \\cdot x_2 \\cdot \\sin(\\beta) - |\\overrightarrow{{F_3}}| \\cdot \\cos(\\alpha_2) \\cdot (X_2 \\cdot \\cos(\\beta))}}$     
        ${{\hspace{{4mm}} M_B = -F_4 \\cdot  {(d[0]*(2/5)):.2f} \\text{{ m}} - {f[0]:.0f}{{\\text{{ N}}}} \\cdot \\hspace{{1mm}} {(d[0]):.0f}{{ \\text{{ m}}}}  {f[2]*calc['cos5']:.2f}{{\\text{{ N}}}} \\cdot \\hspace{{1mm}} {(d[3]*calc['sin9']):.2f}{{ \\text{{ m}}}} - {f[2]*calc['sin5']:.2f}{{\\text{{ N}}}} \\cdot\\hspace{{1mm}}{(d[3]*calc['cos9']):.2f}{{ \\text{{ m}}}}}}$    
        ${{\hspace{{4mm}} M_B = -F_4 \\cdot  {(d[0]*(2/5)):.2f} \\text{{ m}} - {(f[0]*(d[0])):.2f}{{\\text{{ N}} \\cdot \\text{{m}}}} - {((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*((d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$        
        ${{\hspace{{4mm}} M_B = -F_4 \\cdot  {(d[0]*(2/5)):.2f} \\text{{ m}} - {(f[0]*(d[0]))+((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*((d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$      
        
        $\\textbf{{\\small 3. Igualamos y despejamos para F4: }}$ 
        
        ${{\hspace{{4mm}} M_A = M_B }}$     
        ${{\hspace{{4mm}} F_4 \\cdot  {(d[0]*(3/5)):.2f} \\text{{ m}} + ( {((f[1]*calc['sin1']*(d[0]))-((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9']))))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}} ) \\text{{ = }} -F4 \\cdot  {(d[0]*(2/5)):.2f} \\text{{ m}} - {(f[0]*(d[0]))+((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*((d[3]*calc['cos9'])))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} F_4 \\cdot  {(d[0]):.2f} \\text{{ m}} = {-((f[1]*calc['sin1']*(d[0]))-((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*(d[0]+(d[3]*calc['cos9'])))))-((f[0]*(d[0]))+((f[2]*calc['cos5']*(d[3]*calc['sin9']))+(f[2]*calc['sin5']*((d[3]*calc['cos9']))))):.2f}{{\\text{{ N}} \\cdot\\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} F_4 = {f[2]*calc['sin5']-f[0]-f[1]*calc['sin1']:.2f} \\text{{ N}}}}$      
        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_1
        code = 2120041,
        no_pregunta = 4,
        complexity = M,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"""
        Calcule la suma de momentos alrededor del origen $\\textit{{O}}$ de las siguientes fuerzas:
        - La fuerza $\\overrightarrow{{F_1}} = [ {m[0]:.0f}\\hat{{i}} +  {m[3]:.0f}  \\hat{{j}} ] {{ \\text{{ kN}}}}$, que actúa en el punto $A$ con el vector posición $\\overrightarrow{{r_a}} = [ {d[0]:.0f}\\hat{{i}} +  {d[3]:.0f} \\hat{{j}} ]{{ \\text{{ m}}}}$ respecto al origen.
        - La fuerza $\\overrightarrow{{F_2}} = [ {m[4]:.0f}\\hat{{i}} +  {m[1]:.0f}  \\hat{{j}} ] {{ \\text{{ kN}}}}$, que actúa en el punto $B$ con el vector posición $\\overrightarrow{{r_b}} = [ {d[6]:.0f} \\hat{{i}} + {d[9]:.0f}\\hat{{j}} ]{{ \\text{{ m}}}}$ respecto al origen.
        """,
        no_answers = 1,
        a1_name = "Momento en el origen $[kN \\cdot m]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((d[0]*m[3]-d[3]*m[0]) + (d[6]*m[1]-d[9]*m[4]),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP5,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. A continuación, se presenta la solución sugerida:  

        En el ejercicio planteado, se proporcionan las componentes de las fuerzas y de sus repectivos vectores de posición, lo cual permite calcular el momento resultante con respecto al origen utilizando el producto cruz entre cada vector de posición y su correspondiente vector de fuerza. Dado que el análisis se realiza en el plano bidimensional, el momento resultante tendrá una única componente en la dirección $\\hat{{k}}$, perpendicular al plano, se determina multiplicando las componentes perpendiculares entre sí del vector fuerza y del vector posición, tal que:
                
        $\\textbf{{\\small 1. Momento causado por F1:}}$
        
        ${{\hspace{{4mm}} M_1 = \\overrightarrow{{r_x}} \\cdot \\overrightarrow{{F1_y}} - \\overrightarrow{{r_y}} \\cdot \\overrightarrow{{F1_x}} = ( {d[0]:.0f}{{ \\text{{ m }}}}\\cdot {m[3]:.0f}{{ \\text{{ kN }}}} ) - ( {d[3]:.0f}{{ \\text{{ m }}}}\\cdot {m[0]:.0f}{{ \\text{{ kN}}}} )}}$     
        ${{\hspace{{4mm}} M_1 = {(d[0]*m[3]-d[3]*m[0]):.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$    
        
        $\\textbf{{\\small 2. Momento causado por F2:}}$
        
        ${{\hspace{{4mm}} M_2 = \\overrightarrow{{r_x}} \\cdot \\overrightarrow{{F2_y}} - \\overrightarrow{{r_y}} \\cdot \\overrightarrow{{F2_x}} = ( {d[6]:.0f}{{ \\text{{ m }}}} \\cdot {m[1]:.0f}{{ \\text{{ kN }}}} ) - ( {d[9]:.0f}{{ \\text{{ m}}}}\\cdot {m[4]:.0f}{{ \\text{{ kN}}}} )}}$     
        ${{\hspace{{4mm}} M_2 = {(d[6]*m[1]-d[9]*m[4]):.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$
        
        $\\textbf{{\\small 3. Sumatoria de momentos:}}$ 
        
        ${{\hspace{{4mm}} M_O = M_1 + M_2 = {(d[0]*m[3]-d[3]*m[0]):.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}} + ({(d[6]*m[1]-d[9]*m[4]):.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}})}}$      
        ${{\hspace{{4mm}} M_O = {(d[0]*m[3]-d[3]*m[0]) + (d[6]*m[1]-d[9]*m[4]):.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$      
                   
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    
    #========================================================  MOMENTO  =========================================================
    #--------------------------------------------     Momento en un punto en 2D      --------------------------------------------
    #-------------------------------------------------       Nivel dificil     ---------------------------------------------------
    #-------------------------------------------------       Code: 2130011    ---------------------------------------------------

    Questionary(#1_1
        code = 2130011,
        no_pregunta = 1,
        complexity = D,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Si el trabajador ubicado en B ejerce una fuerza  $F_2 = {f[1]:.0f} \\text{{ kN}}$ sobre su cuerda, determine la magnitud de la fuerza $F_1$ que debe aplicar el trabajador en C para evitar que el poste gire. Se sabe que $\\alpha_1 = {a[0]:.0f}°$, $\\alpha_2 = {a[4]:.0f}°$, $Y_1 = {d[0]:.0f} \\text{{ m}}$ y $Y_2 = {d[3]/2:.1f}  \\text{{ m}}$.",
        no_answers = 1,
        a1_name = "Fuerza $F_1$ $[kN]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[1]*calc['cos5']*(d[0]+d[3]/2))/(d[0]*calc['sin1']),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP2,      
        ayuda3 = MP3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para que el poste no gire, es necesario que la suma de momentos en el punto A sea igual a cero, garantizando así que el sistema está en equilibrio. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Descomposición de las fuerzas:}}$

        $\\underline{{Fuerza  \\hspace{{2mm}} F1:}}$ 
        
        ${{\hspace{{4mm}} |F_{{1x}}| = |\\overrightarrow{{F_1}}| \\cdot \\sin(\\alpha_1)}}$       
        ${{\hspace{{4mm}} |F_{{1y}}| = |\\overrightarrow{{F_1}}| \\cdot \\cos(\\alpha_1)}}$       

        $\\underline{{Fuerza  \\hspace{{2mm}} F2:}}$ 

        ${{\hspace{{4mm}} |F_{{2x}}| = |\\overrightarrow{{F_2}}| \\cdot \\cos(\\alpha_2) = {f[1]:.0f}{{\\text{{ kN }} \\cdot\\hspace{{1mm}}}}{calc['cos5']:.2f} = {f[1]*calc['cos5']:.2f}{{ \\text{{ kN}}}}}}$      
        ${{\hspace{{4mm}} |F_{{2y}}| = |\\overrightarrow{{F_2}}| \\cdot \\sin(\\alpha_2) = {f[1]:.0f}{{\\text{{ kN }} \\cdot\\hspace{{1mm}}}}{calc['sin5']:.2f} = {f[1]*calc['sin5']:.2f}{{ \\text{{ kN}}}}}}$      

        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        ${{\hspace{{4mm}} r_1 \\text{{ = }} Y_1 = {d[0]:.0f}{{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} r_2 \\text{{ = }} Y_1 + Y_2 = {(d[0]+d[3])/2:.0f}{{ \\text{{ m}}}}}}$  
        
        $\\textbf{{\\small 3. Cálculo de los momentos generados por F1 y F2:}}$ 

        $\\underline{{Momento \\hspace{{2mm}} Fuerza \\hspace{{2mm}} F1:}}$ 

        La componente perpendicular al vector posición asociado $r_1$ es $F_{{1x}}$. Por la Regla de la mano de derecha el momento es negativo (sentido horario).

        ${{\hspace{{4mm}} M_{{1A}} = - r_1 \\cdot |\\overrightarrow{{F_1}}| \\cdot \\sin(\\alpha_1) = - {d[0]:.0f}{{ \\text{{ m}}}} \\cdot |\\overrightarrow{{F_1}}| \\cdot {calc['sin1']:.2f}}}$
        
        $\\underline{{Momento \\hspace{{2mm}} Fuerza \\hspace{{2mm}} F2:}}$ 

        La componente de la fuerza que es perpendicular al vector posición es $F_{{2x}}$. De acuerdo con la regla de la mano de derecha el momento es positivo (sentido antihorario). 

        ${{\hspace{{4mm}} M_{{2A}} = \\overrightarrow{{r_2}} X \\overrightarrow{{F_2}} = r2 \\cdot\\hspace{{1mm}} F2_y = {(d[0]+d[3]/2):.0f}{{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['cos5']:.2f}{{\\text{{ kN}}}}}}$     
        ${{\hspace{{4mm}} M_{{2A}} = {(f[1]*calc['cos5']*(d[0]+d[3]/2)):.2f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$    
        
        $\\textbf{{\\small 4. Sumatoria de momentos en A: }}$ 

        Se plantea la condición de equilibrio al igualar la sumatoria de momentos en A a 0.
        
        ${{\hspace{{4mm}} \\sum M_A = M_{{1A}} + M_{{2A}} = 0}}$      

        ${{\hspace{{4mm}} - {d[0]:.0f}{{ \\text{{ m}}}} \\cdot |\\overrightarrow{{F_1}}| \\cdot {calc['sin1']:.2f} + {(f[1]*calc['cos5']*(d[0]+d[3]/2)):.2f}{{\\text{{ kN}} \\cdot \\text{{ m}}}} = 0}}$

        ${{\hspace{{4mm}} {d[0]*calc['sin1']:.2f}{{ \\text{{ m}}}} \\cdot |\\overrightarrow{{F_1}}| = {(f[1]*calc['sin5']*(d[0]+d[3]/2)):.2f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$     

        ${{\hspace{{4mm}} |\\overrightarrow{{F_1}}| = \\dfrac{{{(f[1]*calc['cos5']*(d[0]+d[3]/2)):.2f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}{{{d[0]*calc['sin1']:.2f}{{ \\text{{ m}}}}}}}}$     

        ${{\hspace{{4mm}} |\\overrightarrow{{F_1}}| = {(f[1]*calc['cos5']*(d[0]+d[3]/2))/(d[0]*calc['sin1']):.2f}{{ \\text{{ kN}}}}}}$     
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 

    Questionary(#2_1
        code = 2130021,
        no_pregunta = 2,
        complexity = D,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Si el trabajador ubicado en B ejerce una fuerza  $F_2 = {f[1]/2:.1f} \\text{{ kN}}$ sobre su cuerda, y el que está ubicado en C aplica otra fuerza $F_1 = {f[1]*2:.0f} \\text{{ kN}}$, determine la magnitud de la distancia a la que debe aplicarse la fuerza F1, de forma que el poste no gire. Se conoce que $\\alpha_1 = {a[4]:.0f}°$, $\\alpha_2 = {a[0]:.0f}°$ y $Y_2 = {d[3]/2:.1f}  \\text{{ m}}$.",
        no_answers = 1,
        a1_name = "Distancia $Y_1$ $[m]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((f[1]*0.5*calc['cos1']*(d[3])/2)/(f[1]*2*calc['sin5']-f[1]*0.5*calc['cos1'])),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP2,      
        ayuda3 = MP3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector posición $\\overrightarrow{{r}}$. A continuación, se presenta la solución sugerida para el ejercicio:

        Inicialmente, observamos que para que la condición del enunciado se cumpla es necesario que la suma de momentos en A sea igual a cero.
        
        $\\textbf{{\\small 1. Descomposición de las fuerzas:}}$

        $\\underline{{Fuerza  \\hspace{{2mm}} F1 :}}$ 
        
        ${{\hspace{{4mm}} |F1_x| = |\\overrightarrow{{F1}}| \\cdot \\sin(\\alpha_1) = {f[1]*2:.0f}{{\\text{{ kN }} \\cdot\\hspace{{1mm}}}}{calc['sin5']:.2f} = {f[1]*2*calc['sin5']:.2f}{{ \\text{{ kN}}}}}}$             
        ${{\hspace{{4mm}} |F1_y| = |\\overrightarrow{{F1}}| \\cdot \\cos(\\alpha_1) = {f[1]*2:.0f}{{\\text{{ kN }} \\cdot\\hspace{{1mm}}}}{calc['cos5']:.2f} = {f[1]*2*calc['cos5']:.2f}{{ \\text{{ kN}}}}}}$            

        $\\underline{{Fuerza  \\hspace{{2mm}} F2 :}}$ 

        ${{\hspace{{4mm}} |F2_x| = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_2) = {f[1]*0.5:.0f}{{\\text{{ kN }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*0.5*calc['cos1']:.2f}{{ \\text{{ kN}}}}}}$      
        ${{\hspace{{4mm}} |F2_y| = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_2) = {f[1]*0.5:.0f}{{\\text{{ kN }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*0.5*calc['sin1']:.2f}{{ \\text{{ kN}}}}}}$      

        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        ${{\hspace{{4mm}} r1 \\text{{ = }} Y_1 }}$     
        ${{\hspace{{4mm}} r2 \\text{{ = }} Y_1 + Y_2 = Y_1 + {(d[3])/2:.0f}{{ \\text{{ m}}}}}}$  
        
        $\\textbf{{\\small 3.1 Momento de la fuerza F1: }}$ 

        Para calcular el momento de F1 en A vemos que la componente perpendicular al vector posición asociado r1 es $F1_x$, y que por la $\\textit{{Regla de la mano de derecha}}$ el momento sera negativo. Tal que: 

        ${{\hspace{{4mm}} M1_A = - r1 \\cdot |\\overrightarrow{{F1}}| \\cdot \\sin(\\alpha_1) = - Y_1 \\cdot {f[1]*2*calc['sin5']:.2f}{{ \\text{{ kN}}}}}}$
        
        $\\textbf{{\\small 3.2 Momento de la fuerza F2: }}$ 

        En el momento de la fuerza F2, notamos que la componente de la fuerza que es perpendicular al vector posición es $F2_x$, y por la $\\textit{{Regla de la mano de derecha}}$ el momento es positivo. Tal que podemos considerar: 

        ${{\hspace{{4mm}} M2_A = \\overrightarrow{{r_2}} X \\overrightarrow{{F2}} = r2 \\cdot\\hspace{{1mm}} F2_x = ( Y_1 + {(d[3])/2:.0f} ){{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[1]*0.5*calc['cos1']:.2f}{{\\text{{ kN}}}}}}$     
        ${{\hspace{{4mm}} M2_A = ( Y_1 \\cdot\\hspace{{1mm}}{f[1]*0.5*calc['cos1']:.2f}{{\\text{{ kN}}}} + {(f[1]*0.5*calc['cos1']*(d[3]))/2:.2f} ) {{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$    
        
        $\\textbf{{\\small 4. Sumatoria de momentos en A: }}$ 

        Hacemos sumatoria de momentos en A y la igualamos a cero: 
        
        ${{\hspace{{4mm}} \\sum M_A = M1_A + M2_A = 0}}$      
        ${{\hspace{{4mm}} - Y_1 \\cdot {f[1]*2*calc['sin5']:.2f}{{ \\text{{ kN}}}} + Y_1 \\cdot\\hspace{{1mm}}{f[1]*0.5*calc['cos1']:.2f}{{\\text{{ kN}}}} +{(f[1]*0.5*calc['cos1']*(d[3])/2):.2f}{{\\text{{ kN}} \\cdot \\text{{ m}}}} = 0}}$         
        ${{\hspace{{4mm}} Y_1 \\cdot ({f[1]*2*calc['sin5']:.2f}{{ \\text{{ kN}}}} - {f[1]*0.5*calc['cos1']:.2f}{{\\text{{ kN}}}}) = {(f[1]*0.5*calc['cos1']*(d[3])/2):.2f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} Y_1 = \\dfrac{{{(f[1]*0.5*calc['cos1']*(d[3])/2):.2f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}{{{f[1]*2*calc['sin5']-f[1]*0.5*calc['cos1']:.2f}{{\\text{{ kN}}}}}}}}$     
        ${{\hspace{{4mm}} Y_1 = {(f[1]*0.5*calc['cos1']*(d[3])/2)/(f[1]*2*calc['sin5']-f[1]*0.5*calc['cos1']):.2f}{{ \\text{{ m}}}}}}$     
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 2130031,
        no_pregunta = 3,
        complexity = D,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Si el trabajador ubicado en B ejerce una fuerza  $F_2 = {f[1]*2:.0f} \\text{{ kN}}$ sobre su cuerda, y el que está ubicado en C aplica otra fuerza $F_1 = {f[1]:.0f} \\text{{ kN}}$. Calcule el ángulo $\\alpha_2$ asociado a la fuerza $F2$ para evitar que el poste gire. Considere que $\\alpha_1 = {a[0]:.0f}°$, $Y_1 = {d[0]:.0f} \\text{{ m}}$  y $Y_2 = {d[3]:.0f}  \\text{{ m}}$.",
        no_answers = 1,
        a1_name = "Ángulo $\\alpha_2 [°]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(math.degrees(math.acos((d[0]*f[1]*calc['sin1'])/(f[1]*2*(d[0]+d[3])))),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP2,      
        ayuda3 = MP3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector posición $\\overrightarrow{{r}}$. A continuación, vamos a resolver el ejercicio usando esta definición:  

        Para que el poste no gire la sumatoria de momentos en A debe ser igual a cero.
        
        $\\textbf{{\\small 1. Descomposición de las fuerzas:}}$

        $\\underline{{Fuerza  \\hspace{{2mm}} F1 :}}$ 
        
        ${{\hspace{{4mm}} |F1_x| = |\\overrightarrow{{F1}}| \\cdot \\sin(\\alpha_1) = {f[1]:.0f}{{\\text{{ kN }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ kN}}}}}}$             
        ${{\hspace{{4mm}} |F1_y| = |\\overrightarrow{{F1}}| \\cdot \\cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ kN }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ kN}}}}}}$            

        $\\underline{{Fuerza  \\hspace{{2mm}} F2 :}}$ 

        ${{\hspace{{4mm}} |F2_x| = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_2) = {f[1]*2:.0f}{{\\text{{ kN }}}} \\cdot \\cos(\\alpha_2) }}$      
        ${{\hspace{{4mm}} |F2_y| = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_2) = {f[1]*2:.0f}{{\\text{{ kN }}}} \\cdot \\sin(\\alpha_2) }}$      

        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        ${{\hspace{{4mm}} r1 \\text{{ = }} X_1 = {d[0]:.0f}{{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} r2 \\text{{ = }} X_1 + X_2 = {(d[0]+d[3]):.0f}{{ \\text{{ m}}}}}}$      
        
        $\\textbf{{\\small 3.1 Momento de la fuerza F1: }}$ 

        ${{\hspace{{4mm}} M1_A = - r1 \\cdot |\\overrightarrow{{F1}}| \\cdot \\sin(\\alpha_1) = - {d[0]:.0f}{{ \\text{{ m}}}} \\cdot {f[1]*calc['sin1']:.2f}{{ \\text{{ kN}}}}}}$     
        ${{\hspace{{4mm}} M1_A = - {d[0]*f[1]*calc['sin1']:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$     
        
        $\\textbf{{\\small 3.2 Momento de la fuerza F2: }}$ 

        ${{\hspace{{4mm}} M2_A = \\overrightarrow{{r_2}} X \\overrightarrow{{F2}} = r2 \\cdot\\hspace{{1mm}} F2_x = {(d[0] + d[3]):.0f} {{ \\text{{ m}}}} \\cdot\\hspace{{1mm}}{f[1]*2:.0f}{{\\text{{ kN }}}} \\cdot \\cos(\\alpha_2)}}$     
        ${{\hspace{{4mm}} M2_A = ( \\cos(\\alpha_2)\\cdot\\hspace{{1mm}}{(f[1]*2*(d[0]+d[3])):.2f} ) {{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$    
        
        $\\textbf{{\\small 4. Sumatoria de momentos en A: }}$ 
        
        ${{\hspace{{4mm}} \\sum M_A = M1_A + M2_A = 0}}$      
        ${{\hspace{{4mm}}  - {d[0]*f[1]*calc['sin1']:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}} + ( \\cos(\\alpha_2)\\cdot\\hspace{{1mm}}{(f[1]*2*(d[0]+d[3])):.2f} ) {{\\text{{ kN}} \\cdot \\text{{ m}}}} = 0}}$         
        ${{\hspace{{4mm}} ( \\cos(\\alpha_2)\\cdot\\hspace{{1mm}}{(f[1]*2*(d[0]+d[3])):.2f} ) {{\\text{{ kN}} \\cdot \\text{{ m}}}} = {d[0]*f[1]*calc['sin1']:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}} }}$     
        ${{\hspace{{4mm}} \\cos(\\alpha_2) = \\left( \\dfrac{{{d[0]*f[1]*calc['sin1']:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}{{{(f[1]*2*(d[0]+d[3])):.2f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}} \\right) }}$     
        
        ${{\hspace{{4mm}} \\alpha_2 = Cos^{{-1}} \\left( \\dfrac{{{d[0]*f[1]*calc['sin1']:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}{{{(f[1]*2*(d[0]+d[3])):.2f} {{\\text{{ kN}} \\cdot \\text{{ m}}}}}} \\right) }}$
        
        ${{\hspace{{4mm}} \\alpha_2 = {math.degrees(math.acos((d[0]*f[1]*calc['sin1'])/(f[1]*2*(d[0]+d[3])))):.2f}°}}$     
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_1
        code = 2130041,
        no_pregunta = 4,
        complexity = D,
        topic = MO,
        subtopic = M2D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"La suma de momentos respecto al origen $\\textit{{O}}$ de las fuerzas $\\overrightarrow{{F_1}}$ y $\\overrightarrow{{F_2}}$ debe ser igual a cero. La fuerza $F_1$ actúa en el punto $A$, cuyo vector posición es $\\overrightarrow{{r_a}} = [ ({d[2]:.0f})\\hat{{i}} + ({(d[3]):.0f})\\hat{{j}} ]{{ \\text{{ m}}}}$ con respecto al origen. La fuerza $\\overrightarrow{{F_2}} = [ ({c[4]:.0f})\\hat{{i}} + ( {c[1]:.0f} ) \\hat{{j}} ] {{ \\text{{ kN}}}}$ actúa en el punto $B$, con vector posición $\\overrightarrow{{r_b}} = [( {d[8]:.0f} )\\hat{{i}} + ({d[11]:.0f})\\hat{{j}} ]{{ \\text{{ m}}}}$ con respecto al origen. Calcule la componente en $x$ de la fuerza $\\overrightarrow{{F_1}}$, sabiendo que su componente en $y$ es $\\overrightarrow{{F1_y}} = {c[3]:.0f}{{ \\text{{ kN}}}}$.",
        no_answers = 1,
        a1_name = "Componente en $x$ de $F_1$ $[kN \\cdot m]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((d[2]*c[3] + d[8]*c[1] - d[11]*c[4])/(d[3]),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP5,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. A continuación, se presenta la solución sugerida:  

        Se plantea la sumatoria de momentos respecto al origen $\\textit{{O}}$, igualada a cero y de esta ecuación se despeja $\\overrightarrow{{F1_x}}$:
        
        $\\textbf{{\\small 1. Momento causado por la fuerza 1:}}$
        
        ${{\hspace{{4mm}} M_1 = \\overrightarrow{{r_x}} \\cdot \\overrightarrow{{F1_y}} - \\overrightarrow{{r_y}} \\cdot \\overrightarrow{{F1_x}} = ( {d[2]:.0f}{{ \\text{{ m }}}} \\cdot {c[3]:.0f}{{ \\text{{ kN }}}} ) - ( {d[3]:.0f}{{ \\text{{ m }}}} \\cdot \\overrightarrow{{F1_x}} )}}$     
        ${{\hspace{{4mm}} M_1 = {d[2]*c[3]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}} - ( {d[3]:.0f}{{ \\text{{ m }}}} \\cdot \\overrightarrow{{F1_x}} ) }}$    
        
        $\\textbf{{\\small 2. Momento causado por la fuerza 2:}}$
        
        ${{\hspace{{4mm}} M_2 = \\overrightarrow{{r_x}} \\cdot \\overrightarrow{{F2_y}} - \\overrightarrow{{r_y}} \\cdot \\overrightarrow{{F2_x}} = ( {d[8]:.0f}{{ \\text{{ m }}}}  \\cdot {c[1]:.0f}{{ \\text{{ kN }}}} )  - ( {d[11]:.0f}{{ \\text{{ m }}}} \\cdot {c[4]:.0f}{{ \\text{{ kN}}}} )}}$     
        ${{\hspace{{4mm}} M_2 = {d[8]*c[1]-d[11]*c[4]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$
        
        $\\textbf{{\\small 3. Sumatoria de momentos:}}$ 
        
        ${{\hspace{{4mm}} M_O = M_1 + M_2 = ( {d[2]*c[3]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}} - ( {d[3]:.0f}{{ \\text{{ m }}}} \\cdot \\overrightarrow{{F1_x}} )  ) + ( {d[8]*c[1]-d[11]*c[4]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}} ) = 0 }}$      
        ${{\hspace{{4mm}} ( {d[3]:.0f}{{ \\text{{ m }}}} \\cdot \\overrightarrow{{F1_x}} ) = ( {d[2]*c[3]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}} ) + ( {d[8]*c[1]-d[11]*c[4]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}} )}}$      
        ${{\hspace{{4mm}} \\overrightarrow{{F1_x}} = \\dfrac{{{(d[2]*c[3] + d[8]*c[1] - d[11]*c[4]):.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}{{{d[3]:.0f}{{ \\text{{ m }}}}}}}}$          
        ${{\hspace{{4mm}} \\overrightarrow{{F1_x}} = {(d[2]*c[3] + d[8]*c[1] - d[11]*c[4])/(d[3]):.2f}{{ \\text{{ kN}}}}}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),


    #========================================================  MOMENTO  =========================================================
    #--------------------------------------------     Momento en un punto en 3D      --------------------------------------------
    #-------------------------------------------------       Nivel fácil    ---------------------------------------------------
    #-------------------------------------------------       Code: 2210011    ---------------------------------------------------
 
    Questionary(#1_1
        code = 2210011,
        no_pregunta = 1,
        complexity = F,
        topic = MO,
        subtopic = M3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el momento de la fuerza $F_1$ con respecto al origen y expréselo en forma de vector cartesiano. Considere que $F_1 = [ {d[9]:.0f}\\hat{{i}} + {d[12]:.0f} \\hat{{j}}  {d[1]:.0f} \\hat{{k}} ] \\text{{ kN}}$, $d_1 = {d[3]:.0f} \\text{{ m}}$,  $d_2 = {d[0]:.0f}  \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Componente $\\hat{{i}}$ del momento en el origen [$kN \\cdot m$]",
        a2_name = "Componente $\\hat{{j}}$ del momento en el origen [$kN \\cdot m$]",
        a3_name = "Componente $\\hat{{k}}$ del momento en el origen [$kN \\cdot m$]",
        answer1 = lambda f, a, calc, c, d, m: np.round(d[3]*d[1]+d[6]*d[12],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-(d[0]*d[1])-d[6]*d[9],2),
        answer3 = lambda f, a, calc, c, d, m: np.round((d[0]*d[12])-(d[3]*d[9]),2),
        ayuda1 = MP1,
        ayuda2 = MP4,      
        ayuda3 = MP5,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones, el cálculo del momento se facilita al resolver el producto cruz. A continuación, se muestra la solución sugerida para el ejercicio:      

        $\\textbf{{\\small 1. Definición del vector posición:}}$       
        
        ${{\hspace{{4mm}} r_x = d_2 = {d[0]:.0f}{{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} r_y = d_1 = {d[3]:.0f}{{ \\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} r_z = - d_3 = {-d[6]:.0f}{{ \\text{{ m}}}}}}$        

        $\\textbf{{\\small 2. Calculo del momento en el origen: }}$  

        Las ecuaciones del producto cruz por cada componente, pueden ser halladas con el siguiente método:
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\underline{{Componente \\hspace{{2mm}} \\hat{{i}} :}}$
        
        Aplicando el producto cruz, la componente $\\hat{{i}}$ del momento se puede calcular como:
        
        ${{\hspace{{4mm}} M_i = r_y \\cdot F_z - r_z \\cdot F_y = {d[3]:.0f}{{ \\text{{ m}}}} \\cdot ( {d[1]:.0f} ){{ \\text{{ kN}}}} - ( {-d[6]:.0f}{{ \\text{{ m}}}} ) \\cdot {d[12]:.0f}{{ \\text{{ kN}}}}}}$       
        ${{\hspace{{4mm}} M_i = ( {d[3]*d[1]:.0f} ){{ \\text{{ kN}}}} \\cdot {{ \\text{{ m}}}} - ( {-( d[6]*d[12]) :.0f} ) {{ \\text{{ kN}}}} \\cdot {{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} M_i = {d[3]*d[1]+d[6]*d[12]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$       
        
        $\\underline{{Componente \\hspace{{2mm}} \\hat{{j}} :}}$
        
        Aplicando el producto cruz, la componente $\\hat{{j}}$ del momento se puede calcular como:
        
        ${{\hspace{{4mm}} M_j = - ( r_x \\cdot F_z - r_z \\cdot F_x ) = -( {d[0]:.0f}{{ \\text{{ m}}}} \\cdot ( {d[1]:.0f} ){{ \\text{{ kN}}}} - ( {-d[6]:.0f}{{ \\text{{ m}}}} ) \\cdot {d[9]:.0f}{{ \\text{{ kN}}}} )}}$       
        ${{\hspace{{4mm}} M_j = ( {-(d[0]*d[1]):.0f} ){{ \\text{{ kN}}}} \\cdot {{ \\text{{ m}}}} - ( {d[6]*d[9]:.0f} ) {{ \\text{{ kN}}}} \\cdot {{ \\text{{ m}}}} }}$     
        ${{\hspace{{4mm}} M_j = {-(d[0]*d[1])-d[6]*d[9]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$      
        
        $\\underline{{Componente \\hspace{{2mm}} \\hat{{k}} :}}$
        
        Aplicando el producto cruz, la componente $\\hat{{k}}$ del momento se puede calcular como:
        
        ${{\hspace{{4mm}} M_k =  r_x \\cdot F_y - r_y \\cdot F_x  = {d[0]:.0f}{{ \\text{{ m}}}} \\cdot {d[12]:.0f} {{ \\text{{ kN}}}} - {d[3]:.0f}{{ \\text{{ m}}}} \\cdot {d[9]:.0f}{{ \\text{{ kN}}}}}}$       
        ${{\hspace{{4mm}} M_k =  {(d[0]*d[12]):.0f}{{ \\text{{ kN}}}} \\cdot {{ \\text{{ m}}}} - {d[3]*d[9]:.0f} {{ \\text{{ kN}}}} \\cdot {{ \\text{{ m}}}} }}$      
        ${{\hspace{{4mm}} M_k = {(d[0]*d[12])-d[3]*d[9]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$    
        
        Por lo tanto, el momento generado por $F_1$ en el origen es $ [ {d[3]*d[1]+d[6]*d[12]:.0f}\\hat{{i}} + ( {-(d[0]*d[1])-d[6]*d[9]:.0f}) \\hat{{j}} + ({(d[0]*d[12])-d[3]*d[9]:.0f})\\hat{{k}} ]{{ \\text{{ kN}}}} \\cdot {{ \\text{{ m}}}}$
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 2210021,
        no_pregunta = 2,
        complexity = F,
        topic = MO,
        subtopic = M3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de $d_1$ y $d_2$, si el momento en el origen generado por $F_1$ es $ [ {-m[0]:.0f}\\hat{{i}} + ( {-m[1]:.0f}) \\hat{{j}} + ({ (f[1]*m[1]+m[0]*f[0])/(-f[2]):.2f})\\hat{{k}} ]{{ \\text{{ kN}}}} \\cdot {{ \\text{{ m}}}}$. Considere que $F_1 = [ {f[0]:.0f}\\hat{{i}} + {f[1]:.0f} \\hat{{j}} + ( {-f[2]:.0f} ) \\hat{{k}} ] \\text{{ kN}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "$d_1$ $[m]$",
        a2_name = "$d_2$ $[m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((-m[0]-d[6]*f[1])/(-f[2]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((m[1]-d[6]*f[0])/(-f[2]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP5,      
        ayuda3 = MP6,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones, el cálculo del momento se facilita al resolver el producto cruz. A continuación, se muestra la solución sugerida para el ejercicio:      

        $\\textbf{{\\small 1. Obtención del vector posición:}}$       
        
        ${{\hspace{{4mm}} r_x = d_2}}$     
        ${{\hspace{{4mm}} r_y = d_1}}$      
        ${{\hspace{{4mm}} r_z = - d_3 = {-d[6]:.0f}{{ \\text{{ m}}}}}}$         

        $\\textbf{{\\small 2. Expresión de ecuaciones de la componentes de momento: }}$  

        Las ecuaciones del producto cruz por cada componente, pueden ser halladas con el siguiente método:
        """,    
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        ${{\hspace{{4mm}} M_i = d_1 \\cdot F_z - (-d_3) \\cdot F_y }}$     
        ${{\hspace{{4mm}} M_j = - (d_2 \\cdot F_z - (-d_3) \\cdot F_x)}}$     
        ${{\hspace{{4mm}} M_k = d_2 \\cdot F_y - d_1 \\cdot F_x }}$     
        
        Las anteriores ecuaciones se pueden resolver para determinar los valores de $d_1$ y $d_2$:
        
        $\\underline{{Despejar \\text{{ }} d_1 \\text{{ }} de \\text{{ }} la \\text{{ }} ecuación \\text{{ }} 1:}}$        
       
        ${{\hspace{{4mm}} {-m[0]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}} = d_1 \\cdot ( {-f[2]:.0f} ){{ \\text{{ kN}}}} - ( {-d[6]:.0f}{{ \\text{{ m}}}}) \\cdot {f[1]:.0f}{{ \\text{{ kN}}}}}}$       
        ${{\hspace{{4mm}} {-m[0]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}} -  {d[6]*f[1]:.0f} {{\\text{{ kN}} \\cdot \\text{{ m}}}} = d_1 \\cdot ( {-f[2]:.0f} ){{ \\text{{ kN}}}}}}$       
        ${{\hspace{{4mm}} d_1 = \\dfrac{{{-m[0]-d[6]*f[1]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}{{( {-f[2]:.0f} ){{ \\text{{ kN}}}}}}}}$      
        ${{\hspace{{4mm}} d_1 = {(-m[0]-d[6]*f[1])/(-f[2]):.2f}{{\\text{{ m}}}} }}$     
        
        $\\underline{{Despejar \\text{{ }} d_2 \\text{{ }} de \\text{{ }} la \\text{{ }} ecuación \\text{{ }} 2:}}$       
        
        ${{\hspace{{4mm}} {-m[1]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}} = - (d_2 \\cdot ( {-f[2]:.0f} ){{ \\text{{ kN}}}} - ({-d[6]:.0f}{{ \\text{{ m}}}}) \\cdot {f[0]:.0f}{{ \\text{{ kN}}}} )}}$       
        ${{\hspace{{4mm}} {m[1]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}} - {d[6]*f[0]:.0f}{{ \\text{{ kN}}}} = d_2 \\cdot ( {-f[2]:.0f} ){{ \\text{{ kN}}}}}}$       
        ${{\hspace{{4mm}} d_2 = \\dfrac{{{m[1]-d[6]*f[0]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}{{( {-f[2]:.0f} ){{ \\text{{ kN}}}}}}}}$      
        ${{\hspace{{4mm}} d_2 = {(m[1]-d[6]*f[0])/(-f[2]):.2f}{{ \\text{{ m}}}} }}$ 
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 2210021,
        no_pregunta = 3,
        complexity = F,
        topic = MO,
        subtopic = M3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de las componentes $\\hat{{i}}$ y $\\hat{{j}}$ de $F_1$ si el momento en el origen causado por esta fuerza es $ [ {-m[0]:.0f}\\hat{{i}} + ( {-m[1]:.0f}) \\hat{{j}} + ({ (d[0]*(-m[0])-m[1]*d[3])/(d[6]):.2f})\\hat{{k}} ]{{ \\text{{ kN}}}} \\cdot {{ \\text{{ m}}}}$. Considere que la componente $\\hat{{k}}$ de $F_1$ tiene un valor de ${-f[2]:.0f}\\text{{ kN}}$; y que $d_1 = {d[3]:.0f} \\text{{ m}}$,  $d_2 = {d[0]:.0f}  \\text{{ m}}$, $d_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Componente $\\hat{{i}}$ de $F_1$ $[kN]$",
        a2_name = "Componente $\\hat{{j}}$ de $F_1$ $[kN]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((m[1]+d[0]*f[2])/(d[6]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((-m[0]+d[3]*f[2])/(d[6]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP5,      
        ayuda3 = MP6,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones, el cálculo del momento se facilita al resolver el producto cruz. A continuación, se muestra la solución sugerida para el ejercicio:      

        $\\textbf{{\\small 1. Obtención del vector posición:}}$       
        
        ${{\hspace{{4mm}} r_x = d_2 = {d[0]:.0f}{{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} r_y = d_1 = {d[3]:.0f}{{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} r_z = - d_3 = {-d[6]:.0f}{{ \\text{{ m}}}}}}$         

        $\\textbf{{\\small 2. Expresión de ecuaciones de la componentes de momento: }}$ 

        Las ecuaciones del producto cruz por cada componente, pueden ser halladas con el siguiente método:
         
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        ${{\hspace{{4mm}} M_i = d_1 \\cdot F_z - (-d_3) \\cdot F_y }}$     
        ${{\hspace{{4mm}} M_j = - (d_2 \\cdot F_z - (-d_3) \\cdot F_x)}}$     
        ${{\hspace{{4mm}} M_k = d_2 \\cdot F_y - d_1 \\cdot F_x }}$     
        
        Las anteriores ecuaciones se pueden resolver para determinar los valores de $F_x$ y $F_y$:
        
        $\\underline{{Despejar \\text{{ }} F_x \\text{{ }} de \\text{{ }} la \\text{{ }} ecuación \\text{{ }} 2:}}$       
       
        ${{\hspace{{4mm}} {-m[1]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}} = - ({d[0]:.0f}{{ \\text{{ m}}}} \\cdot ( {-f[2]:.0f} ){{ \\text{{ kN}}}} - ({-d[6]:.0f}{{ \\text{{ m}}}}) \\cdot F_x )}}$       
        ${{\hspace{{4mm}} {m[1]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}} + {d[0]*f[2]:.0f}{{ \\text{{ m}}}} \\cdot \\text{{ kN}} = {d[6]:.0f}{{ \\text{{ m}}}} \\cdot F_x}}$       
        ${{\hspace{{4mm}} F_x = \\dfrac{{{m[1]+d[0]*f[2]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}{{( {d[6]:.0f} ){{ \\text{{ m}}}}}}}}$      
        ${{\hspace{{4mm}} F_x = {(m[1]+d[0]*f[2])/(d[6]):.2f}{{\\text{{ kN}}}}}}$     
        
        $\\underline{{Despejar \\text{{ }} F_y \\text{{ }} de \\text{{ }} la \\text{{ }} ecuación \\text{{ }} 1:}}$        
        
        ${{\hspace{{4mm}} {-m[0]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}} = {d[3]:.0f}{{ \\text{{ m}}}} \\cdot ( {-f[2]:.0f} ){{ \\text{{ kN}}}} - ( {-d[6]:.0f}{{ \\text{{ m}}}}) \\cdot F_y}}$       
        ${{\hspace{{4mm}} {-m[0]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}} +  {d[3]*f[2]:.0f} {{\\text{{ kN}} \\cdot \\text{{ m}}}} = {d[6]:.0f}{{ \\text{{ m}}}} \\cdot F_y}}$       
        ${{\hspace{{4mm}} F_y = \\dfrac{{{-m[0]+d[3]*f[2]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}{{( {d[6]:.0f} ){{ \\text{{ m}}}}}}}}$      
        ${{\hspace{{4mm}} F_y = {(-m[0]+d[3]*f[2])/(d[6]):.2f}{{\\text{{ kN}}}} }}$     
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_1
        code = 2210041,
        no_pregunta = 4,
        complexity = F,
        topic = MO,
        subtopic = M3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de los momentos en el punto $A$ generados por las fuerzas $F_1$ y $F_2$. Considere $F_1 = [ {f[0]:.0f}\\hat{{i}} + {f[1]:.0f} \\hat{{j}} + ( {-f[2]:.0f} ) \\hat{{k}} ] \\text{{ kN}}$, $F_2 = [ {-f[3]:.0f}\\hat{{i}} + {f[4]:.0f} \\hat{{j}} + ( {f[5]:.0f} ) \\hat{{k}} ] \\text{{ kN}}$, $d_1 = {d[3]:.0f} \\text{{ m}}$,  $d_2 = {d[0]:.0f}  \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Momento en A causado por $F_1$ [$kN \\cdot m$]",
        a2_name = "Momento en A causado por $F_2$ [$kN \\cdot m$]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D(d[6]*f[1],-d[6]*f[0],0),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D(0,-d[0]*f[5],-d[0]*f[4]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP4,      
        ayuda3 = MP5,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones, el cálculo del momento se facilita al resolver el producto cruz. A continuación, se muestra la solución sugerida para el ejercicio:     

        $\\textbf{{\\small 1. Obtención del vector posición:}}$   
        
        $\\underline{{Vector \\text{{ }} Posición \\text{{ }} r_1 \\text{{ }} asociado \\text{{ }} a \\text{{ }} la \\text{{ }} fuerza \\text{{ }} F_1: }}$         
        
        ${{\hspace{{4mm}} r_{{1x}} = 0 {{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} r_{{1y}} = 0 {{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} r_{{1z}} = - d_3 = {-d[6]:.0f}{{ \\text{{ m}}}}}}$        
        
        $\\underline{{Vector \\text{{ }} Posición \\text{{ }} r2 \\text{{ }} asociado \\text{{ }} a \\text{{ }} la \\text{{ }} fuerza \\text{{ }} F_2: }}$
        
        ${{\hspace{{4mm}} r_{{2x}} = - d_2 = {-d[0]:.0f}{{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} r_{{2y}} = 0 {{ \\text{{ m}}}}}}$     
        ${{\hspace{{4mm}} r_{{2z}} = 0 {{ \\text{{ m}}}}}}$       

        $\\textbf{{\\small 2. Calculo del momento en A de F1: }}$  
        
        $\\underline{{Componente \\text{{ }} \\hat{{i}} :}}$
        
        Aplicando el producto cruz, la componente $\\hat{{i}}$ del momento se puede calcular como:
        
        ${{\hspace{{4mm}} M_{{1i}} = r_y \\cdot F_z - r_z \\cdot F_y = 0 {{ \\text{{ m}}}} \\cdot ( {-f[2]:.0f} ){{ \\text{{ kN}}}} - ( {-d[6]:.0f}{{ \\text{{ m}}}} ) \\cdot {f[1]:.0f}{{ \\text{{ kN}}}}}}$          
        ${{\hspace{{4mm}} M_{{1i}} = {d[6]*f[1]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$       
        
        $\\underline{{Componente \\text{{ }} \\hat{{j}} :}}$
        
        Aplicando el producto cruz, la componente $\\hat{{j}}$ del momento se puede calcular como:
        
        ${{\hspace{{4mm}} M_{{1j}} = - ( r_x \\cdot F_z - r_z \\cdot F_x ) = -( 0 {{ \\text{{ m}}}} \\cdot ( {-f[2]:.0f} ){{ \\text{{ kN}}}} - ( {-d[6]:.0f}{{ \\text{{ m}}}} ) \\cdot {f[0]:.0f}{{ \\text{{ kN}}}} )}}$           
        ${{\hspace{{4mm}} M_{{1j}} = {-d[6]*f[0]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$      
        
        $\\underline{{Componente \\text{{ }} \\hat{{k}} :}}$
        
        Aplicando el producto cruz, la componente $\\hat{{k}}$ del momento se puede calcular como:
        
        ${{\hspace{{4mm}} M_{{1k}} =  r_x \\cdot F_y - r_y \\cdot F_x  = 0 {{ \\text{{ m}}}} \\cdot {f[1]:.0f} {{ \\text{{ kN}}}} - 0 {{ \\text{{ m}}}} \\cdot {f[0]:.0f}{{ \\text{{ kN}}}}}}$         
        ${{\hspace{{4mm}} M_{{1k}} = 0 {{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$     
        
        $\\underline{{Magnitud \\text{{ }} del \\text{{ }} momento \\text{{ }} causado \\text{{ }} por \\text{{ }} F_1:}}$
        
        ${{\hspace{{4mm}} |M_1| = \\sqrt{{ ({d[6]*f[1]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}})^{{2}} + ({-d[6]*f[0]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}})^{{2}} }} }}$     
        ${{\hspace{{4mm}} |M_1| = {Calculations.magnitude3D(d[6]*f[1],-d[6]*f[0],0):.2f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$     
        
        $\\textbf{{\\small 3. Calculo del momento en A de F2: }}$  
        
        $\\underline{{Componente \\text{{ }} \\hat{{i}} :}}$
        
        Aplicando el producto cruz, la componente $\\hat{{i}}$ del momento se puede calcular como:
        
        ${{\hspace{{4mm}} M_{{2i}} = r_y \\cdot F_z - r_z \\cdot F_y = 0 {{ \\text{{ m}}}} \\cdot ( {f[5]:.0f} ){{ \\text{{ kN}}}} - 0 \\cdot {f[4]:.0f}{{ \\text{{ kN}}}}}}$          
        ${{\hspace{{4mm}} M_{{2i}} = 0 {{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$       
        
        $\\underline{{Componente \\text{{ }} \\hat{{j}} :}}$
        
        Aplicando el producto cruz, la componente $\\hat{{j}}$ del momento se puede calcular como:
        
        ${{\hspace{{4mm}} M_{{2j}} = - ( r_x \\cdot F_z - r_z \\cdot F_x ) = -( {-d[0]:.0f} {{ \\text{{ m}}}} \\cdot ( {f[5]:.0f} ){{ \\text{{ kN}}}} - 0 {{ \\text{{ m}}}} \\cdot ( {-f[3]:.0f}{{ \\text{{ kN}}}} ) )}}$           
        ${{\hspace{{4mm}} M_{{2j}} = {d[0]*f[5]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$      
        
        $\\underline{{Componente \\text{{ }} \\hat{{k}} :}}$
        
        Aplicando el producto cruz, la componente $\\hat{{k}}$ del momento se puede calcular como:
        
        ${{\hspace{{4mm}} M_{{2k}} =  r_x \\cdot F_y - r_y \\cdot F_x  = {-d[0]:.0f} {{ \\text{{ m}}}} \\cdot {f[4]:.0f} {{ \\text{{ kN}}}} - 0 {{ \\text{{ m}}}} \\cdot ( {-f[3]:.0f}{{ \\text{{ kN}}}} )}}$    
        ${{\hspace{{4mm}} M_{{2k}} = {-d[0]*f[4]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$     
        
        $\\underline{{Magnitud \\text{{ }} del \\text{{ }} momento \\text{{ }} causado \\text{{ }} por \\text{{ }} F_2:}}$
        
        ${{\hspace{{4mm}} |M_2| = \\sqrt{{ ({d[0]*f[5]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}})^{{2}} + ({-d[0]*f[4]:.0f}{{\\text{{ kN}} \\cdot \\text{{ m}}}})^{{2}} }} }}$               
        ${{\hspace{{4mm}} |M_2| = {Calculations.magnitude3D(0,d[0]*f[5],d[0]*f[4]):.2f}{{\\text{{ kN}} \\cdot \\text{{ m}}}} }}$       
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    
    #========================================================  MOMENTO  =========================================================
    #--------------------------------------------     Momento en un punto en 3D      --------------------------------------------
    #-------------------------------------------------       Nivel medio    ---------------------------------------------------
    #-------------------------------------------------       Code: 2220011    --------------------------------------------------
    
    Questionary(#1_1
        code = 2220011,
        no_pregunta = 1,
        complexity = M,
        topic = MO,
        subtopic = M3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule el momento resultante generado por las tres fuerzas en el origen y expréselo en forma de vector cartesiano. Considere que $F_1 = [{f[0]:.0f}\\hat{{i}} + {f[1]:.0f} \\hat{{j}} {-f[2]:.0f}\\hat{{k}}]\\text{{ N}}$, $F_2 = [{-f[3]:.0f}\\hat{{i}} + {f[4]:.0f} \\hat{{j}} + {f[5]:.0f}\\hat{{k}}]\\text{{ N}}$, $F_3 = [{f[6]:.0f}\\hat{{i}} {-f[7]:.0f}\\hat{{j}} + {f[8]:.0f}\\hat{{k}}]\\text{{ N}}$, $d_1 = {d[3]:.0f} \\text{{ m}}$,  $d_2 = {d[0]:.0f}  \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Componente $\\hat{{i}}$ del momento en el origen [$N \\cdot m$]",
        a2_name = "Componente $\\hat{{j}}$ del momento en el origen [$N \\cdot m$]",
        a3_name = "Componente $\\hat{{k}}$ del momento en el origen [$N \\cdot m$]",
        answer1 = lambda f, a, calc, c, d, m: np.round(d[3]*(-f[2]) + d[3]*(f[5]) + d[3]*f[8] - d[6]*(-f[7]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(d[0]*f[2] + d[6]*f[6]-d[0]*f[8],2),
        answer3 = lambda f, a, calc, c, d, m: np.round(d[0]*f[1]-d[3]*f[0] + d[3]*f[3] - d[0]*f[7]-d[3]*f[6],2),
        ayuda1 = MP1,
        ayuda2 = MP4,
        ayuda3 = "Se puede dividir el problema en componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$, y resolver de manera independiente las componentes del momento.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones, el cálculo del momento se facilita al resolver el producto cruz. A continuación, se muestra la solución sugerida para el ejercicio:      

        $\\textbf{{\\small 1. Calculo del momento en el origen causado por F1: }}$  
        
        ${{\hspace{{4mm}} M_1 = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_1 = ({d[3]:.0f}{{\\text{{ m}}}} \\cdot ({-f[2]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[1]:.0f} {{\\text{{ N}}}})\\hat{{i}} - ({d[0]:.0f}{{\\text{{ m}}}} \\cdot ({-f[2]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[0]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ({d[0]:.0f}{{\\text{{ m}}}} \\cdot {f[1]:.0f} {{\\text{{ N}}}} - {d[3]:.0f}{{\\text{{ m}}}} \\cdot {f[0]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_1 = [ ({d[3]*(-f[2]):.0f})\\hat{{i}} + ({d[0]*f[2]:.0f})\\hat{{j}} + ({d[0]*f[1]-d[3]*f[0]:.0f})\\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$ 
        
        $\\textbf{{\\small 2. Calculo del momento en el origen causado por F2: }}$  
        
        ${{\hspace{{4mm}} M_2 = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_2 = ({d[3]:.0f}{{\\text{{ m}}}} \\cdot {f[5]:.0f} {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[4]:.0f} {{\\text{{ N}}}})\\hat{{i}} - ( 0 {{\\text{{ m}}}} \\cdot ({f[5]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot ({-f[3]:.0f}) {{\\text{{ N}}}})\\hat{{j}} + ( 0 {{\\text{{ m}}}} \\cdot {f[4]:.0f} {{\\text{{ N}}}} - {d[3]:.0f}{{\\text{{ m}}}} \\cdot ({-f[3]:.0f}) {{\\text{{ N}}}})\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_2 = [ ({d[3]*(f[5]):.0f})\\hat{{i}} + 0\\hat{{j}} + ({d[3]*f[3]:.0f})\\hat{{k}} ] {{ \\text{{ N}} \\cdot \\text{{ m}}}} }}$
        
        $\\textbf{{\\small 3. Calculo del momento en el origen causado por F3: }}$  
        
        ${{\hspace{{4mm}} M_3 = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_3 = ({d[3]:.0f}{{\\text{{ m}}}} \\cdot {f[8]:.0f}{{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}})\\hat{{i}} - ({d[0]:.0f}{{\\text{{ m}}}} \\cdot {f[8]:.0f} {{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ({d[0]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}} - {d[3]:.0f}{{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_3 = [ ({d[3]*f[8] + d[6]*f[7]:.0f})\\hat{{i}} - ({d[0]*f[8]-d[6]*f[6]:.0f})\\hat{{j}} - ({d[0]*(f[7])+d[3]*f[6]:.0f})\\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$
        
        $\\textbf{{\\small 4. Sumatoria de momentos en el origen: }}$

        ${{\hspace{{4mm}} \\sum{{M_O}} = [({d[3]*(-f[2]):.0f} + {d[3]*(f[5]):.0f} + {d[3]*f[8] - d[6]*(-f[7]):.0f})\\hat{{i}} + ({d[0]*f[2]:.0f} + 0 + ({d[6]*f[6]-d[0]*f[8]:.0f}))\\hat{{j}} + ({d[0]*f[1]-d[3]*f[0]:.0f} + {d[3]*f[3]:.0f} + ({d[0]*(-f[7])-d[3]*f[6]:.0f}))\\hat{{k}}]{{\\text{{ N}} \\cdot \\text{{ m}}}} }}$      
        ${{\hspace{{4mm}} \\sum{{M_O}} = [({d[3]*(-f[2]) + d[3]*(f[5]) + d[3]*f[8] - d[6]*(-f[7]):.2f})\\hat{{i}} + ({d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f})\\hat{{j}} + ({d[0]*f[1]-d[3]*f[0] + d[3]*f[3] - d[0]*f[7]-d[3]*f[6]:.2f})\\hat{{k}}] {{\\text{{ N}} \\cdot \\text{{ m}}}} }}$      
              
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 2220021,
        no_pregunta = 2,
        complexity = M,
        topic = MO,
        subtopic = M3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las componentes  $\\hat{{j}}$ y $\\hat{{k}}$ de la fuerza $F_2$ si la sumatoria de momentos respecto a los puntos $A$ y en $B$ deben ser iguales. Considere que la componente $\\hat{{i}}$ de $F_2 = {-f[3]:.0f} \\text{{ N}}$ y que $F_1 = [{f[0]:.0f}\\hat{{i}} + {f[1]:.0f} \\hat{{j}} + ({-f[2]:.0f})\\hat{{k}}]\\text{{ N}}$, $F_3 = [{f[6]:.0f}\\hat{{i}} + ({-f[7]:.0f})\\hat{{j}} + {f[8]:.0f}\\hat{{k}}]\\text{{ N}}$, $d_1 = {d[3]:.0f} \\text{{ m}}$,  $d_2 = {d[0]:.0f}  \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Componente $\\hat{{j}}$ de la fuerza $F_2$ $[N]$",
        a2_name = "Componente $\\hat{{k}}$ de la fuerza $F_2$ $[N]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[7]-f[1],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[2]-f[8],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP4,      
        ayuda3 = MP5,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones, el cálculo del momento se facilita al resolver el producto cruz. A continuación, se muestra la solución sugerida para el ejercicio:      

        $\\textbf{{\\small 1. Cálculo del momento en A: }}$
        
        Las únicas fuerzas que causan momento en el punto $A$ son $F_1$ y $F_3$. Dado que, la línea de acción de la fuerza $F_2$ cruza el punto $A$:
        
        $\\underline{{Momento \\text{{ }} causado \\text{{ }} por \\text{{ }} F_1 :}}$  
        
        ${{\hspace{{4mm}} M_{{A1}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_{{A1}} = ( 0 {{\\text{{ m}}}} \\cdot ({-f[2]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[1]:.0f} {{\\text{{ N}}}})\\hat{{i}} - ({d[0]:.0f}{{\\text{{ m}}}} \\cdot ({-f[2]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[0]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ({d[0]:.0f}{{\\text{{ m}}}} \\cdot {f[1]:.0f} {{\\text{{ N}}}} - 0{{\\text{{ m}}}} \\cdot {f[0]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_{{A1}} = [ 0 \\hat{{i}} + {d[0]*f[2]:.0f}\\hat{{j}} + {d[0]*f[1]:.0f} \\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$      
        
        $\\underline{{Momento \\text{{ }} causado \\text{{ }} por \\text{{ }} F_3 :}}$  
        
        ${{\hspace{{4mm}} M_{{A3}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_{{A3}} = ( 0 {{\\text{{ m}}}} \\cdot {f[8]:.0f}{{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}})\\hat{{i}} - ({d[0]:.0f}{{\\text{{ m}}}} \\cdot {f[8]:.0f} {{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ({d[0]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_{{A3}} = [ {d[6]*f[7]:.0f}\\hat{{i}} - ({d[0]*f[8] - d[6]*f[6]:.0f})\\hat{{j}} - ({d[0]*(f[7]):.0f})\\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$    
        
        $\\underline{{Sumatoria \\text{{ }} momentos \\text{{ }} en \\text{{ }} A :}}$ 
         
        ${{\hspace{{4mm}} \\sum{{M_A}} = [ ( 0 + {d[6]*(f[7]):.0f})\\hat{{i}} + ({d[0]*f[2]:.0f} + ({d[6]*f[6]-d[0]*f[8]:.0f}))\\hat{{j}} + ({d[0]*f[1]:.0f} - {d[0]*(f[7]):.0f})\\hat{{k}}]{{\\text{{N}} \\cdot \\text{{ m}}}} }}$     
        ${{\hspace{{4mm}} \\sum{{M_A}} = [({d[6]*f[7]:.2f})\hat{{i}} + ({d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f})\\hat{{j}} + ({d[0]*f[1] - d[0]*f[7]:.2f})\\hat{{k}}] {{\\text{{ N}} \\cdot \\text{{ m}}}} }}$     
        
        $\\textbf{{\\small 2. Cálculo del momento en B: }}$
        
        Las únicas fuerzas que causan momento son en el punto $B$ son $F_2$ y $F_3$. Dado que, la línea de acción de la fuerza $F_1$ cruza el punto $B$:
        
        $\\underline{{Momento \\text{{ }} causado \\text{{ }} por \\text{{ }} F_2 :}}$  
        
        ${{\hspace{{4mm}} M_{{B2}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_{{B2}} = ( 0 {{\\text{{ m}}}} \\cdot F2_z - 0 {{\\text{{ m}}}} \\cdot F2_y )\\hat{{i}} - ( {-d[0]:.0f} {{\\text{{ m}}}} \\cdot F2_z - 0 {{\\text{{ m}}}} \\cdot ({-f[3]:.0f}) {{\\text{{ N}}}})\\hat{{j}} + ( {-d[0]:.0f} {{\\text{{ m}}}} \\cdot  F2_y - 0 {{\\text{{ m}}}} \\cdot ({-f[3]:.0f}) {{\\text{{ N}}}})\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_{{B2}} =  0 {{ \\text{{ N}} \\cdot \\text{{ m }}}} \\hat{{i}} + {d[0]:.0f} {{\\text{{ m}}}} \\cdot F2_z \\hat{{j}} - {d[0]:.0f} {{\\text{{ m}}}} \\ cdot F2_y \\hat{{k}}  }}$
        
        $\\underline{{Momento \\text{{ }} causado \\text{{ }} por \\text{{ }} F_3 :}}$  
        
        ${{\hspace{{4mm}} M_{{B3}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_{{B3}} = ( 0 {{\\text{{ m}}}} \\cdot {f[8]:.0f}{{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}})\\hat{{i}} - ( 0 {{\\text{{ m}}}} \\cdot {f[8]:.0f} {{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ( 0 {{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_{{B3}} = [ {d[6]*f[7]:.0f}\\hat{{i}} + {d[6]*f[6]:.0f}\\hat{{j}} - 0 \\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$    
        
        $\\underline{{Sumatoria \\text{{ }} momentos \\text{{ }} en \\text{{ }} B:}}$
           
        ${{\hspace{{4mm}} \\sum{{M_B}} = [({d[6]*f[7]:.2f} {{\\text{{ N}} \\cdot \\text{{ m}}}})\\hat{{i}} + ({d[6]*f[6]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[0]:.0f} {{\\text{{ m}}}} \\cdot F2_z ) \\hat{{j}} - ({d[0]:.2f}{{\\text{{ m}}}} \\cdot F2_y)\\hat{{k}}] }}$    
        
        $\\textbf{{\\small 3. Despeje de las componentes j y k de F2: }}$
        
        Para cumplir la condición de que el momento en $B$ y el momento en $A$ sean iguales, es necesario que sus componentes también lo sean, tal que:
        
        ${{\hspace{{4mm}} 1.  ({d[6]*f[7]:.2f} {{\\text{{ N}} \\cdot \\text{{ m}}}})\\hat{{i}} = ({d[6]*f[7]:.2f} {{\\text{{ N}} \\cdot \\text{{ m}}}})\\hat{{i}} }}$      
        ${{\hspace{{4mm}} 2.  ({d[6]*f[6]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[0]:.0f} {{\\text{{ m}}}} \\cdot F2_z ) \\hat{{j}} = ({d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}})\\hat{{j}} }}$      
        ${{\hspace{{4mm}} 3.  - ({d[0]:.2f}{{\\text{{ m}}}} \\cdot F2_y)\\hat{{k}} = ({d[0]*f[1] - d[0]*f[7]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}})\\hat{{k}} }}$     
        
        Las ecuaciones 2 y 3 permiten obtener los valores de $F_{{2z}}$ y $F_{{2y}}$ :
        
        $\\underline{{Despeje \\text{{ }} para \\text{{ }} F2_z :}}$

        De la ecuación 2 se obtiene:  
        
        ${{\hspace{{4mm}} ({d[6]*f[6]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[0]:.0f} {{\\text{{ m}}}} \\cdot F2_z ) \\hat{{j}} = ({d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}})\\hat{{j}} }}$      
        ${{\hspace{{4mm}} ({d[0]:.2f} {{\\text{{ m}}}} \\cdot F2_z ) = {d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[6]*f[6]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} F2_z = \\dfrac{{{d[0]*f[2] - d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}}}{{{d[0]:.2f} {{\\text{{ m}}}}}} }}$           
        ${{\hspace{{4mm}} F2_z = {f[2]-f[8]:.2f}{{\\text{{ N}}}}}} $ 
        
        $\\underline{{Despeje \\text{{ }} para \\text{{ }} F2_y :}}$ 

        De la ecuación 3 se obtiene: 
        
        ${{\hspace{{4mm}} - ({d[0]:.2f}{{\\text{{ m}}}} \\cdot F2_y)\\hat{{k}} = ({d[0]*f[1] - d[0]*f[7]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}})\\hat{{k}} }}$            
        ${{\hspace{{4mm}} F2_y = \\dfrac{{{d[0]*f[7] - d[0]*f[1]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}}}{{{d[0]:.2f} {{\\text{{ m}}}}}} }}$           
        ${{\hspace{{4mm}} F2_y = {f[7]-f[1]:.2f}{{\\text{{ N}}}}}} $ 
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 2220031,
        no_pregunta = 3,
        complexity = M,
        topic = MO,
        subtopic = M3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Si la sumatoria de momentos en $A$ y en $B$ deben ser iguales, determine las componentes en las direcciones $\\hat{{j}}$ y $\\hat{{k}}$ de una cuarta fuerza $F_4$, la cual es aplicada sobre el tramo $OA$, a una distancia de ${(d[3]/3):.2f}{{\\text{{ m}}}}$ desde el punto $O$. Considere que la componente $\\hat{{i}}$ de $F_4 = {f[9]:.0f} \\text{{ N}}$ y que $F_1 = [{f[0]:.0f}\\hat{{i}} + {f[1]:.0f} \\hat{{j}} + ({-f[2]:.0f})\\hat{{k}}]\\text{{ N}}$, $F_2 = [({-f[3]:.0f})\\hat{{i}} + {f[4]:.0f} \\hat{{j}} + {f[5]:.0f}\\hat{{k}}]\\text{{ N}}$, $F_3 = [{f[6]:.0f}\\hat{{i}} + ({-f[7]:.0f})\\hat{{j}} + {f[8]:.0f}\\hat{{k}}]\\text{{ N}}$, $d_1 = {d[3]:.0f} \\text{{ m}}$,  $d_2 = {d[0]:.0f}  \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Componente $\\hat{{j}}$ de la fuerza $F_4$ $[N]$",
        a2_name = "Componente $\\hat{{k}}$ de la fuerza $F_4$ $[N]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((d[0]*f[7] - d[0]*f[1] - d[0]*f[4])/d[0],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[2]- f[8] - f[5],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP5,      
        ayuda3 = MP7,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones, el cálculo del momento se facilita al resolver el producto cruz. En este caso, se va a descomponer el problema en obtener las componentes de los momentos en A y en B, para luego igualarlas con el fin de despejar los terminos que se buscan. A continuación, se presenta la solución sugerida para el ejercicio:      

        $\\textbf{{\\small 1. Calculo del momento en A: }}$
        
        Las únicas fuerzas que causan momento en el punto $A$ son $F_1$, $F_3$ y $F_4$ :
        
        $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_1 :}}$  
        
        ${{\hspace{{4mm}} M_{{A1}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_{{A1}} = ( 0 {{\\text{{ m}}}} \\cdot ({-f[2]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[1]:.0f} {{\\text{{ N}}}})\\hat{{i}} - ({d[0]:.0f}{{\\text{{ m}}}} \\cdot ({-f[2]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[0]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ({d[0]:.0f}{{\\text{{ m}}}} \\cdot {f[1]:.0f} {{\\text{{ N}}}} - 0{{\\text{{ m}}}} \\cdot {f[0]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_{{A1}} = [ 0 \\hat{{i}} + {d[0]*f[2]:.0f}\\hat{{j}} + {d[0]*f[1]:.0f} \\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$      
        
        $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_3 :}}$  
        
        ${{\hspace{{4mm}} M_{{A3}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_{{A3}} = ( 0 {{\\text{{ m}}}} \\cdot {f[8]:.0f}{{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}})\\hat{{i}} - ({d[0]:.0f}{{\\text{{ m}}}} \\cdot {f[8]:.0f} {{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ({d[0]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_{{A3}} = [ {d[6]*f[7]:.0f}\\hat{{i}} - ({d[0]*f[8] - d[6]*f[6]:.0f})\\hat{{j}} - ({d[0]*(f[7]):.0f})\\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$    
        
        $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_4 :}}$  
        
        ${{\hspace{{4mm}} M_{{A4}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_{{A4}} = ( ({-2*(d[3]/3):.2f}) {{\\text{{ m}}}} \\cdot F4_z - 0 {{\\text{{ m}}}} \\cdot F4_y)\\hat{{i}} - ( 0 {{\\text{{ m}}}} \\cdot F4_z - 0 {{\\text{{ m}}}} \\cdot {f[9]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ( 0 {{\\text{{ m}}}} \\cdot F4_y - ({-2*(d[3]/3):.2f}) {{\\text{{ m}}}} \\cdot {f[9]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_{{A4}} =  ( ({-2*(d[3]/3):.2f}) {{\\text{{ m}}}} \\cdot F4_z )\\hat{{i}} + 0{{\\text{{ N}} \\cdot \\text{{ m}}}} \\hat{{j}} + {2*(d[3]/3)*f[9]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} \\hat{{k}} }}$    
        
        $\\underline{{Sumatoria \\hspace{{2mm}} momentos \\hspace{{2mm}} en \\hspace{{2mm}} A :}}$ 
         
        ${{\hspace{{4mm}} \\sum{{M_A}} =  ( 0 {{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[6]*(f[7]):.0f}{{\\text{{N}} \\cdot \\text{{ m}}}} - {2*(d[3]/3):.2f} {{\\text{{ m}}}} \\cdot F4_z )\\hat{{i}} + ({d[0]*f[2]:.0f} + ({d[6]*f[6]-d[0]*f[8]:.0f}) + 0){{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{j}} + ({d[0]*f[1]:.0f} - {d[0]*(f[7]) + 2*(d[3]/3)*f[9]:.0f}){{\\text{{ N}} \\cdot \\text{{ m}}}} \\hat{{k}} }}$     
        ${{\hspace{{4mm}} \\sum{{M_A}} = ({d[6]*f[7]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {2*(d[3]/3):.2f} {{\\text{{ m}}}} \\cdot F4_z)\\hat{{i}} + {d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{j}} + ({d[0]*f[1] - d[0]*f[7] + 2*(d[3]/3)*f[9]:.2f}){{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{k}}  }}$     
        
        $\\textbf{{\\small 2. Calculo del momento en B: }}$
        
        Las únicas fuerzas que causan momento en el punto $B$ son $F_2$, $F_3$ Y $F_4$:
        
        $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_2 :}}$  
        
        ${{\hspace{{4mm}} M_{{B2}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_{{B2}} = ( 0 {{\\text{{ m}}}} \\cdot {f[5]:.0f}{{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[4]:.0f}{{\\text{{ N}}}} )\\hat{{i}} - ( {-d[0]:.0f} {{\\text{{ m}}}} \\cdot {f[5]}{{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot ({-f[3]:.0f}) {{\\text{{ N}}}})\\hat{{j}} + ( {-d[0]:.0f} {{\\text{{ m}}}} \\cdot {f[4]:.0f}{{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot ({-f[3]:.0f}) {{\\text{{ N}}}})\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_{{B2}} = [ 0 \\hat{{i}} + {d[0]*f[5]:.0f}\\hat{{j}} - {d[0]*f[4]:.0f} \\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}} }}$
        
        $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_3 :}}$  
        
        ${{\hspace{{4mm}} M_{{B3}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_{{B3}} = ( 0 {{\\text{{ m}}}} \\cdot {f[8]:.0f}{{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}})\\hat{{i}} - ( 0 {{\\text{{ m}}}} \\cdot {f[8]:.0f} {{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ( 0 {{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_{{B3}} = [ {d[6]*f[7]:.0f}\\hat{{i}} + {d[6]*f[6]:.0f}\\hat{{j}} + 0 \\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$    
        
        $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_4 :}}$  
        
        ${{\hspace{{4mm}} M_{{B4}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_{{B4}} = ( ({-2*(d[3]/3):.2f}) {{\\text{{ m}}}} \\cdot F4_z - 0 {{\\text{{ m}}}} \\cdot F4_y)\\hat{{i}} - ( ({-d[0]:.0f}) {{\\text{{ m}}}} \\cdot F4_z - 0 {{\\text{{ m}}}} \\cdot {f[9]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ( ({-d[0]:.0f}) {{\\text{{ m}}}} \\cdot F4_y - ({-2*(d[3]/3):.2f}) {{\\text{{ m}}}} \\cdot {f[9]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_{{B4}} =  ( {-2*(d[3]/3):.2f} {{\\text{{ m}}}} \\cdot F4_z )\\hat{{i}} + {d[0]:.0f} {{\\text{{ m}}}} \\cdot F4_z \\hat{{j}} + ({(2*(d[3]/3)*f[9]):.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[0]:.0f}{{\\text{{ m}}}} \\cdot F4_y )\\hat{{k}} }}$    
        
        $\\underline{{Sumatoria \\hspace{{2mm}} momentos \\hspace{{2mm}} en \\hspace{{2mm}} B :}}$

        ${{\hspace{{4mm}} \\sum{{M_B}} =  ( 0 {{\\text{{N}} \\cdot \\text{{ m}}}} + {d[6]*(f[7]):.0f}{{\\text{{N}} \\cdot \\text{{ m}}}} - {2*(d[3]/3):.2f} {{\\text{{ m}}}} \\cdot F4_z )\\hat{{i}} + ({d[0]*f[5]:.0f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[6]*f[6]:.0f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[0]:.0f} {{\\text{{ m}}}} \\cdot F4_z)\\hat{{j}} + (0 {{\\text{{ N}} \\cdot \\text{{ m}}}} + {(2*(d[3]/3)*f[9]):.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[0]:.0f}{{\\text{{ m}}}}\\cdot F4_y - {d[0]*f[4]:.0f}{{\\text{{ N}} \\cdot \\text{{ m}}}}) \\hat{{k}} }}$     
        ${{\hspace{{4mm}} \\sum{{M_B}} = ({d[6]*f[7]:.2f}{{\\text{{N}} \\cdot \\text{{ m}}}} - {2*(d[3]/3):.2f} {{\\text{{ m}}}} \\cdot F4_z)\\hat{{i}} + ({d[0]*f[5] + d[6]*f[6]:.0f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[0]:.2f} {{\\text{{ m}}}} \\cdot F4_z ) \\hat{{j}} + ({(2*(d[3]/3)*f[9] - d[0]*f[4]):.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[0]:.2f}{{\\text{{ m}}}}\\cdot F4_y)\\hat{{k}} }}$    
        
        $\\textbf{{\\small 3. Despeje de las componentes de la fuerza 4: }}$
        
        Para cumplir la condición de que el momento en $B$ y el momento en $A$ sean iguales, es necesario que sus componentes también lo sean, tal que:
        
        ${{\hspace{{4mm}} 1.  ({d[6]*f[7]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {2*(d[3]/3):.2f} {{\\text{{ m}}}} \\cdot F4_z)\\hat{{i}} = ({d[6]*f[7]:.2f}{{\\text{{N}} \\cdot \\text{{ m}}}} - {2*(d[3]/3):.2f} {{\\text{{ m}}}} \\cdot F4_z)\\hat{{i}} }}$      
        ${{\hspace{{4mm}} 2.  ({d[0]*f[5] + d[6]*f[6]:.0f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[0]:.2f} {{\\text{{ m}}}} \\cdot F4_z )\\hat{{j}} =  {d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{j}}}}$      
        ${{\hspace{{4mm}} 3.  ({(2*(d[3]/3)*f[9] - d[0]*f[4]):.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[0]:.2f}{{\\text{{ m}}}}\\cdot F4_y)\\hat{{k}} =  {d[0]*f[1] - d[0]*f[7] + 2*(d[3]/3)*f[9]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{k}} }}$     
        
        Con las ecuaciones 2 y 3 se obtienen los valores de $F4_z$ y $F4_y$ :
        
        $\\underline{{Despeje \\hspace{{2mm}} para \\hspace{{2mm}} F4_z :}}$  
        
        De la ecuación 2:
        
        ${{\hspace{{4mm}} ({d[0]*f[5] + d[6]*f[6]:.0f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[0]:.2f} {{\\text{{ m}}}} \\cdot F4_z )\\hat{{j}} =  {d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{j}}}}$      
        ${{\hspace{{4mm}} {d[0]:.2f} {{\\text{{ m}}}} \\cdot F4_z  = {d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[0]*f[5] + d[6]*f[6]:.0f}{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} F4_z = \\dfrac{{{d[0]*f[2] -d[0]*f[8] - d[0]*f[5] :.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}}}{{{d[0]:.2f} {{\\text{{ m}}}}}} }}$           
        ${{\hspace{{4mm}} F4_z = {f[2]-f[8] -f[5]:.2f}{{\\text{{ N}}}}}} $ 
        
        $\\underline{{Despeje \\hspace{{2mm}} de \\hspace{{2mm}} por \\hspace{{2mm}} F4_y :}}$
        
        De la ecuación 3:  
        
        ${{\hspace{{4mm}} ({(2*(d[3]/3)*f[9] - d[0]*f[4]):.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[0]:.2f}{{\\text{{ m}}}}\\cdot F4_y)\\hat{{k}} = {d[0]*f[1] - d[0]*f[7] + 2*(d[3]/3)*f[9]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{k}} }}$         
        ${{\hspace{{4mm}} {d[0]:.2f}{{\\text{{ m}}}}\\cdot F4_y = {(2*(d[3]/3)*f[9] - d[0]*f[4]):.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[0]*f[1] - d[0]*f[7] + 2*(d[3]/3)*f[9]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} }}$       
        ${{\hspace{{4mm}} F4_y = \\dfrac{{{d[0]*f[7] - d[0]*f[1] - d[0]*f[4]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}}}{{{d[0]:.2f} {{\\text{{ m}}}}}} }}$           
        ${{\hspace{{4mm}} F4_y = {(d[0]*f[7] - d[0]*f[1] - d[0]*f[4])/d[0]:.2f}{{\\text{{ N}}}}}} $ 
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations',
        ),
    
    
 
    #========================================================  MOMENTO  =========================================================
    #--------------------------------------------     Momento en un punto en 3D      --------------------------------------------
    #-------------------------------------------------       Nivel Dificil   ---------------------------------------------------
    #-------------------------------------------------       Code: 2230011    -------------------------------------------------- 
    Questionary(#1_1
        code = 2230011,
        no_pregunta = 1,
        complexity = D,
        topic = MO,
        subtopic = M3D,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza $F_1$ aplicada sobre la barra $OA$ y la tensión en el cable $AC$ ($T_{{AC}}$), sabiendo que la estructura no gira con respecto al origen $O$. Considere que la magnitud de la tensión del cable $AB$ es ${f[0]:.2f}{{\\text{{ N}}}}$. Se sabe que $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$, $d_3 = {d[6]:.0f} \\text{{ m}}$, $d_4 = {d[9]:.0f} \\text{{ m}}$,  $d_5 = {d[12]:.0f}  \\text{{ m}}$ y  $d_6 = {d[15]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Magnitud Fuerza $F_1$ $[N]$",
        a2_name = "Magnitud Tension $T_{{AC}}$ $[N]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((((d[3]+d[0])*((f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))) + ((d[3]+d[0])*((d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])))*(((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))/((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))))))/d[0],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))/((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MP1,
        ayuda2 = MP5,      
        ayuda3 = MP7,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones es más fácil calcular el momento resolviendo producto cruz y dividiendo el ejercicio en determinar las componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$. A continuación, se presenta la solución sugerida para el ejercicio:   
        
        $\\textbf{{\\small 1. Calculo de componentes de cada tensión: }}$    
        
        Antes de iniciar el cálculo de los momentos mediante el producto cruz, es necesario hallar las componentes de ambas tensiones. Para ello, se utiliza el vector Unitario asociado a cada una: 
        
        $\\underline{{Componentes\\hspace{{2mm}} de \\hspace{{2mm}}T_{{AB}}:}}$
        
        ${{\hspace{{4mm}} \\overrightarrow{{T_{{AB}}}} = |\\overrightarrow{{T_{{AB}}}}| \\cdot \\lambda_{{AB}}}}$    
        ${{\hspace{{4mm}} \\overrightarrow{{T_{{AB}}}} = {f[0]:.2f}{{\\text{{ N}}}} \\cdot [ ( {(d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} )\\hat{{i}} + ( {-(d[0]+d[3])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} )\\hat{{j}} + ( {(d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} )\\hat{{k}}]}}$    
        ${{\hspace{{4mm}} \\overrightarrow{{T_{{AB}}}} = [ ( {(f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} )\\hat{{i}} +  ( {(-f[0]*(d[0]+d[3]))/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} )\\hat{{j}} + ( {(f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} )\\hat{{k}}] {{\\text{{ N}}}}}}$     
        
        $\\underline{{Componentes\\hspace{{2mm}} de \\hspace{{2mm}}T_{{AC}}:}}$
        
        ${{\hspace{{4mm}} \\overrightarrow{{T_{{AC}}}} = |\\overrightarrow{{T_{{AC}}}}| \\cdot \\lambda_{{AC}}}}$    
        ${{\hspace{{4mm}} \\overrightarrow{{T_{{AC}}}} = |\\overrightarrow{{T_{{AC}}}}| \\cdot [ ( {(-d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f} )\\hat{{i}} +  ( {-(d[0]+d[3])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f} )\\hat{{j}} + ( {(d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f} )\\hat{{k}}]}}$       

        $\\textbf{{\\small 2. Calculo del momento en el origen: }}$ 
        
        $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_1 :}}$ 
        
        ${{\hspace{{4mm}} M_{{F_1}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_{{F_1}} = (-F_1 \\cdot {d[0]:.0f}{{\\text{{ m}}}})\\hat{{i}} + 0 {{\\text{{N}} \\cdot \\text{{ m}}}}\\hat{{j}} + 0 {{\\text{{N}} \\cdot \\text{{ m}}}}\\hat{{k}} }}$      
        
        $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} T_{{AB}} :}}$  
        
        ${{\hspace{{4mm}} M_{{T_{{AB}}}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_{{T_{{AB}}}} = ({(d[3]+d[0]) :.0f}{{\\text{{ m}}}} \\cdot {(f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot ({-(f[0]*(d[0]+d[3]))/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} ) {{\\text{{ N}}}} )\\hat{{i}} - ( 0 {{\\text{{ m}}}} \\cdot  {(f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {(f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} {{\\text{{ N}}}})\\hat{{j}} + ( 0 {{\\text{{ m}}}} \\cdot ({(-f[0]*(d[0]+d[3]))/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f}){{\\text{{ N}}}} - {d[3]+d[0]:.0f}{{\\text{{ m}}}} \\cdot {(f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} {{\\text{{ N}}}})\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_{{T_{{AB}}}} = [ {(d[3]+d[0])*((f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}\\hat{{i}} + 0 \\hat{{j}} - {(d[3]+d[0])*((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}\\hat{{k}} ] {{ \\text{{N}} \\cdot \\text{{ m}}}} }}$     
        
        $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} T_{{AC}} :}}$  
        
        ${{\hspace{{4mm}} M_{{T_{{AC}}}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
        ${{\hspace{{4mm}} M_{{T_{{AC}}}} = ({(d[3]+d[0]) :.0f}{{\\text{{ m}}}} \\cdot T_{{AC}} \\cdot {(d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f}  - 0 {{\\text{{ m}}}} \\cdot T_{{AC}} \\cdot ({-(d[0]+d[3])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f}) )\\hat{{i}} - ( 0 {{\\text{{ m}}}} \\cdot  T_{{AC}} \\cdot {(d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f} - 0 {{\\text{{ m}}}} \\cdot T_{{AC}} \\cdot ( {(-d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f} ))\\hat{{j}} + ( 0 {{\\text{{ m}}}} \\cdot T_{{AC}} \\cdot ({(-(d[0]+d[3]))/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f}) - {d[3]+d[0]:.0f}{{\\text{{ m}}}} \\cdot T_{{AC}} \\cdot  ( {(-d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f} ))\\hat{{k}}}}$       
        ${{\hspace{{4mm}} M_{{T_{{AC}}}} = {(d[3]+d[0])*((d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}} \\hat{{i}} + 0 {{ \\text{{N}} \\cdot \\text{{ m}}}} \\hat{{j}} + {(d[3]+d[0])*((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}}\\hat{{k}}  }}$      
        
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} momentos \\hspace{{2mm}} en \\hspace{{2mm}} el \\hspace{{2mm}} origen :}}$
        
        ${{\hspace{{4mm}} \\sum{{M_O}} = ({(d[3]+d[0])*((f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}{{\\text{{N}} \\cdot \\text{{ m}}}} + {(d[3]+d[0])*((d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}} - F_1 \\cdot {d[0]:.0f}{{\\text{{ m}}}})\\hat{{i}} + 0 \\hat{{j}} + ({(d[3]+d[0])*((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}} -{(d[3]+d[0])*((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}{{ \\text{{N}} \\cdot \\text{{ m}}}})\\hat{{k}} = 0\\hat{{i}} + 0\\hat{{j}} + 0\\hat{{k}}}}$      
        
        $\\textbf{{\\small 3. Despeje de la tensión en el cable AC y la fuerza 1: }}$
        
        Para que la barra permanezcca en equilibrio y no gire con respecto al origen $O$, la sumatoria de momentos respecto a dicho punto debe ser igual a cero. Esto implica que cada una de las componentes del momento resultante es igual a cero. Tal que:
        
        ${{\hspace{{4mm}} 1.  ({(d[3]+d[0])*((f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}{{\\text{{N}} \\cdot \\text{{ m}}}} + {(d[3]+d[0])*((d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}} - F_1 \\cdot {d[0]:.0f}{{\\text{{ m}}}})\\hat{{i}} = 0{{\\text{{N}} \\cdot \\text{{ m}}}} \\hat{{i}} }}$      
        ${{\hspace{{4mm}} 2.  0{{\\text{{N}} \\cdot \\text{{ m}}}} \\hat{{j}} =  0 {{\\text{{N}} \\cdot \\text{{ m}}}}\\hat{{j}}}}$      
        ${{\hspace{{4mm}} 3.  ({(d[3]+d[0])*((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}} - {(d[3]+d[0])*((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}{{ \\text{{N}} \\cdot \\text{{ m}}}})\\hat{{k}} =  0 {{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{k}} }}$     
        
        Las ecuaciones 1 y 3 permiten obtener los valores de $F_1$ y $T_{{AC}}$ :
        
        $\\underline{{Despeje \\hspace{{2mm}} para \\hspace{{2mm}} T_{{AC}} :}}$  
        
        De la ecuación 3 se obtiene:
        
        ${{\hspace{{4mm}} ({(d[3]+d[0])*((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}} - {(d[3]+d[0])*((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}{{ \\text{{N}} \\cdot \\text{{ m}}}})\\hat{{k}} =  0 {{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{k}} }}$      
        ${{\hspace{{4mm}} {(d[3]+d[0])*((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}}  = {(d[3]+d[0])*((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}{{ \\text{{N}} \\cdot \\text{{ m}}}}}}$      
        ${{\hspace{{4mm}} T_{{AC}} = {((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))/((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ N}}}}}} $ 
        
        $\\underline{{Despeje \\hspace{{2mm}} de \\hspace{{2mm}} por \\hspace{{2mm}} F_1 :}}$
        
        Con el dato obtenido de la ecuación 1 se obtiene:  
        
        ${{\hspace{{4mm}} ({(d[3]+d[0])*((f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}{{\\text{{N}} \\cdot \\text{{ m}}}} + {(d[3]+d[0])*((d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot{((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))/((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ N}}}}  - F_1 \\cdot {d[0]:.0f}{{\\text{{ m}}}})\\hat{{i}} = 0{{\\text{{N}} \\cdot \\text{{ m}}}} \\hat{{i}} }}$      
        ${{\hspace{{4mm}} F_1 \\cdot {d[0]:.0f}{{\\text{{ m}}}} = {((d[3]+d[0])*((f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))) + ((d[3]+d[0])*((d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])))*(((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))/((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))))):.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} }}$       
        ${{\hspace{{4mm}} F_1 = {(((d[3]+d[0])*((f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))) + ((d[3]+d[0])*((d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])))*(((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))/((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))))))/d[0]:.2f}{{\\text{{ N}}}}}} $     
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),


   
    #========================================================  MOMENTO  =========================================================
    #--------------------------------------        Momento alrededor de un eje      --------------------------------------------
    #-------------------------------------------------       Nivel Fácil   ---------------------------------------------------
    #-------------------------------------------------      Code: 23100##    --------------------------------------------------

    Questionary(#1_1
        code = 2310011,
        no_pregunta = 1,
        complexity = F,
        topic = MO,
        subtopic = "Momento alrededor de un eje",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud del momento $(\\vec{{M_O}})$ generado por la fuerza $\\overrightarrow{{F}}$ con respecto al origen y la magnitud del momento alrededor del eje $L$ ($\\vec{{M_L}}$). Considere que la fuerza $\\overrightarrow{{F}}$ tiene una magnitud de ${f[0]:.0f} \\text{{ N}}$ y su línea de acción cruza las coordenadas $[x={d[2]:.0f}, \\text{{ }} y= {d[0]:.0f}, \\text{{ }} z= {d[3]:.0f}] \\text{{ m}}$ en la dirección positiva de $X$. Por su parte, el eje $L$ cruza el origen en dirección de las coordenadas  $[x={d[2]+1:.0f}, \\text{{ }} y= {d[0]+2:.0f}, \\text{{ }} z= {d[3]+5:.0f}] \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Magnitud del momento con respecto al origen, $M_O$ $[N \\cdot m]$",
        a2_name = "Magnitud del momento alredor del eje $L$, $M_L$ $[N \\cdot m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D(0,f[0]*d[3],(-f[0]*d[0])),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(np.dot([0,f[0]*d[3],-f[0]*d[0]],[(d[2]+1)/Calculations.magnitude3D(d[2]+1,d[0]+2,d[3]+5),(d[0]+2)/Calculations.magnitude3D(d[2]+1,d[0]+2,d[3]+5),(d[3]+5)/Calculations.magnitude3D(d[2]+1,d[0]+2,d[3]+5)]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MAE1,
        ayuda2 = MAE2,      
        ayuda3 = MAE3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento en un punto se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$, mientras que el momento alrededor de un eje se calcula como la proyección del momento en un punto sobre el vector unitario del eje. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Determinación del vector Fuerza y Posición: }}$
        
        ${{\hspace{{4mm}} \\vec{{F}} = [{f[0]:.0f} \\hat{{ i}} + 0 \\hat{{ j}} + 0 \\hat{{ k}}] \\text{{ N}} }}$            
        ${{\hspace{{4mm}} \\vec{{r}} = [{d[2]:.0f}\\hat{{ i}} + {d[0]:.0f} \\hat{{ j}} + {d[3]:.0f} \\hat{{ k}}] \\text{{ m}}}}$     
        
        $\\textbf{{\\small 2. Cálculo de momento con respecto al punto O - Producto Cruz: }}$
        ${{\hspace{{4mm}} \\vec{{M_O}} = [({d[0]:.0f}*0-{d[3]:.0f}*0) \\hat{{ i}} - ({d[2]:.0f}*0-{f[0]:.0f}*{d[3]:.0f}) \\hat{{ j}} + ({d[2]:.0f}*0-{f[0]:.0f}*{d[0]:.0f}) \\hat{{ k}}] \\text{{ N}} \\cdot \\text{{ m}} }}$         
        ${{\hspace{{4mm}} \\vec{{M_O}} = [{d[0]*0-d[3]*0} \\hat{{ i}} + {-1*(d[2]*0-f[0]*d[3])} \\hat{{ j}} + {d[2]*0-f[0]*d[0]} \\hat{{ k}}] \\text{{ N}} \\cdot \\text{{ m}}}}$     

       Con este cálculo, se determina la magnitud del momento con respecto al origen:    

        ${{\hspace{{4mm}} |\\vec{{M_O}}| = \\sqrt{{({d[0]*0-d[3]*0})^2+({-1*(d[2]*0-f[0]*d[3])})^2+({d[2]*0-f[0]*d[0]})^2}}}}$      
        ${{\hspace{{4mm}} |\\vec{{M_O}}| = {Calculations.magnitude3D (d[0]*0-d[3]*0, (-1*(d[2]*0-f[0]*d[3])), (d[2]*0-f[0]*d[0])):.2f} \\text{{ N}} \\cdot \\text{{ m}} }}$

        $\\textbf{{\\small 3. Cálculo del vector unitario del eje L: }}$       
        ${{\hspace{{4mm}} \\vec{{L}} = [{d[2]+1:.0f} \\hat{{ i}} + {d[0]+2:.0f} \\hat{{ j}} + {d[3]+5:.0f} \\hat{{ k}}] \\text{{m}} }}$ 
        ${{\hspace{{4mm}} \\hat{{L}} = \\dfrac{{{d[2]+1:.0f}}}{{\\sqrt{{({d[2]+1:.0f})^2+({d[0]+2:.0f})^2+({d[3]+5:.0f})^2}}}} \\hat{{ i}} + \\dfrac{{{d[0]+2:.0f}}}{{\\sqrt{{({d[2]+1:.0f})^2+({d[0]+2:.0f})^2+({d[3]+5:.0f})^2}}}} \\hat{{ j}} + \\dfrac{{{d[3]+5:.0f}}}{{\\sqrt{{({d[2]+1:.0f})^2+({d[0]+2:.0f})^2+({d[3]+5:.0f})^2}}}} \\hat{{ k}} }}$ 
        ${{\hspace{{4mm}} \\hat{{L}} = {(d[2]+1)/Calculations.magnitude3D(d[2]+1,d[0]+2,d[3]+5):.2f} \\hat{{ i}} + {(d[0]+2)/Calculations.magnitude3D(d[2]+1,d[0]+2,d[3]+5):.2f} \\hat{{ j}} + {(d[3]+5)/Calculations.magnitude3D(d[2]+1,d[0]+2,d[3]+5):.2f} \\hat{{ k}} }}$
        
        $\\textbf{{\\small 4. Cálculo del momento alrededor del eje L: }}$
        ${{\hspace{{4mm}} |\\vec{{M_L}}| = ({d[0]*0-d[3]*0} \\hat{{ i}} + {-1*(d[2]*0-f[0]*d[3])} \\hat{{ j}} + {d[2]*0-f[0]*d[0]} \\hat{{ k}}) \\cdot ({(d[2]+1)/Calculations.magnitude3D(d[2]+1,d[0]+2,d[3]+5):.2f} \\hat{{ i}} + {(d[0]+2)/Calculations.magnitude3D(d[2]+1,d[0]+2,d[3]+5):.2f} \\hat{{ j}} + {(d[3]+5)/Calculations.magnitude3D(d[2]+1,d[0]+2,d[3]+5):.2f} \\hat{{ k}}) }}$          
        ${{\hspace{{4mm}} |\\vec{{M_L}}| = {(d[0]*0-d[3]*0)*((d[2]+1)/Calculations.magnitude3D(d[2]+1,d[0]+2,d[3]+5))+(-1*(d[2]*0-f[0]*d[3]))*((d[0]+2)/Calculations.magnitude3D(d[2]+1,d[0]+2,d[3]+5))+(d[2]*0-f[0]*d[0])*((d[3]+5)/Calculations.magnitude3D(d[2]+1,d[0]+2,d[3]+5)):.2f} \\text{{ N}} \\cdot \\text{{ m}} }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
    ),

    Questionary(#2_1
        code = 2310021,
        no_pregunta = 2,
        complexity = F,
        topic = MO,
        subtopic = "Momento alrededor de un eje",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el momento generado por $|\\vec{{F}}| = {f[0]:.0f} \\text{{ kN}}$ alrededor de la línea que une los puntos $B$ y $A$, teniendo en cuenta que $d_0 = {d[0]:.0f} \\text{{ m}}, d_1 = {d[6]:.0f} \\text{{ m}}, d_2 = {d[3]+4:.0f} \\text{{ m}}, d_3 = {d[6]+3:.0f} \\text{{ m}}, d_4 = {d[3]:.0f} \\text{{ m}}$ y que el vector $\\vec{{F}}$ se dirige en la dirección negativa de $X$.",
        no_answers = 1,
        a1_name = "Momento alrededor de $BA$, $M_{BA} [kN \\cdot m]$:",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*((d[3]+4)-(d[3]))*(d[6]/Calculations.magnitude(d[0],d[6])),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MAE4,
        ayuda2 = MAE5,      
        ayuda3 = MAE1,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento en un punto se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$, mientras que el momento alrededor de un eje se calcula como la proyección del momento en un punto sobre el vector unitario del eje. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Determinación del vector posición asociado a la fuerza y la fuerza: }}$ 

        ${{\hspace{{4mm}} \\vec{{r}} = [0\\hat{{i}}+(x_2 - x_4)\\hat{{j}}+x_3\\hat{{ k}}] \\text{{ m}} }}$       
        ${{\hspace{{4mm}} \\vec{{r}} = [0\\hat{{i}}+{d[3]+4 - (d[3])}\\hat{{j}}+{d[6]+3:.0f}\\hat{{k}}] \\text{{ m}} }}$      
        ${{\hspace{{4mm}} \\vec{{F}} = [{-1*f[0]:.0f}\\hat{{i}}+0\\hat{{j}}+0\\hat{{k}}] \\text{{ kN}}}}$    
        
        $\\textbf{{\\small 2. Cálculo de Momento con respecto al punto B - Producto Cruz: }}$      
        ${{\hspace{{4mm}} \\vec{{M_B}} = (0\\hat{{i}}-{f[0]}*{d[6]+3}\\hat{{j}}+{f[0]}*{(d[3]+4 - (d[3]))}\\hat{{k}})[kN \\cdot m]}}$      
        ${{\hspace{{4mm}} \\vec{{M_B}} = (0\\hat{{i}}-{f[0]*(d[6]+3)}\\hat{{j}}+{f[0]*(d[3]+4 - (d[3]))}\\hat{{k}})[kN \\cdot m]}}$
        
        $\\textbf{{\\small 3. Cálculo del vector unitario de la línea BA:}}$      
        ${{\hspace{{4mm}} \\vec{{BA}} = {d[0]:.0f}\\hat{{i}} + 0\\hat{{j}} + {d[6]:.0f}\\hat{{k}} }}$      
        ${{\hspace{{4mm}} \\vec{{\\lambda_{{BA}} }} = \\dfrac{d[0]}{{\\sqrt{{({d[0]})^2+({d[6]})^2}} }} \\hat{{i}} + 0\\hat{{j}} + \\dfrac{d[6]}{{\\sqrt{{({d[0]})^2+({d[6]})^2}}}}\\hat{{k}} }}$     
        ${{\hspace{{4mm}} \\vec{{\\lambda_{{BA}} }} = {(d[0])/Calculations.magnitude(d[0],d[6]):.2f}\\hat{{i}} + 0\\hat{{j}} + {(d[6])/Calculations.magnitude(d[0],d[6]):.2f}\\hat{{k}}}}$    
        
         $\\textbf{{\\small 4. Momento alrededor de BA - Producto punto: }}$      
        ${{\hspace{{4mm}} \\vec{{M_B}} \\cdot \\vec{{\\lambda_{{BA}}}} = [(0\\hat{{i}}-{f[0]*(d[6]+3)}\\hat{{j}}+{f[0]*(d[3]+4 - (d[3]))}\\hat{{k}}) \\cdot ({(d[0])/Calculations.magnitude(d[0],d[6]):.2f}\\hat{{i}} + 0\\hat{{j}} + {(d[6])/Calculations.magnitude(d[0],d[6]):.2f}\\hat{{k}})] kN \\cdot m}}$      
        ${{\hspace{{4mm}} \\vec{{M_B}} \\cdot \\vec{{\\lambda_{{BA}}}} = {f[0]*((d[3]+4)-(d[3]))*(d[6]/Calculations.magnitude(d[0],d[6])):.2f}kN \\cdot m}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 2310031,
        no_pregunta = 3,
        complexity = F,
        topic = MO,
        subtopic = "Momento alrededor de un eje",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Considere el vector momento $\\vec{{M}} = [{m[0]}\\hat{{i}} + {m[1]}\\hat{{j}} - {m[2]}\\hat{{k}}]$ $kN$ $\\cdot$ $m$. Calcule la magnitud del momento que actúa sobre los ejes $y$ y $L$, conociendo que el vector de $L$ cruza el origen en dirección [${d[2]}\\hat{{i}} - {d[0]}\\hat{{j}} + {d[3]}\\hat{{k}}$] $\\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Momento alrededor del eje $y$ [$kN \\cdot m$]",
        a2_name = "Momento alrededor del eje $L$ [$kN \\cdot m$]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(m[1],2),
        answer2 = lambda f, a, calc, c, d, m: np.round((d[2]*m[0])/Calculations.magnitude3D(d[2],d[0],d[3])+(-1*d[0]*m[1])/Calculations.magnitude3D(d[2],d[0],d[3])+(-1*d[3]*m[2])/Calculations.magnitude3D(d[2],d[0],d[3]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MAE1,
        ayuda2 = MAE3,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        La magnitud del momento alrededor de un eje se calcula mediante el producto punto entre el vector de momento en un punto sobre el eje y el vector director del eje. A continuación, se presenta la solución sugerida para el ejercicio:  

        $\\textbf{{\\small 1. Momento alrededor del eje y:}}$ 
        
        ${{\hspace{{4mm}} \\vec{{M}} \\cdot \\vec{{\\lambda_{{\\hat{{j}}}}}} = 0*{m[0]} + 1*{m[1]} + 0*{-1*m[2]}}}$      
        ${{\hspace{{4mm}} \\vec{{M_y}} = {m[1]}}}kN \\cdot m$

        El momento alrededor el eje $y$ corresponde a la componente en la dirección $\\hat{{j}}$ del vector momento dado en el enunciado.
 
        $\\textbf{{\\small 2. Momento sobre el eje L:}}$       
        ${{\hspace{{4mm}} \\vec{{\\lambda_L}} = \\dfrac{{{d[2]}}}{{\\sqrt{{({d[2]})^2 + (-{d[0]})^2 + ({d[3]})^2}}}}\\hat{{i}} - \\dfrac{d[0]}{{\\sqrt{{({d[2]})^2 + (-{d[0]})^2 + ({d[3]})^2}}}}\\hat{{j}} + \\dfrac{{{d[3]}}}{{\\sqrt{{({d[2]})^2 + (-{d[0]})^2 + ({d[3]})^2}} }}\\hat{{k}} }}$        
       
        ${{\hspace{{4mm}} \\vec{{\\lambda_L}} = {d[2]/Calculations.magnitude3D(d[2],d[0],d[3]):.2f}\\hat{{i}} - {d[0]/Calculations.magnitude3D(d[2],d[0],d[3]):.2f}\\hat{{j}} + {d[3]/Calculations.magnitude3D(d[2],d[0],d[3]):.2f}\\hat{{k}}}}$         
        
        ${{\hspace{{4mm}} \\vec{{M}} \\cdot \\vec{{\\lambda_L}} = ({m[0]}\\hat{{i}} + {m[1]}\\hat{{j}} - {m[2]}\\hat{{k}}) \\cdot ({d[2]/Calculations.magnitude3D(d[2],d[0],d[3]):.2f}\\hat{{i}} - {d[0]/Calculations.magnitude3D(d[2],d[0],d[3]):.2f}\\hat{{j}} + {d[3]/Calculations.magnitude3D(d[2],d[0],d[3]):.2f}\\hat{{k}})}}$        
        ${{\hspace{{4mm}} \\vec{{M_L}} = {(d[2]*m[0])/Calculations.magnitude3D(d[2],d[0],d[3])+(-1*d[0]*m[1])/Calculations.magnitude3D(d[2],d[0],d[3])+(-1*d[3]*m[2])/Calculations.magnitude3D(d[2],d[0],d[3]):.2f}}}kN \\cdot m$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_1
        code = 2310041,
        no_pregunta = 4,
        complexity = F,
        topic = MO,
        subtopic = "Momento alrededor de un eje",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Considere la fuerza $F = {f[0]:.0f} \\text{{ kN}}$ paralela al eje $z$. Calcule el momento alrededor del punto $O$ y determine la componente del momento que va en la misma dirección del elemento $OA$, utilizando: $x_1 = {d[0]:.0f} \\text{{ m}}$, $z_1 = {d[3]:.0f} \\text{{ m}}$, $x_2 = {d[0]+3:.0f} \\text{{ m}}$, $y_2 = {d[3]-1:.0f} \\text{{ m}}$, $z_2 = {d[6]:.0f} \\text{{ m}}$",
        no_answers = 2,
        a1_name = "Momento alrededor del punto $O$ [$kN \\cdot m$]",
        a2_name = "Momento en el elemento $OA$ [$kN \\cdot m$]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude((d[3]-1)*f[0],(d[0]+3)*f[0]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((d[3]-1)*f[0])*d[0]/Calculations.magnitude(d[0],d[3]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "Utilice las coordenadas del punto B para calcular el momento generado por la fuerza. Este será el vector posición necesario.",
        ayuda2 = "Use el punto A para hallar el vector unitario del eje $OA$.",      
        ayuda3 = "Realice el producto punto con ${\\vec{\\lambda_{OA}}}$ para encontrar el momento alrededor de este eje.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        La magnitud del momento alrededor de un eje se calcula mediante el producto punto entre el vector de momento en un punto sobre el eje y el vector director del eje. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Identificación de vectores:}}$ 
        
        ${{\hspace{{4mm}} \\vec{{F}} = [0\\hat{{i}} + 0\\hat{{j}} + {f[0]}\\hat{{k}}] kN}}$       
        ${{\hspace{{4mm}} \\vec{{OA}} = [{d[0]}\\hat{{i}} + 0\\hat{{j}} + {d[3]}\\hat{{k}}] m}}$        
        ${{\hspace{{4mm}} \\vec{{OB}} = \\vec{{r}} = [{d[0]+3}\\hat{{i}} + {d[3]-1}\\hat{{j}} + {d[6]}\\hat{{k}}] m}}$      

        $\\textbf{{\\small 2. Momento con respecto al punto O:}}$    

        Haciendo el producto cruz entre $\\vec{{OB}}$ y $\\vec{{F}}$.

        ${{\hspace{{4mm}} \\vec{{M_O}} = [{(d[3]-1)*f[0]}\\hat{{i}} - {(d[0]+3)*f[0]}\\hat{{j}} + 0\\hat{{k}}] kN \\cdot m }}$    
        ${{\hspace{{4mm}} |\\vec{{M_O}}| = {Calculations.magnitude((d[3]-1)*f[0],(d[0]+3)*f[0]):.2f} kN \\cdot m}}$    

        $\\textbf{{\\small 3. Vector Unitario y Momento con respecto al elemento OA:}}$ 

        A partir del vector $OA$, se obtiene el vector unitario que indica la dirección del elemento. Este vector unitario es utilizado para proyectar el vector momento $\\vec{{M_O}}$ sobre el elemento $OA$.
       
        ${{\hspace{{4mm}} \\vec{{\\lambda_{{OA}}}} = [{d[0]/Calculations.magnitude(d[0],d[3]):.2f}\\hat{{i}} + 0\\hat{{j}} + {d[3]/Calculations.magnitude(d[0],d[3]):.2f}\\hat{{k}}] kN \\cdot m}}$     
        ${{\hspace{{4mm}} |\\vec{{M_{{OA}}}}| = \\vec{{M_O}} \\cdot \\vec{{\\lambda_{{OA}}}}= {((d[3]-1)*f[0])*d[0]/Calculations.magnitude(d[0],d[3]):.2f} kN \\cdot m}}$      
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),



    #=========================================================== MOMENTO ========================================================
    #--------------------------------------------     Momento alrededor de un eje      --------------------------------------------
    #-------------------------------------------------       Nivel medio      ---------------------------------------------------
    #-------------------------------------------------       Code: 23200##    ---------------------------------------------------

     Questionary(#1_1
        code = 2320011,
        no_pregunta = 1,
        complexity = M,
        topic = MO,
        subtopic = "Momento alrededor de un eje",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"La placa de peso $W = {f[0]:.0f} \\text{{ kN}}$ se sostiene en su posición mediante un cable. Calcule el momento generado por la tensión del cable respecto al eje $X$. Considere que $d_0 = {d[0]:.0f} \\text{{ m}}$, $d_1 = {d[3]+2:.0f} \\text{{ m}}$, $d_2 = {d[0]:.0f} \\text{{ m}}$ y $d_3 = {d[3]:.0f} \\text{{ m}}$.",
        no_answers = 1,
        a1_name = "Momento en el eje $X$ [$kN \\cdot m$]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((-1*(d[3]+2)*f[0]*d[0])/(Calculations.magnitude3D(-1*d[0],d[0],(d[3]-(d[3]+2)))),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "La magnitud de la tensión en el cable es igual al peso de la compuerta.",
        ayuda2 = "Halle el vector de la tensión ($\\vec{{T}}$) multiplicando su vector unitario por la magnitud: $\\vec{{T}}=|\\vec{{T}}|\\vec{{\\lambda}}$.",      
        ayuda3 = "Recuerde que el vector unitario del eje $X$ es $1\\hat{{i}} + 0\\hat{{j}} + 0\\hat{{k}}.$",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        La magnitud del momento alrededor de un eje se calcula mediante el producto punto entre el vector de momento en un punto sobre el eje y el vector director del eje. A continuación, se presenta la solución sugerida para el ejercicio:
        
        Para resolver este ejercicio, note que la fuerza generada por el peso de la compuerta es igual a la magnitud de la tensión en el cable.
        
        $\\textbf{{\\small 1. Vector director de T - Vector Unitario:}}$

        ${{\hspace{{4mm}} \\vec{{T}} = -{d[0]}\\hat{{i}}+{d[0]}\\hat{{j}}+({d[3]+2}-{d[3]})\\hat{{k}}}}$     
        
        ${{\hspace{{4mm}} \\vec{{\\lambda_T}} = \\dfrac{{{-d[0]}}}{{\\sqrt{{({(-d[0])})^2 + ({d[0]})^2 + ({d[3]-(d[3]+2)})^2}}}}\\hat{{i}}+\\dfrac{{{d[0]}}}{{\\sqrt{{({(-d[0])})^2 + ({d[0]})^2 + ({d[3]-(d[3]+2)})^2}}}} \\hat{{j}}-\\dfrac{{{d[3]+2-d[3]}}}{{\\sqrt{{({(-d[0])})^2 + ({d[0]})^2 + ({d[3]-(d[3]+2)})^2}}}}}}$         
        
        ${{\hspace{{4mm}} \\vec{{T}} = [{f[0]}*({-d[0]/Calculations.magnitude3D(-1*d[0],d[0],d[3]-(d[3]+2)):.2f}\\hat{{i}} + {d[0]/(Calculations.magnitude3D(-1*d[0],d[0],d[3]-(d[3]+2))):.2f}\\hat{{j}} - {(d[3]-d[3]+2)/(Calculations.magnitude3D(-1*d[0],d[0],d[3]+2-(d[3]))):.2f}\\hat{{k}})] \\text{{ kN}}}}$      
        
        ${{\hspace{{4mm}} \\vec{{T}} = [({-f[0]*d[0]/Calculations.magnitude3D(-1*d[0],d[0],d[3]-(d[3]+2)):.2f}\\hat{{i}} + {f[0]*d[0]/(Calculations.magnitude3D(-1*d[0],d[0],d[3]-(d[3]+2))):.2f}\\hat{{j}} - {(f[0]*(d[3]-d[3]+2))/(Calculations.magnitude3D(-1*d[0],d[0],d[3]+2-(d[3]))):.2f}\\hat{{k}})] \\text{{ kN}}}}$      

        $\\textbf{{\\small 2. Calculo de Momento alrededor del punto O:}}$       
       
        El momento alrededor del punto $O$ se obtiene mediante el producto cruz entre el vector posición $\\vec{{r}}$ y el vector tensión $\\vec{{T}}$. El vector posición $\\vec{{r}}$ se define como ${d[0]:.0f} \\hat{{i}} + 0 \\hat{{j}} + {d[3]+2} \\hat{{k}}.$
         
        ${{\hspace{{4mm}} \\vec{{M_O}} = [({((d[3]+2)*(-1*d[0]*f[0]))/(Calculations.magnitude3D(-1*d[0],d[0],d[3]-(d[3]+2))):.2f}) \\hat{{i}} + ({-((((d[3]-(d[3]+2))*f[0]*d[0])/(Calculations.magnitude3D(-1*d[0],d[0],d[3]-(d[3]+2))))-((-1*d[0]*f[0]*(d[3]+2))/(Calculations.magnitude3D(-1*d[0],d[0],d[3]-(d[3]+2))))):.2f}) \\hat{{j}} + ({(d[0]*(d[0]*f[0]))/(Calculations.magnitude3D(-1*d[0],d[0],d[3]-(d[3]+2))):.2f}) \\hat{{k}}] kN \\cdot m}}$  

        $\\textbf{{\\small 3. Calculo de Momento alrededor el eje X:}}$          
        
        ${{\hspace{{4mm}} \\vec{{M_x}} = \\vec{{M_O}} \\cdot \\vec{{\\lambda_{{\\hat{{i}}}}}} = 1*{((d[3]+2)*(-1*d[0]*f[0]))/(Calculations.magnitude3D(-1*d[0],d[0],d[3]-(d[3]+2))):.2f} + 0*{-((((d[3]-(d[3]+2))*f[0]*d[0])/(Calculations.magnitude3D(-1*d[0],d[0],d[3]-(d[3]+2))))-((-1*d[0]*f[0]*(d[3]+2))/(Calculations.magnitude3D(-1*d[0],d[0],d[3]-(d[3]+2))))):.2f} + 0*{(d[0]*(d[0]*f[0]))/(Calculations.magnitude3D(-1*d[0],d[0],d[3]-(d[3]+2))):.2f}}}$      
        ${{\hspace{{4mm}} \\vec{{M_x}} = {((d[3]+2)*(-1*d[0]*f[0])/(Calculations.magnitude3D(-1*d[0],d[0],d[3]-(d[3]+2)))):.2f}kN \\cdot m}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 
    
    Questionary(#2_1
        code = 2320021,
        no_pregunta = 2,
        complexity = M,
        topic = MO,
        subtopic = "Momento alrededor de un eje",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Considere las fuerzas $F = {f[0]:.0f} \\text{{ N}}$, pararela al eje $x$ negativo, y $P = {f[1]:.0f} \\text{{ N}}$, paralela al eje $z$ positivo. Encuente el momento generado por $F$ y $P$ alrededor del eje $z$ y de la recta $L$, definida por el vector $\\vec{{L}} = [{d[0]:.0f}\\hat{{i}} - {d[3]:.0f}\\hat{{j}} + {d[0]+2:.0f}\\hat{{k}}] \\text{{ m}}$. Considere que $d_0 = {d[6]:.0f} \\text{{ m}}$, $d_1 = {d[9]:.0f} \\text{{ m}}$, $d_2 = {d[12]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Momento alrededor del eje $z$ [$N \\cdot m$]",
        a2_name = "Momento alrededor de la recta $L$ [$N \\cdot m$]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(-1*f[0]*d[12],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((-1*d[3]/Calculations.magnitude3D(d[0],d[3],d[0]+2))*((-1*f[0]*d[9])-(d[6]*f[1])))+((d[0]+2)/Calculations.magnitude3D(d[0],d[3],d[0]+2)*(-1*f[0]*d[12])),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "Calcule el momento generado por cada fuerza con respecto al origen.",
        ayuda2 = "Realice la sumatoria de los momentos para encontrar el vector momento total generado por ambas fuerzas",      
        ayuda3 = "Encuentre la dirección de la recta (vector unitario) y proyecte el vector momento $\\vec{{M}}$ sobre esta usando el producto punto.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        La magnitud del momento alrededor de un eje se calcula mediante el producto punto entre el vector de momento en un punto sobre el eje y el vector director del eje. A continuación, se presenta la solución sugerida para el ejercicio:  

        $\\textbf{{\\small 1. Momento de las fuerzas F y P con respecto a O: }}$ 

        $\\underline{{Momento \\text{{ }} de \\text{{ }} la \\text{{ }} fuerza \\text{{ }} F}}$

        Los vectores para calcular el producto cruz son:

        ${{\hspace{{4mm}} \\vec{{r}} = [{d[6]} \\hat{{i}} - {d[12]} \\hat{{j}} + {d[9]}\\hat{{k}}] \\text{{m}}}}$             
        ${{\hspace{{4mm}} \\vec{{F}} = [-{f[0]} \\hat{{i}} + 0\\hat{{j}} + 0\\hat{{k}}] \\text{{ N}} }}$            

        ${{\hspace{{4mm}} \\vec{{M_F}} = [0 \\hat{{i}} + ({-1*f[0]*d[9]}) \\hat{{j}} + (-{f[0]*d[12]})\\hat{{k}}] N \\cdot m}}$     

        $\\underline{{Momento \\text{{ }} de \\text{{ }} la \\text{{ }} fuerza \\text{{ }} P}}$

        Los vectores para calcular el producto cruz son:

        ${{\hspace{{4mm}} \\vec{{r}} = [{d[6]} \\hat{{i}} + 0 \\hat{{j}} + 0 \\hat{{k}}] \\text{{ m}}}}$                  
        ${{\hspace{{4mm}} \\vec{{P}} = [0 \\hat{{i}} + 0\\hat{{j}} + {f[1]}\\hat{{k}}] \\text{{ N}} }}$            

        ${{\hspace{{4mm}} \\vec{{M_P}} = [0 \\hat{{i}} + ({-1*d[6]*f[1]})\\hat{{j}} + 0 \\hat{{k}}] N \\cdot m}}$    
   
        $\\textbf{{\\small 2. Sumatoria de Momentos con respecto al punto O: }}$         

        ${{\hspace{{4mm}} \\vec{{M_O}} = \\vec{{M_P}} + \\vec{{M_F}} = [0\\hat{{i}} + ({-1*d[6]*f[1]-(f[0]*d[9])})\\hat{{j}} + ({-f[0]*d[12]})\\hat{{k}}] N \\cdot m}}$           

        $\\textbf{{\\small 3. Momento sobre el eje z: }}$          

        ${{\hspace{{4mm}} \\vec{{M_z}} = \\vec{{M_O}} \\cdot \\vec{{\\lambda_{{\\hat{{k}}}}}} = 0*0 + 0*{-1*d[6]*f[1]-(f[0]*d[9]):.2f} + 1*{-f[0]*d[12]:.2f}}}$                                    
        ${{\hspace{{4mm}} \\vec{{M_z}} = \\vec{{M_O}} \\cdot \\vec{{\\lambda_{{\\hat{{K}}}}}} = [{-1*f[0]*d[12]}\\hat{{k}}]N \\cdot m}}$                

        $\\textbf{{\\small 4. Vector director de la recta L - Vector Unitario: }}$    

        ${{\hspace{{4mm}} \\vec{{L}} = {d[0]:.0f}\\hat{{i}} - {d[3]:.0f}\\hat{{j}} + {d[0]+2:.0f}\\hat{{k}}}}$                      
        ${{\hspace{{4mm}} \\vec{{\\lambda_L}} = {d[0]/Calculations.magnitude3D(d[0],d[3],d[0]+2):.2f}\\hat{{i}} - {d[3]/Calculations.magnitude3D(d[0],d[3],d[0]+2):.2f}\\hat{{j}} + {(d[0]+2)/Calculations.magnitude3D(d[0],d[3],d[0]+2):.2f}\\hat{{k}}}}$

        $\\textbf{{\\small 5. Momento sobre la recta L: }}$       

        ${{\hspace{{4mm}} \\vec{{M_L}}=\\vec{{M_O}} \\cdot \\vec{{\\lambda_L}} = (0\\hat{{i}} + ({-1*d[6]*f[1]-(f[0]*d[9])})\\hat{{j}} + ({-f[0]*d[12]})\\hat{{k}}) \\cdot ({d[0]/Calculations.magnitude3D(d[0],d[3],d[0]+2):.2f}\\hat{{i}} - {d[3]/Calculations.magnitude3D(d[0],d[3],d[0]+2):.2f}\\hat{{j}} + {(d[0]+2)/Calculations.magnitude3D(d[0],d[3],d[0]+2):.2f}\\hat{{k}})}}$
        ${{\hspace{{4mm}} \\vec{{M_L}}=\\vec{{M_O}} \\cdot \\vec{{\\lambda_L}} = {((-1*d[3]/Calculations.magnitude3D(d[0],d[3],d[0]+2))*((-1*f[0]*d[9])-(d[6]*f[1])))+((d[0]+2)/Calculations.magnitude3D(d[0],d[3],d[0]+2)*(-1*f[0]*d[12])):.2f} N \\cdot m}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 

    Questionary(#3_1
        code = 2320031,
        no_pregunta = 3,
        complexity = M,
        topic = MO,
        subtopic = "Momento alrededor de un eje",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"""
        Considere la fuerza $F = {f[0]:.0f} \\text{{ kN}}$ aplicada en extremo del cartel publicitario de la izquierda y la fuerza $P = {f[1]:.0f} \\text{{ kN}}$ aplicada en el centro del cartel publicitario de la derecha. La fuerza $F$ es paralela al eje $x$ positivo, mientras que la fuerza $P$ es paralela al eje $z$ y forma un ángulo de inclinación de $\\theta = {a[0]:.0f}°$. Además, considere las siguientes dimensiones: $d_0 ={d[0]+3:.0f} \\text{{ m}}$, $d_1 ={d[0]:.0f} \\text{{m}}$ y $d_2 ={d[3]:.0f} \\text{{ m}}$. 
       
        Determine el momento generado por $F$ y $P$ respecto al eje $z$.""",
        no_answers = 1,
        a1_name = "Momento respecto al eje $z$ $[kN \\cdot m]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(-(((d[3])/2)*f[1]*Calculations.sine(a[0])+f[0]*(d[0]+3+((d[0])/2))),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "La fuerza $F$ únicamente tiene una componente en el eje $x$ y la fuerza $P$ tiene componentes en los ejes $y$ y $z$, utilice el ángulo $\\theta$ para descomponerla.",
        ayuda2 = "Encuentre el momento generado por cada fuerza y luego realice la sumatoria de momentos.",      
        ayuda3 = "El vector unitario del eje $z$ es $0\\hat{{i}}$ + $0\\hat{{j}}$ + $1\\hat{{k}}$.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        La magnitud del momento alrededor de un eje se calcula mediante el producto punto entre el vector de momento en un punto sobre el eje y el vector director del eje. A continuación, se presenta la solución sugerida para el ejercicio:  

        $\\textbf{{\\small 1. Vectores de posición y fuerza para F y P: }}$           

        En primer lugar, se determinan los vectores de posición y de fuerza para calcular el momento mediante el producto cruz.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\underline{{Fuerza \\text{{ }} F}}$
        
        ${{\hspace{{4mm}} \\vec{{F}} = [{f[0]}\\hat{{i}}+0\\hat{{j}}+0\\hat{{k}}] \\text{{ kN}}}}$             
        ${{\hspace{{4mm}} \\vec{{r_F}} = [0\\hat{{i}}+{(d[0]+3+((d[0])/2))}\\hat{{j}} + 0\\hat{{k}}] \\text{{ m}}}}$    

        $\\underline{{Fuerza \\text{{ }} P}}$

        ${{\hspace{{4mm}} \\vec{{P}} = [0\\hat{{i}}-{f[1]*Calculations.sine(a[0]):.2f}\\hat{{j}}+{f[1]*Calculations.cosine(a[0]):.2f}\\hat{{k}}] \\text{{ kN}}}}$           
        ${{\hspace{{4mm}} \\vec{{r_P}} = [{(d[3])/2}\\hat{{i}}+{(d[0]+3+((d[0])/2))}\\hat{{j}}+0\\hat{{k}}] \\text{{ m}}}}$          

        $\\textbf{{\\small 2. Cálculo de Momento para F y P: }}$      

        Al realizar el producto cruz entre los vectores de posición y las fuerzas $F$ y $P$, se obtienen los siguientes vectores de momento con respecto al origen.       

        ${{\hspace{{4mm}} \\vec{{M_{{OP}}}} = [{(d[0]+3+((d[0])/2))*f[1]*Calculations.cosine(a[0]):.2f}\\hat{{i}}-{(d[3]/2)*f[1]*Calculations.cosine(a[0]):.2f}\\hat{{j}}-{((d[3])/2)*f[1]*Calculations.sine(a[0]):.2f}\\hat{{k}}] kN \\cdot m}}$                
        
        ${{\hspace{{4mm}} \\vec{{M_{{OF}}}} = [0\\hat{{i}} + 0\\hat{{j}}-{f[0]*(d[0]+3+((d[0])/2)):.2f}\\hat{{k}}] kN \\cdot m}}$                  
        
        $\\textbf{{\\small 3. Sumatoria de momentos: }}$          

        Se realiza la sumatoria de los momentos generados por cada fuerza. 

        ${{\hspace{{4mm}} \\sum{{\\vec{{M_O}}}} = \\vec{{M_{{OP}}}} + \\vec{{M_{{OF}}}} = [{(d[0]+3+((d[0])/2))*f[1]*Calculations.cosine(a[0]):.2f}\\hat{{i}}-{(d[3]/2)*f[1]*Calculations.cosine(a[0]):.2f}\\hat{{j}}-{((d[3])/2)*f[1]*Calculations.sine(a[0])+f[0]*(d[0]+3+((d[0])/2)):.2f}\\hat{{k}}] kN \\cdot m}}$            
        
        $\\textbf{{\\small 4. Momento alrededor del eje z: }}$     

        El momento alrededor del eje $z$ corresponde a la componente en la dirección $\\hat{{k}}$ del vector momento obtenido respecto al origen.     

        ${{\hspace{{4mm}} \\vec{{M_z}} = \\vec{{M_O}} \\cdot \\vec{{\\lambda_{{\\hat{{k}}}}}} = 0*{(d[0]+3+((d[0])/2))*f[1]*Calculations.cosine(a[0]):.2f} + 0*-{(d[3]/2)*f[1]*Calculations.cosine(a[0]):.2f} + 1*{-(((d[3])/2)*f[1]*Calculations.sine(a[0])+f[0]*(d[0]+3+((d[0])/2))):.2f}}}$  
        ${{\hspace{{4mm}} \\vec{{M_z}} = {-(((d[3])/2)*f[1]*Calculations.sine(a[0])+f[0]*(d[0]+3+((d[0])/2))):.2f} kN \\cdot m }}$       
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    # Questionary(#4_1
    #     code = 2320041,
    #     no_pregunta = 4,
    #     complexity = M,
    #     topic = MO,
    #     subtopic = "Momento alrededor de un eje",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Calcule el momento alrededor del eje $x$ generado por las fuerzas ejercidas por el bloque de concreto: $F_1 = {f[0]:.0f} \\text{{ kN}}$, $F_2 = {f[1]:.0f} \\text{{ kN}}$ y su peso propio $W = {f[2]:.0f} \\text{{ kN}}$. La fuerza $F_1$ es paralela al eje $z$ y está aplicada en el centro de la cara frontal del bloque, mientras que la fuerza $F_2$ es paralela al eje $x$ y actúa en la parte superior, en el centro, como se muestra en la figura. Considere que $d_0 ={d[0]:.0f} \\text{{ m}}$, $d_1 ={d[3]:.0f} \\text{{ m}}$, $d_2 ={d[6]:.0f} \\text{{ m}}$, $\\theta = {a[0]:.0f}°$ y $\\phi = {a[4]:.0f}°$.",
    #     no_answers = 1,
    #     a1_name = "Momento sobre el eje $x$ $[kN \\cdot m]$",
    #     a2_name = "",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(-1*f[0]*Calculations.cosine(a[0])*(d[3]/2)-f[0]*Calculations.sine(a[0])*(d[0]/2),2),
    #     answer2 = lambda f, a, calc, c, d, m: 0,
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "Determine los vectores de cada una de las fuerzas. Utilice los ángulos $\\theta$ y $\\phi$ para descomponerlas.",
    #     ayuda2 = "Encuentre el momento generado por cada fuerza.",      
    #     ayuda3 = "Observe que la única fuerza que genera momento alrededor del eje $x$ es $\\vec{{F_1}}$. Por lo tanto, al calcular este valor, obtiene directamente el momento requerido.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     A continuación, se muestra una posible solución al problema:

    #     $\\textbf{{\\small 1. Definición de los vectores fuerza y posición: }}$ 
        
    #     ${{\hspace{{4mm}} \\vec{{F_1}} = (0\\hat{{i}}+{f[0]*Calculations.sine(a[0])}\\hat{{j}}-{f[0]*Calculations.cosine(a[0])}\\hat{{k}})[N]}}$
    #     ${{\hspace{{4mm}} \\vec{{r_{{F_1}}}} = ({d[3]+d[0]/2}\\hat{{i}}+{d[6]/2}\\hat{{j}}+{d[0]/2}\\hat{{k}})[m]}}$

    #     ${{\hspace{{4mm}} \\vec{{F_2}} = (-{f[1]*Calculations.cosine(a[1])}\\hat{{i}}-{f[1]*Calculations.sine(a[1])}\\hat{{j}}+0\\hat{{k}})[N]}}$
    #     ${{\hspace{{4mm}} \\vec{{r_{{F_2}}}} = ({d[3]+d[0]}\\hat{{i}}+{d[6]}\\hat{{j}}+0\\hat{{k}})[m]}}$

    #     ${{\hspace{{4mm}} \\vec{{W}} = (0\\hat{{i}}-{f[2]}\\hat{{j}}+0\\hat{{k}})[N]}}$
    #     ${{\hspace{{4mm}} \\vec{{r_{{W}}}} = ({d[3]+d[0]/2}\\hat{{i}}+0\\hat{{j}}+0\\hat{{k}})[m]}}$
        
    #     $\\textbf{{\\small 2. Momento generado alrededor del punto O: }}$

    #     Para $F_1$:

    #     ${{\hspace{{4mm}} \\vec{{M_O}} = ({-1*d[3]*f[0]*Calculations.cosine(a[0])-f[0]*Calculations.sine(a[0])*d[0]/2}\\hat{{i}}+{f[0]*Calculations.cosine(a[0])*(d[3]+d[0]/2)}\\hat{{j}}+{f[0]*Calculations.sine(a[0])*(d[3]+d[0]/2)}\\hat{{k}})[N \\cdot m]}}$
        
    #     Para $F_2$:

    #     ${{\hspace{{4mm}} \\vec{{M_O}} = (0\\hat{{i}}+0\\hat{{j}}+{f[1]*Calculations.cosine(a[1])*d[6]-f[1]*Calculations.sine(a[1])*(d[3]+d[0])}\\hat{{k}})[N \\cdot m]}}$
       
    #     Para $W$:

    #     ${{\hspace{{4mm}} \\vec{{M_O}} = (0\\hat{{i}}+0\\hat{{j}}-{f[2]*(d[3]+d[0]/2)}\\hat{{k}})[N \\cdot m]}}$

    #     $\\textbf{{\\small 3. Momento generado alrededor del eje $x$: }}$

    #     Como se puede ver, la unica fuerza que genera momento sobre el eje $x$, esta siendo la tabla de madera, es $F_1$, por lo que:

    #     ${{\hspace{{4mm}} \\vec{{M_z}} = \\vec{{M_O}} \\cdot \\vec{{\\lambda_{{\\hat{{k}}}}}} = 0*{(d[0]+3+((d[0])/2))*f[1]*Calculations.cosine(a[0]):.2f} + 0*-{(d[3]/2)*f[1]*Calculations.cosine(a[0]):.2f} + 1*{-(((d[3])/2)*f[1]*Calculations.sine(a[0])+f[0]*(d[0]+3+((d[0])/2))):.2f}}}$  
    #     ${{\hspace{{4mm}} \\vec{{M_z}} = {-(((d[3])/2)*f[1]*Calculations.sine(a[0])+f[0]*(d[0]+3+((d[0])/2))):.2f} kN \\cdot m }}$       
    #     ${{\hspace{{4mm}} \\sum{{\\vec{{M}}}} \\cdot \\hat{{i}} = ({-1*d[3]*f[0]*Calculations.cosine(a[0])-f[0]*Calculations.sine(a[0])*d[0]/2})[N \\cdot m]}}$
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    #========================================================  MOMENTO  =========================================================
    #--------------------------------------        Momento alrededor de un eje      --------------------------------------------
    #-------------------------------------------------       Nivel Díficil   ---------------------------------------------------
    #-------------------------------------------------      Code: 23300##    --------------------------------------------------

    Questionary(#1_1
        code = 0,
        no_pregunta = 1,
        complexity = D,
        topic = MO,
        subtopic = "Momento alrededor de un eje",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Está sección pronto estará disponible.",
        no_answers = 0,
        a1_name = AX,
        a2_name = AY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(0, 2),
        answer2 = lambda f, a, calc, c, d, m: np.round(0, 2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A1,
        ayuda2 = A2,
        ayuda3 = A3,
        respuesta_P1 = lambda fa, a, calc, c, d, m: f"",
        respuesta_P2 = lambda fa, a, calc, c, d, m: f"",
        respuesta_P3 = lambda fa, a, calc, c, d, m: f"",
        calculos = 'operations',
        ),


    # Questionary(#1_1
    #     code = 2330011,
    #     no_pregunta = 1,
    #     complexity = D,
    #     topic = MO,
    #     subtopic = "Momento alrededor de un eje",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine el momento total (magnitud) que resulta de las fuerzas: $F_1 = {f[0]:.0f}$, $F_2 = {f[1]:.0f}$, $F_3 = {f[2]:.0f}$ aplicadas sobre el cuerpo mostrado, proyectado sobre el eje $y$. Tenga en cuenta que $x_0 = {c[0]:.0f}[m]$, $x_1 = {c[4]:.0f}[m]$, $x_2 = {c[5]:.0f}[m]$, $x_3 = {c[3]:.0f}[m]$, $x_4 = {c[1]:.0f}[m]$ y $x_5 = {c[2]:.0f}[m]$",
    #     no_answers = 1,
    #     a1_name = "Momento en el eje $Y$ [$N \\cdot m$]",
    #     a2_name = "",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(((c[0]*f[0]*(c[2]-c[5]))/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5]))-((f[0]*(c[3]-c[0])*c[5])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5]))-(c[0]*f[1])+((c[5]*f[2]*(c[0]-c[3]))/Calculations.magnitude(c[0]-c[3],c[4]-c[1])),2),
    #     answer2 = lambda f, a, calc, c, d, m: 0,
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "Se le dieron puntos por donde paa la linea de acción de las fuerzas. Uselos para hallar la dirección (vector unitario) y asi encontrar los vectores de cada fuerza.",
    #     ayuda2 = "Realice sumatoria de momentos con los encontrados, que son generados por cada fuerza con respecto al origen.$",      
    #     ayuda3 = "El vector unitario del eje $y$ denominado como $\\hat{{j}} es (0\\hat{{i}} + 1\\hat{{j}} + 0\\hat{{k}}).",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     A continuacion se presenta una posible solución para el problema:
        
    #     $\\textbf{{\\small 1. Hallar los vectores fuerza - Vector Unitario:}}$
    #     Usando las coordenadas dadas en el ejercicio, se puede determinar la direccion del vector fuerza por medio de la resta entre ellas.

    #     Para $\\vec{{F_1}}$:
    #     ${{\hspace{{4mm}} \\vec{{f_1}} = ({c[3]-c[0]})\\hat{{i}}+({c[1]-c[4]})\\hat{{j}}+({c[2]-c[5]})\\hat{{k}}}}$     
    #     ${{\hspace{{4mm}} \\vec{{\\lambda_{{f_1}}}} = \\dfrac{c[3]-c[0]}{{\\sqrt{{{(c[3]-c[0])}^2 + {(c[1]-c[4])}^2 + {(c[2]-c[5])}^2}}}}\\hat{{i}}+\\dfrac{c[1]-c[4]}{{\\sqrt{{{(c[3]-c[0])}^2 + {(c[1]-c[4])}^2 + {(c[2]-c[5])}^2}}}}\\hat{{j}}+\\dfrac{c[2]-c[5]}{{\\sqrt{{{(c[3]-c[0])}^2 + {(c[1]-c[4])}^2 + {(c[2]-c[5])}^2}}}}\\hat{{k}}}}$
    #     ${{\hspace{{4mm}} \\vec{{\\lambda_{{f_1}}}} = ({(c[3]-c[0])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])})\\hat{{i}}+({(c[1]-c[4])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])})\\hat{{j}}+({(c[2]-c[5])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])})\\hat{{k}}}}$

    #     Multiplicando por $F_1$ nos queda:
    #     ${{\hspace{{4mm}} \\vec{{F_1}} = (({f[0]*(c[3]-c[0])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])})\\hat{{i}}+({f[0]*(c[1]-c[4])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])})\\hat{{j}}+({f[0]*(c[2]-c[5])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])})\\hat{{k}})[N]}}$
        
    #     Para $\\vec{{F_2}}$:
    #     ${{\hspace{{4mm}} \\vec{{f_2}} = ({c[0]-c[0]})\\hat{{i}}+({c[4]-c[4]})\\hat{{j}}+({c[5]-c[2]})\\hat{{k}}}}
    #     ${{\hspace{{4mm}} \\vec{{\\lambda_{{f_2}}}} = 0\\hat{{i}} + 0\\hat{{j}} + 1\\hat{{k}}}}$

    #     Multiplicando por $F_2$ nos queda:
    #     ${{\hspace{{4mm}} \\vec{{F_2}} = (0\\hat{{i}} + 0\\hat{{j}} + {f[1]}\\hat{{k}})[N]}}$
        
    #     Para $\\vec{{F_3}}$:
    #     ${{\hspace{{4mm}} \\vec{{f_3}} = ({c[0]-c[3]})\\hat{{i}}+({c[4]-c[1]})\\hat{{j}}+({c[5]-c[5]})\\hat{{k}}}}$     
    #     ${{\hspace{{4mm}} \\vec{{\\lambda_{{f_3}}}} = \\dfrac{c[0]-c[3]}{{\\sqrt{{{(c[0]-c[3])}^2 + {(c[4]-c[1])}^2}}}}\\hat{{i}} + \\dfrac{c[4]-c[1]}{{\\sqrt{{{(c[0]-c[3])}^2 + {(c[4]-c[1])}^2}}}}\\hat{{j}} + 0\\hat{{k}}}}$
    #     ${{\hspace{{4mm}} \\vec{{\\lambda_{{f_3}}}} = ({(c[0]-c[3])/Calculations.magnitude(c[0]-c[3],c[4]-c[1])})\\hat{{i}} + ({(c[4]-c[1])/Calculations.magnitude(c[0]-c[3],c[4]-c[1])})\\hat{{j}} + 0\\hat{{k}}}}$

    #     Multiplicando por $F_3$ nos queda:
    #     ${{\hspace{{4mm}} \\vec{{F_3}} = (({f[2]*(c[0]-c[3])/Calculations.magnitude(c[0]-c[3],c[4]-c[1])})\\hat{{i}} + ({f[2]*(c[4]-c[1])/Calculations.magnitude(c[0]-c[3],c[4]-c[1])})\\hat{{j}} + 0\\hat{{k}})[N]}}$
        
    #     $\\textbf{{\\small 2. Encontrar momento para cada fuerza - Alrededor del origen:}}$
    #     Para $\\vec{{F_1}}$
    #     Haciendo el producto cruz queda el siguiente resultado:
    #     ${{\hspace{{4mm}} \\vec{{M_{{F_1}}}} = (({c[4]*f[0]*(c[2]-c[5])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])}-{c[5]*f[0]*(c[1]-c[4])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])})\\hat{{i}}-({c[0]*f[0]*(c[2]-c[5])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])}-{c[5]*f[0]*(c[3]-c[0])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])})\\hat{{j}}+({c[0]*f[0]*(c[1]-c[4])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])}-{c[4]*f[0]*(c[3]-c[0])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])})\\hat{{k}})[N \\cdot m]}}$
    #     ${{\hspace{{4mm}} \\vec{{M_{{F_1}}}} = (({c[4]*f[0]*(c[2]-c[5])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])-(c[5]*f[0]*(c[1]-c[4])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5]))})\\hat{{i}}-({c[0]*f[0]*(c[2]-c[5])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])-(c[5]*f[0]*(c[3]-c[0])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5]))})\\hat{{j}}+({c[0]*f[0]*(c[1]-c[4])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])-(c[4]*f[0]*(c[3]-c[0])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5]))})\\hat{{k}})[N \\cdot m]}}$
        
    #     Para $\\vec{{F_2}}$
    #     Haciendo el producto cruz queda el siguiente resultado:
    #     ${{\hspace{{4mm}} \\vec{{M_{{F_2}}}} = (({c[4]*f[1]})\\hat{{i}} - ({c[0]*f[1]})\\hat{{j}} + 0\\hat{{k}})[N \\cdot m]}}$
        
    #     Para $\\vec{{F_3}}$
    #     Haciendo el producto cruz queda el siguiente resultado:
    #     ${{\hspace{{4mm}} \\vec{{M_{{F_3}}}} = (({-1*c[5]*f[2]*(c[4]-c[1])/Calculations.magnitude(c[0]-c[3],c[4]-c[1])})\\hat{{i}}+({-1*c[5]*f[2]*(c[0]-c[3])/Calculations.magnitude(c[0]-c[3],c[4]-c[1])})\\hat{{j}}+({c[3]*f[2]*(c[4]-c[1])/Calculations.magnitude(c[0]-c[3],c[4]-c[1])}-{c[1]*f[2]*(c[0]-c[3])/Calculations.magnitude(c[0]-c[3],c[4]-c[1])})\\hat{{k}})[N \\cdot m]}}$
    #     ${{\hspace{{4mm}} \\vec{{M_{{F_3}}}} = (({-1*c[5]*f[2]*(c[4]-c[1])/Calculations.magnitude(c[0]-c[3],c[4]-c[1])})\\hat{{i}}+({-1*c[5]*f[2]*(c[0]-c[3])/Calculations.magnitude(c[0]-c[3],c[4]-c[1])})\\hat{{j}}+({c[3]*f[2]*(c[4]-c[1])/Calculations.magnitude(c[0]-c[3],c[4]-c[1])-(c[1]*f[2]*(c[0]-c[3])/Calculations.magnitude(c[0]-c[3],c[4]-c[1]))})\\hat{{k}})[N \\cdot m]}}$
        
    #     $\\textbf{{\\small 3. Sumatoria de momentos generados por las fuerzas:}}$
    #     Sumando los resultados para cada componente encontrados anteriormente determinamos que:
    #     ${{\hspace{{4mm}} \\sum{{M}} = (({(c[4]*f[0]*(c[2]-c[5])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])-(c[5]*f[0]*(c[1]-c[4])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])))+(c[4]*f[1])+(-1*c[5]*f[2]*(c[4]-c[1])/Calculations.magnitude(c[0]-c[3],c[4]-c[1]))})\\hat{{i}} + ({(c[0]*f[0]*(c[2]-c[5])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])-(c[5]*f[0]*(c[3]-c[0])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])))+(c[0]*f[1])+(-1*c[5]*f[2]*(c[0]-c[3])/Calculations.magnitude(c[0]-c[3],c[4]-c[1]))})\\hat{{j}} + ({(c[0]*f[0]*(c[1]-c[4])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])-(c[4]*f[0]*(c[3]-c[0])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])))+(c[3]*f[2]*(c[4]-c[1])/Calculations.magnitude(c[0]-c[3],c[4]-c[1])-(c[1]*f[2]*(c[0]-c[3])/Calculations.magnitude(c[0]-c[3],c[4]-c[1])))})\\hat{{k}})[N \\cdot m]}}$
        
    #     $\\textbf{{\\small 3. Sumatoria de momentos generados por las fuerzas:}}$
    #     ${{\hspace{{4mm}} \\sum{{M}} \\cdot \\hat{{j}} = {(c[0]*f[0]*(c[2]-c[5])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])-(c[5]*f[0]*(c[3]-c[0])/Calculations.magnitude3D(c[3]-c[0],c[1]-c[4],c[2]-c[5])))+(c[0]*f[1])+(-1*c[5]*f[2]*(c[0]-c[3])/Calculations.magnitude(c[0]-c[3],c[4]-c[1]))}[N \\cdot m]}}$
        
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    # Questionary(#2_1
    #     code = 2330021,
    #     no_pregunta = 2,
    #     complexity = D,
    #     topic = MO,
    #     subtopic = "Momento alrededor de un eje",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Considere las fuerzas $F_1 = {f[0]:.0f}$ y $F_2 = {f[1]:.0f}$ ejercidas sobre el elemento mostrado en la figura. Calcule el momento alrededor de la linea L dada por el vecto $\\vec{{v}}= {d[0]:.0f}\\hat{{i}}+{d[0]+2:.0f}\\hat{{j}}+{d[0]-1:.0f}\\hat{{k}}$, teniendo en cuenta que $x_0 ={d[3]:.0f}$, $x_1 ={d[6]:.0f}$ y $x_2 ={d[9]:.0f}$.",
    #     no_answers = 1,
    #     a1_name = "Momento sobre la linea $L$ [$N \\cdot m$]",
    #     a2_name = "",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(((f[0]*d[6]*d[3]/Calculations.magnitude(d[6],d[9]))*(d[0]/Calculations.magnitude3D(d[0],d[0]+2,d[0]-1)))+((f[0]*d[9]*d[3]/Calculations.magnitude(d[6],d[9]))*((d[0]+2)/Calculations.magnitude3D(d[0],d[0]+2,d[0]-1)))+((-1*f[1]*d[9])*((d[0]-1)/Calculations.magnitude3D(d[0],d[0]+2,d[0]-1))),2),
    #     answer2 = lambda f, a, calc, c, d, m: 0,
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "Se le dieron dimensiones por donde paa la linea de acción de la fuerza $F_1$. Uselos para hallar la dirección (vector unitario) y asi encontrar el vector de la fuerza.",
    #     ayuda2 = "Encuentre el momento generado por cada fuerza con respecto al origen y luego haga sumatoria de momentos.",      
    #     ayuda3 = "Saque el vector unitario de la linea y haga el producto punto con el vector hallado de la sumatoria.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     A continuacion se presenta una posible solución para el problema:
        
    #     $\\textbf{{\\small 1. Hallar los vectores fuerza - Vector Unitario:}}$
    #     Usando las dimensiones dadas en el ejercicio, se puede determinar la direccion del vector fuerza $F_1$.
    
    #     ${{\hspace{{4mm}} \\vec{{\\lambda_{{f_1}}}} = \\dfrac{d[9]}{{\\sqrt{{{d[9]}^2 + {d[6]}^2}}}}\\hat{{i}}-\\dfrac{d[6]}{{\\sqrt{{{d[9]}^2 + {d[6]}^2}}}}\\hat{{j}}+0\\hat{{k}}}}$
    #     Multiplicando el vector hallado por la magnitud de $F_1$, encontramos que:
    #     ${{\hspace{{4mm}} \\vec{{F_1}} = ({d[9]*f[0]/Calculations.magnitude(d[9],d[6])}\\hat{{i}}-{d[6]*f[0]/Calculations.magnitude(d[9],d[6])}\\hat{{j}}+0\\hat{{k}})[N]}}$
    #     ${{\hspace{{4mm}} \\vec{{F_2}} = (0\\hat{{i}}-{f[1]}\\hat{{j}}+0\\hat{{k}})[N]}}$

    #     $\\textbf{{\\small 2. Momento con respecto al punto $O$:}}$
    #     ${{\hspace{{4mm}} \\vec{{M_{{F_1}}}} = ({d[6]*f[0]*d[3]/Calculations.magnitude(d[9],d[6])}\\hat{{i}}+{d[9]*f[0]*d[3]/Calculations.magnitude(d[9],d[6])}\\hat{{j}}+0\\hat{{k}})[N \\cdot m]}}$        
    #     ${{\hspace{{4mm}} \\vec{{M_{{F_2}}}} = (0\\hat{{i}}+0\\hat{{j}}-{f[1]*d[9]}\\hat{{k}})[N \\cdot m]}}$

    #     $\\textbf{{\\small 3. Sumatoria de momento:}}$
    #     ${{\hspace{{4mm}} \\sum{{\\vec{{M}}}} = ({d[6]*f[0]*d[3]/Calculations.magnitude(d[9],d[6])}\\hat{{i}}+{d[9]*f[0]*d[3]/Calculations.magnitude(d[9],d[6])}\\hat{{j}}-{f[1]*d[9]}\\hat{{k}})[N \\cdot m]}}$

    #     $\\textbf{{\\small 4. Vector director de la linea $L$ - Vector Unitario:}}$
    #     ${{\hspace{{4mm}} \\vec{{\\lambda_{{v}}}} = {d[0]/Calculations.magnitude3D(d[0],d[0]+2,d[0]-1)}\\hat{{i}}+{(d[0]+2)/Calculations.magnitude3D(d[0],d[0]+2,d[0]-1)}\\hat{{j}}+{(d[0]-1)/Calculations.magnitude3D(d[0],d[0]+2,d[0]-1)}\\hat{{k}}}}$
        
    #     $\\textbf{{\\small 5. Momento sobre la linea $L$ - Producto Punto:}}$
    #     ${{\hspace{{4mm}} \\sum{{\\vec{{M}}}} \\cdot \\vec{{\\lambda_{{v}}}} = {((f[0]*d[6]*d[3]/Calculations.magnitude(d[6],d[9]))*(d[0]/Calculations.magnitude3D(d[0],d[0]+2,d[0]-1)))+((f[0]*d[9]*d[3]/Calculations.magnitude(d[6],d[9]))*((d[0]+2)/Calculations.magnitude3D(d[0],d[0]+2,d[0]-1)))+((-1*f[1]*d[9])*((d[0]-1)/Calculations.magnitude3D(d[0],d[0]+2,d[0]-1)))}[N \\cdot m]}}$
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    # Questionary(#3_1
    #     code = 2330031,
    #     no_pregunta = 3,
    #     complexity = D,
    #     topic = MO,
    #     subtopic = "Momento alrededor de un eje",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Encuentre el momento generado por $F_1 = {f[0]:.0f}$, $F_2 = {f[1]:.0f}$, $F_3 = {f[2]:.0f}$ aplicadas sobre la viga y columna sobre la linea $L$ teniendo en cuenta que $x_0 = {d[0]:.0f}[m]$, $x_1 = {d[3]:.0f}[m]$, $x_2 = {d[6]:.0f}[m]$, $x_3 = {d[9]:.0f}[m]$, $x_4 = {d[12]:.0f}[m]$ y $x_5 = {d[15]:.0f}[m]$. Considere que $F_1$ se ejerce paralela al eje $x$, $F_2$ se ejerce paralelo al eje $y$ negativo y $F_3$ se ejerce paralelo al eje $z$ negativo.",
    #     no_answers = 1,
    #     a1_name = "Momento sobre la linea $L$ [$N \\cdot m$]",
    #     a2_name = "",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round((d[12]/Calculations.magnitude(d[12],d[15]))*(f[2]*(d[0]+d[3]/2))-((d[15]/Calculations.magnitude(d[12],d[15]))*(f[0]*(d[3]+d[6])+f[2]*(d[0]+d[3]/2))),2),
    #     answer2 = lambda f, a, calc, c, d, m: 0,
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "Revise cuidadosamente donde se encuentran ubicadas las fuerzas para poder encontrar su vector posición.",
    #     ayuda2 = "Encuentre el momento con respecto al origen para cada fuerza y haga sumatoria para hallar el vector momento total.",      
    #     ayuda3 = "Saque el vector unitario de la linea y haga el producto punto con el vector hallado de la sumatoria de momento.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     A continuacion se presenta una posible solución para el problema:
        
    #     $\\textbf{{\\small 1. Determinar los vectores fuerza:}}$
        
    #     ${{\hspace{{4mm}} \\vec{{F_1}} = ({f[0]}\\hat{{i}}+0\\hat{{j}}+0\\hat{{k}})[N]}}$
    #     ${{\hspace{{4mm}} \\vec{{F_2}} = (0\\hat{{i}}-{f[1]}\\hat{{j}}+0\\hat{{k}})[N]}}$
    #     ${{\hspace{{4mm}} \\vec{{F_3}} = (0\\hat{{i}}+0\\hat{{j}}-{f[2]}\\hat{{k}})[N]}}$

    #     $\\textbf{{\\small 2. Encontrar el momento generado por cada fuerza:}}$
    #     Para $F_1$
    #     ${{\hspace{{4mm}} \\vec{M} = (0\\hat{{i}}+0\\hat{{j}}-{f[0]*(d[3]+d[6])}\\hat{{k}})[N \\cdot m]}}$
    #     Para $F_2$
    #     ${{\hspace{{4mm}} \\vec{M} = (0\\hat{{i}}+0\\hat{{j}}-{f[1]*(d[9]/2)}\\hat{{k}})[N \\cdot m]}}$
    #     Para $F_3$
    #     ${{\hspace{{4mm}} \\vec{M} = (0\\hat{{i}}+{f[2]*(d[0]+d[3]/2)}\\hat{{j}}+0\\hat{{k}})[N \\cdot m]}}$

    #     $\\textbf{{\\small 3. Sumatoria de Momentos:}}$
    #     ${{\hspace{{4mm}} \\sum{{\\vec{{M}}}} = (0\\hat{{i}}+{f[2]*(d[0]+d[3]/2)}\\hat{{j}}-{f[0]*(d[3]+d[6])+f[2]*(d[0]+d[3]/2)}\\hat{{k}})[N \\cdot m]}}$

    #     $\\textbf{{\\small 4. Vector Unitario recta $L$:}}$
    #     ${{\hspace{{4mm}} \\vec{{\\lambda_L}} = 0\\hat{{i}}+{d[12]/Calculations.magnitude(d[12],d[15])}\\hat{{j}}+{d[15]/Calculations.magnitude(d[12],d[15])}\\hat{{k}}}}$

    #     $\\textbf{{\\small 5. Momento sobre la linea $L$:}}$
    #     ${{\hspace{{4mm}} \\sum{{\\vec{{M}}}} \\cdot \\vec{{\\lambda_L}} = {(d[12]/Calculations.magnitude(d[12],d[15]))*(f[2]*(d[0]+d[3]/2))-((d[15]/Calculations.magnitude(d[12],d[15]))*(f[0]*(d[3]+d[6])+f[2]*(d[0]+d[3]/2)))}[N \\cdot m]}}$
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    # Questionary(#4_1
        # code = 2330041,
        # no_pregunta = 4,
        # complexity = D,
        # topic = MO,
        # subtopic = "Momento alrededor de un eje",
        # version = 1,
        # pregunta = lambda f, a, calc, c, d, m: f"Considere las tensiones $T_1 = {f[0]:.0f}[N]$, $T_2 = {f[1]:.0f}[N]$, $T_3 = {f[2]:.0f}[N]$ producidas por el elemento colgado. Encuentre el momento generado sobre el eje $x$ teniendo en cuenta que $x_0 = {d[0]:.0f}[m], $\\theta = {a[0]:.0f}°$ y $\\phi = {a[4]:.0f}°.",
        # no_answers = 1,
        # a1_name = "Momento sobre el eje $x$ [$N \\cdot m$]",
        # a2_name = "",
        # a3_name = "",
        # answer1 = lambda f, a, calc, c, d, m: np.round(f[1]*d[0]*(Calculations.sine(a[0]))**2-(f[2]*d[0]*Calculations.sine(a[1])),2),
        # answer2 = lambda f, a, calc, c, d, m: 0,
        # answer3 = lambda f, a, calc, c, d, m: 0,
        # ayuda1 = "Use los angulos dados tanto para encontrar las componentes de las tensiones como para hallar el vector posición de $T_2$.",
        # ayuda2 = "Encuentre el momento con respecto al origen para cada fuerza y haga sumatoria para hallar el vector momento total.",      
        # ayuda3 = "Haga el producto punto con el vector encontrado en la sumatoria y el vector unitario del eje x, siendo $1\\hat{{i}}+0\\hat{{j}}+0\\hat{{k}}$.",
        # respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        # A continuacion se presenta una posible solución para el problema:
        
        # $\\textbf{{\\small 1. Determinar los vectores tension y su vector posición correspondiente:}}$
        
        # ${{\hspace{{4mm}} \\vec{{T_1}} = ({-1*f[0]*Calculations.cosine(a[1])}\\hat{{i}}+{f[0]*Calculations.sine(a[1])}\\hat{{j}}+0\\hat{{k}})[N]}}$
        # ${{\hspace{{4mm}} \\vec{{r_{{T_1}}}} = ({d[0]}\\hat{{i}}+0\\hat{{j}}+0\\hat{{k}})[m]}}$
        # ${{\hspace{{4mm}} \\vec{{T_2}} = ({f[1]*Calculations.cosine(a[1])*Calculations.cosine(a[0])}\\hat{{i}}+{f[1]*Calculations.sine(a[1])}\\hat{{j}}+{f[1]*Calculations.cosine(a[1])*Calculations.sine(a[0])}\\hat{{k}})[N]}}$
        # ${{\hspace{{4mm}} \\vec{{r_{{T_2}}}} = ({-1*d[0]*Calculations.cosine(a[0])}\\hat{{i}}+0\\hat{{j}}-{d[0]*Calculations.sine(a[0])}\\hat{{k}})[m]}}$
        # ${{\hspace{{4mm}} \\vec{{T_3}} = (0\\hat{{i}}+{f[2]*Calculations.sine(a[1])}\\hat{{j}}-{f[2]*Calculations.cosine(a[1])}\\hat{{k}})[N]}}$
        # ${{\hspace{{4mm}} \\vec{{r_{{T_3}}}} = (0\\hat{{i}}+0\\hat{{j}}+{d[0]}\\hat{{k}})[m]}}$

        # $\\textbf{{\\small 2. Momento alrededor del punto $O$:}}$
        # Para $T_1$
        # ${{\hspace{{4mm}} \\vec{{M}} = (0\\hat{{i}}+0\\hat{{j}}+{d[0]*f[0]*Calculations.sine(a[1])}\\hat{{k}})[N \\cdot m]}}$
        # Para $T_2$
        # ${{\hspace{{4mm}} \\vec{{M}} = ({d[0]*f[1]*(Calculations.sine(a[1]))**2}\\hat{{i}}+0\\hat{{j}}-{d[0]*f[1]*Calculations.sine(a[0])*Calculations.cosine(a[1])}\\hat{{k}})[N \\cdot m]}}$
        # Para $T_3$
        # ${{\hspace{{4mm}} \\vec{{M}} = ({-1*d[0]*f[2]*Calculations.sine(a[1])}\\hat{{i}}+0\\hat{{j}}+0\\hat{{k}})[N \\cdot m]}}$

        # $\\textbf{{\\small 3. Sumatoria de momentos:}}$
        # ${{\hspace{{4mm}} \\sum{{\\vec{{M}}}} = ({d[0]*f[1]*(Calculations.sine(a[1]))**2-d[0]*f[2]*Calculations.sine(a[1])}\\hat{{i}}+0\\hat{{j}}+{d[0]*f[0]*Calculations.sine(a[1])-d[0]*f[1]*Calculations.sine(a[0])*Calculations.cosine(a[1])}\\hat{{k}})[N \\cdot m]}}$
        
        # $\\textbf{{\\small 4. Producto punto con el vector unitario del eje $x$:}}$
        # ${{\hspace{{4mm}} \\sum{{\\vec{{M}}}} \\cdot \\hat{{i}}= {d[0]*f[1]*(Calculations.sine(a[1]))**2-d[0]*f[2]*Calculations.sine(a[1])}[N \\cdot m]}}$
        # """,   
        # respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        # respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        # calculos='operations'
        # ),


    #========================================================  MOMENTO  =========================================================
    #-------------------------------------------------       Momento par      ---------------------------------------------------
    #-------------------------------------------------       Nivel Fácil   ------------------------------------------------------
    #-------------------------------------------------      Code: 24100##    ----------------------------------------------------

    Questionary(#1_1
        code = 2410011,
        no_pregunta = 1,
        complexity = F,
        topic = MO,
        subtopic = "Momento par",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Calcule el momento generado por el par de fuerzas $F= {f[0]:.0f}$ $\\text{{ N}}$ mostrado en la figura. Considere que la distancia $d_1 = {d[0]+3:.0f} \\text{{ cm}}$.", 
        no_answers = 1,
        a1_name = "Momento generado por $F$ $[N \\cdot m]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*(4*(d[0]+3)/5)/100,2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MPP1,
        ayuda2 = MPP2,      
        ayuda3 = MPP3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento generado por un par de fuerzas se define como $M = F \\cdot d$, donde $F$ es la magnitud de las fuerzas pares y $d$ es la distancia perpendicular entre estas. A continuación se presenta la solución sugerida para el ejercicio:
       
        $\\textbf{{\\small 1. Distancia perpendicular: }}$

        Se da como referencia el triángulo $6-8-10$, con este hallamos la distancia perpendicular $(d_y)$, la cual esta dada por la función trigonométrica del seno:
        
        ${{\hspace{{4mm}} d_y = d_1 * \\dfrac{{Cateto \\text{{ }} opuesto}}{{Hipotenusa}} }}$    
        
        ${{\hspace{{4mm}} d_y = {d[0]+3:.0f} \\cdot \\dfrac{{8}}{{10}} }}$       
        
        ${{\hspace{{4mm}} d_y = {((4*(d[0]+3)/5))} \\text{{ cm}} = {((4*(d[0]+3)/5)/100)} \\text{{ m}} }} $
        
        $\\textbf{{\\small 2. Calculo de momento par: }}$

        ${{\hspace{{4mm}} M =  F \\cdot d_y}}$                           
        ${{\hspace{{4mm}} M =  ({(f[0]*(4*(d[0]+3)/5)/100):.2f}\\text{{ }} \\hat{{k}}) N \\cdot m}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 2410021,
        no_pregunta = 2,
        complexity = F,
        topic = MO,
        subtopic = "Momento par",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud del momento generado alrededor del punto $A$ y el punto $B$, por las fuerzas $F_1 = {f[0]:.0f} \\text{{ kN}}$, $F_2 = {f[1]:.0f} \\text{{ kN}}$ que actúan sobre el cuerpo mostrado en la figura. Tenga en cuenta que $d_0 = {d[0]:.0f} \\text{{ m}}$ y $d_1 = {d[0]+2:.0f}\\text{{ m}}$",
        no_answers = 2,
        a1_name = "Momento alrededor de $A$ en $[N \\cdot m]$",
        a2_name = "Momento alrededor de $B$ en $[N \\cdot m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[0]+f[1])*(d[0]+2-1),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((f[0]+f[1])*(d[0]+2-1),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MPP1,
        ayuda2 = MPP4,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento generado por un par de fuerzas se define como $M = F \\cdot d$, donde $F$ es la magnitud de las fuerzas pares y $d$ es la distancia perpendicular entre estas. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Momento alrededor de A: }}$ 

        ${{\hspace{{4mm}} \\sum{{\\vec{{M_A}}}} = F_1 \\cdot (d_1-1) + F_2 \\cdot (d_1-1)}}$             
        ${{\hspace{{4mm}} \\sum{{\\vec{{M_A}}}} = {((f[1]+f[0])*((d[0]+2)-1)):.2f} \\text{{ }} N \\cdot m}}$      
        
        $\\textbf{{\\small 2. Momento alrededor de B: }}$ 

        Utilizando momentos pares:

        ${{\hspace{{4mm}} \\sum{{\\vec{{M_B}}}} = F_1 \\cdot (d_1-1) + F_2 \\cdot (d_1-1)}}$             
        ${{\hspace{{4mm}} \\sum{{\\vec{{M_B}}}} = {((f[1]+f[0])*((d[0]+2)-1)):.2f} \\text{{ }} N \\cdot m}}$  

        Utilizando sumatoria de momentos en el punto $B$:

        ${{\hspace{{4mm}} \\sum{{\\vec{{M_B}}}} = F_1 \\cdot (d_0-1) + F_2 \\cdot (d_0-1) + F_1 \\cdot (d_1-d_0) + F_2 \\cdot (d_1-d_0)}}$                  
        ${{\hspace{{4mm}} \\sum{{\\vec{{M_B}}}} = {f[0]*(d[0]-1)+f[1]*(d[0]-1)+f[0]*(d[0]+2-d[0])+f[1]*(d[0]+2-d[0]):.2f} \\text{{ }} N \\cdot m }}$

        En conclusión, se demuestra que un par de fuerzas de igual magnitud, dirección y sentidos opuestos genera un momento cuya magnitud y dirección son independientes del punto de referencia. Es decir, el momento producido por un par es igual respecto a cualquier punto del cuerpo.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 2410031,
        no_pregunta = 3,
        complexity = F,
        topic = MO,
        subtopic = "Momento par",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Una pieza de madera laminada está siendo taladrada para fijarla a un banco de trabajo mediante tornillos. Durante el taladrado, se aplica un momento de $M = {m[0]:.0f}\\text{{ }} N \\cdot m$ sobre la pieza de madera. La fijación se realiza mediante dos clavos ubicados en las siguientes combinaciones: $A$ y $B$, $B$ y $C$. Determine la magnitud de las fuerzas pares que deben ejercer los clavos para contrarrestar el momento. Considere que $d_0 = {d[0]+40:.0f} \\text{{ cm}}$ y $d_1 = {d[3]+40:.0f} \\text{{ cm}}$.",
        no_answers = 2,
        a1_name = "Magnitud par de fuerzas entre $A$ y $B$ $[N]$",
        a2_name = "Magnitud par de fuerzas entre $B$ y $C$ $[N]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(m[0]/((d[0]+40)/100),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(m[0]/((d[3]+40)/100),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(m[0]/(Calculations.magnitude(d[0]+40,d[3]+40)/100),2),
        ayuda1 = MPP1,
        ayuda2 = MPP5,      
        ayuda3 = MPP3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento generado por un par de fuerzas se define como $M = F \\cdot d$, donde $F$ es la magnitud de las fuerzas pares y $d$ es la distancia perpendicular entre estas. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Magnitud del par de fuerzas en los puntos A y B: }}$ 
        
        ${{\hspace{{4mm}} d = {((d[0]+40)/100):.2f} \\text{{ m}}}}$       
        ${{\hspace{{4mm}} M = F \\cdot d}}$          

        ${{\hspace{{4mm}} F = \\dfrac{{M}}{{d}} }}$             

        ${{\hspace{{4mm}} F = \\dfrac{{{m[0]}}}{{{((d[0]+40)/100)}}}\\text{{ N}} }}$             
        
        ${{\hspace{{4mm}} F = {(m[0]/((d[0]+40)/100)):.2f}\\text{{ N}} }}$

        $\\textbf{{\\small 2. Magnitud del par de fuerzas en los puntos B y C: }}$ 
        
        ${{\hspace{{4mm}} d = {((d[3]+40)/100):.2f}\\text{{ m}}}}$          
        ${{\hspace{{4mm}} M = F \\cdot d}}$           

        ${{\hspace{{4mm}} F = \\dfrac{{M}}{{d}} }}$            

        ${{\hspace{{4mm}} F = \\dfrac{{{m[0]}}}{{{((d[3]+40)/100)}}}\\text{{ N}}}}$          
        
        ${{\hspace{{4mm}} F = {(m[0]/((d[3]+40)/100)):.2f}\\text{{ N}} }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_1
        code = 2410041,
        no_pregunta = 4,
        complexity = F,
        topic = MO,
        subtopic = "Momento par",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las componentes del vector momento $\\vec{{M}}$ generado por los pares de fuerzas que actúan sobre la estructura. Considere que la fuerza $F_1 = {f[1]:.0f} \\text{{ N}}$ actúa en la dirección del eje $y$, la fuerza $F_2 = {f[0]:.0f} \\text{{ N}}$ actúa en la dirección del eje $z$ y la distancia $L = {d[0]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Momento resultante componente $\\hat{{i}}$ $[N \\cdot m]$",
        a2_name = "Momento resultante componente $\\hat{{j}}$ $[N \\cdot m]$",
        a3_name = "Momento resultante componente $\\hat{{k}}$ $[N \\cdot m]$",
        answer1 = lambda f, a, calc, c, d, m: 0,
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*(2**(1/2))*d[0],2),
        answer3 = lambda f, a, calc, c, d, m: np.round((-1*f[1]*((2**(1/2))*d[0])),2),
        ayuda1 = MPP1,
        ayuda2 = MPP4,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento generado por un par de fuerzas se define como $M = F \\cdot d$, donde $F$ es la magnitud de las fuerzas pares y $d$ es la distancia perpendicular entre estas. A continuación, se presenta la solución sugerida para el ejercicio:
    
        $\\textbf{{\\small 1. Momento generado por la fuerza F1: }}$                
        ${{\hspace{{4mm}} F_1 = {f[1]} \\text{{ N}}}}$                   
        ${{\hspace{{4mm}} d = {((2**(1/2))*d[0]):.2f} \\text{{ m}}}}$         
               
        ${{\hspace{{4mm}} M = -F_1 \\cdot d}}$               
        ${{\hspace{{4mm}} \\vec{{M_{{F1}}}} = {(-1*f[1]*((2**(1/2))*d[0])):.2f} \\text{{ }} \\hat{{k}} \\text{{ }}N \\cdot m}}$         

        $\\textbf{{\\small 2. Momento generado por la fuerza F2: }}$      
        ${{\hspace{{4mm}} F_2 = {f[0]} \\text{{ N}}}}$             
        ${{\hspace{{4mm}} d = {((2**(1/2))*d[0]):.2f} \\text{{ m}}}}$  

        ${{\hspace{{4mm}} M = F_2 \\cdot d}}$               
        ${{\hspace{{4mm}} \\vec{{M_{{F2}}}} = {(f[0]*(2**(1/2))*d[0]):.2f}\\text{{ }} \\hat{{j}} \\text{{ }}N \\cdot m}}$      
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),



    #========================================================  MOMENTO  =========================================================
    #-------------------------------------------------       Momento par      ---------------------------------------------------
    #-------------------------------------------------       Nivel Medio   ------------------------------------------------------
    #-------------------------------------------------      Code: 24200##    ----------------------------------------------------
   
    Questionary(#1_1
        code = 2420011,
        no_pregunta = 1,
        complexity = M,
        topic = MO,
        subtopic = "Momento par",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el momento generado por las fuerzas $F_1 = {f[0]:.0f} \\text{{ kN}}$ y $F_2 = {f[1]:.0f} \\text{{ kN}}$ que actúan sobre el contenedor. Considere que $d_1 = {d[0]:.0f} \\text{{  m}}$, $d_2 = {d[3]:.0f} \\text{{  m}}$ y $\\theta = {a[0]:.0f}°$.",
        no_answers = 3,
        a1_name = "Componente $\\hat{{i}}$ del momento [$kN \\cdot m$]",
        a2_name = "Componente $\\hat{{j}}$ del momento [$kN \\cdot m$]",
        a3_name = "Componente $\\hat{{k}}$ del momento [$kN \\cdot m$]",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[1]*Calculations.sine(a[0])*d[0],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[1]*Calculations.cosine(a[0])*d[0]+(-f[0]*d[3]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MPP1,
        ayuda2 = MPP7,      
        ayuda3 = MPP4,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento generado por un par de fuerzas se define como $M = F \\cdot d$, donde $F$ es la magnitud de las fuerzas pares y $d$ es la distancia perpendicular entre estas. El efecto del moemnto par se siente de igual manera en todos los puntos del cuerpo. A continuación, se presenta la solución sugerida para el ejercicio:
        
        Para determinar el momento generado por las fuerzas, se calcula por separado el momento producido por cada fuerza:

        $\\textbf{{\\small 1. Cálculo del momento generado por la fuerza F1:}}$

        ${{\hspace{{4mm}} \\vec{{M_{{F1}} }} = [-F_1 \\cdot d_2 \\text{{ }} \\hat{{j}}] \\text{{ }} kN \\cdot m}}$               
        ${{\hspace{{4mm}} \\vec{{M_{{F1}} }} = [{-f[0]*d[3]:.2f}\\text{{ }} \\hat{{j}}] \\text{{ }} kN \\cdot m}}$

        $\\textbf{{\\small 2. Cálculo del momento generado por la fuerza F2:}}$

        Para el cálculo deL momento generado por la fuerza $F_2$ se utiliza momento cruz:     
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        ${{\hspace{{4mm}} \\vec{{r}} = [d_1 \\text{{ }} \\hat{{k}}] \\text{{ }} m }}$       
        ${{\hspace{{4mm}} \\vec{{F_2}} = [F_2 \\cdot Cos(\\theta) \\text{{ }} \\hat{{i}} - F_2 \\cdot Sen(\\theta) \\text{{ }} \\hat{{j}}] \\text{{ }} kN \\cdot m }}$  

        ${{\hspace{{4mm}} \\vec{{M_{{F2}}}} = [F_2 \\cdot Sen(\\theta) \\cdot d_1 \\text{{ }} \\hat{{i}} +  F_2 \\cdot Cos(\\theta) \\cdot d_1 \\text{{ }} \\hat{{j}}] \\text{{ }} kN \\cdot m }}$      
        ${{\hspace{{4mm}} \\vec{{M_{{F2}}}} = [{f[1]*Calculations.sine(a[0])*d[0]:.2f} \\text{{ }} \\hat{{i}} +  {f[1]*Calculations.cosine(a[0])*d[0]:.2f}\\text{{ }} \\hat{{j}}] \\text{{ }} kN \\cdot m }}$      

        $\\textbf{{\\small 3. Sumatoria de momentos:}}$
            
        ${{\hspace{{4mm}} \\vec{{M}} = \\vec{{M_{{F1}} }} + \\vec{{M_{{F2}} }}}}$           
        ${{\hspace{{4mm}} \\vec{{M}} = [{f[1]*Calculations.sine(a[0])*d[0]:.2f} \\text{{ }} \\hat{{i}} +  ({f[1]*Calculations.cosine(a[0])*d[0]+(-f[0]*d[3]):.2f})\\text{{ }} \\hat{{j}}] \\text{{ }} kN \\cdot m}}$
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 
    
    # Questionary(#2_1
    #     code = 2420021,
    #     no_pregunta = 2,
    #     complexity = M,
    #     topic = MO,
    #     subtopic = "Momento par",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"El barril es movilizado mediante la aplicación de dos fuerzas: $F_1 = {f[0]:.0f} \\text{{ N}}$ y $F_2 = {f[1]:.0f} \\text{{ N}}$. Determine las componentes vectoriales del momento generado por estas fuerzas, teniendo en cuenta que la altura de barril es $d_0 = {d[0]:.0f} \\text{{ m}}$, su radio es $d_1 = {d[3]:.0f} \\text{{ m}}$ y $\\theta = {a[0]:.0f}°$",
    #     no_answers = 3,
    #     a1_name = "Momento componente $\\hat{{i}}$",
    #     a2_name = "Momento componente $\\hat{{j}}$",
    #     a3_name = "Momento componente $\\hat{{k}}$",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(f[1]*Calculations.sine(a[0])*d[3]-f[1]*Calculations.cosine(a[0])*d[0],2),
    #     answer2 = lambda f, a, calc, c, d, m: 0,
    #     answer3 = lambda f, a, calc, c, d, m: np.round(f[0]*d[0],2),
    #     ayuda1 = MPP1,
    #     ayuda2 = MPP7,      
    #     ayuda3 = "",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     El momento generado por un par de fuerzas se define como $M = F \\cdot d$, donde $F$ es la magnitud de las fuerzas pares y $d$ es la distancia perpendicular entre estas. A continuación, se presenta la solución sugerida para el ejercicio:

    #     $\\textbf{{\\small 1. Descompocisión de fuerzas e identificación de par de fuerzas: }}$ 

    #     La fuerza $F_1$ es un par de fuerzas sobre el eje $x$
        
    #     ${{\hspace{{4mm}} \\vec{{F_2}} = (0\\hat{{i}} - {f[1]}sen(\\theta)\\hat{{j}}-{f[1]}cos(\\theta)\\hat{{k}})[N]}}$      
    #     ${{\hspace{{4mm}} \\vec{{F_2}} = (0\\hat{{i}} - {f[1]*Calculations.sine(a[0])}\\hat{{j}}-{f[1]*Calculations.cosine(a[0])}\\hat{{k}})[N]}}$

    #     $\\textbf{{\\small 2. Momento generado por las fuerzas: }}$ 

    #     Para $F_1$:
    #     ${{\hspace{{4mm}} \\vec{{M}} = (0\\hat{{i}}+0\\hat{{j}}+{f[0]}\\cdot{d[0]}\\hat{{k}})[N \\cdot m]}}$
    #     ${{\hspace{{4mm}} \\vec{{M}} = (0\\hat{{i}}+0\\hat{{j}}+{f[0]*d[0]}\\hat{{k}})[N \\cdot m]}}$

    #     Para $F_2$:
    #     ${{\hspace{{4mm}} \\vec{{M}} = (({f[1]*Calculations.sine(a[0])}*{d[3]}-({f[1]*Calculations.cosine(a[0])}*{d[0]}))\\hat{{i}}+0\\hat{{j}}+0\\hat{{k}})[N \\cdot m]}}$
    #     ${{\hspace{{4mm}} \\vec{{M}} = (({f[1]*Calculations.sine(a[0])*d[3]-(f[1]*Calculations.cosine(a[0])*d[0])}))\\hat{{i}}+0\\hat{{j}}+0\\hat{{k}})[N \\cdot m]}}$

    #     $\\textbf{{\\small 3. Sumatoria de momentos: }}$
    #     ${{\hspace{{4mm}} \\sum{{\\vec{{M}}}} = (({f[1]*Calculations.sine(a[0])*d[3]-(f[1]*Calculations.cosine(a[0])*d[0])}))\\hat{{i}}+0\\hat{{j}}+{f[0]*d[0]}\\hat{{k}})[N \\cdot m]}}$

    #     $\\textbf{{\\small 4. Identificación de componentes del momento encontrado: }}$
    #     ${{\hspace{{4mm}} \\hat{{i}} = {f[1]*Calculations.sine(a[0])*d[3]-(f[1]*Calculations.cosine(a[0])*d[0])}[N \\cdot m]}}$
    #     ${{\hspace{{4mm}} \\hat{{j}} = 0[N \\cdot m]}}$
    #     ${{\hspace{{4mm}} \\hat{{k}} = {f[0]*d[0]}[N \\cdot m]}}$
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    Questionary(#3_1
        code = 2420031,
        no_pregunta = 3,
        complexity = M,
        topic = MO,
        subtopic = "Momento par",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"La rueda orientable está sometida a dos pares de fuerzas $F_1 = {f[0]:.0f} \\text{{ N}}$ y $F_2$. Si el momento total generado por estas fuerzas es $M = {m[0]:.0f} \\text{{ }} N \\cdot m$, determine la magnitud de la fuerza $F_2$ si la distancia entre las fuerzas es de $d_0 = {d[0]:.0f} \\text{{ cm}}$ y $d_1 = {d[3]:.0f} \\text{{ cm}}$",
        no_answers = 1,
        a1_name = "Magnitud fuerza $F_2$ $[N]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((m[0]-f[0]*(d[0]/100))/(d[3]/100),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MPP1,
        ayuda2 = MPP3,      
        ayuda3 = MPP6,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento generado por un par de fuerzas se define como $M = F \\cdot d$, donde $F$ es la magnitud de las fuerzas pares y $d$ es la distancia perpendicular entre estas. A continuación se presenta la solución sugerida:

        $\\textbf{{\\small 1. Cambio de unidades de las distancias dadas: }}$ 
        
        ${{\hspace{{4mm}} d_0 = {d[0]/100} \\text{{ m}} }}$      
        ${{\hspace{{4mm}} d_1 = {d[3]/100} \\text{{ m}} }}$

        $\\textbf{{\\small 2. Momento generado por las fuerzas: }}$ 

        Para $F_1$:     
        ${{\hspace{{4mm}} \\vec{{M}} = F_1 \\cdot d_0  \\text{{ }} \\hat{{k}} \\text{{ }} N \\cdot m}}$      
        ${{\hspace{{4mm}} \\vec{{M}} = {f[0]*d[0]/100} \\text{{ }} \\hat{{k}} \\text{{ }} N \\cdot m}}$
        
        Para $F_2$:   
        ${{\hspace{{4mm}} \\vec{{M}} = -F_2 \\cdot d_1 \\text{{ }} \\hat{{k}} \\text{{ }} N \\cdot m}}$            
        ${{\hspace{{4mm}} \\vec{{M}} = -F_2*{d[3]/100} \\text{{ }} \\hat{{k}} \\text{{ }} N \\cdot m}}$
        

        $\\textbf{{\\small 3. Sumatoria de momentos - Despejar fuerza F2: }}$
             
        ${{\hspace{{4mm}} \\sum{{\\vec{{M}}}} = {f[0]*d[0]/100} -F_2*{d[3]/100} \\text{{ }} N \\cdot m = {m[0]} \\text{{ }} N \\cdot m}}$                       
        ${{\hspace{{4mm}} F_2 = \\dfrac{{{m[0]}-{f[0]*d[0]/100}}}{{{d[3]/100}}} \\text{{ N}} }}$            
        ${{\hspace{{4mm}} F_2 = {(m[0]-f[0]*(d[0]/100))/(d[3]/100):.2f} \\text{{ N}}}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),   

    
    #========================================================  MOMENTO  =========================================================
    #-------------------------------------------------       Momento par      ---------------------------------------------------
    #-------------------------------------------------       Nivel Díficil   ------------------------------------------------------
    #-------------------------------------------------      Code: 24300##    ----------------------------------------------------

    Questionary(#1_1
        code = 0,
        no_pregunta = 1,
        complexity = D,
        topic = MO,
        subtopic = "Momento par",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Está sección pronto estará disponible.",
        no_answers = 0,
        a1_name = AX,
        a2_name = AY,
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(0, 2),
        answer2 = lambda f, a, calc, c, d, m: np.round(0, 2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = A1,
        ayuda2 = A2,
        ayuda3 = A3,
        respuesta_P1 = lambda fa, a, calc, c, d, m: f"",
        respuesta_P2 = lambda fa, a, calc, c, d, m: f"",
        respuesta_P3 = lambda fa, a, calc, c, d, m: f"",
        calculos = 'operations',
        ),

    # Questionary(#1_1
    #     code = 2430011,
    #     no_pregunta = 1,
    #     complexity = D,
    #     topic = MO,
    #     subtopic = "Momentos pares",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Usted estaba caminando por un centro comercial cuando de repente se le cayó el celular. Cuando este golpeo el suelo se rompió y se doblo como se muestra en la figura. Determine el momento generado por las fuerzas $F_1 = {f[0]:.0f}$, $F_2 = {f[1]:.0f}$ y $F_3 = {f[2]:.0f}$ que sintio su celular (Las componentes vectoriales). Tenga en cuenta que $d_0 = {d[0]+100:.0f}[mm]$, $d_1 = {d[0]+200:.0f}[mm]$, $d_2 = {d[3]+100:.0f}[mm]$, $\\theta = {a[0]:.0f}°$ y $\\phi = {a[4]:.0f}°.",
    #     no_answers = 3,
    #     a1_name = "Momento \\hat{{i}}",
    #     a2_name = "Momento \\hat{{j}}",
    #     a3_name = "Momento \\hat{{k}}",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*(d[0]+200)/1000,2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round((f[1]*(d[0]+100+d[0]+200)*Calculations.cosine(45)/1000)+(f[2]*Calculations.cosine(a[0])*Calculations.cosine(a[1])*(d[3]+100)/1000),2),
    #     answer3 = lambda f, a, calc, c, d, m: np.round(f[2]*Calculations.cosine(a[0])*Calculations.sine(a[1])*(d[3]+100)/1000,2),
    #     ayuda1 = "En la parte inclinada, solo la componente $\\hat{{i}}$ de $F_3$ genera momento, utilice esto como un plano arbitrario y despues proyecte el resultado del momento par usando el angulo $\\phi$.",
    #     ayuda2 = "El momento par generado por las fuerzas $F_2$ solo lo genera su componente de cos(45). Descompongala y haga momento par.",      
    #     ayuda3 = "Realice sumatoria de fuerzas para hallar las componentes del momento resultante.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     A continuacion se presenta una posible solución para el problema:
        
    #     $\\textbf{{\\small 1. Descomposición de fuerzas y su momento - Momento par:}}$

    #     Para $\\vec{F_1}$:
    #     ${{\hspace{{4mm}} \\vec{M} = ({(f[0]*(d[0]+200)/1000)}\\hat{i}+0\\hat{j}+0\\hat{k})[N \\cdot m]}}$     
        
    #     Para $\\vec{F_2}$:
    #     La unica componente que genera momento par es la $\\hat{i}$, entonces
    #     ${{\hspace{{4mm}} \\vec{F_2} = ({(f[1]*Calculations.cosine(45))}\\hat{i}+0\\hat{j}-{(f[1]*Calculations.sine(45))}\\hat{k})[N]}}
    #     ${{\hspace{{4mm}} \\vec{M} = (0\\hat{i}+{(f[1]*Calculations.cosine(45)*(d[0]+100+d[0]+200)/1000)}\\hat{j}+0\\hat{k})[N \\cdot m]}}$ 

        
    #     Para $\\vec{F_3}$:
    #     Se toma la seccion inclinada como plano de referencia, donde luego el momento será proyectado a sus componentes en los ejes definidos usando el angulo $\\phi$.
    #     ${{\hspace{{4mm}} \\vec{F_{3"x"}} = ({(f[2]*Calculations.cosine(a[0]))}\\hat{i}+0\\hat{j}+{(f[2]*Calculations.sine(a[0]))}\\hat{k})}}$
    #     ${{\hspace{{4mm}} M =  {(f[2]*Calculations.cosine(a[0])*(d[3]+100)/1000)}[N \\cdot m]}}$

    #     Proyectado al eje de referencia establecido:
    #     ${{\hspace{{4mm}} \\vec{M} =  (0\\hat{i}+{(f[2]*Calculations.cosine(a[0])*Calculations.cosine(a[1])*(d[3]+100)/1000)}\\hat{j}+{(f[2]*Calculations.cosine(a[0])*Calculations.sine(a[1])*(d[3]+100)/1000)}\\hat{k})[N \\cdot m]}}$
       
    #     $\\textbf{{\\small 2. Sumatoria de momentos:}}$
    #     ${{\hspace{{4mm}} \\vec{M} =  ({(f[0]*(d[0]+200)/1000)}\\hat{i}+{((f[1]*(d[0]+100+d[0]+200)*Calculations.cosine(45)/1000)+(f[2]*Calculations.cosine(a[0])*Calculations.cosine(a[1])/1000))}\\hat{j}+{(f[2]*Calculations.cosine(a[0])*Calculations.sine(a[1])*(d[3]+100)/1000)}\\hat{k})[N \\cdot m]}}$
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    # Questionary(#2_1
    #     code = 2430021,
    #     no_pregunta = 2,
    #     complexity = D,
    #     topic = MO,
    #     subtopic = "Momentos par",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Encuentre la magnitud del momento generado por las fuerzas $F_1 = {f[0]:.0f}[N]$ y $F_2 = {f[1]:.0f}[N]$ aplicadas sobre el sistema mostrado en la figura. Tenga en cuenta que $d_0 = {d[0]:.0f}[m]$ y $d_1 = {d[3]:.0f}[m]$.",
    #     no_answers = 1,
    #     a1_name = "Magnitud del momento [N \\cdot m]",
    #     a2_name = "",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D(f[0]*d[0],f[1]*d[3]*(3/5),f[1]*d[3]*(4/5)),2),
    #     answer2 = lambda f, a, calc, c, d, m: 0,
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "Utilice las distancias dadas, siendo ya las perpendiculares entre el par de fuerzas y tenga en cuenta que el momento par se calcula como $M = F \\cdot d$.",
    #     ayuda2 = "Como puede ver, la fuerza $F_2$ se encuentra en diagonal. Utilice esto como un plano arbitrario y despues proyecte el resultado del momento par usando el triangulo 3-4-5.",      
    #     ayuda3 = "Realice sumatoria de fuerzas para hallar las componentes del momento resultante y luego su magnitud.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     A continuacion se presenta una posible solución para el problema:
        
    #     $\\textbf{{\\small 1. Momento generado por las fuerzas - Momento par:}}$

    #     Para $\\vec{F_1}$:
    #     ${{\hspace{{4mm}} F_1 = {f[0]}[N]}}
    #     ${{\hspace{{4mm}} d = {d[0]}[m]}}
    #     ${{\hspace{{4mm}} \\vec{M} = ({f[0]*d[0]}\\hat{i})[N \\cdot m]}}$ 

    #     Para $\\vec{F_2}$:
    #     ${{\hspace{{4mm}} F_1 = {f[1]}[N]}}
    #     ${{\hspace{{4mm}} d = {d[3]}[m]}}
    #     ${{\hspace{{4mm}} M = ({f[1]*d[3]})[N \\cdot m]}}$ 

    #     $\\textbf{{\\small 2. Descompocisión del momento generado por $F_2$:}}$
    #     Al tomar la seccion inclinada como plano de referencia, el momento debe ser proyectado a sus componentes en los ejes definidos haciendo uso del triangulo 3-4-5 dado en la figura.
    #     ${{\hspace{{4mm}} \\vec{M_"\\hat{{j}}"} = ({f[1]*(3/5)*d[3]}\\hat{j})[N \\cdot m]}}$
    #     ${{\hspace{{4mm}} \\vec{M_"\\hat{{k}}"} = ({f[1]*(4/5)*d[3]}\\hat{k})[N \\cdot m]}}$

    #     $\\textbf{{\\small 3. Sumatoria de momentos:}}$
    #     ${{\hspace{{4mm}} \\vec{M} = ({f[0]*d[0]}\\hat{i}+{f[1]*(3/5)*d[3]}\\hat{j}+{f[1]*(4/5)*d[3]}\\hat{k})[N \\cdot m]}}$
    #     Teniendo esto podemos encontrar la magnitud del momento generado por las fuerzas.
    #     ${{\hspace{{4mm}} |\\vec{M}| = {Calculations.magnitude3D(f[0]*d[0],f[1]*d[3]*(3/5),f[1]*d[3]*(4/5))}[N \\cdot m]}}$
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),
        
    # Questionary(#3_1
    #     code = 2430031,
    #     no_pregunta = 3,
    #     complexity = D,
    #     topic = MO,
    #     subtopic = "Momentos par",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Encuentre la distancia $d$ tal que el momento generado por los pares de fuerzas $F_1 = {f[0]:.0f}[N]$, $F_2 = {f[1]:.0f}[N]$ y $F_3 = {f[2]:.0f}[N]$ sea de $M = {m[0]:.0f}[N \\cdot m]$. Tenga en cuenta que $d_0 = {d[0]+14:.0f}[m]$, $d_1 = {d[0]+3:.0f}[m]$, $d_2 = {d[0]:.0f}[m]$ y \\theta = {a[0]:.0f}.",
    #     no_answers = 1,
    #     a1_name = "Distancia d [m]",
    #     a2_name = "",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round((m[0]-f[0]*Calculations.cosine(a[0])*(d[0]+10)+f[1]*((d[0]+14)-(d[0]+3)-d[0])-f[2]*((d[0]+14)-(d[0]+3)-d[0]))/(f[0]*Calculations.sine(a[0])+f[2]),2),
    #     answer2 = lambda f, a, calc, c, d, m: 0,
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "Utilice las distancias dadas para determinar la distancia perpendicular entre las fuerzas. Tenga en cuenta que se le esta dando un triangulo 3-4-5 para encontrar la distancia $L$ mostrada en la figura.",
    #     ayuda2 = "Encuentre el momento par generado por las fuerzas usando las distancias encontradas la definición de momento par. Tenga en cuenta que debe descomponer la fuerza $F_1$.",      
    #     ayuda3 = "Haga sumatoria de momentos igualada al momento dado para despejar y hallar $d$",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     A continuacion se presenta una posible solución para el problema:
        
    #     $\\textbf{{\\small 1. Distancias perpendiculares entre las fuerzas:}}$

    #     Para $\\vec{F_1}$:
    #     La distancia perpendicular entre la componente \\hat{i} de $F_1$ es $d_0$ y para la componente \\hat{j} es $d$
    #     Para $\\vec{F_2}$:
    #     ${{\hspace{{4mm}} d_{F2} = ({d[0]+14}-{d[0]+3}-{d[0]})[m]}}
    #     ${{\hspace{{4mm}} d_{F2} = ({d[0]+14-d[0]+3-d[0]})[m]}}
    #     Para $\\vec{F_3}$:
    #     Sabemos que:
    #     ${{\hspace{{4mm}} L = (d+x)[m]}}$ 
    #     La distancia x se encuentra haciendo triangulos semejantes con la distancia perpendicular hallada para $F_2$:
    #     ${{\hspace{{4mm}} \\dfrac{({d[0]+14-d[0]+3-d[0]})}{"x"} = \\dfrac{3}{4}}}$
    #     ${{\hspace{{4mm}} x = \\dfrac{(4*({d[0]+14-d[0]+3-d[0]}))}{3}}}$
    #     ${{\hspace{{4mm}} x = {(4*({d[0]+14-d[0]+3-d[0]})/3)}}}$
    #     Entonces:
    #     ${{\hspace{{4mm}} L = (d+{(4*({d[0]+14-d[0]+3-d[0]})/3)})[m]}}$ 

    #     $\\textbf{{\\small 2. Momentos pares:}}$
    #     Para $\\vec{F_1}$:
    #     ${{\hspace{{4mm}} \\vec{F_1} = ({(f[0]*Calculations.cosine(a[0]))}\\hat{i}+{(f[0]*Calculations.sine(a[0]))}\\hat{j})[N]}}$
    #     Entonces los momentos para cada componente son:
    #     Para \\hat{i}
    #     ${{\hspace{{4mm}} \\vec{M} = ({(f[0]*Calculations.cosine(a[0])*(d[0]+13))})\\hat{k}[N \\cdot m]}}$
    #     Para \\hat{j}
    #     ${{\hspace{{4mm}} \\vec{M} = ({(f[0]*Calculations.sine(a[0]))}*d)\\hat{k}[N \\cdot m]}}$

    #     Para $\\vec{F_2}$:
    #     ${{\hspace{{4mm}} \\vec{M} = ({(-1*f[1]*(d[0]+14-d[0]+3-d[0]))})\\hat{k}[N \\cdot m]}}$
        
    #     Para $\\vec{F_3}$:
    #     ${{\hspace{{4mm}} \\vec{M} = ({f[2]})*(d+{(4*({d[0]+14-d[0]+3-d[0]})/3)})\\hat{k}}}$
    #     ${{\hspace{{4mm}} \\vec{M} = ({f[2]}*d+{(f[2]*4*({d[0]+14-d[0]+3-d[0]})/3)})\\hat{k}}}$

    #     $\\textbf{{\\small 3. Sumatoria de momentos:}}$
    #     ${{\hspace{{4mm}} \\sum{M} = {m[0]}}}$
    #     ${{\hspace{{4mm}} \\sum{M} = {(f[0]*Calculations.cosine(a[0])*(d[0]+13))}+{(f[0]*Calculations.sine(a[0]))}*d-{(f[1]*(d[0]+14-d[0]+3-d[0]))}+{f[2]}*d+{(f[2]*4*({d[0]+14-d[0]+3-d[0]})/3)}}}$
    #     ${{\hspace{{4mm}} {m[0]} = {(f[0]*Calculations.cosine(a[0])*(d[0]+13))}+{(f[0]*Calculations.sine(a[0]))}*d-{(f[1]*(d[0]+14-d[0]+3-d[0]))}+{f[2]}*d+{(f[2]*4*({d[0]+14-d[0]+3-d[0]})/3)}}}$
    #     Despejando $d$ encontramos que:
    #     ${{\hspace{{4mm}} d = \\dfrac{m[0]-f[0]*Calculations.cosine(a[0])*(d[0]+13)+f[1]*(d[0]+14-d[0]+3-d[0])-(f[2]*4*({d[0]+14-d[0]+3-d[0]})/3)}{f[0]*Calculations.sine(a[0])+f[2]}[m]}}$
    #     ${{\hspace{{4mm}} d = {(m[0]-f[0]*Calculations.cosine(a[0])*(d[0]+10)+f[1]*((d[0]+14)-(d[0]+3)-d[0])-f[2]*((d[0]+14)-(d[0]+3)-d[0]))/(f[0]*Calculations.sine(a[0])+f[2])}[m]}}$
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),



    #========================================================  INCERTIDUMBRE  =========================================================
    #-------------------------------------------------       Nivel Fácil   ---------------------------------------------------
    #-------------------------------------------------       Code: 31100#1    --------------------------------------------------

    Questionary(#1_1
        code = 3110011,
        no_pregunta = 1,
        complexity = F,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"De acuerdo con la función de probabilidad acumulada $F(x)$ mostrada, ¿Cuál es la fuerza $F$ con una probabilidad de excedencia del ${round(((m[1]-5)/5))*5:.0f}$%?",
        no_answers = 1,
        a1_name = "$F$ $[N]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(100-round(((m[1]-5)/5))*5,2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = I1,
        ayuda2 = I2,      
        ayuda3 = I3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        La probabilidad de excedencia es la probabilidad de que la variable aleatoria $X$ tome un valor mayor al que se está evaluando. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Calcular la probabilidad de ocurrencia: }}$

        Dado que la función de distribución acumulada representa la probabilidad de ocurrencia, primero se calcula esta como la diferencia entre 1 y la probabilidad de excedencia.

        ${{\hspace{{4mm}} P(F \\leq f) = 1 - P(F > f)}}$          
        ${{\hspace{{4mm}} P(F \\leq f) = 1 - {(round(((m[1]-5)/5))*5)/100:.2f}}}$    
        ${{\hspace{{4mm}} P(F \\leq f) = {1-((round(((m[1]-5)/5))*5)/100):.2f}  }}$
        
        $\\textbf{{\\small 2. Determinar la probabilidad de excedencia: }}$

        En el eje $Y$, se ubica la probabilidad de ocurrencia calculada en el punto $1$. Luego, en el eje $X$, se determina la fuerza asociada, que en este caso es ${100-round(((m[1]-5)/5))*5:.2f}$ $N$.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 3110021,
        no_pregunta = 2,
        complexity = F,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es la probabilidad de ocurrencia de la fuerza de ${round(((m[1]-5)/5))*5:.0f}$ $\\text{{ N}}$?",
        no_answers = 1,
        a1_name = "Probabilidad de ocurrencia [%]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(round(((m[1]-5)/5))*5,2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = I1,
        ayuda2 = I4,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        La probabilidad de ocurrencia es la probabilidad de que la variable aleatoria $X$ tome un valor menor o igual al que se está evaluando $(P(X \\leq x))$. Este valor se obtiene directamente de la gráfica de distribución acumulada. 
        
        A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Determinar la probabilidad de ocurrencia: }}$

        Teniendo en cuenta que la probabilidad de ocurrencia se obtiene de la gráfica de distribución acumulada de la variable aleatoria $F$, primero se ubica en el eje $X$ la fuerza indicada en el enunciado ${round(((m[1]-5)/5))*5:.0f}$ $\\text{{ N}}$, y luego se proyecta su correspondiente valor en el eje $Y$. En este caso, la probabilidad es ${round(((m[1]-5)/5))*5:.2f}$%.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 3110031,
        no_pregunta = 3,
        complexity = F,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"De acuerdo con la función de probabilidad acumulada $F(x)$ mostrada, ¿Cuál es la fuerza $F$ con una probabilidad de ocurrencia del ${m[1]-5:.0f}$%?",
        no_answers = 1,
        a1_name = "$F$ $[N]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(math.sqrt(((m[1]-5)-1*10**-13)/0.01),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = I1,
        ayuda2 = I2,      
        ayuda3 = I3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        La probabilidad de ocurrencia es la probabilidad de que la variable aleatoria $X$ tome un valor menor o igual al que se está evaluando $(P(X \\leq x))$. Este valor se obtiene directamente de la gráfica de distribución acumulada. 
       
        A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Calcular la fuerza: }}$

        Para determinar la fuerza asociada a la probabilidad de ocurrencia indicada en el enunciado, se despeja $F$ de la ecuación que describe a la distribución acumulada.

        ${{\hspace{{4mm}} P(F \\leq f) = 0.01F^2+1*10^{{-13}}}}$          

        ${{\hspace{{4mm}} F = \\sqrt{{\\dfrac{{P(F \\leq f) - 1*10^{{-13}}}}{{0.01}} }} }}$  

        ${{\hspace{{4mm}} F = {math.sqrt(((m[1]-5)-1*10**-13)/0.01):.2f} \\text{{ N}} }}$  
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_1
        code = 3110041,
        no_pregunta = 4,
        complexity = F,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es la probabilidad de excedencia de la fuerza de ${(m[1]-5):.0f}$ $\\text{{ N}}$?",
        no_answers = 1,
        a1_name = "Probabilidad de excedencia [%]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(100-(0.01*(m[1]-5)**2+1*10**(-13)),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = I1,
        ayuda2 = I4,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        La probabilidad de excedencia es la probabilidad de que la variable aleatoria $X$ tome un valor mayor al que se está evaluando. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Calcular la probabilidad de ocurrencia: }}$

        Dado que la función de distribución acumulada representa la probabilidad de ocurrencia, primero se calcula esta como la diferencia entre 1 y la probabilidad de excedencia.

        ${{\hspace{{4mm}} P(F \\leq f) = 0.01F^2+1*10^{{-13}}}}$           

        ${{\hspace{{4mm}} P(F \\leq f) = {0.01*(m[1]-5)**2+1*10**(0-13):.2f} \\% }}$  

        
        $\\textbf{{\\small 2. Calcular la probabilidad de excedencia: }}$

        ${{\hspace{{4mm}} P(F > f) = 1 - P(F \\leq f)}}$ 

        ${{\hspace{{4mm}} P(F > f) = 1 - {0.01*(m[1]-5)**2+1*10**(-13):.2f} \\%}}$ 

        ${{\hspace{{4mm}} P(F > f) = {100-(0.01*(m[1]-5)**2+1*10**(-13)):.2f} \\%}}$ 
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    #========================================================  INCERTIDUMBRE  =========================================================
    #-------------------------------------------------       Nivel Medio   ---------------------------------------------------
    #-------------------------------------------------       Code: 31200#1    --------------------------------------------------

    Questionary(#1_1
        code = 3120011,
        no_pregunta = 1,
        complexity = M,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuál es la probabilidad de ocurrencia del momento ${d[0]+5:.0f}$ $\\text{{N}} \\cdot \\text{{m}}$?", 
        no_answers = 1,
        a1_name = "Probabilidad de ocurrencia [%]",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(((d[0]+5)-5)*0.1*100,2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = I5,
        ayuda2 = I6,
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m:f"""
        La probabilidad de ocurrencia de un valor en evaluación corresponde a la probabilidad acumulada hasta ese punto. En este caso, es el área desde el inicio de la función hasta el punto en evaluación.

        A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Calcular la probabilidad de ocurrencia: }}$

        La probabilidad de ocurrencia se calcula desde el inicio de la función $(5)$ hasta el valor en evaluación $({d[0]+5:.0f})$.

        ${{\hspace{{4mm}} P(M \\leq m) = ({d[0]+5:.0f}-5)*\\dfrac{{1}}{{10}} }}$  

        ${{\hspace{{4mm}} P(M \\leq m) = {(d[0])*0.1*100:.2f} \\%}}$           

        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),

    Questionary(#2_1
        code = 3120021,
        no_pregunta = 2,
        complexity = M,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"De acuerdo con la función de probabilidad acumulada mostrada, ¿Cuál es la tensión $(T)$ asociada a la probabilidad de excedencia del ${d[0]+5:.0f}$ $\\%$?", 
        no_answers = 1,
        a1_name = "Tensión $(T)$ $[N]$",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(((((100-(d[0]+5))/100)-0.3))/0.01,2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = I2,
        ayuda2 = I3,
        ayuda3 = I7,
        respuesta_P1 = lambda f, a, calc, c, d, m:f"""
        La distribución acumulada de la tensión $(T)$ brinda información sobre la probabilidad de ocurrencia. Por lo tanto, primero halle la probabilidad de ocurrencia asociada a la probabilidad de excedencia dada, luego calcule la ecuación de la recta y despeje el valor de la variable solicitada.
        
        A continuación, se presenta la solución sugerida para el ejercicio:
        

        $\\textbf{{\\small 1. Calcular la probabilidad de ocurrencia: }}$

        La probabilidad de excedencia se calcula como la diferencia entre 1 y la probabilidad de ocurrencia.

        ${{\hspace{{4mm}} P(T \\leq t) = 1 - P(T > t)}}$          
        ${{\hspace{{4mm}} P(T \\leq t) = 1 - {d[0]+5:.0f} \\%}}$    
        ${{\hspace{{4mm}} P(T \\leq t) = {100-(d[0]+5):.0f} \\% }}$

        $\\textbf{{\\small 2. Despejar la variable solicitada: }}$

        La probabilidad de excedencia del ${d[0]+5:.0f}$ % está descrita por la segunda recta. La ecuación de esta recta es $P(T \\leq t) = 0.01T + 0.3$. A partir de esta ecuación, se despeja la tensión $(T)$.

        ${{\hspace{{4mm}} P(T \\leq t) = 0.01T + 0.3}}$   

        ${{\hspace{{4mm}} T = \\dfrac{{P(T \\leq t) - 0.3}}{{0.01}} }}$    

        ${{\hspace{{4mm}} T = {((((100-(d[0]+5))/100)-0.3))/0.01:.2f} \\text{{ N}} }}$
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),

    Questionary(#3_1
        code = 3120031,
        no_pregunta = 3,
        complexity = M,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"De acuerdo con la función de densidad mostrada, ¿Cuál es la distancia asociada a una probabilidad de excedencia del ${d[0]+5:.0f}$ $\\%$?", 
        no_answers = 1,
        a1_name = "Distancia $(D)$ $[m]$",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(90-math.sqrt(((d[0]+5)*60)/0.025),2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = I2,
        ayuda2 = I3,
        ayuda3 = I6,
        respuesta_P1 = lambda f, a, calc, c, d, m:f"""
        La probabilidad de excedencia es la probabilidad de que la variable aleatoria $X$ tome un valor mayor al que se está evaluando. Para calcularla a partir de la función de densidad, es necesario determinar el área bajo la curva. En el caso de la probabilidad de excedencia, esta área se encuentra al lado derecho del triángulo.
        
        A continuación, se presenta la solución sugerida para el ejercicio:

        Para determinar la distancia, se puede aplicar la ecuación de la distribución acumulada triangular, hallar la ecuación de cada recta e integrar, o establecer una sistema de ecuaciones con geometría. Está última opción será el método utilizado para la solución.

        $\\textbf{{\\small 1. Establecer sistema de ecuaciones con geometría: }}$

        Las ecuaciones utilizadas surgen de establecer semejanza entre dos triángulos y conocer que el área del lado derecho equivalente a ${d[0]+5:.0f}$ $\\%$.

        $\\underline{{Ecuación \\text{{ }} 1}}$
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        La semejanza entre triángulos se da entre el triángulo morado y el triángulo azul:

        ${{\hspace{{4mm}} \\dfrac{{30}}{{0.025}} = \\dfrac{{b}}{{h}} }}$

        $\\underline{{Ecuación \\text{{ }} 2}}$

        El área del triángulo azul equivale a la probabilidad de excedencia dada $({d[0]+5:.0f}$ $\\%$).

        ${{\hspace{{4mm}} \\dfrac{{b \\cdot h}}{{2}} = {d[0]+5:.0f} \\% }}$


        $\\textbf{{\\small 2. Resolver el sistema de ecuaciones: }}$

        Con el sistema planteado se busca despejar $b$.

        De 1:

        ${{\hspace{{4mm}} h = \\dfrac{{b \\cdot 0.025}}{{30}} }}$

        Reemplazar 1 en 2:

        ${{\hspace{{4mm}} {d[0]+5:.0f} \\% = \\dfrac{{b^2 \\cdot 0.025}}{{60}} }}$

        ${{\hspace{{4mm}} b = \\sqrt{{ \\dfrac{{ {d[0]+5:.0f} \\% \\cdot 60}}{{0.025}} }} }}$

        ${{\hspace{{4mm}} b = {math.sqrt((((d[0]+5)/100)*60)/0.025):.2f} \\text{{ m}} }}$

        
        $\\textbf{{\\small 3. Halllar la distancia solicitada:}}$

        ${{\hspace{{4mm}} D = 90 - b }}$

        ${{\hspace{{4mm}} D = {90 - math.sqrt((((d[0]+5)/100)*60)/0.025):.2f} \\text{{ m}} }}$
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),

    Questionary(#4_1
        code = 3120041,
        no_pregunta = 4,
        complexity = M,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"La función de probabilidad acumulada $P(W \\leq w) = 1 - e^{{(-0.1w)}}$ describe el peso de una carga de arena en kiloNewtons. ¿Cuál es el peso $(w)$ asociado a una probabilidad de excedencia del ${d[0]+5:.0f}$ $\\%$?",
        no_answers = 1,
        a1_name = "Peso ($W$) $[kN]$",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: np.round(math.log(1-(1-(d[0]+5)/100))/-0.1,2),
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = I2,
        ayuda2 = I3,
        ayuda3 = I6,
        respuesta_P1 = lambda f, a, calc, c, d, m:f"""
        La probabilidad de excedencia es la probabilidad de que la variable aleatoria $X$ tome un valor mayor al que se está evaluando. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de la probabilidad de ocurrencia: }}$

        Dado que la función de distribución acumulada representa la probabilidad de ocurrencia, primero se calcula esta como la diferencia entre 1 y la probabilidad de excedencia.

        ${{\hspace{{4mm}} P(F \\leq f) = 1 - P(F > f)}}$          
        ${{\hspace{{4mm}} P(F \\leq f) = 1 - {(d[0]+5)/100:.2f}}}$    
        ${{\hspace{{4mm}} P(F \\leq f) = {1-((d[0]+5)/100):.2f}  }}$


        $\\textbf{{\\small 2. Despeje del peso (W): }}$

        La función de probabilidad acumulada es $P(W \\leq w) = 1 - e^{{(-0.1w)}}$:
        
        ${{\hspace{{4mm}} P(W \\leq w) = 1 - e^{{(-0.1w)}} }}$      
        
        ${{\hspace{{4mm}} 1 - P(W \\leq w) = e^{{(-0.1w)}} }}$       
        
        ${{\hspace{{4mm}} ln(1 - P(W \\leq w)) = ln(e^{{(-0.1w)}})}}$        
        
        ${{\hspace{{4mm}} ln(1 - P(W \\leq w)) = -0.1w}}$       
        
        ${{\hspace{{4mm}} w = \\dfrac{{ln(1 - P(W \\leq w))}}{{-0.1}} }}$     
        
        ${{\hspace{{4mm}} w = {math.log(1-(1-((d[0]+5)/100)))/-0.1:.2f} \\text{{ kN}}}}$
        """, 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),


    #========================================================  INCERTIDUMBRE  =========================================================
    #-------------------------------------------------       Nivel Díficil   ---------------------------------------------------
    #-------------------------------------------------       Code: 31300#1    --------------------------------------------------

    Questionary(#1_1
        code = 3130011,
        no_pregunta = 1,
        complexity = D,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Esta sección de la aplicación está en implementación. ¡Pronto estará disponible!",
        no_answers = 3,
        a1_name = "",
        a2_name = "",
        a3_name = "",
        answer1=lambda f, a, calc, c, d, m: 0,
        answer2=lambda f, a, calc, c, d, m: 0,
        answer3=lambda f, a, calc, c, d, m: 0,
        ayuda1 = "",
        ayuda2 = "",
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m:"", 
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",    
        calculos='operations'
        ),



    #========================================================  SISTEMAS EQUIVALENTES  =========================================================
    #-------------------------------------------------       Sistemas equivalentes 2D-3D      --------------------------------------------
    #-------------------------------------------------       Nivel Fácil   ---------------------------------------------------
    #-------------------------------------------------       Code: 41100##    --------------------------------------------------
    Questionary(#1_1
        code = 4110011,
        no_pregunta = 1,
        complexity = F,
        topic = "Sistemas equivalentes",
        subtopic = "Sistemas equivalentes",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Reemplace las fuerzas que actúan sobre la viga por una sola fuerza resultante. Determine las componentes de dicha fuerza (Indique el signo de la dirección de las fuerzas) y la ubicación de esta fuerza medida desde el extremo A. Considere $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$, $F_3 = {f[2]:.0f} \\text{{ N}}$, $\\alpha_1 = {a[0]:.0f}°$, $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ fm}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Componente $F_{{Rx}}$ $[N]$",
        a2_name = "Componente $F_{{Ry}}$ $[N]$",
        a3_name = "Distancia desde el extremo A $[m]$",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[1]*calc['sin1'] - f[2]*(3/5),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-f[0] -  f[1]*calc['cos1'] - f[2]*(4/5),2),
        answer3 = lambda f, a, calc, c, d, m: np.round((f[1]*calc['cos1']*d[0] + f[2]*(4/5)*(d[0] + d[3]))/(f[0] + f[1]*calc['cos1'] + f[2]*(4/5)), 2),
        ayuda1 = SE1,
        ayuda2 = SE2,      
        ayuda3 = SE3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        En un sistema equivalente, se busca simplificar un sistema complejo de fuerzas y momentos a un sistema más simple que genere el mismo efecto rotacional y traslacional. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Determinar fuerza resultante: }}$
        
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} X:}}$  
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{Rx}}}}$          
        ${{\hspace{{4mm}} F_{{Rx}} = F_2 \\cdot \\sin(\\alpha_1) - F_3 \\cdot \\dfrac{{3}}{{5}} = {f[1]*calc['sin1']:.2f} \\text{{ N}} - {f[2]*(3/5):.2f} \\text{{ N}} }}$          
        ${{\hspace{{4mm}} F_{{Rx}} = {f[1]*calc['sin1'] - f[2]*(3/5):.2f} \\text{{ N}} }}$          
        
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} Y:}}$  
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{Ry}}}}$          
        ${{\hspace{{4mm}} F_{{Ry}} = - F_1 - F_2 \\cdot \\cos(\\alpha_1) - F_3 \\cdot \\dfrac{{4}}{{5}} = {-f[0]:.0f}\\text{{ N}} - {f[1]*calc['cos1']:.2f} \\text{{ N}} - {f[2]*(4/5):.2f} \\text{{ N}} }}$          
        ${{\hspace{{4mm}} F_{{Ry}} = {-f[0] -  f[1]*calc['cos1'] - f[2]*(4/5):.2f} \\text{{ N}} }}$          
        
        $\\textbf{{\\small 2. Ubicación de fuerza resultante: }}$
        
        ${{\hspace{{4mm}} \\sum{{M_A}} = d \\cdot F_{{Ry}}}}$     
        ${{\hspace{{4mm}} d \\cdot F_{{Ry}} = - F_2 \\cdot \\cos(\\alpha_1) \\cdot d_1 - F_3 \\cdot \\dfrac{{4}}{{5}} \\cdot (d_1 + d_2) }}$     
        ${{\hspace{{4mm}} d \\cdot ({-f[0] -  f[1]*calc['cos1'] - f[2]*(4/5):.2f}) \\text{{ N}}  = - {f[1]*calc['cos1']:.2f} \\text{{ N}} \\cdot {d[0]:.0f} \\text{{ m}} - {f[2]*(4/5):.2f} \\text{{ N}} \\cdot {d[0] + d[3]:.0f} \\text{{ m}} }}$     
        ${{\hspace{{4mm}} d \\cdot ({-f[0] -  f[1]*calc['cos1'] - f[2]*(4/5):.2f}) \\text{{ N}}  = {-f[1]*calc['cos1']*d[0] - f[2]*(4/5)*(d[0] + d[3]):.2f} \\text{{ N}} \\cdot \\text{{ m}} }}$     
        ${{\hspace{{4mm}} d = {(f[1]*calc['cos1']*d[0] + f[2]*(4/5)*(d[0] + d[3]))/(f[0] + f[1]*calc['cos1'] + f[2]*(4/5)):.2f} \\text{{ m}} }}$     
        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 4110021,
        no_pregunta = 2,
        complexity = F,
        topic = "Sistemas equivalentes",
        subtopic = "Sistemas equivalentes",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"La losa de construcción está sometida a cuatro cargas de columnas. Determine la magnitud de $F_1$ y la coordenada en X de la fuerza resultante, si se sabe que la coordenada en Y donde actúa dicha fuerza es ${(d[0]+d[3])/2 :.2f} \\text{{ m}}$. Considere $F_2 = {f[1]:.0f} \\text{{ kN}}$, $F_3 = {f[1]/2:.2f} \\text{{ kN}}$, $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f} \\text{{ m}}$, $d_3 = {d[6]:.0f} \\text{{ m}}$, $d_4 = {d[9]:.0f} \\text{{ m}}$ y $d_5 = {d[12]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "$F_1$ [kN]",
        a2_name = "Coordenada en X [m]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[1]/2 + f[1]*(d[0]/(d[0]+d[3])),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((f[1]/2 + f[1]*(d[0]/(d[0]+d[3])))*(d[9] + d[12]) + f[1]*(d[6] + d[9] + d[12]) + (f[1]*d[12])/2)/(2*f[1] + f[1]*(d[0]/(d[0]+d[3]))) ,2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = SE1,
        ayuda2 = SE2,      
        ayuda3 = SE3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        En un sistema equivalente, se busca simplificar un sistema complejo de fuerzas y momentos a un sistema más simple que genere el mismo efecto rotacional y traslacional. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Determinar fuerza resultante: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_z}} = F_R}}$          
        ${{\hspace{{4mm}} F_R = - F_1 - F_2 - F_3 = - F_1 - {f[1]:.0f} \\text{{ kN}} - {f[1]/2:.2f} \\text{{ kN}} }}$          
        ${{\hspace{{4mm}} F_R = - F_1 - {(3*f[1])/2:.2f} \\text{{ kN}} }}$          
        
        $\\textbf{{\\small 2. Ubicación de fuerza resultante: }}$
        
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} momentos \\hspace{{2mm}} respecto \\hspace{{2mm}} al \\hspace{{2mm}} eje \\hspace{{2mm}} X:}}$  
        
        ${{\hspace{{4mm}} \\sum{{M_x}} = y \\cdot F_R}}$     
        ${{\hspace{{4mm}} - (F_1 + {(3*f[1])/2:.0f} \\text{{ kN}}) \\cdot {(d[0]+d[3])/2:.2f} \\text{{ m}} = - {f[1]:.0f} \\text{{ kN}} \\cdot {d[0] + d[3]:.0f} \\text{{ m}} - {f[1]/2:.2f} \\text{{ kN}} \\cdot {d[0]:.0f} \\text{{ m}}}}$     
        ${{\hspace{{4mm}} F_1 \\cdot {(d[0]+d[3])/2:.2f} \\text{{ m}} = {f[1]*(d[0] + d[3]):.0f} \\text{{ kN}} \\cdot \\text{{ m}} + {(f[1]*d[0])/2:.2f} \\text{{ kN}} \\cdot \\text{{ m}} - {((3*f[1])/2)*(d[0]+d[3])/2 :.2f} \\text{{ kN}} \\cdot \\text{{ m}} }}$     
        ${{\hspace{{4mm}} F_1 \\cdot {(d[0]+d[3])/2:.2f} \\text{{ m}} = {f[1]*(d[0] + d[3]) + (f[1]*d[0])/2 - 3*f[1]*(d[0]+d[3])/4 :.2f} \\text{{ kN}} \\cdot \\text{{ m}} }}$     
        ${{\hspace{{4mm}} F_1 = {f[1]/2 + f[1]*(d[0]/(d[0]+d[3])):.2f} \\text{{ kN}}  }}$     
        
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} momentos \\hspace{{2mm}} respecto \\hspace{{2mm}} al \\hspace{{2mm}} eje \\hspace{{2mm}} Y:}}$  
        
        ${{\hspace{{4mm}} \\sum{{M_y}} = x \\cdot F_R}}$     
        ${{\hspace{{4mm}} {2*f[1] + f[1]*(d[0]/(d[0]+d[3])) :.2f} \\text{{ kN}} \\cdot x = {f[1]/2 + f[1]*(d[0]/(d[0]+d[3])):.2f}\\text{{ kN}} \\cdot {d[9] + d[12]:.0f} \\text{{ m}}  + {f[1]:.0f} \\text{{ kN}} \\cdot {d[6] + d[9] + d[12]:.0f} \\text{{ m}} + {f[1]/2:.2f} \\text{{ kN}} \\cdot {d[12]:.0f} \\text{{ m}}}}$     
        ${{\hspace{{4mm}} {2*f[1] + f[1]*(d[0]/(d[0]+d[3])) :.2f} \\text{{ kN}} \\cdot x = {(f[1]/2 + f[1]*(d[0]/(d[0]+d[3])))*(d[9] + d[12]) + f[1]*(d[6] + d[9] + d[12]) + (f[1]*d[12])/2:.2f} \\text{{ kN}} \\cdot \\text{{ m}}}}$     
        ${{\hspace{{4mm}} x = {((f[1]/2 + f[1]*(d[0]/(d[0]+d[3])))*(d[9] + d[12]) + f[1]*(d[6] + d[9] + d[12]) + (f[1]*d[12])/2)/(2*f[1] + f[1]*(d[0]/(d[0]+d[3]))) :.2f} \\text{{ m}}}}$     
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),  

    Questionary(#3_1
        code = 4110031,
        no_pregunta = 3,
        complexity = F,
        topic = "Sistemas equivalentes",
        subtopic = "Sistemas equivalentes",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Se utiliza un puntual ajustable BC para colocar la estructura en posición vertical. Reemplace el sistema mostrado con un sistema equivalente fuerza-par en A y determine las componentes del momento resultante. Considere $F_1 = {f[0]:.0f} \\text{{ kN}}$, $d_1 = {2 + d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[0]:.0f}  \\text{{ m}}$, $d_3 = {d[3]:.0f} \\text{{ m}}$ y $d_4 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Componente $M_{{Rx}}$ [$kN \\cdot m$]",
        a2_name = "Componente $M_{{Ry}}$ [$kN \\cdot m$]",
        a3_name = "Componente $M_{{Rz}}$ [$kN \\cdot m$]",
        answer1 = lambda f, a, calc, c, d, m: np.round(d[6]*(f[0]*(d[3]))/(Calculations.magnitude3D(d[3],d[6],2)),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-(d[0])*(f[0]*d[6])/(Calculations.magnitude3D(d[3],d[6],2)),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(-(d[0]+2)*(f[0]*(d[3]))/(Calculations.magnitude3D(d[3],d[6],2)), 2),
        ayuda1 = SE4,
        ayuda2 = SE5,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Un sistema equivalente fuerza-par es la combinación de una fuerza aplicada y un momento que producen el mismo efecto rotacional y traslacional sobre un cuerpo rígido que el sistema original. A continuación, se presenta la solución sugerida para el ejercicio:
       
        Para determinar el momento resultante en el sistema equivalente, cabe notar que solo es necesario calcular el momento que produce la fuerza $F_1$. Dado que, al trasladar la fuerza $F_1$ al punto A, esta fuerza ya no produce momento en dicho punto:
        
        $\\textbf{{\\small 1. Descomposición F1: }}$
        
        ${{\hspace{{4mm}} \\overrightarrow{{F_1}} = |\\overrightarrow{{F_1}}| \\cdot \\lambda_{{CB}}}}$    
        ${{\hspace{{4mm}} \\overrightarrow{{F_1}} = {f[0]:.0f}{{\\text{{ kN}}}} \\cdot [ ( {(2)/(Calculations.magnitude3D(2,d[3],d[6])):.2f} )\\hat{{i}} + ( {-(d[3])/(Calculations.magnitude3D(2,d[3],d[6])):.2f} )\\hat{{j}} + ( {(d[6])/(Calculations.magnitude3D(2,d[3],d[6])):.2f} )\\hat{{k}}]}}$    
        ${{\hspace{{4mm}} \\overrightarrow{{F_1}} = [ {(f[0]*2)/(Calculations.magnitude3D(2,d[6],d[3])):.2f} \\hat{{i}} - {(f[0]*(d[3]))/(Calculations.magnitude3D(d[3],d[6],2)):.2f} \\hat{{j}} + ( {(f[0]*d[6])/(Calculations.magnitude3D(d[3],d[6],2)):.2f} )\\hat{{k}}] {{\\text{{ kN}}}}}}$     
        
       
        $\\textbf{{\\small 2. Calculo del momento resultante: }}$  
        
        $\\underline{{Componente \\hspace{{2mm}} \\hat{{i}} :}}$
        
        Haciendo Producto Cruz, la componente $\\hat{{i}}$ del momento se puede calcular como:
        
        ${{\hspace{{4mm}} M_i = r_y \\cdot F_z - r_z \\cdot F_y = 0 \\text{{ m}} \\cdot  {(f[0]*d[6])/(Calculations.magnitude3D(d[3],d[6],2)):.2f}  \\text{{ kN}} + {d[6]:.0f} \\text{{ m}} \\cdot {(f[0]*(d[3]))/(Calculations.magnitude3D(d[3],d[6],2)):.2f} \\text{{ kN}}}}$       
        ${{\hspace{{4mm}} M_i = {d[6]*(f[0]*(d[3]))/(Calculations.magnitude3D(d[3],d[6],2)):.2f} \\text{{ kN}} \\cdot \\text{{ m}} }}$       
        
        $\\underline{{Componente \\hspace{{2mm}} \\hat{{j}} :}}$
        
        Haciendo Producto Cruz, la componente $\\hat{{j}}$ del momento se puede calcular como:
        
        ${{\hspace{{4mm}} M_j = - ( r_x \\cdot F_z - r_z \\cdot F_x ) = -( {d[0]+2:.0f} \\text{{ m}} \\cdot {(f[0]*d[6])/(Calculations.magnitude3D(d[3],d[6],2)):.2f} \\text{{ kN}} - {d[6]:.0f} \\text{{ m}} \\cdot {(f[0]*2)/(Calculations.magnitude3D(2,d[6],d[3])):.2f} \\text{{ kN}} )}}$       
        ${{\hspace{{4mm}} M_j =  {d[6]*(f[0]*2)/(Calculations.magnitude3D(2,d[6],d[3])):.2f} \\text{{ kN}} \\cdot \\text{{ m}} - {(d[0]+2)*(f[0]*d[6])/(Calculations.magnitude3D(d[3],d[6],2)):.2f} \\text{{ kN}} \\cdot \\text{{ m}} = {-(d[0])*(f[0]*d[6])/(Calculations.magnitude3D(d[3],d[6],2)):.2f} \\text{{ kN}} \\cdot \\text{{ m}}}}$   
        
        $\\underline{{Componente \\hspace{{2mm}} \\hat{{k}} :}}$
        
        Haciendo Producto Cruz, la componente $\\hat{{k}}$ del momento se puede calcular como:
        
        ${{\hspace{{4mm}} M_k=  r_x \\cdot F_y - r_y \\cdot F_x  = {d[0] + 2:.0f} \\text{{ m}} \\cdot {-(f[0]*(d[3]))/(Calculations.magnitude3D(d[3],d[6],2)):.2f} \\text{{ kN}} - 0 \\text{{ m}} \\cdot {(f[0]*2)/(Calculations.magnitude3D(2,d[6],d[3])):.2f}{{ \\text{{ kN}}}}}}$       
        ${{\hspace{{4mm}} M_k = {-(d[0]+2)*(f[0]*(d[3]))/(Calculations.magnitude3D(d[3],d[6],2)):.2f}{{\\text{{ kN}} \\cdot \\text{{ m}}}}}}$   
        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_1
        code = 4110041,
        no_pregunta = 4,
        complexity = F,
        topic = "Sistemas equivalentes",
        subtopic = "Sistemas equivalentes",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Sustituya la fuerza y el par dados por un sistema fuerza-momento equivalente en el punto $A$. Considere que $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$, $d_0 = {d[0]:.0f} \\text{{ m}}$ y $\\theta = {a[0]:.0f}°$.",
        no_answers = 2,
        a1_name = "Magnitud Fuerza equivalente $[N]$",
        a2_name = "Magnitud Momento equivalente $[N \\cdot m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[1],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(abs(f[1]*Calculations.sine(a[0])*d[0]-f[0]*d[0]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = SE1,
        ayuda2 = SE2,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Un sistema equivalente fuerza-par es la combinación de una fuerza aplicada y un momento que producen el mismo efecto rotacional y traslacional sobre un cuerpo rígido que el sistema original. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Cálculo fuerza equivalente: }}$

        La fuerza equivalente es igual a la fuerza $F_2$, dado que, las fuerzas pares $F_1$ se anulan entre sí.

        ${{\hspace{{4mm}} |F_{{eq}}| = {f[1]:.2f} \\text{{ N}}}}$     
        
        $\\textbf{{\\small 2. Cálculo del momento equivalente: }}$

        $\\underline{{Momento \\text{{ }} par:}}$ 

        ${{\hspace{{4mm}} M_{{F1}} = -F_1 \\cdot d_0}}$           
        ${{\hspace{{4mm}} M_{{F1}} = {(-1*f[0]*d[0]):.2f} \\text{{ }} \\hat{{k}} \\text{{ }} N \\cdot m}}$         

        $\\underline{{Momento \\text{{ }} generado \\text{{ }} por \\text{{ }} F2:}}$ 

        ${{\hspace{{4mm}} M_{{F2}} = F_2 \\cdot sen(\\theta)}}$           
        ${{\hspace{{4mm}} M_{{F2}} = {(f[1]*Calculations.sine(a[0])*d[0]):.2f} \\text{{ }} \\hat{{k}} \\text{{ }} N \\cdot m}}$       

        $\\underline{{Sumatoria \\text{{ }} de \\text{{ }} momentos \\text{{ }} en \\text{{ }} A:}}$ 

        ${{\hspace{{4mm}} \\sum{{M_A}} = M_{{F1}} + M_{{F2}}}}$                  
        ${{\hspace{{4mm}} M_A = {(f[1]*Calculations.sine(a[0])*d[0])-(f[0]*d[0]):.2f} \\text{{ }} \\hat{{k}} \\text{{ }} N \\cdot m}}$     
        ${{\hspace{{4mm}} |M_A| = |M_{{eq}}| = {abs((f[1]*Calculations.sine(a[0])*d[0])-(f[0]*d[0])):.2f} \\text{{ }} \\hat{{k}} \\text{{ }} N \\cdot m}}$          
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
    ),
    
    Questionary(#5_1
        code = 4110051,
        no_pregunta = 5,
        complexity = F,
        topic = "Sistemas equivalentes",
        subtopic = "Sistemas equivalentes",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Reemplace el sistema de cargas aplicado, por una carga y un momento en el punto $O$. La fuerza $F = {f[0]:.0f} \\text{{ kN}}$ está en el plano $y-z$ y forma un ángulo $\\phi = {a[0]:.0f}°$ con el eje $Z$. Considere que $d_0 = {d[0]+10:.0f} \\text{{ m}}$, $d_1 = {d[0]+2:.0f} \\text{{ m}}$ y $\\theta = {a[4]:.0f}°$, el cual se encuentra en el plano en el plano $x-z$.",
        no_answers = 2,
        a1_name = "Magnitud Fuerza equivalente $[kN]$",
        a2_name = "Magnitud Momento equivalente $[kN \\cdot m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D((d[0]+10)*f[0]*Calculations.cosine(a[0])-(d[0]+2)*Calculations.sine(a[0])*f[0]*Calculations.sine(a[4]),(d[0]+2)*Calculations.cosine(a[4])*f[0]*Calculations.cosine(a[0]),(d[0]+2)*Calculations.cosine(a[4])*f[0]*Calculations.sine(a[0])),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = SE1,
        ayuda2 = SE2,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Un sistema equivalente fuerza-par es la combinación de una fuerza aplicada y un momento que producen el mismo efecto rotacional y traslacional sobre un cuerpo rígido que el sistema original. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Cálculo fuerza equivalente: }}$

        La fuerza equivalente es igual a la fuerza $F$, dado que, es la única fuerza aplicada en el sistema.

        ${{\hspace{{4mm}} |F_{{eq}}| = F = {f[0]:.2f} \\text{{ kN}}}}$     
        
        $\\textbf{{\\small 2. Cálculo del momento equivalente: }}$

        ${{\hspace{{4mm}} \\vec{{r}} = [d_1 \\cdot Cos(\\theta) \\hat{{ i}} + d_0 \\hat{{ j}} - d_1 \\cdot Sen(\\theta) \\hat{{ k}}] \\text{{ m}}}}$       
        ${{\hspace{{4mm}} \\vec{{r}} = [{d[0]+2} \\cdot Cos({a[4]}) \\hat{{ i}}+ {d[0]+10} \\hat{{ j}} - {d[0]+2} \\cdot Sen({a[4]})\\hat{{k}}] \\text{{ m}}}}$

        ${{\hspace{{4mm}} \\vec{{F}} = [0 \\hat{{ i}} - F \\cdot Sen(\\phi) \\hat{{ j}} + F \\cdot Cos(\\phi) \\hat{{ k}}] \\text{{ kN}}}}$          
        ${{\hspace{{4mm}} \\vec{{F}} = [0 \\hat{{ i}} - {f[0]:.0f} \\cdot Sen({a[0]:.0f}) \\hat{{ j}} + {f[0]:.0f} \\cdot Cos({a[0]:.0f}) \\hat{{ k}}] \\text{{ kN}}}}$

        Al realizar el producto cruz se obtiene:

        ${{\hspace{{4mm}} \\vec{{M}} = [({(d[0]+10)*f[0]*Calculations.cosine(a[0])-(d[0]+2)*Calculations.sine(a[0])*f[0]*Calculations.sine(a[4]):.2f})\\hat{{i}}-({(d[0]+2)*Calculations.cosine(a[4])*f[0]*Calculations.cosine(a[0]):.2f})\\hat{{j}}-({(d[0]+2)*Calculations.cosine(a[4])*f[0]*Calculations.sine(a[0]):.2f})\\hat{{k}}] \\text{{ }} kN \\cdot m}}$
       
        
        Encontrando la magnitud tenemos que:

        ${{\hspace{{4mm}} |\\vec{{M}}| = {Calculations.magnitude3D((d[0]+10)*f[0]*Calculations.cosine(a[0])-(d[0]+2)*Calculations.sine(a[0])*f[0]*Calculations.sine(a[4]),(d[0]+2)*Calculations.cosine(a[4])*f[0]*Calculations.cosine(a[0]),(d[0]+2)*Calculations.cosine(a[4])*f[0]*Calculations.sine(a[0])):.2f} \\text{{ }} kN \\cdot m}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
   

   
    #========================================================  SISTEMAS EQUIVALENTES  =========================================================
    #-------------------------------------------------       Sistemas equivalentes 2D-3D      --------------------------------------------
    #-------------------------------------------------       Nivel Medio   ---------------------------------------------------
    #-------------------------------------------------       Code: 41200##    --------------------------------------------------
    Questionary(#1_1
        code = 4120011,
        no_pregunta = 1,
        complexity = M,
        topic = "Sistemas equivalentes",
        subtopic = "Sistemas equivalentes",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Reemplace el sistema de fuerzas que actúa sobre el poste por una única fuerza resultante ubicada en el tramo AB. Determine las componentes de esta fuerza (Indique el signo de la dirección de las fuerzas) y la posición donde actúa, medida desde el extremo B. Considere $F_1 = {f[1]/4:.2f} \\text{{ N}}$, $F_2 = {f[1]:.2f} \\text{{ N}}$, $F_3 = {f[1]*1.3:.2f} \\text{{ N}}$, $\\alpha_1 = {a[0]:.0f}°$, $d_1 = {d[0]/10:.2f} \\text{{ m}}$,  $d_2 = {(2*d[0])/10:.2f}  \\text{{ m}}$, $d_3 = {d[6]:.0f} \\text{{ m}}$, $d_4 = {d[9]:.0f}  \\text{{ m}}$ y $d_5 = {d[12]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Componente $F_{{Rx}}$ [N]",
        a2_name = "Componente $F_{{Ry}}$ [N]",
        a3_name = "Distancia desde el extremo B [m]",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[1]/4)*calc['cos1'] - f[1]*(4/5) - f[1]*1.3,2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[1]*(3/5) - (f[1]/4)*calc['sin1'],2),
        answer3 = lambda f, a, calc, c, d, m: np.round(((f[1]/4)*calc['sin1']*(2*(d[0]/10)) + f[1]*(4/5)*d[12] + f[1]*(3/5)*(d[0]/20) + f[1]*1.3*(d[12] + d[9]))/(-(f[1]/4)*calc['cos1'] + f[1]*(4/5) + f[1]*1.3), 2),
        ayuda1 = SE1,
        ayuda2 = SE2,      
        ayuda3 = SE3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        En un sistema equivalente, se busca simplificar un sistema complejo de fuerzas y momentos a un sistema más simple que genere el mismo efecto rotacional y traslacional. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Determinar fuerza resultante: }}$
        
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} X:}}$  
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{Rx}}}}$          
        ${{\hspace{{4mm}} F_{{Rx}} = F_1 \\cdot \\cos(\\alpha_1) - F_2 \\cdot \\dfrac{{4}}{{5}} - F_3 = {(f[1]/4)*calc['cos1']:.2f} \\text{{ N}} - {f[1]*(4/5):.2f} \\text{{ N}}  - {f[1]*1.3:.2f} \\text{{ N}}}}$          
        ${{\hspace{{4mm}} F_{{Rx}} = {(f[1]/4)*calc['cos1'] - f[1]*(4/5) - f[1]*1.3:.2f} \\text{{ N}} }}$          
        
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} Y:}}$  
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{Ry}}}}$          
        ${{\hspace{{4mm}} F_{{Ry}} = F_2 \\cdot \\dfrac{{3}}{{5}} - F_1 \\cdot \\sin(\\alpha_1) = {f[1]*(3/5):.2f}\\text{{ N}} - {(f[1]/4)*calc['sin1']:.2f} \\text{{ N}} }}$          
        ${{\hspace{{4mm}} F_{{Ry}} = {f[1]*(3/5) - (f[1]/4)*calc['sin1']:.2f} \\text{{ N}} }}$          
        
        $\\textbf{{\\small 2. Ubicación de fuerza resultante: }}$
        
        ${{\hspace{{4mm}} \\sum{{M_B}} = d \\cdot F_{{Rx}}}}$     
        ${{\hspace{{4mm}} d \\cdot F_{{Rx}} = - F_1 \\cdot \\sin(\\alpha_1) \\cdot d_2 - F_2 \\cdot \\dfrac{{4}}{{5}} \\cdot d_5 - F_2 \\cdot \\dfrac{{3}}{{5}} \\cdot \\dfrac{{d_1}}{{2}} - F_3 \\cdot (d_5 + d_4)}}$     
        ${{\hspace{{4mm}} d \\cdot ({(f[1]/4)*calc['cos1'] - f[1]*(4/5) - f[1]*1.3:.2f}) \\text{{ N}}  = - {(f[1]/4)*calc['sin1']:.2f} \\text{{ N}} \\cdot {(d[0]*2)/10:.2f} \\text{{ m}} - {f[1]*(4/5):.2f} \\text{{ N}} \\cdot {d[12]:.0f} \\text{{ m}} - {f[1]*(3/5):.2f} \\text{{ N}} \\cdot {d[0]/20:.2f} \\text{{ m}} - {f[1]*1.3:.0f} \\text{{ N}} \\cdot {d[12] + d[9]:.0f} \\text{{ m}}}}$     
        ${{\hspace{{4mm}} d \\cdot ({(f[1]/4)*calc['cos1'] - f[1]*(4/5) - f[1]*1.3:.2f}) \\text{{ N}}  = - {(f[1]/4)*calc['sin1']*(2*(d[0]/10)) + f[1]*(4/5)*d[12] + f[1]*(3/5)*(d[0]/20) + f[1]*1.3*(d[12] + d[9]):.2f} \\text{{ N}} \\cdot \\text{{ m}}}}$     
        ${{\hspace{{4mm}} d = {((f[1]/4)*calc['sin1']*(2*(d[0]/10)) + f[1]*(4/5)*d[12] + f[1]*(3/5)*(d[0]/20) + f[1]*1.3*(d[12] + d[9]))/(-(f[1]/4)*calc['cos1'] + f[1]*(4/5) + f[1]*1.3):.2f} \\text{{ m}}}}$     
        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    Questionary(#2_1
        code = 4120021,
        no_pregunta = 2,
        complexity = M,
        topic = "Sistemas equivalentes",
        subtopic = "Sistemas equivalentes",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Las ménsulas están sometidas a la acción de cuatro cargas. Determine la magnitud de $F_1$ y $F_3$ (utilizando el signo correspondiente para indicar su dirección), de modo que la fuerza resultante pase por el origen. Considere $F_2 = {f[2]:.0f} \\text{{ N}}$, $F_4 = {f[4]:.2f} \\text{{ N}}$, $d_1 = {d[0]/10:.2f} \\text{{ m}}$,  $d_2 = {(3*d[0])/20:.2f} \\text{{ m}}$, $d_3 = {(d[0]+d[3])*(3/20):.2f} \\text{{ m}}$, $d_4 = {(d[0]+d[3])/10:.2f} \\text{{ m}}$, $d_5 = {(d[0]+d[6])/10:.2f} \\text{{ m}}$ y $d_6 = {(d[0]+d[6])*(3/20):.2f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "$F_1$ $[N]$",
        a2_name = "$F_3$ $[N]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(-((2/3)*(f[4]-f[2]) + ((2*f[2]-f[4])*(d[0]+d[3]) - f[4]*(d[0]+d[6]))*(2/3)*(1/(d[3] - d[6]))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-(((2*f[2]-f[4])*(d[0]+d[3]) - f[4]*(d[0]+d[6]))*(2/3)*(1/(d[3] - d[6]))) ,2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = SE1,
        ayuda2 = SE2,      
        ayuda3 = SE3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        En un sistema equivalente, se busca simplificar un sistema complejo de fuerzas y momentos a un sistema más simple que genere el mismo efecto rotacional y traslacional. A continuación, se presenta la solución sugerida para el ejercicio:
        
        Para la solución se considera que  $F_1$ y $F_3$ actúan en la dirección negativa del eje $Z$.
        
        $\\textbf{{\\small 1. Ubicación de fuerza resultante: }}$
        
        Para cumplir la condición de que la fuerza resultante pase por el origen, la sumatoria de momentos respecto a los ejes $X$ y $Y$ debe ser igual a cero:        
        
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} momentos \\hspace{{2mm}} respecto \\hspace{{2mm}} al \\hspace{{2mm}} eje \\hspace{{2mm}} Y:}}$  
        
        ${{\hspace{{4mm}} \\sum{{M_y}} = F_1 \\cdot d_2 + F_2 \\cdot d_1 - F_3 \\cdot d_2 - F_4 \\cdot d_1= 0}}$     
        ${{\hspace{{4mm}} F_1 \\cdot {d[0]*(3/20):.2f} \\text{{ m}}  + {f[2]:.0f} \\text{{ N}} \\cdot {d[0]/10:.2f} \\text{{ m}} - F_3 \\cdot {d[0]*(3/20):.2f} \\text{{ m}} - {f[4]:.0f} \\text{{ N}} \\cdot {d[0]/10:.2f} \\text{{ m}} = 0}}$     
        ${{\hspace{{4mm}} (F_1 - F_3) \\cdot {d[0]*(3/20):.2f} \\text{{ m}} = {(d[0]/10)*(f[4]-f[2]):.2f} \\text{{ N}} \\cdot \\text{{ m}}}}$     
        ${{\hspace{{4mm}} F_1 = {(2/3)*(f[4]-f[2]):.2f} \\text{{ N}} + F_3 }}$        
        
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} momentos \\hspace{{2mm}} respecto \\hspace{{2mm}} al \\hspace{{2mm}} eje \\hspace{{2mm}} X:}}$  
        
        ${{\hspace{{4mm}} \\sum{{M_x}} = F_1 \\cdot d_3 - F_2 \\cdot d_4 - F_3 \\cdot d_6 + F_4 \\cdot d_5 = 0}}$     
        ${{\hspace{{4mm}} F_1 \\cdot {(d[0] + d[3])*(3/20):.2f} \\text{{ m}} + {f[4]:.0f} \\text{{ N}} \\cdot {(d[0]+d[6])/10:.2f} \\text{{ m}} - F_3 \\cdot {(d[0] + d[6])*(3/20):.2f} \\text{{ m}} - {f[2]:.0f} \\text{{ N}} \\cdot {(d[0]+d[3])/10:.2f} \\text{{ m}}= 0}}$     
        ${{\hspace{{4mm}} ({(2/3)*(f[4]-f[2]):.2f} \\text{{ N}} + F_3) \\cdot {(d[0] + d[3])*(3/20):.2f} \\text{{ m}} - F_3 \\cdot {(d[0] + d[6])*(3/20):.2f} \\text{{ m}} = {(f[2]*(d[0]+d[3]))/10:.2f} \\text{{ N}} \\cdot \\text{{ m}} - {f[4]*(d[0]+d[6])/10:.2f} \\text{{ N}} \\cdot \\text{{ m}}}}$     
        ${{\hspace{{4mm}} {(f[4]-f[2])*(d[0] + d[3])*(1/10):.2f} \\text{{ N}} \\cdot \\text{{ m}} + F_3 \\cdot {(d[0] + d[3])*(3/20):.2f} \\text{{ m}} - F_3 \\cdot {(d[0] + d[6])*(3/20):.2f} \\text{{ m}} = {(f[2]*(d[0]+d[3]) - f[4]*(d[0]+d[6]))*(1/10):.2f} \\text{{ N}} \\cdot \\text{{ m}}}}$     
        ${{\hspace{{4mm}} F_3 \\cdot {(d[3] - d[6])*(3/20):.2f} \\text{{ m}} = {((2*f[2]-f[4])*(d[0]+d[3]) - f[4]*(d[0]+d[6]))*(1/10):.2f} \\text{{ N}} \\cdot \\text{{ m}}}}$     
        ${{\hspace{{4mm}} F_3 = {((2*f[2]-f[4])*(d[0]+d[3]) - f[4]*(d[0]+d[6]))*(2/3)*(1/(d[3] - d[6])):.2f} \\text{{ N}}}}$     
                
        Finalmente, se obtiene $F_1$:
        
        ${{\hspace{{4mm}} F_1 = {(2/3)*(f[4]-f[2]):.2f} \\text{{ N}} + F_3 }}$        
        ${{\hspace{{4mm}} F_1 = {(2/3)*(f[4]-f[2]):.2f} \\text{{ N}} + {((2*f[2]-f[4])*(d[0]+d[3]) - f[4]*(d[0]+d[6]))*(2/3)*(1/(d[0] - d[6])):.2f} \\text{{ N}} }}$        
        ${{\hspace{{4mm}} F_1 = {(2/3)*(f[4]-f[2]) + ((2*f[2]-f[4])*(d[0]+d[3]) - f[4]*(d[0]+d[6]))*(2/3)*(1/(d[3] - d[6])):.2f} \\text{{ N}} }}$      

        Para la respuesta, se ingresa con el signo correspondiente, teniendo en cuenta la suposición inicial:        
        ${{\hspace{{4mm}} F_1 = {-((2/3)*(f[4]-f[2]) + ((2*f[2]-f[4])*(d[0]+d[3]) - f[4]*(d[0]+d[6]))*(2/3)*(1/(d[3] - d[6]))):.2f} \\text{{ N}} }}$           
        ${{\hspace{{4mm}} F_3 = {-(((2*f[2]-f[4])*(d[0]+d[3]) - f[4]*(d[0]+d[6]))*(2/3)*(1/(d[3] - d[6]))):.2f} \\text{{ N}}}}$    
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 4120031,
        no_pregunta = 3,
        complexity = M,
        topic = "Sistemas equivalentes",
        subtopic = "Sistemas equivalentes",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"El techo de una estructura está sometido a cargas de viento que actúan perpendicularmente a la cubierta, tal como se muestra en la figura. Determine la fuerza y el momento resultante equivalente en el punto $B$. Tenga presente que todas las fuerzas mostradas actuan perpendicularmente a la cubierta. Considere los siguientes valores para las fuerzas y las distancias: $F_1 = {f[1]:.0f} \\text{{ N}}$, $F_2 = {f[2]:.0f} \\text{{ N}}$, $d_1 = {d[0]+(3/2):.2f} \\text{{ m}}$,  $d_2 = {d[0]:.1f} \\text{{ m}}$, $d_3 = {d[3]:.1f} \\text{{ m}}$ y $d_4 = {d[3]+1:.1f} \\text{{ m}}$.",    
        no_answers = 2,
        a1_name = "Fuerza resultante $F_R$ $[N]$",
        a2_name = "Momento resultante $M_R$ $[N \\cdot m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((d[0]/(Calculations.magnitude((d[3]*2+1),d[0])))*(2*f[1]+4*f[2]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((d[3]*2+1)/(Calculations.magnitude((d[3]*2+1),d[0])))*2*(f[2]*(d[3]*2+1) + f[1]*(d[3]+1)) - 2*(d[0]/(Calculations.magnitude((d[3]*2+1),d[0])))*(f[2]*(3*d[0]+3) + f[1]*(d[0]+(3/2)+((d[0]*d[3])/(2*d[3]+1)))) ,2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = SE1,
        ayuda2 = SE4,      
        ayuda3 = SE6,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        En un sistema equivalente, se busca simplificar un sistema complejo de fuerzas y momentos a un sistema más simple que genere el mismo efecto rotacional y traslacional. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Determinar fuerza resultante: }}$
        
        Todas las fuerzas mostradas actúan en la dirección positivade  $\\hat{{i}}$ y sus componentes en $\\hat{{j}}$ se cancelan entre sí. Por lo tanto, la fuerza resultante solo tiene únicamente una componente en $\\hat{{i}}$, la cual corresponde a la suma de las respectivas componentes de cada una de las fuerzas.
        
        Dado que cada fuerza es perpendicular a la cubierta del techo y todas tienen el mismo ángulo asociado; se puede encontrar el ángulo de una fuerza y este será aplicable a las demás:   
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        ${{\hspace{{4mm}} \\alpha = \\arcsin(\\dfrac{{d_2}}{{\\sqrt{{(d_3 + d_4)^{{2}} + (d_2)^{{2}}}}}}) }}$

        La fuerza resultante es:
        
        ${{\hspace{{4mm}} F_R = \\sin(\\alpha) \\cdot (2F_1 + 4F_2) }}$     
        ${{\hspace{{4mm}} F_R = \\dfrac{{d_2}}{{\\sqrt{{(d_3 + d_4)^{{2}} + (d_2)^{{2}}}}}} \\cdot (2F_1 + 4F_2) }}$     
        ${{\hspace{{4mm}} F_R = {(d[0]/(Calculations.magnitude((d[3]*2+1),d[0])))*(2*f[1]+4*f[2]):.2f} \\text{{ N}}}}$     
        
        $\\textbf{{\\small 2. Determinar el momento resultante con respecto a B: }}$
        
        Sabiendo que las componentes $\\hat{{j}}$ de las fuerzas realizan momento par y que las componenetes $\\hat{{i}}$ de las fuerzas realizan momento según su altura, se puede obtener que la sumatoria de momentos con respecto al punto $B$ es:
        
        ${{\hspace{{4mm}} \\sum{{M_B}} = F_2 \\cos(\\alpha) \\cdot 2(d_4 + d_3) + F_1 \\cdot \\cos(\\alpha) \\cdot 2d_4 - 2 \\cdot \\sin(\\alpha) ( F_2 \\cdot d_1 + F_2 \\cdot (d_1 + d_2) + F_1 \\cdot \\left(d_1 + \\dfrac{{d_2 \\cdot d_3}}{{d_3 + d_4}}\\right) }}$      
        ${{\hspace{{4mm}} \\sum{{M_B}} = M_R = {((d[3]*2+1)/(Calculations.magnitude((d[3]*2+1),d[0])))*2*(f[2]*(d[3]*2+1) + f[1]*(d[3]+1)) - 2*(d[0]/(Calculations.magnitude((d[3]*2+1),d[0])))*(f[2]*(3*d[0]+3) + f[1]*(d[0]+(3/2)+((d[0]*d[3])/(2*d[3]+1)))):.2f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
   
    Questionary(#4_1
        code = 4120041,
        no_pregunta = 4,
        complexity = M,
        topic = "Sistemas equivalentes",
        subtopic = "Sistemas equivalentes",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Considere la placa de cimentación mostrada en la figura, la cual recibe cuatro cargas $F_1 = {f[0]:.0f} \\text{{ kN}}$, $F_2 = {f[1]:.0f} \\text{{ kN}}$, $F_3 = {f[2]:.0f} \\text{{ kN}}$ y $F_4 = {f[3]:.0f} \\text{{ kN}}$. Encuentre el sistema equivalente de una sola fuerza aplicada sobre la placa y dónde está ubicada con respecto al origen. Considere que $d_0 = {d[0]:.0f} \\text{{ m}}$ y $d_1 = {d[3]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Distancia en $x$ $[m]$",
        a2_name = "Distancia en $z$ $[m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((f[2]+f[1])*d[0])/(f[0]+f[1]+f[2]+f[3]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((f[2]+f[3])*d[3])/(f[0]+f[1]+f[2]+f[3]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = SE1,
        ayuda2 = SE2,      
        ayuda3 = SE3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        En un sistema equivalente, se busca simplificar un sistema complejo de fuerzas y momentos a un sistema más simple que genere el mismo efecto rotacional y traslacional. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Determinar fuerza resultante: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = F_R}}$          
        ${{\hspace{{4mm}} F_R = - F_1 - F_2 - F_3 - F_4 }}$          
        ${{\hspace{{4mm}} F_R = -{(f[0]+f[1]+f[2]+f[3])} \\text{{ kN}} }}$          
        
        $\\textbf{{\\small 2. Ubicación de fuerza resultante: }}$

        Se realiza la sumatoria de momentos con respecto al origen:

        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} momentos \\hspace{{2mm}} respecto \\hspace{{2mm}} al \\hspace{{2mm}} eje \\hspace{{2mm}} X:}}$

        ${{\hspace{{4mm}} \\sum{{M_x}} = z \\cdot F_R}}$          
        ${{\hspace{{4mm}} (F_3 + F_4) \\cdot d_1 = z \\cdot F_R}}$          
        ${{\hspace{{4mm}} z = \\dfrac{{(F_3 + F_4) \\cdot d_1}}{{F_R}} }}$            
        ${{\hspace{{4mm}} z = {((f[2]+f[3])*d[3])/(f[0]+f[1]+f[2]+f[3]):.2f} \\text{{ m}} }}$            

        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} momentos \\hspace{{2mm}} respecto \\hspace{{2mm}} al \\hspace{{2mm}} eje \\hspace{{2mm}} Z:}}$

        ${{\hspace{{4mm}} \\sum{{M_z}} = - x \\cdot F_R}}$          
        ${{\hspace{{4mm}} -(F_2 + F_3) \\cdot d_0 = - x \\cdot F_R}}$             
        ${{\hspace{{4mm}} x = \\dfrac{{(F_2 + F_3) \\cdot d_0}}{{F_R}} }}$          
        ${{\hspace{{4mm}} x = {((f[2]+f[1])*d[0])/(f[0]+f[1]+f[2]+f[3]):.2f} \\text{{ m}} }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 

    Questionary(#5_1
        code = 4130051,
        no_pregunta = 5,
        complexity = M,
        topic = "Sistemas equivalentes",
        subtopic = "Sistemas equivalentes",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Reemplace el sistema de fuerzas mostrado por una única fuerza ubicada a lo largo de la linea $C-B$, reporte la localización con respecto al punto $C$. Considere que $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$, $F_3 = {f[2]:.0f} \\text{{ N}}$ y $M = {m[0]:.0f} \\text{{ }} N \\cdot m$, $d_0 = {d[0]:.0f} \\text{{ m}}$ y $\\theta = {a[0]:.0f}°$. ",
        no_answers = 2,
        a1_name = "Distancia $x$ $[m]$",
        a2_name = "Distancia $y$ $[m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((m[0]+f[1]*Calculations.cosine(a[0])*d[0]+f[2]*d[0])/(f[0]+f[1]*Calculations.cosine(a[0])+f[2]+f[1]*Calculations.sine(a[0])),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((m[0]+f[1]*Calculations.cosine(a[0])*d[0]+f[2]*d[0])/(f[0]+f[1]*Calculations.cosine(a[0])+f[2]+f[1]*Calculations.sine(a[0])),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = SE1,
        ayuda2 = SE2,      
        ayuda3 = SE3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        En un sistema equivalente, se busca simplificar un sistema complejo de fuerzas y momentos a un sistema más simple que genere el mismo efecto rotacional y traslacional. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Determinar fuerza resultante: }}$

        Es importante tener en cuenta que las fuerzas $F_1$ únicamente generan un momento par y no tienen ningún efecto traslacional.

        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} X:}}$  
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{Rx}}}}$           
        ${{\hspace{{4mm}} F_{{Rx}} = F_2 \\cdot \\cos(\\theta) + F_1}}$           
        ${{\hspace{{4mm}} F_{{Rx}} = {f[0]+f[1]*Calculations.cosine(a[0]):.2f} \\text{{ N}} }}$          
        
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} Y:}}$  
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{Ry}}}}$          
        ${{\hspace{{4mm}} F_{{Ry}} = -F_2 \\cdot \\sin(\\theta) - F_3}}$          
        ${{\hspace{{4mm}} F_{{Ry}} = {f[2]+f[1]*Calculations.sine(a[0]):.2f} \\text{{ N}} }}$          
        
        Por lo tanto la fuerza resultante $|F_R| = {Calculations.magnitude(f[0]+f[1]*Calculations.cosine(a[0]),f[2]+f[1]*Calculations.sine(a[0])):.2f} \\text{{ N}}$
        
        
        $\\textbf{{\\small 2. Ubicación de la fuerza resultante: }}$

        Se realiza la sumatoria de momentos con respecto al punto $C$. Para el sistema equivalente, se considera que las distancias desde la fuerza hasta el punto $C$ en $X$ y en $Y$ son iguales, dado que, la figura es un cuadrado. En los cálculos, estas distancias se identifican como $d$:      

        ${{\hspace{{4mm}} \\sum{{M_{{C_{{Original}}}}}} = \\sum{{M_{{C_{{Equivalente}}}}}}}}$             
        ${{\hspace{{4mm}} - M - F_2 \\cdot Cos({a[0]}) - F_3 \\cdot d_0 = - F_{{Rx}} \\cdot d - F_{{Ry}} \\cdot d }}$           

        ${{\hspace{{4mm}} d = \\dfrac{{M + F_2 \\cdot Cos({a[0]}) + F_3 \\cdot d_0}}{{F_{{Rx}}+F_{{Ry}}}} }}$              
        ${{\hspace{{4mm}} d = {(m[0]+f[1]*Calculations.cosine(a[0])*d[0]+f[2]*d[0])/(f[0]+f[1]*Calculations.cosine(a[0])+f[2]+f[1]*Calculations.sine(a[0])):.2f} \\text{{ m}} }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),


    #========================================================  SISTEMAS EQUIVALENTES  =========================================================
    #-------------------------------------------------       Sistemas equivalentes 2D-3D      --------------------------------------------
    #-------------------------------------------------       Nivel Díficil   ---------------------------------------------------
    #-------------------------------------------------       Code: 41300##    --------------------------------------------------
    Questionary(#1_1
        code = 4130011,
        no_pregunta = 1,
        complexity = D,
        topic = "Sistemas equivalentes",
        subtopic = "Sistemas equivalentes",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Teniendo como origen el punto F, reemplace el sistema de fuerzas y momentos mostrado en la imagen por una sola fuerza resultante ubicada a lo largo de la linea $F$-$C$. Considere $F_1 = {m[0]*(3/2):.2f} \\text{{ N}}$, $F_2 = {m[0]*2:.0f} \\text{{ N}}$, $F_3 = {m[1]:.0f} \\text{{ N}}$, $F_4 = {m[0]/2:.2f} \\text{{ N}}$, $M = {m[0]:.0f} \\text{{ N}} \\cdot \\text{{ m}}$,  $\\alpha_1 = {a[0]:.0f}°$, $d_1 = {d[0]*(3/4):.2f} \\text{{ m}}$ y $d_2 = {(d[0]):.0f} \\text{{ m}}$. ",
        no_answers = 3,
        a1_name = "Magnitud fuerza resultante $|F_R|$ [N]",
        a2_name = "Coordenada X [m]",
        a3_name = "Coordenada Y [m]",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude((m[0]/2)*calc['cos1'] - m[0]*2, m[1] + (m[0]/2)*calc['sin1']),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((m[1]*(3/2)*d[0] + 2*m[0]*d[0] - m[0]*(3/2)*d[0]*(3/4)*(d[0]/(Calculations.magnitude(d[0]*(3/4),d[0]))) - m[0])/(m[1] + (m[0]/2)*calc['sin1'] - (2/3)*((m[0]/2)*calc['cos1'] - m[0]*2)),2),
        answer3 = lambda f, a, calc, c, d, m: np.round((2/3)*(m[1]*(3/2)*d[0] + 2*m[0]*d[0] - m[0]*(3/2)*d[0]*(3/4)*(d[0]/(Calculations.magnitude(d[0]*(3/4),d[0]))) - m[0])/(m[1] + (m[0]/2)*calc['sin1'] - (2/3)*((m[0]/2)*calc['cos1'] - m[0]*2)), 2),
        ayuda1 = SE1,
        ayuda2 = SE2,      
        ayuda3 = SE3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        En un sistema equivalente, se busca simplificar un sistema complejo de fuerzas y momentos a un sistema más simple que genere el mismo efecto rotacional y traslacional. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Determinar fuerza resultante: }}$
        
        Es importante tener en cuenta que las fuerzas $F_1$ únicamente generan un momento par y no tienen ningún efecto traslacional.

        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} X:}}$  
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{Rx}}}}$          
        ${{\hspace{{4mm}} F_{{Rx}} = F_4 \\cdot \\cos(\\alpha_1) - F_2 = {(m[0]/2)*calc['cos1']:.2f} \\text{{ N}} - {m[0]*2:.2f} \\text{{ N}}}}$          
        ${{\hspace{{4mm}} F_{{Rx}} = {(m[0]/2)*calc['cos1'] - m[0]*2:.2f} \\text{{ N}} }}$          
        
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} Y:}}$  
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{Ry}}}}$          
        ${{\hspace{{4mm}} F_{{Ry}} = F_4 \\cdot \\sin(\\alpha_1) + F_3 = {(m[0]/2)*calc['sin1']:.2f} \\text{{ N}} + {m[1]:.0f} \\text{{ N}}}}$          
        ${{\hspace{{4mm}} F_{{Ry}} = {m[1] + (m[0]/2)*calc['sin1']:.2f} \\text{{ N}} }}$          
        
        Por lo tanto la fuerza resultante $|F_R| = {Calculations.magnitude((m[0]/2)*calc['cos1'] - m[0]*2, m[1] + (m[0]/2)*calc['sin1']):.2f} \\text{{ N}}$
        
        $\\textbf{{\\small 2. Ubicación de fuerza resultante: }}$
        
        Teniendo en cuenta que las coordenadas de la fuerza resultante están ubicadas sobre la linea F-C, se puede establecer una relación entre ambas utilizando triángulos semejantes:

        ${{\hspace{{4mm}} \\dfrac{{d_2}}{{2d_1}} = \\dfrac{{y}}{{x}}}}$     
        ${{\hspace{{4mm}} y = \\dfrac{{d_2}}{{2d_1}} \\cdot x }}$     
        ${{\hspace{{4mm}} y = {(2/3):.2f} \\cdot x }}$     
        
        Ahora, se puede determinar la coordenada x utilizando la condición de equivalencia de momentos en los sistemas. Haciendo producto cruz se obtiene:
        
        ${{\hspace{{4mm}} \\sum{{M_F}} = x \\cdot F_{{Ry}} - y \\cdot F_{{Rx}}}}$     
        ${{\hspace{{4mm}} x \\cdot F_{{Ry}} - y \\cdot F_{{Rx}} = F_3 \\cdot 2d_1 + F_2 \\cdot d_2 - F_1 \\cdot \\dfrac{{d_2}}{{\\sqrt{{(d_1)^{{2}} + (d_2)^{{2}}}}}} \\cdot d_1 - M}}$     
        ${{\hspace{{4mm}} x \\cdot {m[1] + (m[0]/2)*calc['sin1']:.2f} \\text{{ N}} - {(2/3):.2f} \\cdot x \\cdot ({(m[0]/2)*calc['cos1'] - m[0]*2:.2f}) \\text{{ N}} = {m[1]:.0f} \\text{{ N}} \\cdot {d[0]*(3/2):.2f} \\text{{ m}} + {m[0]*2:.0f} \\text{{ N}} \\cdot {d[0]:.0f} \\text{{ m}} - {m[0]*(3/2)*((d[0]*(3/4)*d[0])/Calculations.magnitude(d[0]*(3/2),d[0])):.2f} \\text{{ N}} \\cdot {d[0]*3/4:.2f} \\text{{ m}} - {m[0]:.0f} \\text{{ N}} \\cdot \\text{{ m}}}}$     
        ${{\hspace{{4mm}} x \\cdot ({m[1] + (m[0]/2)*calc['sin1'] - (2/3)*((m[0]/2)*calc['cos1'] - m[0]*2):.2f}) \\text{{ N}} = {m[1]*(3/2)*d[0] + 2*m[0]*d[0] - m[0]*(3/2)*d[0]*(3/4)*(d[0]/(Calculations.magnitude(d[0]*(3/4),d[0]))) - m[0]:.2f} \\text{{ N}} \\cdot \\text{{ m}}}}$     
        ${{\hspace{{4mm}} x = {(m[1]*(3/2)*d[0] + 2*m[0]*d[0] - m[0]*(3/2)*d[0]*(3/4)*(d[0]/(Calculations.magnitude(d[0]*(3/4),d[0]))) - m[0])/(m[1] + (m[0]/2)*calc['sin1'] - (2/3)*((m[0]/2)*calc['cos1'] - m[0]*2)):.2f} \\text{{ m}}}}$     
        
        Con la coordenada x es posible calcular la coordenada y a partir de la ecuación de triángulos semejantes:
        
        ${{\hspace{{4mm}} y = {2/3:.2f} \\cdot {(m[1]*(3/2)*d[0] + 2*m[0]*d[0] - m[0]*(3/2)*d[0]*(3/4)*(d[0]/(Calculations.magnitude(d[0]*(3/4),d[0]))) - m[0])/(m[1] + (m[0]/2)*calc['sin1'] - (2/3)*((m[0]/2)*calc['cos1'] - m[0]*2)):.2f} \\text{{ m}} }}$     
        ${{\hspace{{4mm}} y = {(2/3)*(m[1]*(3/2)*d[0] + 2*m[0]*d[0] - m[0]*(3/2)*d[0]*(3/4)*(d[0]/(Calculations.magnitude(d[0]*(3/4),d[0]))) - m[0])/(m[1] + (m[0]/2)*calc['sin1'] - (2/3)*((m[0]/2)*calc['cos1'] - m[0]*2)):.2f} \\text{{ m}} }}$     
        
       La solución presentada toma como referencia el punto F. Sin embargo, también se pudo realizar desde otro punto y ajustar la respuesta al sistema de coordenadas propuesto.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 4130021,
        no_pregunta = 2,
        complexity = D,
        topic = "Sistemas equivalentes",
        subtopic = "Sistemas equivalentes",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de $F_1$ y la coordenada en $X$ de la fuerza resultante que reemplaza el sistema mostrado, si se sabe que debe estar ubicada sobre el tramo $AB$. Considere $M = {32+m[0]*(1/10):.2f} \\text{{ kN}} \\cdot \\text{{ m}}$, $F_2 = {79+m[1]*(1/5):.2f} \\text{{ kN}}$, $F_3 = {24+m[0]*(3/40):.2f} \\text{{ kN}}$, $F_4 = {119+m[2]*(1/5):.2f} \\text{{ kN}}$, $d_1 = {(31+d[0])/4:.2f} \\text{{ m}}$,  $d_2 = {d[3]:.2f} \\text{{ m}}$, $d_3 = {6+d[6]*(1/5):.2f} \\text{{ m}}$, $d_4 = {(23+d[0])/4:.2f} \\text{{ m}}$, $d_5 = {(19+d[0])/4:.2f} \\text{{ m}}$, $\\alpha_1 = {72+d[9]*(2/5):.2f}°$ y $\\alpha_2 = {60+d[9]*(2/5):.2f}°$, el cual relaciona el eje $z$ con el plano $xy$.",
        no_answers = 2,
        a1_name = "$F_1$ $[kN]$",
        a2_name = "Coordenada en $X$ $[m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((24+m[0]*(3/40))*((119+m[2]*(1/5))*Calculations.cosine(60+d[9]*(2/5))*((21+d[0])/2) + (79+m[1]*(1/5))*(6+d[6]*(1/5))))/(Calculations.cosine(72+d[9]*(2/5))*((119+m[2]*(1/5))*Calculations.cosine(60+d[9]*(2/5))*((21+d[0])/2) + (79+m[1]*(1/5))*(6+d[6]*(1/5))) + ((32+m[0]*(1/10))-(24+m[0]*(3/40))*((31+d[0])/4))*Calculations.sine(72+d[9]*(2/5))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((Calculations.cosine(72+d[9]*(2/5))*((119+m[2]*(1/5))*Calculations.cosine(60+d[9]*(2/5))*((21+d[0])/2) + (79+m[1]*(1/5))*(6+d[6]*(1/5))) + ((32+m[0]*(1/10))-(24+m[0]*(3/40))*((31+d[0])/4))*Calculations.sine(72+d[9]*(2/5)))/((24+m[0]*(3/40))*Calculations.sine(72+d[9]*(2/5)))) + (31+d[0])/4,2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = SE1,
        ayuda2 = SE2,      
        ayuda3 = SE3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        En un sistema equivalente se esta buscando reducir un sistema complejo a un sistema de fuerzas y momentos que producen mismo efecto rotacional y traslacional. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Determinar fuerza resultante: }}$
        
        Se debe tener presente que las fuerzas $F_4$ generan un momento par y no tienen un efecto traslacional en el sistema:
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{Rx}}}}$          
        ${{\hspace{{4mm}} F_{{Rx}} = F_2 }}$          
                
        ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{Ry}}}}$          
        ${{\hspace{{4mm}} F_{{Ry}} = F_1 \\cdot \\cos(\\alpha_1) - F_3 }}$          
                
        ${{\hspace{{4mm}} \\sum{{F_z}} = F_{{Rz}}}}$          
        ${{\hspace{{4mm}} F_{{Rz}} = - F_1 \\cdot \\sin(\\alpha_1)}}$  

        ${{\hspace{{4mm}} F_{{R}} = ({79+m[1]*(1/5):.2f}) \\text{{ }} \\hat{{ i}} + (F_1 \\cdot \\cos({72+d[9]*(2/5):.2f}°) - {24+m[0]*(3/40):.2f}) \\text{{ }} \\hat{{ j}} + (-F_1 \\cdot \\sin({72+d[9]*(2/5):.2f}°) \\text{{ }} \\hat{{ k}} }}$     
                     
        
        $\\textbf{{\\small 2. Condición de momento: }}$
        
        Inicialmente, se calcula el momento en el punto $A$ que producen las fuerzas en el sistema original: 
        
        $\\underline{{Fuerza \\hspace{{2mm}} 1:}}$  

        ${{\hspace{{4mm}} M_1 = d_1 \\cdot F_1 \\sin(\\alpha_1) \\hat{{j}} + d_1 \\cdot F_1 \\cos(\\alpha_1) \\hat{{k}} }}$ 

        $\\underline{{Fuerza \\hspace{{2mm}} 2:}}$  

        ${{\hspace{{4mm}} M_2 = d_3 \\cdot F_2 \\hat{{j}} }}$   

        $\\underline{{Fuerza \\hspace{{2mm}} 3:}}$     

        La fuerza $F_3$ no ejerce momento en el punto A

        $\\underline{{Fuerza \\hspace{{2mm}} 4:}}$   

        ${{\hspace{{4mm}} M_{{par}} = F_4 \\cdot (d_4 + d_5) \\cdot \\cos(\\alpha_2) \\hat{{j}} }}$    
   
        
        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 \\hat{{i}} + ( d_1 \\cdot F_1 \\sin(\\alpha_1) + d_3 \\cdot F_2 + F_4 \\cdot (d_4 + d_5) \\cdot \\cos(\\alpha_2)) \\hat{{j}} + (d_1 \\cdot F_1 \\cos(\\alpha_1) - M) \\hat{{k}} }}$      


        Luego, se iguala el momento hallado en el punto $A$ con el momento que sería efectuado por la resultante ubicada a una distancia $x$ del punto $A$, el cual es:
        
        ${{\hspace{{4mm}} M_{{F_R}} = 0 \\hat{{i}} - x \\cdot F_{{Rz}} \\hat{{j}} + x \\cdot F_{{Ry}} \\hat{{k}} }}$     
        
        $\\underline{{Condición \\hspace{{2mm}} de \\hspace{{2mm}} momento - Componente \\hspace{{2mm}} \\hat{{j}}:}}$  
        
        ${{\hspace{{4mm}} x \\cdot F_1 \\cdot \\sin(\\alpha_1) = M_{{par}} + M_2 + d_1 \\cdot F_1 \\sin(\\alpha_1)}}$     
       
        ${{\hspace{{4mm}} x = \\dfrac{{M_{{par}} + M_2}}{{F_1 \\cdot \\sin(\\alpha_1)}} + d_1 }}$     
        
        $\\underline{{Condición \\hspace{{2mm}} de \\hspace{{2mm}} momento - Componente \\hspace{{2mm}} \\hat{{k}}:}}$  
        
        ${{\hspace{{4mm}} x \\cdot (F_1 \\cdot \\cos(\\alpha_1) - F_3) = d_1 \\cdot F_1 \\cos(\\alpha_1) - M}}$     
       
        ${{\hspace{{4mm}} (\\dfrac{{M_{{par}} + M_2}}{{F_1 \\cdot \\sin(\\alpha_1)}} + d_1) \\cdot F_1 \\cdot \\cos(\\alpha_1) - F_3 \\cdot (\\dfrac{{M_{{par}} + M_2}}{{F_1 \\cdot \\sin(\\alpha_1)}} + d_1 ) = d_1 \\cdot F_1 \\cos(\\alpha_1) - M}}$     
        
        ${{\hspace{{4mm}} \\dfrac{{M_{{par}} + M_2}}{{F_1 \\cdot \\sin(\\alpha_1)}} \\cdot F_1 \\cdot \\cos(\\alpha_1) + d_1 \\cdot F_1 \\cdot \\cos(\\alpha_1) - F_3 \\cdot (\\dfrac{{M_{{par}} + M_2}}{{F_1 \\cdot \\sin(\\alpha_1)}} + d_1 ) = d_1 \\cdot F_1 \\cos(\\alpha_1) - M}}$     
        
        ${{\hspace{{4mm}} \\dfrac{{\\cos(\\alpha_1) }}{{\\sin(\\alpha_1)}} \\cdot (M_{{par}} + M_2) - F_3 \\cdot d_1 + M = F_3 \\cdot \\dfrac{{M_{{par}} + M_2}}{{F_1 \\cdot \\sin(\\alpha_1)}}}}$     
        
        ${{\hspace{{4mm}} F_1 = F_3 \\cdot \\dfrac{{M_{{par}} + M_2}}{{(\\cos(\\alpha_1) \\cdot (M_{{par}} + M_2) + (M - F_3 \\cdot d_1) \\cdot \\sin(\\alpha_1)}}}}$     
        
        ${{\hspace{{4mm}} F_1 = {((24+m[0]*(3/40))*((119+m[2]*(1/5))*Calculations.cosine(60+d[9]*(2/5))*((21+d[0])/2) + (79+m[1]*(1/5))*(6+d[6]*(1/5))))/(Calculations.cosine(72+d[9]*(2/5))*((119+m[2]*(1/5))*Calculations.cosine(60+d[9]*(2/5))*((21+d[0])/2) + (79+m[1]*(1/5))*(6+d[6]*(1/5))) + ((32+m[0]*(1/10))-(24+m[0]*(3/40))*((31+d[0])/4))*Calculations.sine(72+d[9]*(2/5))):.2f} \\text{{ kN}}}}$     
        
        Finalmente, se halla $x$:
        
        ${{\hspace{{4mm}} x = \\dfrac{{M_{{par}} + M_2}}{{F_1 \\cdot \\sin(\\alpha_1)}} + d_1 }}$     
        
        ${{\hspace{{4mm}} x = {((Calculations.cosine(72+d[9]*(2/5))*((119+m[2]*(1/5))*Calculations.cosine(60+d[9]*(2/5))*((21+d[0])/2) + (79+m[1]*(1/5))*(6+d[6]*(1/5))) + ((32+m[0]*(1/10))-(24+m[0]*(3/40))*((31+d[0])/4))*Calculations.sine(72+d[9]*(2/5)))/((24+m[0]*(3/40))*Calculations.sine(72+d[9]*(2/5)))) + (31+d[0])/4:.2f} \\text{{ m}}}}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
   

    #========================================================  ARMADURAS  =========================================================
    #-------------------------------------------------         Cerchas      --------------------------------------------
    #-------------------------------------------------       Nivel Fácil   ---------------------------------------------------
    #-------------------------------------------------       Code: 5110011    --------------------------------------------------

    Questionary(#1_1
        code = 5110011,
        no_pregunta = 1,
        complexity = F,
        topic = "Armaduras",
        subtopic = "Cerchas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las reacciones en los apoyos A y D (Indique el signo de la dirección de las fuerzas). Considere $F_1 = {f[0]:.0f} \\text{{ kN}}$, $F_2 = {f[1]:.0f} \\text{{ kN}}$,  $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Reacción $A_x$ [kN]",
        a2_name = "Reacción $A_y$ [kN]",
        a3_name = "Reacción $D_y$ [kN]",
        answer1 = lambda f, a, calc, c, d, m: np.round(0,2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0] + f[1] - ((f[0]*d[0]+f[1]*(d[0] + d[3]))/(2*d[0] + d[3])),2),
        answer3 = lambda f, a, calc, c, d, m: np.round((f[0]*d[0]+f[1]*(d[0] + d[3]))/(2*d[0] + d[3]) , 2),
        ayuda1 = C1,
        ayuda2 = C2,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Las reacciones se pueden describir como la respuestas o las restricciones que generan los apoyos o soportes para evitar que una estructura sea sometida a traslación y/o rotación. A continuación, se presenta la solución sugerida para el ejercicio:
        
        En el problema, se identifican dos apoyos, de los cuales se deduce el número de restricciones a encontrar: el A, de segundo grado (dos restricciones); y el D, de primer grado (una restricción). 
        
        $\\textbf{{\\small 1. Condición de equilibrio - Sumatoria de fuerzas en X: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_x}} = A_x = 0}}$    
        
        $\\textbf{{\\small 2. Condición de equilibrio - Momento en A: }}$
        
        Para encontrar una de las reacciones restantes, se utiliza la condición de equilibrio que establece que la suma de momentos en cualquier punto debe ser igual a cero. Se selecciona un punto donde actúe una de las reacciones para tener una incógnita por resolver (Distinto al caso si evaluaramos Sumatoria de fuerzas en Y, donde habría más de una incógnita). 
        
        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{M_A}} = - F_1 \\cdot d_1 - F_2 \\cdot (d_1 + d_2) + D_y \\cdot (2 \\cdot d_1 + d_2) = 0}}$     
         ${{\hspace{{4mm}} \\sum{{M_A}} = - {f[0]:.0f} \\text{{ kN}} \\cdot {d[0]:.0f} \\text{{ m}} - {f[1]:.0f} \\text{{ kN}} \\cdot {d[0] + d[3]:.0f} \\text{{ m}} + D_y \\cdot {2*d[0] + d[3]:.0f} \\text{{ m}} = 0}}$     
        ${{\hspace{{4mm}} D_y \\cdot {2*d[0] + d[3]:.0f} \\text{{ m}} = {f[0]*d[0]:.0f} \\text{{ kN}} \\cdot \\text{{ m}} + {f[1]*(d[0] + d[3]):.0f} \\text{{ kN}} \\cdot \\text{{ m}}}}$     
        ${{\hspace{{4mm}} D_y = \\dfrac{{ {f[0]*d[0]+f[1]*(d[0] + d[3]):.0f} \\text{{ kN}} \\cdot \\text{{ m}} }}{{ {2*d[0] + d[3]:.0f} \\text{{ m}} }} }}$      
        ${{\hspace{{4mm}} D_y = {(f[0]*d[0]+f[1]*(d[0] + d[3]))/(2*d[0] + d[3]):.2f} \\text{{ kN}} }}$     
        
        $\\textbf{{\\small 3. Condición de equilibrio - Sumatoria de fuerzas en Y: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + D_y - F_1 - F_2 = 0}}$     
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y +  {(f[0]*d[0]+f[1]*(d[0] + d[3]))/(2*d[0] + d[3]):.0f} \\text{{ kN}} - {f[0]:.0f} \\text{{ kN}}  - {f[1]:.0f} \\text{{ kN}} = 0}}$      
        ${{\hspace{{4mm}} A_y = {f[0]:.0f} \\text{{ kN}}  + {f[1]:.0f} \\text{{ kN}} - {(f[0]*d[0]+f[1]*(d[0] + d[3]))/(2*d[0] + d[3]):.0f} \\text{{ kN}} }}$     
        ${{\hspace{{4mm}} A_y = {f[0] + f[1] - ((f[0]*d[0]+f[1]*(d[0] + d[3]))/(2*d[0] + d[3])) :.2f} \\text{{ kN}} }}$   
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 5110021,
        no_pregunta = 2,
        complexity = F,
        topic = "Armaduras",
        subtopic = "Cerchas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las fuerzas internas de los miembros AC, AD y BC (Use el signo negativo si el elemento está en compresión y el signo positivo si el elemento esta en tensión). Considere $F_1 = {f[0]:.0f} \\text{{ kN}}$, $d_1 = {d[0]:.0f} \\text{{ m}}$, $\\alpha_1 = {(a[2]/7):.2f}°$ y $\\alpha_2 = {(a[1]/4):.2f}°$.",
        no_answers = 3,
        a1_name = "Fuerza en AC $[kN]$",
        a2_name = "Fuerza en AD $[kN]$",
        a3_name = "Fuerza en BC $[kN]$",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.sine((a[2]/7))))- (f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7)))))*((Calculations.cosine((a[1]/4)))/(Calculations.sine((a[2]/7)))),2),
        answer3 = lambda f, a, calc, c, d, m: np.round((-f[0] + (Calculations.sine((a[1]/4)))*(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))))/(Calculations.sine((a[1]/4))), 2),
        ayuda1 = C3,
        ayuda2 = C6,    
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre sí por puntos llamados nodos, formando triángulos. El método de los nodos es una técnica usada para determinar las fuerzas internas en una cercha, basándose en el principio de que cada nodo está en equilibrio. A continuación, se presenta la solución sugerida para el ejercicio: 
        
        $\\textbf{{\\small 1. Cálculo de las reacciones en los apoyos: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$               
        ${{\hspace{{4mm}} \\sum{{F_x}} = A_x + F_1= 0}}$     
        ${{\hspace{{4mm}} A_x = {-f[0]:.0f} \\text{{ kN}} }}$         
              
        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{M_A}} = - F_1 \\cdot \\left(\\dfrac{{d_1}}{{tan(\\alpha_2)}}\\right) + B_y \\cdot (2 \\cdot d_1 ) = - {f[0]:.0f} \\text{{ kN}} \\cdot {(d[0])/(Calculations.tangent((a[1]/4))):.0f} \\text{{ m}} + B_y \\cdot {2*d[0]:.0f} \\text{{ m}} = 0}}$     
        ${{\hspace{{4mm}} B_y \\cdot {2*d[0]:.0f} \\text{{ m}} = {f[0]*((d[0])/(Calculations.tangent((a[1]/4)))):.0f} \\text{{ kN}} \\cdot \\text{{ m}} }}$         
        ${{\hspace{{4mm}} B_y = {(f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]):.2f} \\text{{ kN}} }}$     
             
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + B_y = A_y +  {(f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]):.2f} \\text{{ kN}} = 0}}$     
        ${{\hspace{{4mm}} A_y = {-((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0])) :.2f} \\text{{ kN}} }}$
        
        $\\textbf{{\\small 2. Nodo A: }}$

        En el nodo A se pueden determinar las fuerzas internas $F_{{AD}}$ y $F_{{AC}}$. Para ello, se define un sistema de ecuaciones utilizando la sumatoria de fuerzas en los ejes estándar. Alternativamente, se puede cambiar el sistema de referencia, alineando uno de los nuevos ejes de forma que sea perpendicular a una de las fuerzas desconocidas.
    
        A continuación, se presenta la solución utilizando el primer método, en el cual se resolverá el sistema de ecuaciones mediante sustitución:

        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{AD}} \\cdot \\cos(\\alpha_1) + F{{AC}} \\cdot \\sin(\\alpha_2) - |A_x| = F_{{AD}} \\cdot {Calculations.cosine((a[2]/7)):.2f} + F_{{AC}} \\cdot {Calculations.sine((a[1]/4)):.2f} - {f[0]:.0f} \\text{{ kN}}  = 0 }}$     
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = F_{{AD}} \\cdot \\sin(\\alpha_1) + F{{AC}} \\cdot \\cos(\\alpha_2) - |A_y| = F_{{AD}} \\cdot {Calculations.sine((a[2]/7)):.2f} + F_{{AC}} \\cdot {Calculations.cosine((a[1]/4)):.2f} - {((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0])) :.2f} \\text{{ kN}} = 0 }}$      
        
        De la ecuación 2, se despeja $F_{{AD}}$ en términos de $F_{{AC}}$:
        
        ${{\hspace{{4mm}} F_{{AD}} \\cdot {Calculations.sine((a[2]/7)):.2f} + F_{{AC}} \\cdot {Calculations.cosine((a[1]/4)):.2f} - {((f[0]*d[3])/(2*d[0])) :.2f} \\text{{ kN}} = 0 }}$      
        ${{\hspace{{4mm}} F_{{AD}} = {((f[0]*d[3])/(2*d[0]*Calculations.sine((a[2]/7)))):.2f} \\text{{ kN}} - F_{{AC}} \\cdot {(Calculations.cosine((a[1]/4)))/(Calculations.sine((a[2]/7))):.2f} }}$ 
        
        Se reemplaza en la ecuación 1:     
              
        ${{\hspace{{4mm}} F_{{AD}} \\cdot {Calculations.cosine((a[2]/7)):.2f} + F_{{AC}} \\cdot {Calculations.sine((a[1]/4)):.2f} - {f[0]:.0f} \\text{{ kN}} = 0 }}$      
        ${{\hspace{{4mm}} ({((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))) :.2f} \\text{{ kN}} - F_{{AC}} \\cdot {(Calculations.cosine((a[1]/4)))/(Calculations.sine((a[2]/7))):.2f} ) \\cdot {Calculations.cosine((a[2]/7)):.2f} + F_{{AC}} \\cdot {Calculations.sine((a[1]/4)):.2f} = {f[0]:.0f} \\text{{ kN}}}}$       
        ${{\hspace{{4mm}} F_{{AC}} \\cdot ({Calculations.sine((a[1]/4)) - (Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))):.2f}) = {f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))):.2f} \\text{{ kN}}}}$      
        ${{\hspace{{4mm}} F_{{AC}} = {(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))):.2f} \\text{{ kN}} }}$       
              
        Se calcula $F_{{AD}}$:
        
        ${{\hspace{{4mm}} F_{{AD}} = {((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.sine((a[2]/7)))):.2f} \\text{{ kN}} - F_{{AC}} \\cdot {(Calculations.cosine((a[1]/4)))/(Calculations.sine((a[2]/7))):.2f}}}$      
        ${{\hspace{{4mm}} F_{{AD}} = {((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.sine((a[2]/7)))):.2f} \\text{{ kN}} - {(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7)))))*(Calculations.cosine((a[1]/4)))/(Calculations.sine((a[2]/7))):.2f} \\text{{ kN}} }}$     
        ${{\hspace{{4mm}} F_{{AD}} = {((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.sine((a[2]/7))))- (f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7)))))*(Calculations.cosine((a[1]/4)))/(Calculations.sine((a[2]/7))):.2f} \\text{{ kN}} }}$     
        
        $\\textbf{{\\small 3. Nodo C: }}$

        Para el nodo C, se obtienen las siguientes ecuaciones:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{CB}} \\cdot \\sin(\\alpha_2) + ({-(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))):.2f} \\text{{ kN}} ) \\cdot \\sin(\\alpha_2) + F_1 = F_{{CB}} \\cdot {Calculations.sine((a[1]/4)):.2f} + ( {-(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))):.2f} \\text{{ kN}} ) \\cdot {Calculations.sine((a[1]/4)):.2f} + {f[0]:.0f} \\text{{ kN}} = 0 }}$      
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = F_{{CB}} \\cdot \\cos(\\alpha_2) + ({-(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))):.2f} \\text{{ kN}} ) \\cdot \\cos(\\alpha_2) + F_{{CD}} = F_{{CB}} \\cdot {Calculations.cosine((a[1]/4)):.2f} + ( {-(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))):.2f} \\text{{ kN}} ) \\cdot {Calculations.cosine((a[1]/4)):.2f} + F_{{CD}} = 0 }}$      
        
        Dada la pregunta del ejercicio, solo se necesita despejar F_{{CB}} de la primera ecuación:
        
        ${{\hspace{{4mm}} F_{{CB}} \\cdot {Calculations.sine((a[1]/4)):.2f} + ( {-(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))):.2f} \\text{{ kN}} ) \\cdot {Calculations.sine((a[1]/4)):.2f} + {f[0]:.0f} \\text{{ kN}} = 0 }}$      
        ${{\hspace{{4mm}} F_{{CB}} \\cdot {Calculations.sine((a[1]/4)):.2f} = {-f[0] + (Calculations.sine((a[1]/4)))*(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))):.2f} \\text{{ kN}}}}$      
        ${{\hspace{{4mm}} F_{{CB}} = {(-f[0] + (Calculations.sine((a[1]/4)))*(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))))/(Calculations.sine((a[1]/4))):.2f} \\text{{ kN}}}}$      
        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    Questionary(#3_1
        code = 5110031,
        no_pregunta = 3,
        complexity = F,
        topic = "Armaduras",
        subtopic = "Cerchas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las fuerzas internas de los miembros $AC$ y $AD$ (Use el signo negativo si el elemento está en compresión y el signo positivo si el elemento esta en tensión). Considere $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$, $d_0 = {d[0]:.0f} \\text{{ m}}$ y $d_1 = {d[3]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Fuerza en $AC$ $[N]$",
        a2_name = "Fuerza en $AD$ $[N]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[1]-((d[3]*f[0]+(5/2)*d[0]*f[1])/(3*d[0])))*(Calculations.magnitude(d[3],d[0]/2)/d[3]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]-((f[1]-((d[3]*f[0]+(5/2)*d[0]*f[1])/(3*d[0])))*(Calculations.magnitude(d[3],d[0]/2)/d[3]))*(Calculations.cosine(Calculations.arctangent(d[3]/(0.5*d[0])))),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = C2,
        ayuda2 = C3,      
        ayuda3 = C6,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre sí por puntos llamados nodos, formando triángulos. El método de los nodos es una técnica usada para determinar las fuerzas internas en una cercha, basándose en el principio de que cada nodo está en equilibrio. A continuación, se presenta la solución sugerida para el ejercicio: 
        
        $\\textbf{{\\small 1. Cálculo de las reacciones en los apoyos: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$        
        ${{\hspace{{4mm}} \\sum{{F_x}} = {f[0]} - A_x = 0}}$      
        ${{\hspace{{4mm}} A_x = {f[0]} \\text{{ N}} }}$ 

        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{M_A}} = -{d[3]}*{f[0]}-\\dfrac{5}{2}*{d[0]}*{f[1]}+3*{d[0]}*B_y = 0 }}$         
        ${{\hspace{{4mm}} B_y = {(d[3]*f[0]+(5/2)*d[0]*f[1])/(3*d[0]):.2f} \\text{{ N}} }}$       

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$       
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + B_y - {f[1]} = 0}}$       
        ${{\hspace{{4mm}} A_y + B_y = {f[1]}}}$        
        ${{\hspace{{4mm}} A_y = {f[1]} - B_y}}$           
        ${{\hspace{{4mm}} A_y = {f[1]-(d[3]*f[0]+(5/2)*d[0]*f[1])/(3*d[0]):.2f} \\text{{ N}} }}$  

        $\\textbf{{\\small 2. Nodo A: }}$

        En el nodo $A$ se pueden determinar las fuerzas internas $F_{{AD}}$ y $F_{{AC}}$, se suponen las dos fuerzas a tensión para realizar el equilibrio.

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$       
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + F_{{AC}} \\cdot Sen({Calculations.arctangent(d[3]/(0.5*d[0])):.2f}°) = 0 }}$      
        ${{\hspace{{4mm}} F_{{AC}} = \\dfrac{{-A_y}}{{Sen({Calculations.arctangent(d[3]/(0.5*d[0])):.2f}°)}} }}$              
        ${{\hspace{{4mm}} F_{{AC}} = {(f[1]-((d[3]*f[0]+(5/2)*d[0]*f[1])/(3*d[0])))*(Calculations.magnitude(d[3],d[0]/2)/d[3]):.2f} \\text{{ N}}}}$        

        {'El elemento $AC$ está a Tensión.' if ((f[1]-((d[3]*f[0]+(5/2)*d[0]*f[1])/(3*d[0])))*(Calculations.magnitude(d[3],d[0]/2)/d[3])) > 0 else 'El elemento $AC$ está a Compresión.'} 

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{F_x}} = -A_x + F_{{AD}} + F_{{AC}} \\cdot Cos({Calculations.arctangent(d[3]/(0.5*d[0])):.2f}°)= 0 }}$   
        ${{\hspace{{4mm}} F_{{AD}} = A_x - F_{{AC}} \\cdot Cos({Calculations.arctangent(d[3]/(0.5*d[0])):.2f}°)= 0 }}$     
        ${{\hspace{{4mm}} F_{{AD}} = {f[0]-((f[1]-((d[3]*f[0]+(5/2)*d[0]*f[1])/(3*d[0])))*(Calculations.magnitude(d[3],d[0]/2)/d[3]))*(Calculations.cosine(Calculations.arctangent(d[3]/(0.5*d[0])))):.2f} \\text{{ N}} }}$        
       
        {'El elemento $AD$ está a Tensión.' if (f[0]-((f[1]-((d[3]*f[0]+(5/2)*d[0]*f[1])/(3*d[0])))*(Calculations.magnitude(d[3],d[0]/2)/d[3]))*(Calculations.cosine(Calculations.arctangent(d[3]/(0.5*d[0]))))) > 0 else 'El elemento $AD$ está a Compresión.'} 
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
    ),

    Questionary(#4_1
        code = 5110041,
        no_pregunta = 4,
        complexity = F,
        topic = "Armaduras",
        subtopic = "Cerchas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"La fuerza $F = {f[0]:.0f} \\text{{ kN}}$ es aplicada en la zona inferior del puente, encuentre la fuerza interna del elemento $HJ$ (Use el signo negativo si el elemento está en compresión y el signo positivo si el elemento esta en tensión). Considere que las distancias $d_0 = {d[0]:.0f} \\text{{ m}}$ y $d_1 = {d[3]:.0f} \\text{{ m}}$",
        no_answers = 1,
        a1_name = "Fuerza en $HJ$ $[kN]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(-(f[0]/2)/Calculations.sine(Calculations.arctangent(d[0]/d[3])),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = C2,
        ayuda2 = C7,      
        ayuda3 = C8,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre sí por puntos llamados nodos, formando triángulos. El método de los nodos es una técnica usada para determinar las fuerzas internas en una cercha, basándose en el principio de que cada nodo está en equilibrio. A continuación, se presenta la solución sugerida para el ejercicio: 
        
        $\\textbf{{\\small 1. Cálculo de las reacciones en los apoyos: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$            
        ${{\hspace{{4mm}} A_x = 0 \\text{{ kN}}}}$        

        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$              
        ${{\hspace{{4mm}} \\sum{{M_A}} = L_y \\cdot 6 \\dot d_1 - F \\cdot 3 \\dot d_1 = 0}}$          
        ${{\hspace{{4mm}} L_y = \\dfrac{{F}}{{2}} }}$               
        ${{\hspace{{4mm}} L_y = {f[0]/2:.2f} \\text{{ kN}} }}$

       Teniendo en cuenta que la cercha es simétrica en geometría y carga, las reacciones verticales de los apoyos son iguales: $A_y = L_y = {f[0]/2:.2f} \\text{{ kN}}$

       
        $\\textbf{{\\small 2. Cálculo de la fuerza interna del elemento HJ: }}$

        Al analizar el nodo $K$, se determina que el elemento $KJ$ es un elemento de fuerza cero. Luego, al analizar el nodo $J$, se concluye que el elemento $JI$ también es de fuerza cero, y que el elemento $HJ$ tiene una fuerza igual a la del elemento $LJ$. Por lo tanto, al encontrar la fuerza $LJ$ con el análisis del nodo $L$ se encuentra la fuerza $HJ$ también.
        
        $\\underline{{Nodo \\hspace{{2mm}} L:}}$

        Se suponen las fuerzas a tensión.
 
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$        
        ${{\hspace{{4mm}} \\sum{{F_y}} = L_y + F_{{LJ}} \\cdot Sen({Calculations.arctangent(d[0]/d[3]):.2f}°) = 0 }}$               
        ${{\hspace{{4mm}} F_{{LJ}} = \\dfrac{{-L_y}}{{Sen({Calculations.arctangent(d[0]/d[3]):.2f}°)}} }}$                      
        ${{\hspace{{4mm}} F_{{LJ}} = {-(f[0]/2)/Calculations.sine(Calculations.arctangent(d[0]/d[3])):.2f} \\text{{ kN}}}}$                

        {'El elemento $LJ$ está a Tensión.' if (-(f[0]/2)/Calculations.sine(Calculations.arctangent(d[0]/d[3]))) > 0 else 'El elemento $LJ$ está a Compresión.'} 

        De acuerdo, con el análisis en el nodo $J$ mencionado anteriormente, la fuerza del elemento $LJ$ es igual a la del elemento $HJ$. Por lo tanto:

        ${{\hspace{{4mm}} F_{{LJ}} = F_{{HJ}} = {-(f[0]/2)/Calculations.sine(Calculations.arctangent(d[0]/d[3])):.2f} \\text{{ kN}}}}$      

        {'El elemento $HJ$ está a Tensión.' if (-(f[0]/2)/Calculations.sine(Calculations.arctangent(d[0]/d[3]))) > 0 else 'El elemento $HJ$ está a Compresión.'} 
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
   


    #========================================================  ARMADURAS  =========================================================
    #-------------------------------------------------         Cerchas      --------------------------------------------
    #-------------------------------------------------       Nivel Medio   ---------------------------------------------------
    #-------------------------------------------------       Code: 5120011    --------------------------------------------------

    Questionary(#1_1
        code = 5120011,
        no_pregunta = 1,
        complexity = M,
        topic = "Armaduras",
        subtopic = "Cerchas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"La armadura que se presenta soporta el panel de un anuncio. Determine las reacciones en los apoyos A y F (Indique el signo de la dirección de las fuerzas). Considere $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$,  $F_3 = {f[2]:.0f} \\text{{ N}}$, $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$, $d_3 = {d[6]:.0f} \\text{{ m}}$ y $d_4 = {d[9]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Reacción $F_x$ [N]",
        a2_name = "Reacción $F_y$ [N]",
        a3_name = "Reacción $A_y$ [N]",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0] + f[1],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[2] - (f[2]*d[3] + f[1]*d[6] + f[0]*(d[6] + d[9]))/(d[0] + d[3]),2),
        answer3 = lambda f, a, calc, c, d, m: np.round((f[2]*d[3] + f[1]*d[6] + f[0]*(d[6] + d[9]))/(d[0] + d[3]), 2),
        ayuda1 = C1,
        ayuda2 = C2,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Las reacciones se pueden describir como la respuestas o las restricciones que generan los apoyos o soportes para evitar que una estructura sea sometida a traslación y/o rotación. A continuación, se presenta la solución sugerida para el ejercicio:
        
        En el problema, se identifican dos apoyos, de los cuales se deduce el número de restricciones a encontrar: el F, de segundo grado (dos restricciones); y el A, de primer grado (una restricción). 
                
        $\\textbf{{\\small 1. Condición de equilibrio - Sumatoria de fuerzas en X: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_x - F_1 - F_2 = 0 }}$          
        ${{\hspace{{4mm}} F_x = {f[0] + f[1]:.2f} \\text{{ N}} }}$    
        
        $\\textbf{{\\small 2. Condición de equilibrio - Momento en F: }}$

        Para encontrar una de las reacciones restantes, se utiliza la condición de equilibrio que establece que la suma de momentos en cualquier punto debe ser igual a cero. Se selecciona un punto donde actúe una de las reacciones para tener una incógnita por resolver (Distinto al caso si evaluaramos Sumatoria de fuerzas en Y, donde habría más de una incógnita). 
        
        ${{\hspace{{4mm}} \\sum{{M_F}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{M_F}} = F_3 \\cdot d_2 + F_2 \\cdot d_2 + F_1 \\cdot (d_3 + d_4) - A_y \\cdot (d_1 + d_2) = {f[2]:.0f} \\text{{ N}} \\cdot {d[3]:.0f} \\text{{ m}} + {f[1]:.0f} \\text{{ N}} \\cdot {d[6]:.0f} \\text{{ m}} + {f[0]:.0f} \\text{{ N}} \\cdot {d[6] + d[9]:.0f} \\text{{ m}} - A_y \\cdot {d[0] + d[3]:.0f} \\text{{ m}} = 0}}$     
        ${{\hspace{{4mm}} A_y \\cdot {d[0] + d[3]:.0f} \\text{{ m}} = {f[2]*d[3]:.0f} \\text{{ N}} \\cdot \\text{{ m}} + {f[1]*d[6]:.0f} \\text{{ N}} \\cdot \\text{{ m}} + {f[0]*(d[6] + d[9]) :.0f} \\text{{ N}} \\cdot \\text{{ m}}  }}$      
        ${{\hspace{{4mm}} A_y = {(f[2]*d[3] + f[1]*d[6] + f[0]*(d[6] + d[9]))/(d[0] + d[3]):.2f} \\text{{ N}} }}$     
        
        $\\textbf{{\\small 3. Condición de equilibrio - Sumatoria de fuerzas en Y: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + F_y - F_3 = F_y + {(f[2]*d[3] + f[1]*d[6] + f[0]*(d[6] + d[9]))/(d[0] + d[3]):.2f} \\text{{ N}} - {f[2]:.0f} \\text{{ N}} = 0}}$        
        ${{\hspace{{4mm}} F_y = {f[2] - (f[2]*d[3] + f[1]*d[6] + f[0]*(d[6] + d[9]))/(d[0] + d[3]) :.2f} \\text{{ N}} }}$
        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 5120021,
        no_pregunta = 2,
        complexity = M,
        topic = "Armaduras",
        subtopic = "Cerchas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las fuerzas internas de los miembros AB, FD y CE de la armadura Gambrel presentada (Use el signo negativo si el elemento está en compresión y el signo positivo si el elemento esta en tensión). Considere $F_1 = {f[0]:.0f} \\text{{ kN}}$, $F_2 = {f[1]:.0f} \\text{{ kN}}$, $F_3 = {f[2]:.0f} \\text{{ kN}}$, $d_1 = {d[0]:.0f} \\text{{ m}}$, $d_2 = {d[3]:.0f}  \\text{{ m}}$,  $d_3 = {d[6]:.0f} \\text{{ m}}$ y $d_4 = {d[9]:.0f}  \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Fuerza en AB $[kN]$",
        a2_name = "Fuerza en DF $[kN]$",
        a3_name = "Fuerza en CE $[kN]$",
        answer1 = lambda f, a, calc, c, d, m: np.round(-((f[1] + (f[0]/2))/((d[6])/(Calculations.magnitude(d[0],d[6])))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-((f[0]/2) + ((f[1] + (f[0]/2))*(d[0]/d[3])))/(((d[9] + d[6])/(Calculations.magnitude(d[3],d[9])))),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(((f[1] + (f[0]/2))/(d[6]))*(d[0]), 2),
        ayuda1 = "La armadura Gambrel se caracteriza por ser una estructura simétrica. ¿Qué nos dice esto sobre las reacciones y las fuerzas de cada elemento?",
        ayuda2 = C3,      
        ayuda3 = C6,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre sí por puntos llamados nodos, formando triángulos. El método de los nodos es una técnica usada para determinar las fuerzas internas en una cercha, basándose en el principio de que cada nodo está en equilibrio. A continuación, se presenta la solución sugerida para el ejercicio: 

        $\\textbf{{\\small 1. Cálculo de las reacciones en los apoyos: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$               
        ${{\hspace{{4mm}} \\sum{{F_x}} = H_x = 0}}$             
              
        Dado que la cercha es simétrica, se sabe que $H_y$ = $A_y$. Tal que, se puede obtener el siguiente resultado de la sumatoria de fuerzas en Y: 
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + H_y - (2F_3 + 2F_2 + F_1) = 2A_y - {2*f[2] + 2*f[1] + f[0]:.0f} \\text{{ kN}} = 0}}$     
        ${{\hspace{{4mm}} H_y = A_y = {f[2] + f[1] + (f[0]/2):.2f} \\text{{ kN}} }}$
        
        $\\textbf{{\\small 2. Nodo A: }}$

        En el nodo A se pueden obtener las siguientes ecuaciones:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{AC}} - F_{{AB}} \\cdot \\dfrac{{d_1}}{{\\sqrt{{(d_1)^{{2}} + (d_3)^{{2}}}}}} = F_{{AC}} - F_{{AB}} \\cdot {(d[0])/(Calculations.magnitude(d[0],d[6])):.2f} = 0 }}$     
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = A_y - F_3 - F_{{AB}} \\cdot \\dfrac{{d_3}}{{\\sqrt{{(d_1)^{{2}} + (d_3)^{{2}}}}}}= {f[2] + f[1] + (f[0]/2):.2f} \\text{{ kN}} - {f[2]:.2f} \\text{{ kN}} - F_{{AB}} \\cdot {(d[6])/(Calculations.magnitude(d[0],d[6])):.2f} = 0 }}$      
        
        De la ecuación 2, se obtiene $F_{{AB}}$:
        
        ${{\hspace{{4mm}} {f[2] + f[1] + (f[0]/2):.2f} \\text{{ kN}} - {f[2]:.2f} \\text{{ kN}} - F_{{AB}} \\cdot {(d[6])/(Calculations.magnitude(d[0],d[6])):.2f}= 0}}$      
        ${{\hspace{{4mm}} F_{{AB}} \\cdot {(d[6])/(Calculations.magnitude(d[0],d[6])):.2f} = {f[1] + (f[0]/2):.2f} \\text{{ kN}}}}$      
        ${{\hspace{{4mm}} F_{{AB}} = {(f[1] + (f[0]/2))/((d[6])/(Calculations.magnitude(d[0],d[6]))):.2f} \\text{{ kN}}}}$      
        
        El elemento AB se encuentra a $\\textbf{{\\small Compresión}}$.

        Ahora bien, al analizar el nodo C, se observa que solo estan involucradas las fuerzas $F_{{AC}}$ y $F_{{CE}}$, dado que, el elemento BC es de fuerza cero. De este modo, se puede calcular $F_{{CE}}$ calculando $F_{{AC}}$ de la ecuación 1 del nodo A, reemplazando el dato de $F_{{AB}}$ obtenido previamente:
        
        ${{\hspace{{4mm}} F_{{AC}} - {(f[1] + (f[0]/2))/((d[6])/(Calculations.magnitude(d[0],d[6]))):.2f} \\text{{ kN}} \\cdot {(d[0])/(Calculations.magnitude(d[0],d[6])):.2f} = 0}}$      
        ${{\hspace{{4mm}} F_{{CE}} = F_{{AC}} = {((f[1] + (f[0]/2))/(d[6]))*(d[0]):.2f} \\text{{ kN}} }}$       
        
        El elemento CE se encuentra a $\\textbf{{\\small Tensión}}$.

        $\\textbf{{\\small 3. Nodo B: }}$

        Como la cercha es simétrica se podrá resolver para el nodo B el resultado de $F_{{BD}}$, que va a ser el mismo que $F_{{DF}}$:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{AB}} \\cdot \\dfrac{{d_1}}{{\\sqrt{{(d_1)^{{2}} + (d_3)^{{2}}}}}} - F_{{BE}} \\cdot \\dfrac{{d_2}}{{\\sqrt{{(d_2)^{{2}} + (d_3)^{{2}}}}}} - F_{{BD}} \\cdot \\dfrac{{d_2}}{{\\sqrt{{(d_2)^{{2}} + (d_4)^{{2}}}}}} = {((f[1] + (f[0]/2))/(d[6]))*(d[0]):.2f} \\text{{ kN}}  - F_{{BE}} \\cdot {(d[3])/(Calculations.magnitude(d[3],d[6])):.2f} - F_{{BD}} \\cdot {(d[3])/(Calculations.magnitude(d[3],d[9])):.2f} = 0}}$      
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = - F_2 + F_{{AB}} \\cdot \\dfrac{{d_3}}{{\\sqrt{{(d_1)^{{2}} + (d_3)^{{2}}}}}} + F_{{BE}} \\cdot \\dfrac{{d_3}}{{\\sqrt{{(d_2)^{{2}} + (d_3)^{{2}}}}}} - F_{{BD}} \\cdot \\dfrac{{d_4}}{{\\sqrt{{(d_2)^{{2}} + (d_4)^{{2}}}}}} = - {f[1]:.0f}\\text{{ kN}} + {(f[1] + (f[0]/2)):.2f} \\text{{ kN}}  + F_{{BE}} \\cdot {(d[6])/(Calculations.magnitude(d[3],d[6])):.2f} - F_{{BD}} \\cdot {(d[9])/(Calculations.magnitude(d[3],d[9])):.2f}  = 0 }}$      
        
        Se observa que a partir de la primera ecuación se puede despejar $F_{{BE}}$ en términos de $F_{{BD}}$. Luego, se realiza la sustitución en la segunda ecuación para resolver $F_{{BD}}$:
        
        ${{\hspace{{4mm}} {(f[1] + (f[0]/2))*(d[0]/d[6]):.2f} \\text{{ kN}}  - F_{{BE}} \\cdot {(d[3])/(Calculations.magnitude(d[3],d[6])):.2f} - F_{{BD}} \\cdot {(d[3])/(Calculations.magnitude(d[3],d[9])):.2f} = 0}}$      
        ${{\hspace{{4mm}} F_{{BE}} \\cdot {(d[3])/(Calculations.magnitude(d[3],d[6])):.2f} = {(f[1] + (f[0]/2))*(d[0]/d[6]):.2f} \\text{{ kN}}  - F_{{BD}} \\cdot {(d[3])/(Calculations.magnitude(d[3],d[9])):.2f}}}$      
        ${{\hspace{{4mm}} F_{{BE}} = {((f[1] + (f[0]/2))*((d[0]*(Calculations.magnitude(d[3],d[6])))/(d[6]*d[3]))):.2f} \\text{{ kN}} - F_{{BD}} \\cdot {(Calculations.magnitude(d[3],d[6]))/(Calculations.magnitude(d[3],d[9])):.2f}}}$     
        
        Finalmente:       
        ${{\hspace{{4mm}} {(f[0]/2):.2f} \\text{{ kN}} + F_{{BE}} \\cdot {(d[6])/(Calculations.magnitude(d[3],d[6])):.2f} - F_{{BD}} \\cdot {(d[9])/(Calculations.magnitude(d[3],d[9])):.2f} = 0 }}$      
        ${{\hspace{{4mm}} F_{{BD}} \\cdot {(d[9])/(Calculations.magnitude(d[3],d[9])):.2f} =  {(f[0]/2):.2f} \\text{{ kN}} + ({((f[1] + (f[0]/2))*((d[0]*(Calculations.magnitude(d[3],d[6])))/(d[6]*d[3]))):.2f} \\text{{ kN}} - F_{{BD}} \\cdot {(Calculations.magnitude(d[3],d[6]))/(Calculations.magnitude(d[3],d[9])):.2f}) \\cdot {(d[6])/(Calculations.magnitude(d[3],d[6])):.2f}}}$      
        ${{\hspace{{4mm}} F_{{BD}} \\cdot {(d[9])/(Calculations.magnitude(d[3],d[9])):.2f} =  {(f[0]/2) + ((f[1] + (f[0]/2))*(d[0]/d[3])):.2f} \\text{{ kN}} - F_{{BD}} \\cdot {(d[6])/(Calculations.magnitude(d[3],d[9])):.2f} }}$      
        ${{\hspace{{4mm}} F_{{BD}} \\cdot {((d[9] + d[6])/(Calculations.magnitude(d[3],d[9]))):.2f} = {(f[0]/2) + ((f[1] + (f[0]/2))*(d[0]/d[3])):.2f} \\text{{ kN}}}}$      
        ${{\hspace{{4mm}} F_{{DF}} = F_{{BD}} = {((f[0]/2) + ((f[1] + (f[0]/2))*(d[0]/d[3])))/(((d[9] + d[6])/(Calculations.magnitude(d[3],d[9])))):.2f} \\text{{ kN}}}}$                       
       
        El elemento DF se encuentra a $\\textbf{{\\small Compresión}}$.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 5120031,
        no_pregunta = 3,
        complexity = M,
        topic = "Armaduras",
        subtopic = "Cerchas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Si la fuerza máxima que cualquier elemento puede soportar es ${f[0] + 25:.0f} \\text{{ N}}$ a tensión y ${f[0]:.0f}\\text{{ N}}$ a compresión, calcule cuál es la fuerza $F_1$ máxima que puede ser soportada en el nodo E. Considere $d_1 = {d[0]:.0f} \\text{{ m}}$ y $\\alpha_1 = {(a[1]/3):.2f}°$ .",
        no_answers = 1,
        a1_name = "$F_1$ $[N]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(min(((f[0]+ 25)/2)*(Calculations.tangent((a[1]/3))),(f[0])*(Calculations.sine((a[1]/3)))),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = C3,
        ayuda2 = C6,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""     
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre sí por puntos llamados nodos, formando triángulos. El método de los nodos es una técnica usada para determinar las fuerzas internas en una cercha, basándose en el principio de que cada nodo está en equilibrio. A continuación, se presenta la solución sugerida para el ejercicio: 

        $\\textbf{{\\small 1. Cálculo de las reacciones en los apoyos: }}$     
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$               
        ${{\hspace{{4mm}} \\sum{{F_x}} = C_x = 0}}$             
              
        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{M_A}} = C_y \\cdot d_1 - F_1 \\cdot 2d_1 = 0}}$     
        ${{\hspace{{4mm}} C_y = 2F_1 }}$     
             
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + C_y - F_1 = 0}}$     
        ${{\hspace{{4mm}} A_y = -F_1 }}$     
        
        Teniendo en cuenta la configuración de la cercha y las reacciones en los apoyos, se puede concluir que la cercha es simétrica tanto en geometría como en carga, tal que $F_{{AB}} = F_{{ED}}$; $F_{{AC}} = F_{{EC}}$; y $F_{{BC}} = F_{{DC}}$. Por lo cual, solo será necesario evaluar 4 fuerzas internas:
        
        $\\textbf{{\\small 2. Nodo A: }}$     
        
        Del nodo A se pueden obtener las siguientes ecuaciones:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{AB}} \\cdot \\cos(\\alpha_1) - F_{{AC}} =  F_{{AB}} \\cdot {Calculations.cosine((a[1]/3)):.2f} - F_{{AC}} = 0 }}$     
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = F_{{AB}} \\cdot \\sin(\\alpha_1) - F_1 = F_{{AB}} \\cdot {Calculations.sine((a[1]/3)):.2f} - F_1 = 0 }}$     
        
        La ecuación 2. se usa para determinar $F_{{AB}}$:

        ${{\hspace{{4mm}} F_{{AB}} \\cdot {Calculations.sine((a[1]/3)):.2f} - F_1 = 0 }}$     
        ${{\hspace{{4mm}} F_{{AB}} = F_1 \\cdot {1/(Calculations.sine((a[1]/3))):.2f}}}$     
        
        De la ecuación 1. se obtiene $F_{{AC}}$:
        
        ${{\hspace{{4mm}} F_{{AB}} \\cdot {Calculations.cosine((a[1]/3)):.2f} - F_{{AC}} = 0 }}$     
        ${{\hspace{{4mm}} F_{{AC}} = F_1 \\cdot {1/(Calculations.tangent((a[1]/3))):.2f}}}$     
        
        $\\textbf{{\\small 3. Nodo B: }}$     
        
        En el nodo B se puede obtener las siguientes ecuaciones:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{BD}} - F_{{AB}} \\cdot \\cos(\\alpha_1) - F_{{BC}} \\cdot \\cos(\\alpha_1) = F_{{BD}} - F_{{AB}} \\cdot {Calculations.cosine((a[1]/3)):.2f} - F_{{BC}} \\cdot {Calculations.cosine((a[1]/3)):.2f} = 0 }}$     
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = F_{{BC}} \\cdot \\sin(\\alpha_1) - F_{{AB}} \\cdot \\sin(\\alpha_1) = F_{{BC}} \\cdot {Calculations.sine((a[1]/3)):.2f} - F_{{AB}} \\cdot {Calculations.sine((a[1]/3)):.2f} = 0 }}$     
        
        De la ecuación 2 se obtiene:     
        ${{\hspace{{4mm}} F_{{BC}} \\cdot {Calculations.sine((a[1]/3)):.2f} - F_{{AB}} \\cdot {Calculations.sine((a[1]/3)):.2f} = 0 }}$     
        ${{\hspace{{4mm}} F_{{BC}} = F_{{AB}} = F_1 \\cdot {1/(Calculations.sine((a[1]/3))):.2f}}}$     
        
        De la ecuación 1. se obtiene $F_{{BD}}$:
        
        ${{\hspace{{4mm}} F_{{BD}} - F_{{AB}} \\cdot {Calculations.cosine((a[1]/3)):.2f} - F_{{BC}} \\cdot {Calculations.cosine((a[1]/3)):.2f} = 0 }}$     
        ${{\hspace{{4mm}} F_{{BD}} =  F_1 \\cdot {2/(Calculations.tangent((a[1]/3))):.2f}}}$     
        
        $\\textbf{{\\small 4. Evaluación de la condición de resistencia máxima: }}$     
        
        $\\underline{{Elementos \\hspace{{2mm}} de \\hspace{{2mm}} Tensión:}}$      
        
        Los elementos de tensión encontrados son AB y BD, tal que, estas fuerzas deben ser menor o igual a ${f[0]+ 25:.0f} \\text{{ N}}$. Dado que, el elemento BD tiene que resistir más o igual fuerza AB, se halla $F_1$ con este:
        
        ${{\hspace{{4mm}} F_{{BD}} = F_1 \\cdot {2/(Calculations.tangent((a[1]/3))):.2f} = {f[0]+ 25:.0f} \\text{{ N}} }}$     
        ${{\hspace{{4mm}} F_1 = {((f[0]+ 25)/2)*(Calculations.tangent((a[1]/3))):.2f} \\text{{ N}}}}$     
        
        $\\underline{{Elementos \\hspace{{2mm}} de \\hspace{{2mm}} Compresión:}}$  
        
        Los elementos de compresión encontrados son AC y BC, tal que, estas fuerzas deben ser menor o igual a ${f[0]:.0f} \\text{{ N}}$. Dado que, el elemento BC tiene que resistir más o igual fuerza que AC, se halla $F_1$ con este:
        
        ${{\hspace{{4mm}} F_{{BC}} = F_1 \\cdot {1/(Calculations.sine((a[1]/3))):.2f} = {f[0]:.0f} \\text{{ N}} }}$     
        ${{\hspace{{4mm}} F_1 = {(f[0])*(Calculations.sine((a[1]/3))):.2f} \\text{{ N}}}}$     
        
        Finalmente, se selecciona el menor valor de $F_1$: ${min(((f[0]+ 25)/2)*(Calculations.tangent((a[1]/3))),(f[0])*(Calculations.sine((a[1]/3)))):.2f}$ $\\text{{ N}}$. Dado que, si selecciona el mayor valor, el otro elemento crítico no resistiría y la estructura fallaría.  
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#4_1
        code = 5120041,
        no_pregunta = 4,
        complexity = M,
        topic = "Armaduras",
        subtopic = "Cerchas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuántos elementos de fuerza cero tiene la armadura Fink mostrada?",
        no_answers = 1,
        a1_name = "Número de elementos de fuerza cero",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(7,2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = C3,
        ayuda2 = C4,      
        ayuda3 = C5,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre sí por puntos llamados nodos, formando triángulos. Un elemento de fuerza cero se define como un miembro de la armadura que no experimenta ninguna fuerza axial (Tensión o compresión). A continuación, se presenta la solución sugerida para el ejercicio: 
        
        Primero, se debe tener en cuenta que si hay tres elementos conectados en un nodo, donde dos de ellos son colineales y no hay cargas externas aplicadas en el nodo, el tercer miembro va a ser de fuerza cero. Esto nos permite identificar en la evaluación de los nodos B, J y N los elementos $BC$, $JI$ y $NM$ son elementos de fuerza cero.
        
        Una vez identificados los anteriores elementos de fuerza cero, si se realiza la sumatoria de fuerzas en los nodos C, I y M, se encontrará que los elementos $CD$, $IL$ y $ML$ también son de fuerza cero.    
        
        Por otro lado, al ser $IL$ y $ML$ elementos de fuerza cero, al evaluar el equilibrio en el nodo L, se determina que el elemento $LK$ es de fuerza cero.  
        
        En resumen, se identifican un total de 7 elementos de fuerza cero: $BC$, $JI$, $NM$, $CD$, $IL$, $ML$ y $LK$. 
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#5_1
        code = 5120051,
        no_pregunta = 5,
        complexity = M,
        topic = "Armaduras",
        subtopic = "Cerchas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuántos elementos de fuerza cero tiene la armadura mostrada?",
        no_answers = 1,
        a1_name = "Número de elementos de fuerza cero",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: 11,
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = C3,
        ayuda2 = C4,      
        ayuda3 = C5,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre sí por puntos llamados nodos, formando triángulos. Un elemento de fuerza cero se define como un miembro de la armadura que no experimenta ninguna fuerza axial (Tensión o compresión). A continuación, se presenta la solución sugerida para el ejercicio: 
        
        Primero, se debe tener en cuenta que si hay tres elementos conectados en un nodo, donde dos de ellos son colineales y no hay cargas externas aplicadas en el nodo, el tercer miembro va a ser de fuerza cero. Esto nos permite identificar bajo el sistema de coordenadas convencional, en los nodos $C$, $G$, $H$, $K$ y $O$ los elementos $BC$, $FG$, $HI$, $JK$ y $NO$ son elementos de fuerza cero.
        
        Una vez identificados los anteriores elementos de fuerza cero, se evalúa dicha colinealidad bajo un sistema de coordenadas arbitrario, en los nodos $B$, $F$, $J$, y $N$ los elementos $BE$, $FE$, $JM$, y $NM$ son elementos de fuerza cero.

        Finalmente, al identificar que los anteriores elementos son de fuerza cero, los nodos $E$ y $M$ muestran una colinealidad entre tres elementos, de estos nodos se concluye que los miembros $DE$ y $LM$ son de fuerza cero.
        
        En resumen, se identifican un total de 11 elementos de fuerza cero: $BC$, $FG$, $HI$, $JK$, $NO$, $BE$, $FE$, $JM$, $NM$, $DE$ y $LM$.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 

    Questionary(#6_1
        code = 5120061,
        no_pregunta = 6,
        complexity = M,
        topic = "Armaduras",
        subtopic = "Cerchas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las fuerzas internas de los elementos $EG$ y $GH$ de la cercha presentada (Use negativo si el elemento esta en compresión y positivo si el elemento esta tensión). Considere que $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$, $F_3 = {f[2]:.0f} \\text{{ N}}$, $F_4 = {f[3]:.0f} \\text{{ N}}$ y $d_0 = {d[0]:.0f} \\text{{ m}}$.",  
        no_answers = 2,
        a1_name = "Fuerza en $EG$ $[N]$",
        a2_name = "Fuerza en $GH$ $[N]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(-(f[1] + 2*f[2] + 3*f[3])/(4),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((f[1]+2*f[2]+3*f[3])/4)-f[3],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = C2,
        ayuda2 = C7,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre sí por puntos llamados nodos, formando triángulos. A continuación, se presenta la solución sugerida para el ejercicio: 
        
        $\\textbf{{\\small 1. Cálculo de las reacciones en los apoyos: }}$  
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$      
        ${{\hspace{{4mm}} A_x = 0 \\text{{ N}} }}$

        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$    
        ${{\hspace{{4mm}} \\sum{{M_A}} = - F_2 \\cdot d_0 - F_3 \\cdot 2d_0 - F_4 \\cdot 3d_0 + J_y \\cdot 4d_0=0}}$      
        ${{\hspace{{4mm}} J_y = \\dfrac{{F_2 + 2F_3 + 3F_4}}{{4}} }}$          
        ${{\hspace{{4mm}} J_y = {(f[1] + 2*f[2] + 3*f[3])/(4):.2f} \\text{{ N}} }}$

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$    
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + J_y - F_1 - F_2 - F_3 - F_4 =0 }}$     
        ${{\hspace{{4mm}} A_y = F_1 + F_2 + F_3 + F_4 - J_y}}$         
        ${{\hspace{{4mm}} A_y = {f[0]+f[1]+f[2]+f[3]-((f[1] + 2*f[2] + 3*f[3])/(4)):.2f} \\text{{ N}} }}$

        
        $\\textbf{{\\small 2. Condición de equilibrio del corte seleccionado: }}$     
        
        En la cercha mostrada, se realiza un corte a través de los elementos $EG$, $GH$ y $HJ$ y se selecciona la parte de la derecha del corte. En esta sección, las fuerzas que deben considerarse para hacer el equilibrio son:  las fuerzas internas $F_{{EG}}$, $F_{{GH}}$, $F_{{HJ}}$, la carga externa $F_4$ y la reacción $J_y$. Las fuerzas internas se suponen a tensión.
        
        $\\underline{{Despeje \\hspace{{2mm}} de \\hspace{{2mm}} F_{{EG}}:}}$    

        ${{\hspace{{4mm}} \\sum{{M_H}} = 0 }}$    
        ${{\hspace{{4mm}} \\sum{{M_H}} = F_{{EG}} \\cdot d_0 + J_y \\cdot d_0 = 0}}$      
        ${{\hspace{{4mm}} F_{{EG}} = -J_y}}$                  
        ${{\hspace{{4mm}} F_{{EG}} = {-(f[1] + 2*f[2] + 3*f[3])/(4):.2f} \\text{{ N}}}}$

        {'El elemento $EG$ está a Tensión.' if (-(f[1] + 2*f[2] + 3*f[3])/(4)) > 0 else 'El elemento $EG$ está a Compresión.'}   

        $\\underline{{Despeje \\hspace{{2mm}} de \\hspace{{2mm}} F_{{GH}}:}}$   

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$  
        ${{\hspace{{4mm}} \\sum{{F_y}} = -F_4 - F_{{GH}} + J_y = 0 }}$   
        ${{\hspace{{4mm}} F_{{GH}} = J_y - F_4 }}$                
        ${{\hspace{{4mm}} F_{{HI}} = {((f[1] + 2*f[2] + 3*f[3])/(4))-f[3]:.2f} \\text{{ N}}}}$  

        {'El elemento $GH$ está a Tensión.' if (((f[1] + 2*f[2] + 3*f[3])/(4))-f[3]) > 0 else 'El elemento $GH$ está a Compresión.'}   
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),



    #========================================================  ARMADURAS  =========================================================
    #-------------------------------------------------         Cerchas      --------------------------------------------
    #-------------------------------------------------       Nivel Dificil   ---------------------------------------------------
    #-------------------------------------------------       Code: 5130011    --------------------------------------------------

    Questionary(#1_1
        code = 5130011,
        no_pregunta = 1,
        complexity = D,
        topic = "Armaduras",
        subtopic = "Cerchas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las fuerzas internas de los miembros DC, HC y DH de la armadura presentada (Use negativo si el elemento esta en compresión y positivo si el elemento esta tensión). Considere $F_1 = {f[0]:.0f} \\text{{ kN}}$, $F_2 = {f[1]:.0f} \\text{{ kN}}$, $F_3 = {f[2]:.0f} \\text{{ kN}}$, $F_4 = {f[3]:.0f} \\text{{ kN}}$, $d_1 = {d[0]:.0f} \\text{{ m}}$ y $d_2 = {d[3]:.0f}  \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Fuerza en DC $[kN]$",
        a2_name = "Fuerza en HC $[kN]$",
        a3_name = "Fuerza en DH $[kN]$",
        answer1 = lambda f, a, calc, c, d, m: np.round(-(f[3]*d[3]+f[2]*2*d[3])/((d[0]*d[3])/(Calculations.magnitude(d[0],d[3]))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[3] + 2*f[2],2),
        answer3 = lambda f, a, calc, c, d, m: np.round((f[3]+f[2]*2)*(d[3]/d[0]) - f[1], 2),
        ayuda1 = C7,
        ayuda2 = C3,      
        ayuda3 = C6,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre sí por puntos llamados nodos, formando triángulos. A continuación, se presenta la solución sugerida para el ejercicio: 
        
        $\\textbf{{\\small 1. Cálculo de las reacciones en los apoyos: }}$     
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$               
        ${{\hspace{{4mm}} \\sum{{F_x}} = A_x - F_3 - F_4 = 0}}$             
        ${{\hspace{{4mm}} A_x = F_3 + F_4 = {f[2] + f[3] :.0f} \\text{{ kN}}}}$        
             
        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{M_A}} = F_4 \\cdot d_2 + F_3 \\cdot 2d_2 + F_1 \\cdot d_1 - F_y \\cdot 2d_1 = 0}}$     
        ${{\hspace{{4mm}} F_y = \\dfrac{{F_4 \\cdot d_2 + F_3 \\cdot 2d_2 + F_1 \\cdot d_1}}{{2d_1}} = {(f[3]*d[3]+f[2]*2*d[3]+f[0]*d[0])/(2*d[0]):.2f} \\text{{ kN}} }}$     
             
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + F_y - F_1 - F_2 = 0}}$     
        ${{\hspace{{4mm}} A_y = F_1 + F_2 - F_y = {f[0] + f[1] - (f[3]*d[3]+f[2]*2*d[3]+f[0]*d[0])/(2*d[0]) :.2f} \\text{{ kN}} }}$     
        
        $\\textbf{{\\small 2. Condición de equilibrio del corte seleccionado: }}$     
        
        En la cercha mostrada, se realiza un corte que aísla la parte compuesta por los nodos F,E, D, G, H y la siguientes fuerzas: las reacciones en F y las fuerzas $F_1$, $F_2$, $F_{{DC}}$, $F_{{HC}}$ y $F_{{HI}}$. A partir de estas fuerzas, se utilizan las ecuaciones de equilibrio para encontrar las incógnitas deseadas:

        $\\underline{{Despeje \\hspace{{2mm}} de \\hspace{{2mm}} F_{{DC}}:}}$    
        
        ${{\hspace{{4mm}} \\sum{{M_H}} = F_1 \\cdot d_1 - F_y \\cdot 2d_1 - F_{{DC}} \\cdot  \\dfrac{{d_1}}{{\\sqrt{{(d_1)^{{2}} + (d_2)^{{2}}}}}}  \\cdot d_2 = {f[0]*d[0]:.2f} \\text{{ kN}} \\cdot \\text{{ m}} - {(f[3]*d[3]+f[2]*2*d[3]+f[0]*d[0]):.2f} \\text{{ kN}} \\cdot \\text{{ m}} - F_{{DC}} \\cdot {(d[0]*d[3])/(Calculations.magnitude(d[0],d[3])):.2f} \\text{{ m}} = 0 }}$      
        ${{\hspace{{4mm}} F_{{DC}} \\cdot {(d[0]*d[3])/(Calculations.magnitude(d[0],d[3])):.2f} \\text{{ m}} = {- (f[3]*d[3]+f[2]*2*d[3]):.2f} \\text{{ kN}} \\cdot \\text{{ m}} }}$      
        ${{\hspace{{4mm}} F_{{DC}} = {-(f[3]*d[3]+f[2]*2*d[3])/((d[0]*d[3])/(Calculations.magnitude(d[0],d[3]))):.2f} \\text{{ kN}}  }}$   

        {'El elemento DC está a Tensión.' if (-(f[3]*d[3]+f[2]*2*d[3])/((d[0]*d[3])/(Calculations.magnitude(d[0],d[3])))) > 0 else 'El elemento DC está a Compresión.'}  
        
        $\\underline{{Despeje \\hspace{{2mm}} de \\hspace{{2mm}} F_{{HC}}:}}$     

        Teniendo en cuenta que el elemento DC está en compresión :
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{HC}} - F_{{DC}} \\cdot \\dfrac{{d_1}}{{\\sqrt{{(d_1)^{{2}} + (d_2)^{{2}}}}}} = F_{{HC}} - {f[3] + 2*f[2]:.2f} \\text{{ kN}} = 0 }}$     
        ${{\hspace{{4mm}} F_{{HC}} = {f[3] + 2*f[2]:.2f} \\text{{ kN}} }}$  

        {'El elemento HC está a Tensión.' if (f[3] + 2*f[2]) > 0 else 'El elemento HC está a Compresión.'}     
        
        $\\textbf{{\\small 3. Nodo D: }}$ 
        
        Para encontrar la fuerza $F_{{DH}}$, se puede evaluar el nodo D:
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{DH}} - F_2 + F_{{DC}} \\cdot \\dfrac{{d_2}}{{\\sqrt{{(d_1)^{{2}} + (d_2)^{{2}}}}}} = F_{{DH}} - {f[1]:.2f} \\text{{ kN}} + {(f[3]+f[2]*2)*(d[3]/d[0]):.2f} \\text{{ kN}} = 0 }}$      
        ${{\hspace{{4mm}} F_{{DH}} =  {f[1] - (f[3]+f[2]*2)*(d[3]/d[0]):.2f} \\text{{ kN}} }}$  

        {'El elemento DH está a Tensión.' if (f[1] - (f[3]+f[2]*2)*(d[3]/d[0])) < 0 else 'El elemento DH está a Compresión.'}   
                        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 5130021,
        no_pregunta = 2,
        complexity = D,
        topic = "Armaduras",
        subtopic = "Cerchas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Si la fuerza máxima que cualquier elemento puede soportar es ${f[0] + 35:.0f} \\text{{ N}}$ a tensión y ${f[0]:.0f}\\text{{ N}}$ a compresión, calcule cuál es la fuerza $F_1$ máxima que puede ser soportada en el nodo E. Considere $d_1 = {d[0]:.0f} \\text{{ m}}$ .",
        no_answers = 1,
        a1_name = "$F_1$ $[N]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(min(((f[0] + 35)*(3*(d[0]/2)))/(Calculations.magnitude((d[0]/2), (3/2)*d[0])),(f[0])*(6*Calculations.sine(45))),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = C3,
        ayuda2 = C6,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre sí por puntos llamados nodos, formando triángulos. El método de los nodos es una técnica usada para determinar las fuerzas internas en una cercha, basándose en el principio de que cada nodo está en equilibrio. A continuación, se presenta la solución sugerida para el ejercicio: 

        $\\textbf{{\\small 1. Cálculo de las reacciones en los apoyos: }}$             
              
        ${{\hspace{{4mm}} \\sum{{M_E}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{M_E}} = A_x \\cdot \\dfrac{{3}}{{2}} \\cdot d_1 - F_1 \\cdot \\dfrac{{1}}{{2}} \\cdot d_1 = 0}}$     
        ${{\hspace{{4mm}} A_x = \\dfrac{{1}}{{3}} \\cdot F_1}}$      
             
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$               
        ${{\hspace{{4mm}} \\sum{{F_x}} = A_x - E_x = 0}}$      
        ${{\hspace{{4mm}} E_x = \\dfrac{{1}}{{3}} \\cdot F_1}}$       
             
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = E_y - F_1 = 0}}$     
        ${{\hspace{{4mm}} E_y = F_1 }}$     
        
        $\\textbf{{\\small 2. Nodo E: }}$     
        
        En el nodo E se pueden obtener las siguientes ecuaciones:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{EC}} \\cdot \\dfrac{{{d[0]/2:.2f}}}{{{Calculations.magnitude((d[0]/2), (3/2)*d[0]):.2f}}} - \\dfrac{{1}}{{3}} \\cdot F_1 =  0 }}$     
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = F_1 + F_{{ED}} - F_{{EC}} \\cdot \\dfrac{{{(3/2)*d[0]:.2f}}}{{{Calculations.magnitude((d[0]/2), (3/2)*d[0]):.2f}}} = 0 }}$     
        
        De la ecuación 2. se obtiene $F_{{EC}}$:

        ${{\hspace{{4mm}} F_{{EC}} \\cdot \\dfrac{{{d[0]/2:.2f}}}{{{Calculations.magnitude((d[0]/2), (3/2)*d[0]):.2f}}} = \\dfrac{{1}}{{3}} \\cdot F_1 }}$     
        ${{\hspace{{4mm}} F_{{EC}} = F_1 \\cdot {(Calculations.magnitude((d[0]/2), (3/2)*d[0]))/(3*(d[0]/2)):.2f}}}$     
        
        De la ecuación 1. se obtiene $F_{{ED}}$:
        
        ${{\hspace{{4mm}} F_{{ED}} = F_{{EC}} \\cdot \\dfrac{{{(3/2)*d[0]:.2f}}}{{{Calculations.magnitude((d[0]/2), (3/2)*d[0]):.2f}}} - F_1 }}$     
        ${{\hspace{{4mm}} F_{{ED}} = 0 }}$     
        
        $\\textbf{{\\small 3. Nodo A: }}$     
        
        Del nodo A se pueden obtener las siguientes ecuaciones:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = \\dfrac{{1}}{{3}} \\cdot F_1 - F_{{AD}} \\cdot {Calculations.cosine(45):.2f} - F_{{AB}} \\cdot {Calculations.cosine(45):.2f} = 0 }}$     
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = F_{{AB}} \\cdot {Calculations.sine(45):.2f} - F_{{AD}} \\cdot {Calculations.sine(45):.2f} = 0 }}$     
        
        De la ecuación 2 se determina:
        ${{\hspace{{4mm}} F_{{AD}} = F_{{AB}} }}$     
        
        De la ecuación 1. se obtiene $F_{{AB}}$ y $F_{{AD}}$:
        
        ${{\hspace{{4mm}} F_{{AD}} = F_{{AB}} = F_1 \\cdot {1/(6*Calculations.cosine(45)):.2f} }}$         
        
        $\\textbf{{\\small 4. Nodo D: }}$     
        
        Del nodo D se pueden obtener las siguientes ecuaciones:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{DA}} \\cdot {Calculations.cosine(45):.2f} - F_{{DC}} \\cdot {Calculations.cosine(45):.2f} = 0 }}$     
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = F_{{DA}} \\cdot {Calculations.cosine(45):.2f} + F_{{DC}} \\cdot {Calculations.cosine(45):.2f} - F_{{DB}} = 0 }}$     
        
        De la ecuación 2. se determina:
        ${{\hspace{{4mm}} F_{{DC}} = F_{{DA}} = F_1 \\cdot {1/(6*Calculations.cosine(45)):.2f} }}$     
        
        De la ecuación 1. se obtiene $F_{{DB}}$:
        
        ${{\hspace{{4mm}} F_{{DB}} = 2 \\cdot F_{{DA}} \\cdot {Calculations.cosine(45):.2f} }}$          
        
        A partir de las anteriores ecuaciones, se evidencia que $F_{{DC}} = F_{{BC}}$ .
        
        $\\textbf{{\\small 5. Evaluación de la condición de resistencia máxima: }}$     
        
        $\\underline{{Elementos \\hspace{{2mm}} de \\hspace{{2mm}} Tensión:}}$      
        
        Los elementos de tensión encontrados son EC y DB, tal que, estas fuerzas deben ser menor o igual a ${f[0] + 35:.0f} \\text{{ N}}$. Dado que, el elemento EC tiene que resistir más fuerza que DB, se halla $F_1$ con este:     

        ${{\hspace{{4mm}} F_{{EC}} = F_1 \\cdot {(Calculations.magnitude((d[0]/2), (3/2)*d[0]))/(3*(d[0]/2)):.2f} = {f[0] + 35:.0f} \\text{{ N}} }}$     
        ${{\hspace{{4mm}} F_1 = {((f[0] + 35)*(3*(d[0]/2)))/(Calculations.magnitude((d[0]/2), (3/2)*d[0])):.2f} \\text{{ N}}}}$     
        
        $\\underline{{Elementos \\hspace{{2mm}} de \\hspace{{2mm}} Compresión:}}$    
        
        Los elementos de compresión encontrados son AD, AB, DC y BC, estas fuerzas deben ser menor o igual a ${f[0]:.0f} \\text{{ N}}$. Dado que, todos estos elementos tienen fuerza interna de igual magnitud, se puede evaluar de la siguiente manera:
        
        ${{\hspace{{4mm}} F_{{AD}} = F_{{AB}} = F_{{DC}} = F_{{BC}} = F_1 \\cdot {1/(6*Calculations.cosine(45)):.2f} = {f[0]:.0f} \\text{{ N}} }}$     
        ${{\hspace{{4mm}} F_1 = {(f[0])*(6*Calculations.sine(45)):.2f} \\text{{ N}}}}$     
        
        Finalmente, se selecciona el menor valor de $F_1$: ${min((f[0])*(6*Calculations.sine(45)),((f[0] + 35)*(3*(d[0]/2)))/(Calculations.magnitude((d[0]/2), (3/2)*d[0]))):.2f}$ $\\text{{ N}}$. Dado que, si selecciona el mayor valor, los otros elementos críticos no resistirían y la estructura fallaría.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),



    #-------------------------------------------------         Marcos      --------------------------------------------
    #-------------------------------------------------       Nivel Fácil   ---------------------------------------------------
    #-------------------------------------------------       Code: 5210011    --------------------------------------------------

    Questionary(#1_1
        code = 5210011,
        no_pregunta = 1,
        complexity = F,
        topic = "Armaduras",
        subtopic = "Marcos",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la fuerza sobre el elemento BD y las componentes de la reacción en C (Indique el signo de la dirección de las fuerzas). Considere $F_1 = {f[0]:.0f} \\text{{ N}}$,  $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Reacción $C_x$ [N]",
        a2_name = "Reacción $C_y$ [N]",
        a3_name = "Fuerza BD [N]",
        answer1 = lambda f, a, calc, c, d, m: np.round(-(f[0]*(d[3] + d[6])*d[3])/(d[0]*d[6]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-(f[0]*(d[3] + d[6]))/(d[6]) + f[0],2),
        answer3 = lambda f, a, calc, c, d, m: np.round((f[0]*(d[3] + d[6])*(Calculations.magnitude(d[0],d[3])))/(d[0]*d[6]), 2),
        ayuda1 = MA1,
        ayuda2 = MA2,      
        ayuda3 = MA3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Los marcos son estructuras en las cuales al menos un elemento esta sometido a la acción de varias fuerzas. A continuación, se presenta la solución sugerida para el ejercicio: 
        
        Las fuerzas solicitadas en el ejercicio se pueden encontrar analizando el elemento ABC, dado que, la fuerza del elemento BD está dirigida a lo largo de BD: 
        
        $\\textbf{{\\small 1. Condición de equilibrio - Momento en C: }}$
        
        ${{\hspace{{4mm}} \\sum{{M_C}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{M_C}} = F_1 \\cdot (d_2 + d_3) - F_{{BD}} \\cdot \\dfrac{{d_1}}{{\\sqrt{{(d_1)^{{2}} + (d_2)^{{2}}}}}} \\cdot d_3 = 0  }}$      
        ${{\hspace{{4mm}} \\sum{{M_C}} = {f[0]:.0f} \\text{{ N}} \\cdot {d[3] + d[6]:.0f} \\text{{ m}} - F_{{BD}} \\cdot {(d[0]*d[6])/(Calculations.magnitude(d[0],d[3])) :.2f} \\text{{ m}} = 0 }}$     
        ${{\hspace{{4mm}} F_{{BD}} \\cdot {(d[0]*d[6])/(Calculations.magnitude(d[0],d[3])) :.2f} \\text{{ m}} = {f[0]*(d[3] + d[6]):.0f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
        ${{\hspace{{4mm}} F_{{BD}} = {(f[0]*(d[3] + d[6])*(Calculations.magnitude(d[0],d[3])))/(d[0]*d[6]):.2f} \\text{{ N}} }}$      
        
        $\\textbf{{\\small 2. Condición de equilibrio - Sumatoria de fuerzas en X: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{BD}} \\cdot \\dfrac{{d_2}}{{\\sqrt{{(d_1)^{{2}} + (d_2)^{{2}}}}}} + C_x = 0  }}$      
        ${{\hspace{{4mm}} \\sum{{F_x}} = {(f[0]*(d[3] + d[6])*(Calculations.magnitude(d[0],d[3])))/(d[0]*d[6]):.2f} \\cdot {(d[3])/(Calculations.magnitude(d[0],d[3])):.2f} \\text{{ N}} + C_x = 0 }}$     
        ${{\hspace{{4mm}} C_x = {-(f[0]*(d[3] + d[6])*d[3])/(d[0]*d[6]):.2f} \\text{{ N}} }}$      
        
        $\\textbf{{\\small 3. Condición de equilibrio - Sumatoria de fuerzas en Y: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{BD}} \\cdot \\dfrac{{d_1}}{{\\sqrt{{(d_1)^{{2}} + (d_2)^{{2}}}}}} + C_y - F_1 = 0  }}$      
        ${{\hspace{{4mm}} \\sum{{F_y}} = {(f[0]*(d[3] + d[6])*(Calculations.magnitude(d[0],d[3])))/(d[0]*d[6]):.2f} \\cdot {(d[0])/(Calculations.magnitude(d[0],d[3])):.2f} \\text{{ N}} + C_y - {f[0]:.0f} \\text{{ N}}= 0 }}$     
        ${{\hspace{{4mm}} C_y = {-(f[0]*(d[3] + d[6]))/(d[6]) + f[0]:.2f} \\text{{ N}} }}$       
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#1_2
        code = 5210012,
        no_pregunta = 2,
        complexity = F,
        topic = "Armaduras",
        subtopic = "Marcos",
        version = 2,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la componente vertical de la reacción en A y ambas componentes de la reacción en B (Indique el signo de la dirección de las fuerzas). Considere $F_1 = {f[0]:.0f} \\text{{ N}}$,  $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$, $d_3 = {d[6]:.0f} \\text{{ m}}$ y $d_4 = {d[0]*(3/5):.2f} \\text{{ m}}$ .",
        no_answers = 3,
        a1_name = "Reacción $B_x$ [N]",
        a2_name = "Reacción $B_y$ [N]",
        a3_name = "Reacción $A_y$ [N]",
        answer1 = lambda f, a, calc, c, d, m: np.round(-f[0]*(2/5)*(d[0]/(d[6]+d[3])),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*(3/5) + d[3]*f[0]*(2/(5*(d[6]+d[3]))),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(f[0]-(f[0]*(3/5) + d[3]*f[0]*(2/(5*(d[6]+d[3])))), 2),
        ayuda1 = MA1,
        ayuda2 = MA2,      
        ayuda3 = MA3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Los marcos son estructuras en las cuales al menos un elemento esta sometido a la acción de varias fuerzas. A continuación, se presenta la solución sugerida para el ejercicio: 
         
        $\\textbf{{\\small 1. Condición de equilibrio global - Momento en A: }}$
        
        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{M_A}} = F_1 \\cdot (d_1 - d_4) + B_x \\cdot (d_3 + d_2) = 0  }}$      
        ${{\hspace{{4mm}} B_x \\cdot {d[6] + d[3] :.0f} \\text{{ m}} = {-f[0]*(2/5)*d[0]:.2f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
        ${{\hspace{{4mm}} B_x = {-f[0]*(2/5)*(d[0]/(d[6]+d[3])):.2f} \\text{{ N}} }}$      
        
        $\\textbf{{\\small 2. Condición de equilibrio elemento BCD - Momento en C: }}$
        
        ${{\hspace{{4mm}} \\sum{{M_C}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{M_C}} = B_y \\cdot d_1 - F_1 \\cdot d_4 - B_x \\cdot d_2 = 0  }}$      
        ${{\hspace{{4mm}} B_y \\cdot {d[0]:.0f} \\text{{ m}} = {f[0]*(3/5)*d[0]:.2f} \\text{{ N}} \\cdot \\text{{ m}} + {d[3]*f[0]*(2/5)*(d[0]/(d[6]+d[3])):.2f} \\text{{ N}} \\cdot \\text{{ m}}}}$      
        ${{\hspace{{4mm}} B_y= {f[0]*(3/5) + d[3]*f[0]*(2/(5*(d[6]+d[3]))):.2f} \\text{{ N}} }}$      
        
        $\\textbf{{\\small 3. Condición de equilibrio global - Sumatoria de fuerzas en Y: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + B_y - F_1 = 0  }}$       
        ${{\hspace{{4mm}} A_y = {f[0]-(f[0]*(3/5) + d[3]*f[0]*(2/(5*(d[6]+d[3])))):.2f} \\text{{ N}} }}$      
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    #========================================================  ARMADURAS  =========================================================
    #-------------------------------------------------         Marcos      --------------------------------------------
    #-------------------------------------------------       Nivel Medio   ---------------------------------------------------
    #-------------------------------------------------       Code: 5220011    --------------------------------------------------

    Questionary(#1_1
        code = 5220011,
        no_pregunta = 1,
        complexity = M,
        topic = "Armaduras",
        subtopic = "Marcos",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las componentes de la reacción en D y la componente vertical de la reacción en E (Indique el signo de la dirección de las fuerzas). Considere $F_1 = {f[0]:.0f} \\text{{ N}}$, $M_1 = {m[0]:.0f} \\text{{  N}} \\cdot \\text {{ m}}$,  $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Reacción $D_x$ [N]",
        a2_name = "Reacción $D_y$ [N]",
        a3_name = "Reacción $E_y$ [N]",
        answer1 = lambda f, a, calc, c, d, m: np.round((m[0] - ((-m[0] + f[0]*d[3])/(d[6] + d[3]))*d[3])/d[0],2),
        answer2 = lambda f, a, calc, c, d, m: np.round((-m[0] + f[0]*d[3])/(d[6] + d[3]),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(f[0]-(-m[0] + f[0]*d[3])/(d[6] + d[3]), 2),
        ayuda1 = MA4,
        ayuda2 = MA1,
        ayuda3 = MA3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Los marcos son estructuras en las cuales al menos un elemento esta sometido a la acción de varias fuerzas. A continuación, se presenta la solución sugerida para el ejercicio: 
        
        $\\textbf{{\\small 1. Condición de equilibrio global - Momento en E: }}$
        
        ${{\hspace{{4mm}} \\sum{{M_E}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{M_E}} = F_1 \\cdot d_2 - D_y \\cdot (d_3 + d_2) - M_1 = 0  }}$      
        ${{\hspace{{4mm}} \\sum{{M_E}} = {f[0]:.0f} \\text{{ N}} \\cdot {d[3]:.0f} \\text{{ m}} - D_y \\cdot {d[6] + d[3] :.0f} \\text{{ m}} - {m[0]:.0f} \\text{{  N}} \\cdot \\text {{ m}} = 0 }}$     
        ${{\hspace{{4mm}} D_y \\cdot {d[6] + d[3] :.0f} \\text{{ m}} = {f[0]*d[3]-m[0]:.0f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
        ${{\hspace{{4mm}} D_y = {(-m[0] + f[0]*d[3])/(d[6] + d[3]):.2f} \\text{{ N}} }}$      
        
        $\\textbf{{\\small 2. Condición de equilibrio global- Sumatoria de fuerzas en Y: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = {(-m[0] + f[0]*d[3])/(d[6] + d[3]):.2f} \\text{{ N}} - {f[0]:.0f} \\text{{ N}} + E_y = 0  }}$       
        ${{\hspace{{4mm}} E_y = {f[0]-(-m[0] + f[0]*d[3])/(d[6] + d[3]):.2f} \\text{{ N}} }}$      
        
        $\\textbf{{\\small 3. Condición de equilibrio Elemento ACD - Momento en C: }}$
        
        ${{\hspace{{4mm}} \\sum{{M_C}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{M_C}} = {(-m[0] + f[0]*d[3])/(d[6] + d[3]):.2f} \\text{{ N}} \\cdot {d[3]:.0f} \\text{{ m}} - {m[0]:.0f} \\text{{  N}} \\cdot \\text {{ m}} + D_x \\cdot {d[0]:.0f} \\text{{ m}} = 0  }}$      
        ${{\hspace{{4mm}} D_x \\cdot {d[0]:.0f} \\text{{ m}} = {m[0] - ((-m[0] + f[0]*d[3])/(d[6] + d[3]))*d[3]:.2f} \\text{{ N}} \\cdot \\text {{ m}}}}$      
        ${{\hspace{{4mm}} D_x  = {(m[0] - ((-m[0] + f[0]*d[3])/(d[6] + d[3]))*d[3])/d[0]:.2f} \\text{{ N}} }}$      
        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 5220021,
        no_pregunta = 2,
        complexity = M,
        topic = "Armaduras",
        subtopic = "Marcos",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de las componentes de las fuerzas ejercidas sobre el elemento ACEG en C. Considere $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$, $F_3 = {f[2]:.0f} \\text{{ N}}$, $d_1 = {d[0]:.0f} \\text{{ m}}$, $d_2 = {d[3]:.0f} \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Fuerza $C_x$ [N]",
        a2_name = "Fuerza $C_y$ [N]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(abs(-(f[2]*d[3]- d[0]*(f[0]+f[1]))/d[6]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(abs(((f[2]*d[3] - d[0]*(f[0]+f[1])) + 2*f[0]*d[0] - f[2]*d[3])/d[0]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MA1,
        ayuda2 = MA2,      
        ayuda3 = MA3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Los marcos son estructuras en las cuales al menos un elemento esta sometido a la acción de varias fuerzas. A continuación, se presenta la solución sugerida para el ejercicio: 
        
        $\\textbf{{\\small 1. Condición de equilibrio global - Momento en D: }}$
        
        ${{\hspace{{4mm}} \\sum{{M_D}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{M_D}} = F_1 \\cdot 2d_1 + F_2 \\cdot 2d_1 - 2F_3 \\cdot d_2 + E_x \\cdot 2d_3 = 0  }}$      
        ${{\hspace{{4mm}} \\sum{{M_D}} = {f[0]:.0f} \\text{{ N}} \\cdot {2*d[0]:.0f} \\text{{ m}} + {f[1]:.0f} \\cdot {2*d[0]:.0f} \\text{{ m}} - {2*f[2]:.0f} \\text{{  N}} \\cdot {d[3]:.0f} \\text {{ m}} + E_x \\cdot {2*d[6]:.0f} \\text{{ m}} = 0 }}$     
        ${{\hspace{{4mm}} E_x \\cdot {2*d[6]:.0f} \\text{{ m}} = {2*(f[2]*d[3]- d[0]*(f[0]+f[1])):.0f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
        ${{\hspace{{4mm}} E_x = {(f[2]*d[3] - d[0]*(f[0]+f[1]))/d[6]:.2f} \\text{{ N}} }}$      
        
        $\\textbf{{\\small 2. Condición de equilibrio Elemento ACEG- Sumatoria de fuerzas en X: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_x}} = {(f[2]*d[3]- d[0]*(f[0]+f[1]))/d[6]:.2f} \\text{{ N}} + C_x = 0  }}$       
        ${{\hspace{{4mm}} C_x = {-(f[2]*d[3]- d[0]*(f[0]+f[1]))/d[6]:.2f} \\text{{ N}} }}$      

        Por lo tanto, la magnitud de la reacción $C_x$ es ${abs(-(f[2]*d[3]- d[0]*(f[0]+f[1]))/d[6]):.2f} \\text{{ N}}$.
        
        $\\textbf{{\\small 3. Condición de equilibrio Elemento ACEG - Momento en E: }}$
        
        ${{\hspace{{4mm}} \\sum{{M_E}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{M_E}} = {(f[2]*d[3]- d[0]*(f[0]+f[1]))/d[6]:.2f} \\text{{ N}} \\cdot {d[6]:.0f} \\text{{ m}} + {f[0]:.0f} \\text{{ N}} \\cdot {2*d[0]:.0f} \\text{{ m}} - {f[2]:.0f} \\text{{  N}} \\cdot {d[3]:.0f} \\text {{ m}} - C_y \\cdot {d[0]:.0f} \\text{{ m}} = 0  }}$      
        ${{\hspace{{4mm}} C_y \\cdot {d[0]:.0f} \\text{{ m}} = {(f[2]*d[3]- d[0]*(f[0]+f[1])) + 2*f[0]*d[0] - f[2]*d[3]:.2f} \\text{{ N}} \\cdot \\text {{ m}}}}$      
        ${{\hspace{{4mm}} C_y  = {((f[2]*d[3] - d[0]*(f[0]+f[1])) + 2*f[0]*d[0] - f[2]*d[3])/d[0]:.2f} \\text{{ N}} }}$      
        
        Por lo tanto, la magnitud de la reacción $C_y$ es ${abs(((f[2]*d[3] - d[0]*(f[0]+f[1])) + 2*f[0]*d[0] - f[2]*d[3])/d[0]):.2f} \\text{{ N}}$.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    #========================================================  ARMADURAS  =========================================================
    #-------------------------------------------------         Marcos      --------------------------------------------
    #-------------------------------------------------       Nivel Difícil   ---------------------------------------------------
    #-------------------------------------------------       Code: 5220011    --------------------------------------------------

    Questionary(#1_1
        code = 5230011,
        no_pregunta = 1,
        complexity = D,
        topic = "Armaduras",
        subtopic = "Marcos",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de las componentes vertical y horizontal de la reacción en el pasador B. Considere $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$, $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$, $d_3 = {d[6]:.0f} \\text{{ m}}$ y $d_4 = {d[9]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "$B_x$ [N]",
        a2_name = "$B_y$ [N]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(abs(-((f[1]*d[3])/d[6]) - (f[0]/2))/(((2*d[3])/d[6]) + ((2*d[3] + d[0])/(d[9]*2))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(abs(((-((f[1]*d[3])/d[6]) - (f[0]/2))/(((2*d[3])/d[6]) + ((2*d[3] + d[0])/(d[9]*2))))*((2*d[3])/d[6]) + (f[1]*d[3])/d[6]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = MA1,
        ayuda2 = MA2,      
        ayuda3 = MA3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Los marcos son estructuras en las cuales al menos un elemento esta sometido a la acción de varias fuerzas. A continuación, se presenta la solución sugerida para el ejercicio: 
        
        Para solucionar este ejercicio es necesario revisar ambos segmentos del Marco con el objetivo de definir un sistema de ecuaciones en función de la reacción en B. Se resalta que para cumplir con la condición de equilibrio, las reacciones sobre el pasador deben ser opuestas entre los dos elementos conectados, para esta solución se asume $B_y$ y $B_x$ positivos en AB y negativos en CB:
        
        $\\textbf{{\\small 1. Condición de equilibrio Elemento AB - Momento en A: }}$
        
        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{M_A}} = B_y \\cdot d_3 - B_x \\cdot 2d_2 - F_2 \\cdot d_2 = 0  }}$      
        ${{\hspace{{4mm}} \\sum{{M_A}} = B_y \\cdot {d[6]:.0f} \\text{{ m}} - B_x \\cdot {2*d[3] :.0f} \\text{{ m}} - {f[1]:.0f} \\text{{  N}} \\cdot {d[3] :.0f} \\text {{ m}} = 0 }}$     
        ${{\hspace{{4mm}} B_y \\cdot {d[6]:.0f} \\text{{ m}} = B_x \\cdot {2*d[3] :.0f} \\text{{ m}} + {f[1]*d[3]:.0f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
        ${{\hspace{{4mm}} B_y = B_x \\cdot {(2*d[3])/d[6] :.2f} + {(f[1]*d[3])/d[6]:.2f} \\text{{ N}} }}$      
        
        $\\textbf{{\\small 2. Condición de equilibrio Elemento CB - Momento en C: }}$
        
        ${{\hspace{{4mm}} \\sum{{M_C}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{M_C}} = B_y \\cdot 2d_4 + B_x \\cdot (2d_2 + d_1) + F_1 \\cdot d_4 = 0  }}$      
        ${{\hspace{{4mm}} \\sum{{M_C}} = B_y \\cdot {2*d[9]:.0f} \\text{{ m}} + B_x \\cdot {2*d[3] + d[0]:.0f} \\text{{ m}} + {f[0]:.0f} \\text{{  N}} \\cdot {d[9]:.0f} \\text {{ m}} = 0 }}$     
        ${{\hspace{{4mm}} B_y \\cdot {2*d[9]:.0f} \\text{{ m}} = - B_x \\cdot {2*d[3] + d[0]:.0f} \\text{{ m}} + {f[0]*d[9]:.0f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
        ${{\hspace{{4mm}} B_y = - B_x \\cdot {(2*d[3] + d[0])/(d[9]*2):.2f} - {(f[0]/2):.2f} \\text{{ N}} }}$      
        
        $\\textbf{{\\small 3. Despeje de las reacciones en B: }}$
        
        Con las anteriores ecuaciones se hallar $B_x$:
        
        ${{\hspace{{4mm}} B_x \\cdot {(2*d[3])/d[6] :.2f} + {(f[1]*d[3])/d[6]:.2f} \\text{{ N}} = - B_x \\cdot {(2*d[3] + d[0])/(d[9]*2):.2f} - {(f[0]/2):.2f} \\text{{ N}}  }}$          
        ${{\hspace{{4mm}} B_x \\cdot {((2*d[3])/d[6]) + ((2*d[3] + d[0])/(d[9]*2)):.2f} = {-((f[1]*d[3])/d[6]) - (f[0]/2) :.2f} \\text{{ N}} }}$      
        ${{\hspace{{4mm}} B_x = {(-((f[1]*d[3])/d[6]) - (f[0]/2))/(((2*d[3])/d[6]) + ((2*d[3] + d[0])/(d[9]*2))):.2f} \\text{{ N}} }}$       

        Por lo cual, la magnitud de $B_x$ es ${abs(-((f[1]*d[3])/d[6]) - (f[0]/2))/(((2*d[3])/d[6]) + ((2*d[3] + d[0])/(d[9]*2))):.2f} \\text{{ N}}$.
        
        Ahora, a partir de $B_x$ se puede encontrar $B_y$:
        
        ${{\hspace{{4mm}} B_y = B_x \\cdot {(2*d[3])/d[6] :.2f} + {(f[1]*d[3])/d[6]:.2f} \\text{{ N}} }}$      
        ${{\hspace{{4mm}} B_y = {((-((f[1]*d[3])/d[6]) - (f[0]/2))/(((2*d[3])/d[6]) + ((2*d[3] + d[0])/(d[9]*2))))*((2*d[3])/d[6]) + (f[1]*d[3])/d[6]:.2f} \\text{{ N}} }}$      
        
        Por lo cual, la magnitud de $B_y$ es ${abs(((-((f[1]*d[3])/d[6]) - (f[0]/2))/(((2*d[3])/d[6]) + ((2*d[3] + d[0])/(d[9]*2))))*((2*d[3])/d[6]) + (f[1]*d[3])/d[6]):.2f} \\text{{ N}} $.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#1_2
        code = 5230021,
        no_pregunta = 2,
        complexity = D,
        topic = "Armaduras",
        subtopic = "Marcos",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza en el elemento FD y las componentes de la fuerza ejercida sobre el segmento ABC en el pasador C. Considere $F_1 = {f[0]:.0f} \\text{{ N}}$, $d_1 = {2*d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[0]:.0f}  \\text{{ m}}$, $d_3 = {2*d[3]:.0f} \\text{{ m}}$ y $d_4 = {d[3]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Fuerza $C_x$ [N]",
        a2_name = "Fuerza $C_y$ [N]",
        a3_name = "Fuerza $F_{{FD}}$ [N]",
        answer1 = lambda f, a, calc, c, d, m: np.round((3*f[0]*(d[0]/d[3])),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(2*f[0],2),
        answer3 = lambda f, a, calc, c, d, m: np.round((f[0]*3)/((2*d[3]/Calculations.magnitude(d[0], (2*d[3])))),2),
        ayuda1 = MA1,
        ayuda2 = MA2,      
        ayuda3 = MA3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Los marcos son estructuras en las cuales al menos un elemento esta sometido a la acción de varias fuerzas. A continuación, se presenta la solución sugerida para el ejercicio: 
        
        $\\textbf{{\\small 1. Condición de equilibrio global: }}$
        
        $\\underline{{Momento \\hspace{{2mm}} en \\hspace{{2mm}} C:}}$     
        
        ${{\hspace{{4mm}} \\sum{{M_C}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{M_C}} = F_1 \\cdot (d_1 + d_2) - R_{{Ay}} \\cdot (d_1 + d_2) = 0  }}$      
        ${{\hspace{{4mm}} R_{{Ay}} = F_1 = {f[0]:.0f} \\text{{ N}} }}$      
        
        $\\underline{{Sumatoria \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} Y:}}$     
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = R_{{Ay}} + R_{{Cy}} - F_1 = 0  }}$      
        ${{\hspace{{4mm}} R_{{Cy}} = 0 }}$
        
        Es importante notar que el hecho de que $R_{{Cy}}$ sea cero no implica que en el pasador C que conecta los elementos ABC y CDE no haya reacciones. Teniendo esto en cuenta, se procede a encontrar las fuerzas que actúan en dicho pasador:
    
        $\\textbf{{\\small 2. Condición de equilibrio Elemento ABC: }}$
        
        $\\underline{{Momento \\hspace{{2mm}} en \\hspace{{2mm}} C:}}$     
        
        ${{\hspace{{4mm}} \\sum{{M_C}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{M_C}} = F_{{BD}} \\cdot \\dfrac{{d_4}}{{sqrt{{(d_2)^{{2}} + (d_4)^{{2}}}}}} \\cdot d_2 - R_{{Ay}} \\cdot (d_1 + d_2) = 0  }}$      
        ${{\hspace{{4mm}} \\sum{{M_C}} = F_{{BD}} \\cdot {d[0]*(d[3]/Calculations.magnitude(d[0],d[3])):.2f} \\text{{ m}} - {f[0]:.0f} \\text{{ N}} \\cdot {3*d[0]:.0f} \\text{{ m}} = 0 }}$     
        ${{\hspace{{4mm}} F_{{BD}} \\cdot {d[0]*(d[3]/Calculations.magnitude(d[0],d[3])):.2f} \\text{{ m}} = {f[0]*3*d[0]:.2f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
        ${{\hspace{{4mm}} F_{{BD}} = {(f[0]*3)/((d[3]/Calculations.magnitude(d[0],d[3]))):.2f} \\text{{ N}} }}$      
        
        $\\underline{{Sumatoria \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} Y:}}$     
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = R_{{Ay}} - F_{{BD}} \\cdot \\dfrac{{d_4}}{{\\sqrt{{(d_2)^{{2}} + (d_4)^{{2}}}}}} + C_y = 0  }}$      
        ${{\hspace{{4mm}} C_y = F_{{BD}} \\cdot \\dfrac{{d_4}}{{\\sqrt{{(d_2)^{{2}} + (d_4)^{{2}}}}}} - R_{{Ay}}}}$      
        ${{\hspace{{4mm}} C_y = {(f[0]*3)/((d[3]/Calculations.magnitude(d[0],d[3]))):.2f} \\cdot {(d[3]/Calculations.magnitude(d[0],d[3])):.2f} \\text{{ N}}  - {f[0]:.0f} \\text{{ N}}}}$      
        ${{\hspace{{4mm}} C_y = {2*f[0]:.2f} \\text{{ N}}}}$      

        $\\underline{{Sumatoria \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} X:}}$     
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_x}} = C_x - F_{{BD}} \\cdot \\dfrac{{d_2}}{{\\sqrt{{(d_2)^{{2}} + (d_4)^{{2}}}}}} = 0  }}$      
        ${{\hspace{{4mm}} C_x = F_{{BD}} \\cdot \\dfrac{{d_4}}{{\\sqrt{{(d_2)^{{2}} + (d_4)^{{2}}}}}} }}$      
        ${{\hspace{{4mm}} C_x = {(f[0]*3)/((d[3]/Calculations.magnitude(d[0],d[3]))):.2f} \\cdot {(d[0]/Calculations.magnitude(d[0],d[3])):.2f} \\text{{ N}}}}$      
        ${{\hspace{{4mm}} C_x = {3*f[0]*(d[0]/d[3]):.2f} \\text{{ N}}}}$           
        
        $\\textbf{{\\small 3. Condición de equilibrio Elemento EFG - Momento en E: }}$     
        
        ${{\hspace{{4mm}} \\sum{{M_G}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{M_G}} = F_1 \\cdot (d_1 + d_2) - F_{{FD}} \\cdot \\dfrac{{d_3}}{{\\sqrt{{(d_3)^{{2}} + (d_4)^{{2}}}}}} \\cdot d_2 = 0  }}$      
        ${{\hspace{{4mm}} \\sum{{M_G}} = {f[0]:.0f} \\text{{ N}} \\cdot {3*d[0]:.0f} \\text{{ m}} - F_{{FD}} \\cdot {d[0]*((2*d[3])/Calculations.magnitude(d[0], (2*d[3]))):.2f} \\text{{ m}} = 0 }}$     
        ${{\hspace{{4mm}} F_{{FD}} \\cdot {d[0]*((2*d[3])/Calculations.magnitude(d[0], (2*d[3]))):.2f} \\text{{ m}} = {f[0]*3*d[0]:.2f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
        ${{\hspace{{4mm}} F_{{FD}} = {(f[0]*3)/((2*d[3]/Calculations.magnitude(d[0], (2*d[3])))):.2f} \\text{{ N}} }}$      
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),


#========================================================  CENTROIDES  =========================================================
    #-------------------------------------------------       Centroides    --------------------------------------------
    #-------------------------------------------------       Nivel Fácil   ---------------------------------------------------
    #-------------------------------------------------       Code: 61100#1    --------------------------------------------------

    Questionary(#1_1
        code = 6110011,
        no_pregunta = 1,
        complexity = F,
        topic = "Centroides",
        subtopic = "Centroides",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Localice el centroide $\\bar{{Y}}$ del área de la sección transversal del elemento. Considere $d_1 = {d[0] + d[3]:.0f} \\text{{ cm}}$,  $d_2 = {d[3]:.0f}  \\text{{ cm}}$, $d_3 = {d[3]+1:.0f} \\text{{ cm}}$ y $d_4 = {d[6]+ 2*d[0]:.0f} \\text{{ cm}}$.",
        no_answers = 1,
        a1_name = "Distancia $\\bar{{Y}}$ $[cm]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((d[3]*(d[3]+ 2*d[0] + d[6] + 1)*((d[3]+ 2*d[0] + d[6] + 1)*(1/2) + d[3]) + (d[0] + d[3]*(1/2))*(d[3]+1)*((d[3]+1)*(1/3) + d[3]) + d[3]*(d[3]+d[0])*d[3])/(d[3]*(d[3]+d[0])*2 + (d[0] + d[3]*(1/2))*(d[3]+1) + d[3]*(d[3]+ 2*d[0] + d[6] + 1)),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = CT1,
        ayuda2 = CT2,      
        ayuda3 = CT3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El centroide se define como el centro geométrico de un objeto, en otras palabras, representa la posición promedio del área del objeto. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. División de la figura compuesta: }}$

        En el ejercicio se muestra una figura que puede segmentarse en 4 componentes con centroides comúnmente conocidos, como triángulos y rectángulos.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Partes componentes: }}$
        
        Primero se encuentra el área de cada componente y su centroide con respecto al origen:
        
        $\\underline{{Componente \\hspace{{2mm}} 1:}}$  
        
        ${{\hspace{{4mm}} A_1 = b \\cdot h = 2d_1 \\cdot d_2}}$    

        ${{\hspace{{4mm}} A_1 = {d[3]*(d[3]+d[0])*2:.2f} \\text{{ }}cm^2}}$     
             
        ${{\hspace{{4mm}} \\bar{{Y_1}} = \\dfrac{{h}}{{2}} = {d[3]/2:.2f} \\text{{ cm}}}}$                 
             
        ${{\hspace{{4mm}} A_1 \\cdot \\bar{{Y_1}} = {d[3]*(d[3]+d[0])*(d[3]):.2f} \\text{{ }}cm^3}}$                 
        
        $\\underline{{Componentes \\hspace{{2mm}} 2 \\hspace{{2mm}} y \\hspace{{2mm}} 3 :}}$  
        
        ${{\hspace{{4mm}} A_2 = A_3 = \\dfrac{{b \\cdot h}}{{2}} = \\dfrac{{ (d_1 - \\dfrac{{d_2}}{{2}}) \\cdot d_3 }}{{2}}}}$     
        
        ${{\hspace{{4mm}} A_2 = A_3 = {(d[0] + d[3]*(1/2))*(d[3]+1)*(1/2):.2f} \\text{{ }}cm^2}}$     
             
        ${{\hspace{{4mm}} \\bar{{Y_2}} = \\bar{{Y_3}} = \\dfrac{{h}}{{3}} + d_2 = {(d[3]+1)*(1/3) + d[3]:.2f} \\text{{ cm}}}}$                 
              
        ${{\hspace{{4mm}} A_2 \\cdot \\bar{{Y_2}} = A_3 \\cdot \\bar{{Y_3}} = {(d[0] + d[3]*(1/2))*(d[3]+1)*(1/2)*((d[3]+1)*(1/3) + d[3]):.2f} \\text{{ }}cm^3}}$                 
        
        $\\underline{{Componente \\hspace{{2mm}} 4:}}$  
        
        ${{\hspace{{4mm}} A_4 = b \\cdot h =  d_2 \\cdot (d_3 + d_4)}}$     
        
        ${{\hspace{{4mm}} A_4 = {d[3]*(d[3]+ 2*d[0] + d[6] + 1):.2f} \\text{{ }}cm^2}}$     
             
        ${{\hspace{{4mm}} \\bar{{Y_4}} = \\dfrac{{h}}{{2}} + d_2 = {(d[3]+ 2*d[0] + d[6] + 1)*(1/2) + d[3]:.2f} \\text{{ }}cm}}$               
             
        ${{\hspace{{4mm}} A_4 \\cdot \\bar{{Y_4}} = {d[3]*(d[3]+ 2*d[0] + d[6] + 1)*((d[3]+ 2*d[0] + d[6] + 1)*(1/2) + d[3]):.2f} \\text{{ }}cm^3}}$                 
           
        $\\textbf{{\\small 2. Determinar el centroide en Y: }}$
        
        El centroide se calcula con la ecuación $\\bar{{Y}} = \\dfrac{{\\sum{{\\bar{{Y_i}} \\cdot A_i}}}}{{\\sum{{A_i}}}}$:
        
        ${{\hspace{{4mm}} \\bar{{Y}} = \\dfrac{{\\sum{{\\bar{{Y_i}} \\cdot A_i}}}}{{\\sum{{A_i}}}} = \\dfrac{{ {d[3]*(d[3]+d[0])*d[3]:.2f} \\text{{ }}cm^3 + 2 \\cdot {(d[0] + d[3]*(1/2))*(d[3]+1)*(1/2)*((d[3]+1)*(1/3) + d[3]):.2f} \\text{{ }}cm^3 + {d[3]*(d[3]+ 2*d[0] + d[6] + 1)*((d[3]+ 2*d[0] + d[6] + 1)*(1/2) + d[3]):.2f} \\text{{ }}cm^3 }}{{{d[3]*(d[3]+d[0])*2:.2f} \\text{{ }}cm^2 + 2 \\cdot {(d[0] + d[3]*(1/2))*(d[3]+1)*(1/2):.2f} \\text{{ }}cm^2 + {d[3]*(d[3]+ 2*d[0] + d[6] + 1):.2f} \\text{{ }}cm^2}}}}$     
        
        ${{\hspace{{4mm}} \\bar{{Y}}  = \\dfrac{{{d[3]*(d[3]+ 2*d[0] + d[6] + 1)*((d[3]+ 2*d[0] + d[6] + 1)*(1/2) + d[3]) + (d[0] + d[3]*(1/2))*(d[3]+1)*((d[3]+1)*(1/3) + d[3]) + d[3]*(d[3]+d[0])*d[3]:.2f}  \\text{{ }}cm^3  }}{{{d[3]*(d[3]+d[0])*2 + (d[0] + d[3]*(1/2))*(d[3]+1) + d[3]*(d[3]+ 2*d[0] + d[6] + 1):.2f} \\text{{ }}cm^2}}}}$     
        
        ${{\hspace{{4mm}} \\bar{{Y}} = {(d[3]*(d[3]+ 2*d[0] + d[6] + 1)*((d[3]+ 2*d[0] + d[6] + 1)*(1/2) + d[3]) + (d[0] + d[3]*(1/2))*(d[3]+1)*((d[3]+1)*(1/3) + d[3]) + d[3]*(d[3]+d[0])*d[3])/(d[3]*(d[3]+d[0])*2 + (d[0] + d[3]*(1/2))*(d[3]+1) + d[3]*(d[3]+ 2*d[0] + d[6] + 1)):.2f} \\text{{ }}cm}}$     
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#2_1
        code = 6110021,
        no_pregunta = 2,
        complexity = F,
        topic = "Centroides",
        subtopic = "Centroides",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Cada uno de los tres elementos del marco tienen una masa por unidad de longitud de ${d[0]:.0f} \\dfrac{{kg}}{{m}}$. Determine la posición del centro de masa $(\\bar{{X}}, \\bar{{Y}})$ y calcule la reacción en el apoyo E. Considere $d_1 = {d[3]:.0f} \\text{{ m}}$,  $d_2 = {d[6]:.0f}  \\text{{ m}}$, $d_3 = {d[9]:.0f} \\text{{ m}}$, $d_4 = {d[12]:.0f} \\text{{ m}}$ y la aceleración debida a la gravedad $g = 9,81 \\dfrac{{m}}{{s^2}}$.",
        no_answers = 3,
        a1_name = "Distancia $\\bar{{X}}$ [m]",
        a2_name = "Distancia $\\bar{{Y}}$ [m]",
        a3_name = "Reacción $E_y$ [N]",
        answer1 = lambda f, a, calc, c, d, m: np.round((d[9]*(1/2)*(Calculations.magnitude(d[9],d[6]))*d[0] + (1/2)*d[0]*(d[9]+d[12])*(d[9]+d[12]))/(d[0]*(d[3]+d[6]) + d[0]*Calculations.magnitude(d[9],d[6]) + d[0]*(d[9]+d[12])),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((1/2)*d[0]*(d[3]+d[6])*(d[3]+d[6]) + (d[3]+d[6]*(1/2))*(Calculations.magnitude(d[9],d[6]))*d[0] + d[0]*(d[3]+d[6])*(d[9]+d[12]))/(d[0]*(d[3]+d[6]) + d[0]*Calculations.magnitude(d[9],d[6]) + d[0]*(d[9]+d[12])),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(((981/100)*(d[9]*(1/2)*(Calculations.magnitude(d[9],d[6]))*d[0] + (1/2)*d[0]*(d[9]+d[12])*(d[9]+d[12])))/(d[9]+d[12]),2),
        ayuda1 = CT4,
        ayuda2 = CT5,      
        ayuda3 = CT6,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El centro de masa es el punto en el que se considera que toda la masa de la estructura está concentrada. A continuación, se presenta la solución sugerida para el ejercicio:
        
        El marco está compuesto por tres elementos cuyos centros de masa se encuentran en el punto medio de su longitud.
        
        $\\textbf{{\\small 1. Tabulación de cálculos: }}$
        
        Teniendo en cuenta que la masa de cada elemento se calcula mediante el producto de la densidad lineal por la longitud se puede obtener la siguiente tabla:

        $Elemento$ $\\hspace{{9mm}}$ $L(m)$ $\\hspace{{18mm}}$  $M(kg)$ $\\hspace{{17mm}}$ $\\bar{{X}}(m)$ $\\hspace{{12mm}}$ $\\bar{{Y}}(m)$ $\\hspace{{16mm}}$ $\\bar{{X}} \\cdot M(kg \\cdot m)$ $\\hspace{{22mm}}$ $\\bar{{Y}} \\cdot M(kg \\cdot m)$     

        $AC$ $\\hspace{{15mm}}$ $d_1+d_2$ $\\hspace{{13mm}}$ $m^* \\cdot (d_1+d_2)$ $\\hspace{{14mm}}$ $0$ $\\hspace{{16mm}}$ $\\dfrac{{d_1+d_2}}{{2}}$ $\\hspace{{14mm}}$ $0 \\cdot m^* \\cdot (d_1+d_2)$ $\\hspace{{14mm}}$ $\\dfrac{{d_1+d_2}}{{2}} \\cdot m^2 \\cdot (d_1+d_2)$     
        $BD$ $\\hspace{{15mm}}$ $\\sqrt{{d_2^2+d_3^2}}$ $\\hspace{{9mm}}$ $m^* \\cdot \\sqrt{{d_2^2+d_3^2}}$ $\\hspace{{13mm}}$ $\\dfrac{{d_3}}{{2}}$ $\\hspace{{14mm}}$ $d_1+\\dfrac{{d_2}}{{2}}$ $\\hspace{{13mm}}$ $\\dfrac{{d_3}}{{2}} \\cdot m^* \\cdot \\sqrt{{d_2^2+d_3^2}}$ $\\hspace{{8mm}}$ $\\left(d_1+\\dfrac{{d_2}}{{2}}\\right) \\cdot m^* \\cdot \\sqrt{{d_2^2+d_3^2}}$          
        $CE$ $\\hspace{{15mm}}$ $d_3+d_4$ $\\hspace{{13mm}}$ $m^* \\cdot (d_3+d_4)$ $\\hspace{{10mm}}$ $\\dfrac{{d_3+d_4}}{{2}}$ $\\hspace{{10mm}}$ $d_1+d_2$ $\\hspace{{11mm}}$ $\\dfrac{{d_3+d_4}}{{2}} \\cdot m^* \\cdot (d_1+d_2)$ $\\hspace{{8mm}}$ $(d_1+d_2) \\cdot m^* \\cdot (d_1+d_2)$     

        Siendo m^* la masa por unidad de longitud.

        Reemplazando:

        $Elemento$ $\\hspace{{6mm}}$ $L(m)$ $\\hspace{{6mm}}$  $M(kg)$ $\\hspace{{6mm}}$ $\\bar{{X}}(m)$ $\\hspace{{6mm}}$ $\\bar{{Y}}(m)$ $\\hspace{{6mm}}$ $\\bar{{X}} \\cdot M(kg \\cdot m)$ $\\hspace{{6mm}}$ $\\bar{{Y}} \\cdot M(kg \\cdot m)$     

        $AC$ $\\hspace{{15mm}}$ ${d[3]+d[6]:.2f}$ $\\hspace{{9mm}}$ ${d[0]*(d[3]+d[6]):.2f}$ $\\hspace{{10mm}}$ $0$ $\\hspace{{15mm}}$ ${(1/2)*(d[3]+d[6]):.2f}$ $\\hspace{{12mm}}$ $0$ $\\hspace{{18mm}}$ ${(1/2)*d[0]*(d[3]+d[6])*(d[3]+d[6]):.2f}$     
        $BD$ $\\hspace{{15mm}}$ ${Calculations.magnitude(d[9],d[6]):.2f}$ $\\hspace{{9mm}}$ ${d[0]*Calculations.magnitude(d[9],d[6]):.2f}$ $\\hspace{{10mm}}$ ${d[9]*(1/2):.2f}$ $\\hspace{{10mm}}$ ${d[3]+d[6]*(1/2):.2f}$  $\\hspace{{10mm}}$ ${d[9]*(1/2)*(Calculations.magnitude(d[9],d[6]))*d[0]:.2f}$ $\\hspace{{15mm}}$ ${(d[3]+d[6]*(1/2))*(Calculations.magnitude(d[9],d[6]))*d[0]:.2f}$     
        $CE$ $\\hspace{{15mm}}$ ${d[9]+d[12]:.2f}$ $\\hspace{{9mm}}$ ${d[0]*(d[9]+d[12]):.2f}$ $\\hspace{{10mm}}$ ${(1/2)*(d[9]+d[12]):.2f}$ $\\hspace{{10mm}}$ ${(d[3]+d[6]):.2f}$ $\\hspace{{10mm}}$ ${(1/2)*d[0]*(d[9]+d[12])*(d[9]+d[12]):.2f}$ $\\hspace{{15mm}}$ ${d[0]*(d[3]+d[6])*(d[9]+d[12]):.2f}$          
        
        $\\textbf{{\\small 2. Determinar el centro de masa en X: }}$
        
        Se aplica la fórmula para determinar la coordenada $\\bar{{X}}$ :
        
        ${{\hspace{{4mm}} \\bar{{X}} = \\dfrac{{\\sum{{\\bar{{X_i}} \\cdot M_i}}}}{{\\sum{{M_i}}}}}}$     
        
        ${{\hspace{{4mm}} \\bar{{X}} = {(d[9]*(1/2)*(Calculations.magnitude(d[9],d[6]))*d[0] + (1/2)*d[0]*(d[9]+d[12])*(d[9]+d[12]))/(d[0]*(d[3]+d[6]) + d[0]*Calculations.magnitude(d[9],d[6]) + d[0]*(d[9]+d[12])):.2f} \\text{{ m}}}}$     
           
        $\\textbf{{\\small 3. Determinar el centro de masa en Y: }}$
        
        Se aplica la fórmula para determinar la coordenada $\\bar{{Y}}$ :
        
        ${{\hspace{{4mm}} \\bar{{Y}} = \\dfrac{{\\sum{{\\bar{{Y_i}} \\cdot M_i}}}}{{\\sum{{M_i}}}}}}$     
        
        ${{\hspace{{4mm}} \\bar{{Y}} = {((1/2)*d[0]*(d[3]+d[6])*(d[3]+d[6]) + (d[3]+d[6]*(1/2))*(Calculations.magnitude(d[9],d[6]))*d[0] + d[0]*(d[3]+d[6])*(d[9]+d[12]))/(d[0]*(d[3]+d[6]) + d[0]*Calculations.magnitude(d[9],d[6]) + d[0]*(d[9]+d[12])):.2f} \\text{{ m}}}}$     
        
        $\\textbf{{\\small 4. Encontrar la reacción en E: }}$
        
        E es un apoyo de tipo 1, por lo cual, tiene solo una reacción. Dado que, el peso de la estructura tiene únicamente una componente negativa en la dirección $\\hat{{j}}$ y está ubicada en el centro de masa, la reacción se puede calcular de la siguiente manera:

        ${{\hspace{{4mm}} \\sum{{M_A}} = E_y \\cdot (d_3 + d_4) -  W \\cdot \\bar{{X}} = 0}}$     
       
        ${{\hspace{{4mm}} E_y \\cdot (d_3 + d_4) - \\sum{{M_i}} \\cdot g \\cdot \\dfrac{{\\sum{{\\bar{{X_i}} \\cdot M_i}}}}{{\\sum{{M_i}}}} = 0}}$     
        
        ${{\hspace{{4mm}} E_y = \\dfrac{{ g \\cdot \\sum{{\\bar{{X_i}} \\cdot M_i}}}}{{(d_3 + d_4)}} }}$     
        
        ${{\hspace{{4mm}} E_y = {((981/100)*(d[9]*(1/2)*(Calculations.magnitude(d[9],d[6]))*d[0] + (1/2)*d[0]*(d[9]+d[12])*(d[9]+d[12])))/(d[9]+d[12]):.2f} \\text{{ N}}}}$     
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    Questionary(#3_1
        code = 6110031,
        no_pregunta = 3,
        complexity = F,
        topic = "Centroides",
        subtopic = "Centroides",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"La cercha está compuesta por 5 elementos. Determine la distancia $d_1$ en la que debe unirse el cable de izado para evitar que la armadura gire cuando es levantada. Considere $d_2 = {d[0]:.0f} \\text{{ m}}$ y $d_3 = {d[3]:.0f} \\text{{ m}}$",
        no_answers = 1,
        a1_name = "Distancia $d_1$ [m]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((d[0]*(9/4)*Calculations.magnitude(d[0]*(1/2),d[3]) + d[0]*(3/2)*d[0])/(3*Calculations.magnitude(d[0]*(1/2),d[3]) + 2*d[0]),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = CT8,
        ayuda2 = CT7,      
        ayuda3 = CT6,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El centroide se define como el centro geométrico de un objeto, en otras palabras, representa la posición promedio de la longitud, área o volumen de un objeto. A continuación, se presenta la solución sugerida para el ejercicio:
        
        La cercha está compuesta por cinco elementos cuyos centroides se encuentran en el punto medio de su longitud. Para que la cercha no gire, se debe posicionar el cable de izado en el centroide $\\bar{{X}}$ de la estructura:
        
        $\\textbf{{\\small 1. Tabulación de cálculos: }}$

        $Elemento$ $\\hspace{{13mm}}$ $L(m)$ $\\hspace{{15mm}}$ $\\bar{{X}}(m)$ $\\hspace{{15mm}}$ $\\bar{{X}} \\cdot L(m^2)$    

        $AB$ $\\hspace{{15mm}}$ ${{\\sqrt{{\\left(\\dfrac{{d_2}}{{2}}\\right)^2+d_3^2}}}}$ $\\hspace{{10mm}}$ ${{\\dfrac{{d_2}}{{4}}}}$ $\\hspace{{13mm}}$ ${{\\sqrt{{\\left(\\dfrac{{d_2}}{{2}}\\right)^2+d_3^2}} \\cdot \\dfrac{{d_2}}{{4}}}}$     
        
        $AC$ $\\hspace{{25mm}}$ ${{d_2}}$ $\\hspace{{19mm}}$ ${{\\dfrac{{d_2}}{{2}}}}$ $\\hspace{{22mm}}$ ${{d_2 \\cdot \\dfrac{{d_2}}{{2}}}}$     
        
        $BC$ $\\hspace{{15mm}}$ ${{\\sqrt{{\\left(\\dfrac{{d_2}}{{2}}\\right)^2+d_3^2}}}}$ $\\hspace{{10mm}}$ ${{\\dfrac{{3d_2}}{{4}}}}$ $\\hspace{{13mm}}$ ${{\\sqrt{{\\left(\\dfrac{{d_2}}{{2}}\\right)^2+d_3^2}} \\cdot \\dfrac{{3d_2}}{{4}}}}$     
        
        $BD$ $\\hspace{{25mm}}$ ${{d_2}}$ $\\hspace{{19mm}}$ ${{d_2}}$ $\\hspace{{22mm}}$ ${{d_2 \\cdot \\dfrac{{d_2}}{{2}}}}$     
        $CD$ $\\hspace{{15mm}}$ ${{\\sqrt{{\\left(\\dfrac{{d_2}}{{2}}\\right)^2+d_3^2}}}}$ $\\hspace{{10mm}}$ ${{\\dfrac{{5d_2}}{{4}}}}$ $\\hspace{{13mm}}$ ${{\\sqrt{{\\left(\\dfrac{{d_2}}{{2}}\\right)^2+d_3^2}} \\cdot \\dfrac{{5d_2}}{{4}}}}$
        
        Reemplazando:
        
        $Elemento$ $\\hspace{{6mm}}$ $L(m)$ $\\hspace{{7mm}}$ $\\bar{{X}}(m)$ $\\hspace{{7mm}}$ $\\bar{{X}} \\cdot L(m^2)$    

        $AB$ $\\hspace{{15mm}}$ ${Calculations.magnitude(d[0]*(1/2),d[3]):.2f}$ $\\hspace{{10mm}}$ ${d[0]*(1/4):.2f}$ $\\hspace{{13mm}}$ ${d[0]*(1/4)*Calculations.magnitude(d[0]*(1/2),d[3]):.2f}$     
        $AC$ $\\hspace{{15mm}}$ ${d[0]:.2f}$ $\\hspace{{10mm}}$ ${d[0]*(1/2):.2f}$ $\\hspace{{13mm}}$ ${d[0]*(1/2)*d[0]:.2f}$     
        $BC$ $\\hspace{{15mm}}$ ${Calculations.magnitude(d[0]*(1/2),d[3]):.2f}$ $\\hspace{{10mm}}$ ${d[0]*(3/4):.2f}$ $\\hspace{{13mm}}$ ${d[0]*(3/4)*Calculations.magnitude(d[0]*(1/2),d[3]):.2f}$     
        $BD$ $\\hspace{{15mm}}$ ${d[0]:.2f}$ $\\hspace{{10mm}}$ ${d[0]:.2f}$ $\\hspace{{13mm}}$ ${d[0]*d[0]:.2f}$     
        $CD$ $\\hspace{{15mm}}$ ${Calculations.magnitude(d[0]*(1/2),d[3]):.2f}$ $\\hspace{{10mm}}$ ${d[0]*(5/4):.2f}$ $\\hspace{{13mm}}$ ${d[0]*(5/4)*Calculations.magnitude(d[0]*(1/2),d[3]):.2f}$
        
        $\\textbf{{\\small 2. Determinar el centroide en X: }}$
        
        Se aplica la fórmula para determinar la coordenada $\\bar{{X}}$ :
        
        ${{\hspace{{4mm}} d_1 = \\bar{{X}} = \\dfrac{{\\sum{{\\bar{{X_i}} \\cdot L_i}}}}{{\\sum{{L_i}}}}}}$     
        
        ${{\hspace{{4mm}} \\bar{{X}} = {(d[0]*(9/4)*Calculations.magnitude(d[0]*(1/2),d[3]) + d[0]*(3/2)*d[0])/(3*Calculations.magnitude(d[0]*(1/2),d[3]) + 2*d[0]):.2f} \\text{{ m}}}}$       
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    #========================================================  CENTROIDES  =========================================================
    #-------------------------------------------------       Centroides    --------------------------------------------
    #-------------------------------------------------       Nivel Medio   ---------------------------------------------------
    #-------------------------------------------------       Code: 61200#1    --------------------------------------------------

    Questionary(#1_1
        code = 6120011,
        no_pregunta = 1,
        complexity = M,
        topic = "Centroides",
        subtopic = "Centroides",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"En la imagen se muestra la sección transversal de una vigueta con longitud de ${(d[0]+1)*(1/2):.2f} \\text{{ m}}$ compuesta por dos materiales. Teniendo en cuenta que la vigueta es simétrica respecto al eje X, determine la coordenada $\\bar{{Y}}$ (en cm) del centro de masa. Considere $\\rho_1 = {7700+d[3]*20:.0f} \\dfrac{{ kg}}{{m^3}}$, $\\rho_2 = {2050+d[3]*100:.0f} \\dfrac{{ kg}}{{m^3}}$, $d_1 = {40+d[6]*5:.0f} \\text{{ cm}}$,  $d_2 = {60+d[6]*4:.0f}  \\text{{ cm}}$, $d_3 = {100+d[9]*4:.0f} \\text{{ cm}}$, $d_4 = {d[9]+4:.0f} \\text{{ cm}}$ y $d_5 = {d[9]*(1/2) + 1:.2f} \\text{{ cm}}$.",
        no_answers = 1,
        a1_name = "Distancia $\\bar{{Y}}$ [cm]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((d[9]*(1/2)+1)*(1/2)*(d[9]*(1/2)+1)*(40+5*d[6])*((d[0]+1)*(1/2))*(1/10000)*(7700+d[3]*20) + ((d[9]*(1/2)+1)+(100+d[9]*4)*(1/2))*((d[9]*(1/2)+1)*(100+4*d[9])*((d[0]+1)*(1/2))*(1/10000)*(7700+d[3]*20)) + ((d[9]*(1/2)+1)*(3/2) + (100+d[9]*4))*(d[9]*(1/2)+1)*(60+d[6]*4)*((d[0]+1)*(1/2))*(1/10000)*(2050+d[3]*100) + 2*(d[9]*4+99)*(d[9]*(1/2)+1)*(d[9]+4)*((d[0]+1)*(1/2))*(1/10000)*(2050+d[3]*100))/((d[9]*(1/2)+1)*(40+5*d[6])*((d[0]+1)*(1/2))*(1/10000)*(7700+d[3]*20) + (d[9]*(1/2)+1)*(100+4*d[9])*((d[0]+1)*(1/2))*(1/10000)*(7700+d[3]*20) + (d[9]*(1/2)+1)*(60+d[6]*4)*((d[0]+1)*(1/2))*(1/10000)*(2050+d[3]*100) + 2*(d[9]*(1/2)+1)*(d[9]+4)*((d[0]+1)*(1/2))*(1/10000)*(2050+d[3]*100)),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = CT4,
        ayuda2 = CT6,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El centro de masa es el punto en el que se considera que toda la masa de la estructura está concentrada. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. División de figura compuesta: }}$
        
        Es posible dividir el perfil de la vigueta en 5 regiones, cuyos centroides son comunes y conocidos:
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Tabulación de cálculos: }}$
        
        Teniendo en cuenta que la masa de cada elemento se calcula mediante el producto de la densidad por volumen se puede obtener:
        
        $Elemento$ $\\hspace{{10mm}}$ $V(m^3)$ $\\hspace{{6mm}}$ $\\rho (kg/m^3)$ $\\hspace{{6mm}}$ $M(kg)$ $\\hspace{{25mm}}$ $\\bar{{Y}}(cm)$ $\\hspace{{40mm}}$ $\\bar{{Y}} \\cdot M(kg \\cdot cm)$     

        $\\hspace{{5mm}}$ $1$ $\\hspace{{15mm}}$ ${{d_1 \\cdot d_5 \\cdot L}}$ $\\hspace{{10mm}}$ ${{\\rho_1}}$ $\\hspace{{7mm}}$ ${{\\rho_1 \\cdot (d_1 \\cdot d_5 \\cdot L)}}$ $\\hspace{{22mm}}$ ${{\\dfrac{{d_5}}{{2}}}}$ $\\hspace{{35mm}}$ ${{\\left(\\dfrac{{d_5}}{{2}}\\right) \\cdot (\\rho_1 \\cdot (d_1 \\cdot d_5 \\cdot L)}}$     
        $\\hspace{{5mm}}$ $2$ $\\hspace{{15mm}}$ ${{d_3 \\cdot d_5 \\cdot L}}$ $\\hspace{{10mm}}$ ${{\\rho_1}}$ $\\hspace{{7mm}}$ ${{\\rho_1 \\cdot (d_3 \\cdot d_5 \\cdot L)}}$ $\\hspace{{18mm}}$ ${{d_5+\\dfrac{{d_3}}{{2}}}}$ $\\hspace{{30mm}}$ ${{\\left(d_5+\\dfrac{{d_3}}{{2}}\\right) \\cdot (\\rho_1 \\cdot (d_3 \\cdot d_5 \\cdot L)}}$     
        $\\hspace{{5mm}}$ $3$ $\\hspace{{15mm}}$ ${{d_2 \\cdot d_5 \\cdot L}}$ $\\hspace{{10mm}}$ ${{\\rho_2}}$ $\\hspace{{7mm}}$ ${{\\rho_2 \\cdot (d_2 \\cdot d_5 \\cdot L)}}$ $\\hspace{{15mm}}$ ${{d_5+d_3+\\dfrac{{d_5}}{{2}}}}$ $\\hspace{{22mm}}$ ${{\\left(d_5+d_3+\\dfrac{{d_5}}{{2}}\\right) \\cdot (\\rho_2 \\cdot (d_2 \\cdot d_5 \\cdot L)}}$     
        $\\hspace{{5mm}}$ $4$ $\\hspace{{15mm}}$ ${{d_4 \\cdot d_5 \\cdot L}}$ $\\hspace{{10mm}}$ ${{\\rho_2}}$ $\\hspace{{7mm}}$ ${{\\rho_2 \\cdot (d_4 \\cdot d_5 \\cdot L)}}$ $\\hspace{{10mm}}$ ${{d_5+(d_3-d_4)+\\dfrac{{d_4}}{{2}}}}$ $\\hspace{{13mm}}$ ${{\\left(d_5+(d_3-d_4)+\\dfrac{{d_4}}{{2}}\\right) \\cdot (\\rho_2 \\cdot (d_4 \\cdot d_5 \\cdot L)}}$     
        $\\hspace{{5mm}}$ $5$ $\\hspace{{15mm}}$ ${{d_4 \\cdot d_5 \\cdot L}}$ $\\hspace{{10mm}}$ ${{\\rho_2}}$ $\\hspace{{7mm}}$ ${{\\rho_2 \\cdot (d_4 \\cdot d_5 \\cdot L)}}$ $\\hspace{{10mm}}$ ${{d_5+(d_3-d_4)+\\dfrac{{d_4}}{{2}}}}$ $\\hspace{{13mm}}$ ${{\\left(d_5+(d_3-d_4)+\\dfrac{{d_4}}{{2}}\\right) \\cdot (\\rho_2 \\cdot (d_4 \\cdot d_5 \\cdot L)}}$    

        Siendo $L$, la longitud dada en el enunciado.

        Reemplazando:

        $Elemento$ $\\hspace{{6mm}}$ $V(m^3)$ $\\hspace{{6mm}}$ $\\rho (kg/m^3)$ $\\hspace{{6mm}}$ $M(kg)$ $\\hspace{{6mm}}$ $\\bar{{Y}}(cm)$ $\\hspace{{8mm}}$ $\\bar{{Y}} \\cdot M(kg \\cdot cm)$     

        $\\hspace{{5mm}}$ $1$ $\\hspace{{15mm}}$ ${(d[9]*(1/2)+1)*(40+5*d[6])*((d[0]+1)*(1/2))*(1/10000):.2f}$ $\\hspace{{10mm}}$ ${7700+d[3]*20:.2f}$ $\\hspace{{7mm}}$ ${(d[9]*(1/2)+1)*(40+5*d[6])*((d[0]+1)*(1/2))*(1/10000)*(7700+d[3]*20):.2f}$ $\\hspace{{10mm}}$ ${(d[9]*(1/2)+1)*(1/2):.2f}$ $\\hspace{{13mm}}$ ${(d[9]*(1/2)+1)*(1/2)*(d[9]*(1/2)+1)*(40+5*d[6])*((d[0]+1)*(1/2))*(1/10000)*(7700+d[3]*20):.2f}$     
        $\\hspace{{5mm}}$ $2$ $\\hspace{{15mm}}$ ${(d[9]*(1/2)+1)*(100+4*d[9])*((d[0]+1)*(1/2))*(1/10000):.2f}$ $\\hspace{{10mm}}$ ${7700+d[3]*20:.2f}$ $\\hspace{{7mm}}$ ${(d[9]*(1/2)+1)*(100+4*d[9])*((d[0]+1)*(1/2))*(1/10000)*(7700+d[3]*20):.2f}$ $\\hspace{{8mm}}$ ${(d[9]*(1/2)+1)+(100+d[9]*4)*(1/2):.2f}$ $\\hspace{{13mm}}$ ${((d[9]*(1/2)+1)+(100+d[9]*4)*(1/2))*((d[9]*(1/2)+1)*(100+4*d[9])*((d[0]+1)*(1/2))*(1/10000)*(7700+d[3]*20)):.2f}$     
        $\\hspace{{5mm}}$ $3$ $\\hspace{{15mm}}$ ${(d[9]*(1/2)+1)*(60+d[6]*4)*((d[0]+1)*(1/2))*(1/10000):.2f}$ $\\hspace{{10mm}}$ ${2050+d[3]*100:.2f}$ $\\hspace{{7mm}}$ ${(d[9]*(1/2)+1)*(60+d[6]*4)*((d[0]+1)*(1/2))*(1/10000)*(2050+d[3]*100):.2f}$ $\\hspace{{8mm}}$ ${(d[9]*(1/2)+1)*(3/2) + (100+d[9]*4):.2f}$ $\\hspace{{13mm}}$ ${((d[9]*(1/2)+1)*(3/2) + (100+d[9]*4))*(d[9]*(1/2)+1)*(60+d[6]*4)*((d[0]+1)*(1/2))*(1/10000)*(2050+d[3]*100):.2f}$     
        $\\hspace{{5mm}}$ $4$ $\\hspace{{15mm}}$ ${(d[9]*(1/2)+1)*(d[9]+4)*((d[0]+1)*(1/2))*(1/10000):.2f}$ $\\hspace{{10mm}}$ ${2050+d[3]*100:.2f}$ $\\hspace{{7mm}}$ ${(d[9]*(1/2)+1)*(d[9]+4)*((d[0]+1)*(1/2))*(1/10000)*(2050+d[3]*100):.2f}$ $\\hspace{{10mm}}$ ${(d[9]*4+99):.2f}$ $\\hspace{{13mm}}$ ${(d[9]*4+99)*(d[9]*(1/2)+1)*(d[9]+4)*((d[0]+1)*(1/2))*(1/10000)*(2050+d[3]*100):.2f}$     
        $\\hspace{{5mm}}$ $5$ $\\hspace{{15mm}}$ ${(d[9]*(1/2)+1)*(d[9]+4)*((d[0]+1)*(1/2))*(1/10000):.2f}$ $\\hspace{{10mm}}$ ${2050+d[3]*100:.2f}$ $\\hspace{{7mm}}$ ${(d[9]*(1/2)+1)*(d[9]+4)*((d[0]+1)*(1/2))*(1/10000)*(2050+d[3]*100):.2f}$ $\\hspace{{10mm}}$ ${(d[9]*4+99):.2f}$ $\\hspace{{13mm}}$ ${(d[9]*4+99)*(d[9]*(1/2)+1)*(d[9]+4)*((d[0]+1)*(1/2))*(1/10000)*(2050+d[3]*100):.2f}$     
           
        $\\textbf{{\\small 3. Determinar el centroide en Y: }}$
        
        Se aplica la fórmula para determinar la coordenada $\\bar{{Y}}$ :
        
        ${{\hspace{{4mm}} \\bar{{Y}} = \\dfrac{{\\sum{{\\bar{{Y_i}} \\cdot M_i}}}}{{\\sum{{M_i}}}}}}$     
        
        ${{\hspace{{4mm}} \\bar{{Y}} = {((d[9]*(1/2)+1)*(1/2)*(d[9]*(1/2)+1)*(40+5*d[6])*((d[0]+1)*(1/2))*(1/10000)*(7700+d[3]*20) + ((d[9]*(1/2)+1)+(100+d[9]*4)*(1/2))*((d[9]*(1/2)+1)*(100+4*d[9])*((d[0]+1)*(1/2))*(1/10000)*(7700+d[3]*20)) + ((d[9]*(1/2)+1)*(3/2) + (100+d[9]*4))*(d[9]*(1/2)+1)*(60+d[6]*4)*((d[0]+1)*(1/2))*(1/10000)*(2050+d[3]*100) + 2*(d[9]*4+99)*(d[9]*(1/2)+1)*(d[9]+4)*((d[0]+1)*(1/2))*(1/10000)*(2050+d[3]*100))/((d[9]*(1/2)+1)*(40+5*d[6])*((d[0]+1)*(1/2))*(1/10000)*(7700+d[3]*20) + (d[9]*(1/2)+1)*(100+4*d[9])*((d[0]+1)*(1/2))*(1/10000)*(7700+d[3]*20) + (d[9]*(1/2)+1)*(60+d[6]*4)*((d[0]+1)*(1/2))*(1/10000)*(2050+d[3]*100) + 2*(d[9]*(1/2)+1)*(d[9]+4)*((d[0]+1)*(1/2))*(1/10000)*(2050+d[3]*100)):.2f} \\text{{ cm}}}}$     
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
   
    Questionary(#2_1
        code = 6120021,
        no_pregunta = 2,
        complexity = M,
        topic = "Centroides",
        subtopic = "Centroides",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"En el marco mostrado, los elementos $AC$ y $CE$ tienen una masa por unidad de longitud de $m_1 = {d[0]:.0f} \\dfrac{{kg}}{{m}}$, mientras que el elemento $BD$ una masa por unidad de longitud de $m_2 = {d[3]:.0f} \\dfrac{{kg}}{{m}}$. Ubique la posición del centro de masa $(\\bar{{X}}, \\bar{{Y}})$ y calcule la reacción a momento en el punto A. Considere los siguientes datos: $d_1 = {d[6]:.0f} \\text{{ m}}$,  $d_2 = {d[9]:.0f}  \\text{{ m}}$, $d_3 = {d[12]:.0f} \\text{{ m}}$, $d_4 = {d[15]:.0f} \\text{{ m}}$, $d_5 = {d[18]:.0f} \\text{{ m}}$ y la aceleración debida a la gravedad $g = 9,81 \\dfrac{{m}}{{s^2}}$.",
        no_answers = 3,
        a1_name = "Distancia $\\bar{{X}}$ $[m]$",
        a2_name = "Distancia $\\bar{{Y}}$ $[m]$",
        a3_name = "Reacción $M_A$ $[N \\cdot m]$",
        answer1 = lambda f, a, calc, c, d, m: np.round(((d[18]+d[15])*(1/2)*d[0]*Calculations.magnitude((d[12]+d[15]),(d[18]+d[15])) + (1/2)*(d[18])*d[3]*Calculations.magnitude((d[12]+d[9]),d[18]))/(d[0]*(d[9]+d[6])+d[0]*Calculations.magnitude((d[12]+d[15]),(d[18]+d[15]))+d[3]*Calculations.magnitude((d[12]+d[9]),d[18])),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((1/2)*d[0]*(d[9]+d[6])*(d[9]+d[6]) + (d[6]+d[9]+(d[12]+d[15])*(1/2))*d[0]*Calculations.magnitude((d[12]+d[15]),(d[18]+d[15])) + (d[6]+(d[9]+d[12])*(1/2))*d[3]*Calculations.magnitude((d[12]+d[9]),d[18]))/(d[0]*(d[9]+d[6])+d[0]*Calculations.magnitude((d[12]+d[15]),(d[18]+d[15]))+d[3]*Calculations.magnitude((d[12]+d[9]),d[18])),2),
        answer3 = lambda f, a, calc, c, d, m: np.round((981/100)*((d[18]+d[15])*(1/2)*d[0]*Calculations.magnitude((d[12]+d[15]),(d[18]+d[15])) + (1/2)*(d[18])*d[3]*Calculations.magnitude((d[12]+d[9]),d[18])),2),
        ayuda1 = CT4,
        ayuda2 = CT6,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El centro de masa es el punto en el que se considera que toda la masa de la estructura está concentrada. A continuación, se presenta la solución sugerida para el ejercicio:
        
        El marco está compuesto por tres elementos cuyos centros de masa se encuentran en el punto medio de su longitud.
        
        $\\textbf{{\\small 1. Tabulación de cálculos: }}$
        
        Teniendo en cuenta que la masa de cada elemento se calcula mediante el producto de la densidad por volumen se puede obtener:
        
        $Elemento$ $\\hspace{{6mm}}$ $L(m)$ $\\hspace{{6mm}}$ $\\rho (kg/m)$ $\\hspace{{6mm}}$ $M(kg)$ $\\hspace{{6mm}}$ $\\bar{{X}}(m)$ $\\hspace{{6mm}}$ $\\bar{{Y}}(m)$ $\\hspace{{6mm}}$ $\\bar{{X}} \\cdot M(kg \\cdot m)$ $\\hspace{{6mm}}$ $\\bar{{Y}} \\cdot M(kg \\cdot m)$     

        $AC$ $\\hspace{{15mm}}$ ${d[9]+d[6]:.2f}$ $\\hspace{{10mm}}$ ${d[0]:.2f}$ $\\hspace{{9mm}}$ ${d[0]*(d[9]+d[6]):.2f}$ $\\hspace{{10mm}}$ $0$ $\\hspace{{15mm}}$ ${(1/2)*(d[9]+d[6]):.2f}$ $\\hspace{{12mm}}$ $0$ $\\hspace{{18mm}}$ ${(1/2)*d[0]*(d[9]+d[6])*(d[9]+d[6]):.2f}$     
        $CE$ $\\hspace{{15mm}}$ ${Calculations.magnitude((d[12]+d[15]),(d[18]+d[15])):.2f}$ $\\hspace{{10mm}}$ ${d[0]:.2f}$ $\\hspace{{9mm}}$ ${d[0]*Calculations.magnitude((d[12]+d[15]),(d[18]+d[15])):.2f}$ $\\hspace{{10mm}}$ ${(d[18]+d[15])*(1/2):.2f}$ $\\hspace{{10mm}}$ ${d[6]+d[9]+(d[12]+d[15])*(1/2):.2f}$  $\\hspace{{10mm}}$ ${(d[18]+d[15])*(1/2)*d[0]*Calculations.magnitude((d[12]+d[15]),(d[18]+d[15])):.2f}$ $\\hspace{{11mm}}$ ${(d[6]+d[9]+(d[12]+d[15])*(1/2))*d[0]*Calculations.magnitude((d[12]+d[15]),(d[18]+d[15])):.2f}$     
        $BD$ $\\hspace{{15mm}}$ ${Calculations.magnitude((d[12]+d[9]),d[18]):.2f}$ $\\hspace{{10mm}}$ ${d[3]:.2f}$ $\\hspace{{8mm}}$ ${d[3]*Calculations.magnitude((d[12]+d[9]),d[18]):.2f}$ $\\hspace{{10mm}}$ ${(1/2)*(d[18]):.2f}$ $\\hspace{{10mm}}$ ${d[6]+(d[9]+d[12])*(1/2):.2f}$ $\\hspace{{10mm}}$ ${(1/2)*(d[18])*d[3]*Calculations.magnitude((d[12]+d[9]),d[18]):.2f}$ $\\hspace{{15mm}}$ ${(d[6]+(d[9]+d[12])*(1/2))*d[3]*Calculations.magnitude((d[12]+d[9]),d[18]):.2f}$          
        
        $\\textbf{{\\small 2. Determinar el centroide en X: }}$
        
        Se aplica la fórmula para determinar la coordenada $\\bar{{X}}$ :
        
        ${{\hspace{{4mm}} \\bar{{X}} = \\dfrac{{\\sum{{\\bar{{X_i}} \\cdot M_i}}}}{{\\sum{{M_i}}}}}}$     
        ${{\hspace{{4mm}} \\bar{{X}} = {((d[18]+d[15])*(1/2)*d[0]*Calculations.magnitude((d[12]+d[15]),(d[18]+d[15])) + (1/2)*(d[18])*d[3]*Calculations.magnitude((d[12]+d[9]),d[18]))/(d[0]*(d[9]+d[6])+d[0]*Calculations.magnitude((d[12]+d[15]),(d[18]+d[15]))+d[3]*Calculations.magnitude((d[12]+d[9]),d[18])):.2f} \\text{{ m}}}}$     
           
        $\\textbf{{\\small 3. Determinar el centroide en Y: }}$
        
        Se aplica la fórmula para determinar la coordenada $\\bar{{Y}}$ :
        
        ${{\hspace{{4mm}} \\bar{{Y}} = \\dfrac{{\\sum{{\\bar{{Y_i}} \\cdot M_i}}}}{{\\sum{{M_i}}}}}}$     
        ${{\hspace{{4mm}} \\bar{{Y}} = {((1/2)*d[0]*(d[9]+d[6])*(d[9]+d[6]) + (d[6]+d[9]+(d[12]+d[15])*(1/2))*d[0]*Calculations.magnitude((d[12]+d[15]),(d[18]+d[15])) + (d[6]+(d[9]+d[12])*(1/2))*d[3]*Calculations.magnitude((d[12]+d[9]),d[18]))/(d[0]*(d[9]+d[6])+d[0]*Calculations.magnitude((d[12]+d[15]),(d[18]+d[15]))+d[3]*Calculations.magnitude((d[12]+d[9]),d[18])):.2f} \\text{{ m}}}}$     
        
        $\\textbf{{\\small 4. Encontrar reacción en A: }}$
        
        El punto A corresponde a un apoyo de grado 3, por lo que tiene 3 reacciones, sin embargo, en el enunciado solo se solicita la reacción a momento. Considerando que el peso de la estructura actúa en la dirección negativa de $\\hat{{j}}$ y que está aplicado en el centro de masa, dicho momento se determina como:
        
        ${{\hspace{{4mm}} \\sum{{M_A}} = M_A -  W \\cdot \\bar{{X}} = 0}}$     
        ${{\hspace{{4mm}} M_A = g \\cdot \\bar{{X}} \\cdot \\sum{{M_i}} }}$     
        ${{\hspace{{4mm}} M_A = {(981/100)*((d[18]+d[15])*(1/2)*d[0]*Calculations.magnitude((d[12]+d[15]),(d[18]+d[15])) + (1/2)*(d[18])*d[3]*Calculations.magnitude((d[12]+d[9]),d[18])):.2f} \\text{{ N}} \\cdot \\text{{ m}}}}$     
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    #========================================================  CENTROIDES  =========================================================
    #-------------------------------------------------       Centroides    --------------------------------------------
    #-------------------------------------------------       Nivel Díficil   ---------------------------------------------------
    #-------------------------------------------------       Code: 61300#1    --------------------------------------------------

    Questionary(#1_1
        code = 6130011,
        no_pregunta = 1,
        complexity = D,
        topic = "Centroides",
        subtopic = "Centroides",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"En la imagen se muestra el perfil de un elemento con un ancho constante de ${26+d[0]:.0f} \\text{{ cm}}$ compuesto por dos materiales. Ubique la posición del centro de masa $(\\bar{{X}}, \\bar{{Y}})$. Considere $\\rho_1 = {7700+d[3]*20:.0f} \\dfrac{{ kg}}{{m^3}}$, $\\rho_2 = {2750+d[3]*100:.0f} \\dfrac{{ kg}}{{m^3}}$, $d_1 = {45+d[6]:.0f} \\text{{ cm}}$,  $d_2 = {30+d[9]:.0f}  \\text{{ cm}}$, $d_3 = {50+d[12]:.0f} \\text{{ cm}}$, $d_4 = {24+d[15]:.0f} \\text{{ cm}}$, $d_5 = {10+(d[6]-d[15])*(1/2):.2f} \\text{{ cm}}$ y $d_6 = {46+d[18]:.2f} \\text{{ cm}}$.",
        no_answers = 2,
        a1_name = "Distancia $\\bar{{Y}}$ [cm]",
        a2_name = "Distancia $\\bar{{X}}$ [cm]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((1/1000000)*(96+d[12]+d[18])*(91+d[18]+d[6])*(26+d[0])*(2750+d[3]*100)*(30+d[9]+(96+d[12]+d[18])*(1/2))+(1/1000000)*(1/2)*(30+d[9])*(46+d[18])*(26+d[0])*(2750+d[3]*100)*(2/3)*(30+d[9])+(1/2)*(30+d[9])*(1/1000000)*(45+d[6])*(30+d[9])*(26+d[0])*(7700+d[3]*20)+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(7700+d[3]*20)*((30+d[9])-(2*(24+d[15]))/(3*math.pi))+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(2750+d[3]*100)*((30+d[9])+(2*(24+d[15]))/(3*math.pi))+(-1/1000000)*((math.pi*(46+d[18])**2)/4)*(26+d[0])*(2750+d[3]*100)*(126+d[9]+d[12]+d[18]-(4*(46+d[18]))/(3*math.pi)))/((1/1000000)*(96+d[12]+d[18])*(91+d[18]+d[6])*(26+d[0])*(2750+d[3]*100)+(1/1000000)*(1/2)*(30+d[9])*(46+d[18])*(26+d[0])*(2750+d[3]*100)+(1/1000000)*(45+d[6])*(30+d[9])*(26+d[0])*(7700+d[3]*20)+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(7700+d[3]*20)+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(2750+d[3]*100)+(-1/1000000)*((math.pi*(46+d[18])**2)/4)*(26+d[0])*(2750+d[3]*100)),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((1/1000000)*(96+d[12]+d[18])*(91+d[18]+d[6])*(26+d[0])*(2750+d[3]*100)*((91+d[6]+d[18])*(1/2))+(1/1000000)*(1/2)*(30+d[9])*(46+d[18])*(26+d[0])*(2750+d[3]*100)*(45+d[6]+(1/3)*(46+d[18]))+(1/2)*(45+d[6])*(1/1000000)*(45+d[6])*(30+d[9])*(26+d[0])*(7700+d[3]*20)+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(7700+d[3]*20)*(22+d[6]*(1/2))+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(2750+d[3]*100)*(22+d[6]*(1/2))+(-1/1000000)*((math.pi*(46+d[18])**2)/4)*(26+d[0])*(2750+d[3]*100)*(45+d[6]+46+d[18]-(4*(46+d[18]))/(3*math.pi)))/((1/1000000)*(96+d[12]+d[18])*(91+d[18]+d[6])*(26+d[0])*(2750+d[3]*100)+(1/1000000)*(1/2)*(30+d[9])*(46+d[18])*(26+d[0])*(2750+d[3]*100)+(1/1000000)*(45+d[6])*(30+d[9])*(26+d[0])*(7700+d[3]*20)+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(7700+d[3]*20)+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(2750+d[3]*100)+(-1/1000000)*((math.pi*(46+d[18])**2)/4)*(26+d[0])*(2750+d[3]*100)),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = CT4,
        ayuda2 = CT6,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El centro de masa es el punto en el que se considera que toda la masa de la estructura está concentrada. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. División de figura compuesta: }}$

        Es posible dividir el perfil en 6 elementos para calcular el centro de masa. Este se puede obtener a partir de la suma de los elementos 1, 2 y 3 restando la suma de los elementos 4, 5 y 6:
        """,
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Tabulación de cálculos: }}$
        
        Teniendo en cuenta que la masa de cada elemento se calcula mediante el producto de la densidad por volumen se puede obtener:
        
        $Elemento$ $\\hspace{{6mm}}$ $V(m^3)$ $\\hspace{{6mm}}$ $\\rho (kg/m^3)$ $\\hspace{{7mm}}$ $M(kg)$ $\\hspace{{7mm}}$ $\\bar{{X}}(cm)$ $\\hspace{{6mm}}$ $\\bar{{Y}}(cm)$ $\\hspace{{8mm}}$ $\\bar{{X}} \\cdot M(kg \\cdot cm)$ $\\hspace{{6mm}}$ $\\bar{{Y}} \\cdot M(kg \\cdot cm)$     

        $1$ $\\hspace{{15mm}}$ ${(1/1000000)*(96+d[12]+d[18])*(91+d[18]+d[6])*(26+d[0]):.3f}$ $\\hspace{{11mm}}$ ${2750+d[3]*100:.2f}$ $\\hspace{{10mm}}$ ${(1/1000000)*(96+d[12]+d[18])*(91+d[18]+d[6])*(26+d[0])*(2750+d[3]*100):.2f}$ $\\hspace{{9mm}}$ ${30+d[9]+(96+d[12]+d[18])*(1/2):.2f}$ $\\hspace{{10mm}}$ ${(91+d[6]+d[18])*(1/2):.2f}$ $\\hspace{{13mm}}$ ${(1/1000000)*(96+d[12]+d[18])*(91+d[18]+d[6])*(26+d[0])*(2750+d[3]*100)*(30+d[9]+(96+d[12]+d[18])*(1/2)):.2f}$ $\\hspace{{13mm}}$ ${(1/1000000)*(96+d[12]+d[18])*(91+d[18]+d[6])*(26+d[0])*(2750+d[3]*100)*((91+d[6]+d[18])*(1/2)):.2f}$     
        $2$ $\\hspace{{15mm}}$ ${(1/1000000)*(1/2)*(30+d[9])*(46+d[18])*(26+d[0]):.3f}$ $\\hspace{{11mm}}$ ${2750+d[3]*100:.2f}$ $\\hspace{{10mm}}$ ${(1/1000000)*(1/2)*(30+d[9])*(46+d[18])*(26+d[0])*(2750+d[3]*100):.2f}$ $\\hspace{{12mm}}$ ${(2/3)*(30+d[9]):.2f}$ $\\hspace{{10mm}}$ ${45+d[6]+(1/3)*(46+d[18]):.2f}$ $\\hspace{{13mm}}$ ${(1/1000000)*(1/2)*(30+d[9])*(46+d[18])*(26+d[0])*(2750+d[3]*100)*(2/3)*(30+d[9]):.2f}$ $\\hspace{{15mm}}$ ${(1/1000000)*(1/2)*(30+d[9])*(46+d[18])*(26+d[0])*(2750+d[3]*100)*(45+d[6]+(1/3)*(46+d[18])):.2f}$     
        $3$ $\\hspace{{15mm}}$ ${(1/1000000)*(45+d[6])*(30+d[9])*(26+d[0]):.3f}$ $\\hspace{{11mm}}$ ${7700+d[3]*20:.2f}$ $\\hspace{{10mm}}$ ${(1/1000000)*(45+d[6])*(30+d[9])*(26+d[0])*(7700+d[3]*20):.2f}$ $\\hspace{{10mm}}$ ${(1/2)*(30+d[9]):.2f}$ $\\hspace{{10mm}}$ ${(1/2)*(45+d[6]):.2f}$ $\\hspace{{13mm}}$ ${(1/2)*(30+d[9])*(1/1000000)*(45+d[6])*(30+d[9])*(26+d[0])*(7700+d[3]*20):.2f}$ $\\hspace{{15mm}}$ ${(1/2)*(45+d[6])*(1/1000000)*(45+d[6])*(30+d[9])*(26+d[0])*(7700+d[3]*20):.2f}$     
        $4$ $\\hspace{{15mm}}$ ${(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0]):.3f}$ $\\hspace{{9mm}}$ ${7700+d[3]*20:.2f}$ $\\hspace{{10mm}}$ ${(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(7700+d[3]*20):.2f}$ $\\hspace{{8mm}}$ ${(30+d[9])-(2*(24+d[15]))/(3*math.pi):.2f}$ $\\hspace{{10mm}}$ ${22+d[6]*(1/2):.2f}$ $\\hspace{{13mm}}$ ${(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(7700+d[3]*20)*((30+d[9])-(2*(24+d[15]))/(3*math.pi)):.2f}$ $\\hspace{{13mm}}$ ${(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(7700+d[3]*20)*(22+d[6]*(1/2)):.2f}$     
        $5$ $\\hspace{{15mm}}$ ${(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0]):.3f}$ $\\hspace{{9mm}}$ ${2750+d[3]*100:.2f}$ $\\hspace{{10mm}}$ ${(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(2750+d[3]*100):.2f}$ $\\hspace{{8mm}}$ ${(30+d[9])+(2*(24+d[15]))/(3*math.pi):.2f}$ $\\hspace{{10mm}}$ ${22+d[6]*(1/2):.2f}$ $\\hspace{{13mm}}$ ${(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(2750+d[3]*100)*((30+d[9])+(2*(24+d[15]))/(3*math.pi)):.2f}$ $\\hspace{{13mm}}$ ${(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(2750+d[3]*100)*(22+d[6]*(1/2)):.2f}$     
        $6$ $\\hspace{{15mm}}$ ${(-1/1000000)*((math.pi*(46+d[18])**2)/4)*(26+d[0]):.3f}$ $\\hspace{{9mm}}$ ${2750+d[3]*100:.2f}$ $\\hspace{{10mm}}$ ${(-1/1000000)*((math.pi*(46+d[18])**2)/4)*(26+d[0])*(2750+d[3]*100):.2f}$ $\\hspace{{6mm}}$ ${126+d[9]+d[12]+d[18]-(4*(46+d[18]))/(3*math.pi):.2f}$ $\\hspace{{9mm}}$ ${45+d[6]+46+d[18]-(4*(46+d[18]))/(3*math.pi):.2f}$ $\\hspace{{13mm}}$ ${(-1/1000000)*((math.pi*(46+d[18])**2)/4)*(26+d[0])*(2750+d[3]*100)*(126+d[9]+d[12]+d[18]-(4*(46+d[18]))/(3*math.pi)):.2f}$ $\\hspace{{11mm}}$ ${(-1/1000000)*((math.pi*(46+d[18])**2)/4)*(26+d[0])*(2750+d[3]*100)*(45+d[6]+46+d[18]-(4*(46+d[18]))/(3*math.pi)):.2f}$    
           
        $\\textbf{{\\small 3. Determinar el centroide en X: }}$
        
        Se aplica la fórmula para determinar la coordenada $\\bar{{X}}$ :
        
        ${{\hspace{{4mm}} \\bar{{X}} = \\dfrac{{\\sum{{\\bar{{X_i}} \\cdot M_i}}}}{{\\sum{{M_i}}}}}}$     
       
        ${{\hspace{{4mm}} \\bar{{X}} = {((1/1000000)*(96+d[12]+d[18])*(91+d[18]+d[6])*(26+d[0])*(2750+d[3]*100)*(30+d[9]+(96+d[12]+d[18])*(1/2))+(1/1000000)*(1/2)*(30+d[9])*(46+d[18])*(26+d[0])*(2750+d[3]*100)*(2/3)*(30+d[9])+(1/2)*(30+d[9])*(1/1000000)*(45+d[6])*(30+d[9])*(26+d[0])*(7700+d[3]*20)+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(7700+d[3]*20)*((30+d[9])-(2*(24+d[15]))/(3*math.pi))+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(2750+d[3]*100)*((30+d[9])+(2*(24+d[15]))/(3*math.pi))+(-1/1000000)*((math.pi*(46+d[18])**2)/4)*(26+d[0])*(2750+d[3]*100)*(126+d[9]+d[12]+d[18]-(4*(46+d[18]))/(3*math.pi)))/((1/1000000)*(96+d[12]+d[18])*(91+d[18]+d[6])*(26+d[0])*(2750+d[3]*100)+(1/1000000)*(1/2)*(30+d[9])*(46+d[18])*(26+d[0])*(2750+d[3]*100)+(1/1000000)*(45+d[6])*(30+d[9])*(26+d[0])*(7700+d[3]*20)+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(7700+d[3]*20)+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(2750+d[3]*100)+(-1/1000000)*((math.pi*(46+d[18])**2)/4)*(26+d[0])*(2750+d[3]*100)):.2f} \\text{{ cm}}}}$     
        
        $\\textbf{{\\small 4. Determinar el centroide en Y: }}$
        
        Se aplica la fórmula para determinar la coordenada $\\bar{{Y}}$ :
        
        ${{\hspace{{4mm}} \\bar{{Y}} = \\dfrac{{\\sum{{\\bar{{Y_i}} \\cdot M_i}}}}{{\\sum{{M_i}}}}}}$     
        
        ${{\hspace{{4mm}} \\bar{{Y}} = {((1/1000000)*(96+d[12]+d[18])*(91+d[18]+d[6])*(26+d[0])*(2750+d[3]*100)*((91+d[6]+d[18])*(1/2))+(1/1000000)*(1/2)*(30+d[9])*(46+d[18])*(26+d[0])*(2750+d[3]*100)*(45+d[6]+(1/3)*(46+d[18]))+(1/2)*(45+d[6])*(1/1000000)*(45+d[6])*(30+d[9])*(26+d[0])*(7700+d[3]*20)+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(7700+d[3]*20)*(22+d[6]*(1/2))+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(2750+d[3]*100)*(22+d[6]*(1/2))+(-1/1000000)*((math.pi*(46+d[18])**2)/4)*(26+d[0])*(2750+d[3]*100)*(45+d[6]+46+d[18]-(4*(46+d[18]))/(3*math.pi)))/((1/1000000)*(96+d[12]+d[18])*(91+d[18]+d[6])*(26+d[0])*(2750+d[3]*100)+(1/1000000)*(1/2)*(30+d[9])*(46+d[18])*(26+d[0])*(2750+d[3]*100)+(1/1000000)*(45+d[6])*(30+d[9])*(26+d[0])*(7700+d[3]*20)+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(7700+d[3]*20)+(-1/1000000)*((math.pi*(((24+d[15])/2))**2)/2)*(26+d[0])*(2750+d[3]*100)+(-1/1000000)*((math.pi*(46+d[18])**2)/4)*(26+d[0])*(2750+d[3]*100)):.2f} \\text{{ cm}}}}$     
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),


    #=================================================  FUERZAS DISTRIBUIDAS =========================================================
    #-------------------------------------------------       Vigas    --------------------------------------------
    #-------------------------------------------------       Nivel Fácil   ---------------------------------------------------
    #-------------------------------------------------       Code: 71100#1    --------------------------------------------------
    Questionary(#1_1
        code = 7110011,
        no_pregunta = 1,
        complexity = F,
        topic = FD,
        subtopic = "Vigas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Reemplace la carga distribuida por una fuerza resultante equivalente y especifique su ubicación medida desde el punto A. Considere $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$, $w_1 = {100+m[0]:.0f} \\dfrac{{N}}{{m}}$ y $w_2 = {m[1]:.0f} \\dfrac{{N}}{{m}}$.",
        no_answers = 2,
        a1_name = "Magnitud fuerza resultante $|F_R|$ $[N]$",
        a2_name = "Distancia desde el punto A $[m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((100+m[0])*d[0]+((100+m[0]-m[1])*d[3])/2+m[1]*d[3]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((100+m[0])*d[0]*d[0]*(1/2) + ((100+m[0]-m[1])*d[3])*(1/2)*(d[0]+d[3]/3) + m[1]*d[3]*(d[0]+d[3]/2))/((100+m[0])*d[0]+((100+m[0]-m[1])*d[3])/2+m[1]*d[3]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = FD1,
        ayuda2 = FD2,
        ayuda3 = FD3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una fuerza distribuida es una carga que actúa sobre una superficie o a lo largo de un segmento, en lugar de estar concentrada en un solo punto. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. División de fuerza distribuida: }}$

        En el ejercicio se muestra una fuerza distribuida que puede dividirse en 3 distribuciones más simples, cuyos centroides son conocidos y comunes, como triángulos y rectángulos.      
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        
        $\\textbf{{\\small 2. Puntualización de las fuerzas: }}$
        
        Teniendo en cuenta la configuración mostrada, se puede determinar la ubicación de las tres fuerzas.
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"""
        La magnitud de cada una de las fuerzas se calcula de la siguiente forma:
        
        ${{\hspace{{4mm}} F_1 = w_1 \\cdot d_1}}$     
        ${{\hspace{{4mm}} F_2 = \\dfrac{{(w_1 - w_2) \\cdot d_2}}{{2}}}}$         
        ${{\hspace{{4mm}} F_3 = w_2 \\cdot d_2}}$     
            
        $\\textbf{{\\small 3. Magnitud y ubicación de fuerza resultante: }}$
        
        La fuerza resultante será la sumatoria de las tres fuerzas puntuales encontradas:
        
        ${{\hspace{{4mm}} F_R = F_1 + F_2 + F_3}}$     
        ${{\hspace{{4mm}} F_R = {(100+m[0])*d[0]+((100+m[0]-m[1])*d[3])/2+m[1]*d[3]:.2f} \\text{{ N}}}}$
        
        Con este resultado se puede realizar sumatoria de momentos en A para determinar la ubicación de la fuerza resultante, medida desde A. Esto equivale a hallar el centroide de la fuerza distribuida:

        ${{\hspace{{4mm}} \\sum{{M_A}} = - d \\cdot F_R}}$     
        ${{\hspace{{4mm}} - d \\cdot F_R = - F_1 \\cdot \\dfrac{{d_1}}{{2}} - F_2 \\cdot (d_1 + \\dfrac{{d_2}}{{3}}) - F_3 \\cdot (d_1 + \\dfrac{{d_2}}{{2}})}}$     
        ${{\hspace{{4mm}} - d \\cdot {(100+m[0])*d[0]+((100+m[0]-m[1])*d[3])/2+m[1]*d[3]:.2f} \\text{{ N}} = {-(100+m[0])*d[0]*d[0]*(1/2):.2f} \\text{{ N}} \\cdot \\text{{ m}} - {((100+m[0]-m[1])*d[3])*(1/2)*(d[0]+d[3]/3):.2f} \\text{{ N}} \\cdot \\text{{ m}} - {m[1]*d[3]*(d[0]+d[3]/2):.2f}\\text{{ N}} \\cdot \\text{{ m}}}}$     
        ${{\hspace{{4mm}} d = {((100+m[0])*d[0]*d[0]*(1/2) + ((100+m[0]-m[1])*d[3])*(1/2)*(d[0]+d[3]/3) + m[1]*d[3]*(d[0]+d[3]/2))/((100+m[0])*d[0]+((100+m[0]-m[1])*d[3])/2+m[1]*d[3]):.2f} \\text{{ m}}}}$     
        """,
        calculos='operations'
        ),
    
    Questionary(#2_1
        code = 7110021,
        no_pregunta = 2,
        complexity = F,
        topic = FD,
        subtopic = "Vigas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine el valor de $w_2$ de modo que la restricción de rotación (momento de reacción) en el apoyo sea igual a cero. Considere $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$ y $w_1 = {f[0]:.0f} \\dfrac{{N}}{{m}}$.",
        no_answers = 1,
        a1_name = "$w_2$ $\\left[\\dfrac{{N}}{{m}}\\right]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[0]*d[0]*(1/6)*d[0])/(d[3]*(1/2)*(d[0]+d[3]*(1/3))),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = FD1,
        ayuda2 = FD2,
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una fuerza distribuida es una carga que actúa sobre una superficie o a lo largo de un segmento, en lugar de estar concentrada en un solo punto. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Puntualización de las fuerzas: }}$
        
        Con la configuración mostrada, se puede determinar la ubicación de las dos fuerzas resultantes:
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        Las magnitudes de cada fuerza son:
        
        ${{\hspace{{4mm}} F_1 = \\dfrac{{w_1 \\cdot d_1}}{{2}}}}$     
       
        ${{\hspace{{4mm}} F_2 = \\dfrac{{w_2 \\cdot d_2}}{{2}}}}$            
            
        $\\textbf{{\\small 2. Sumatoria de momentos en A: }}$
        
        Dado que no debe haber restricción de rotación en el apoyo, la sumatoria de momentos en A debe ser igual a cero. Esto permite determinar el valor de $w_2$:

        ${{\hspace{{4mm}} \\sum{{M_A}} = F_2 \\cdot (d_1 + \\dfrac{{d_2}}{{3}}) - F_1 \\cdot \\dfrac{{d_1}}{{3}} = 0}}$      
        
        ${{\hspace{{4mm}} \\dfrac{{w_2 \\cdot d_2}}{{2}} \\cdot (d_1 + \\dfrac{{d_2}}{{3}}) = \\dfrac{{w_1 \\cdot d_1}}{{2}} \\cdot \\dfrac{{d_1}}{{3}}}}$     
       
        ${{\hspace{{4mm}} w_2 \\cdot {d[3]*(1/2)*(d[0]+d[3]*(1/3)):.2f} \\text{{ }} m^2 = {f[0]*d[0]*(1/6)*d[0]:.2f} \\text{{ N}} \\cdot \\text{{ m}}}}$     
        
        ${{\hspace{{4mm}} w_2 = {(f[0]*d[0]*(1/6)*d[0])/(d[3]*(1/2)*(d[0]+d[3]*(1/3))):.2f} \\dfrac{{N}}{{m}}}}$     
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
   
    Questionary(#3_1
        code = 7110031,
        no_pregunta = 3,
        complexity = F,
        topic = FD,
        subtopic = "Vigas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las reacciones en los apoyos $A$ y $B$. Considere $d_1 = {d[6]:.0f} \\text{{ m}}$, $d_2 = {d[9]*2:.0f}  \\text{{ m}}$, $d_3 = {(d[6]/2)+1:.1f} \\text{{ m}}$, $w_1 = {f[1]:.0f} \\dfrac{{N}}{{m}}$ y $w_2 = {f[2]+10:.0f} \\dfrac{{N}}{{m}}$ .",
        no_answers = 3,
        a1_name = "Reacción $A_x$ $[N]$",
        a2_name = "Reacción $A_y$ $[N]$",
        a3_name = "Reacción $B_y$ $[N]$",
        answer1 = lambda f, a, calc, c, d, m: np.round(0,2),
        answer2 = lambda f, a, calc, c, d, m: np.round((f[1]*d[6]/2)+(((f[2]+10)*(d[9]*2)))/2+(f[2]+10)*(1+(d[6]/2))-(-f[1]*d[6]*(d[6]/(3*d[9]*2)) + (f[2]+10)*d[9]*2*(1/3)+(f[2]+10)*((d[6]/2)+1)*(1+(((d[6]/2)+1)/(2*d[9]*2)))),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(-f[1]*d[6]*(d[6]/(3*d[9]*2)) + (f[2]+10)*d[9]*2*(1/3)+(f[2]+10)*((d[6]/2)+1)*(1+(((d[6]/2)+1)/(2*d[9]*2))),2),
        ayuda1 = FD1,
        ayuda2 = FD2,
        ayuda3 = FD3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una fuerza distribuida es una carga que actúa sobre una superficie o a lo largo de un segmento, en lugar de estar concentrada en un solo punto. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. División de fuerza distribuida: }}$
        
        En el ejercicio se muestra una fuerza distribuida que puede dividirse en 3 distribuciones más simples, cuyos centroides son conocidos y comunes, como triángulos y rectángulos.  
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Puntualización de las fuerzas: }}$
        
        Teniendo en cuenta la configuración mostrada, se puede determinar la ubicación de las tres fuerzas.
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"""
        La magnitud de cada una de las fuerzas se calcula de la siguiente forma:
        
        ${{\hspace{{4mm}} F_1 = \\dfrac{{w_1 \\cdot d_1}}{{2}}}}$     
        
        ${{\hspace{{4mm}} F_2 = \\dfrac{{w_2 \\cdot d_2}}{{2}}}}$         
        
        ${{\hspace{{4mm}} F_3 = w_2 \\cdot d_3}}$     
            
        $\\textbf{{\\small 3. Condición de equilibrio: }}$
        
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} momentos \\hspace{{2mm}} en \\hspace{{2mm}} A:}}$  
        
        ${{\hspace{{4mm}} \\sum{{M_A}} = F_1 \\cdot \\dfrac{{2d_1}}{{3}} - F_2 \\cdot \\dfrac{{2d_2}}{{3}} - F_3 \\cdot (d_2 + \\dfrac{{d_3}}{{2}}) + B_y \\cdot d_2 = 0 }}$     
        
        ${{\hspace{{4mm}} B_y \\cdot d_2 =  - F_1 \\cdot \\dfrac{{2d_1}}{{3}} + F_2 \\cdot \\dfrac{{2d_2}}{{3}} + F_3 \\cdot (d_2 + \\dfrac{{d_3}}{{2}})}}$     
        
        ${{\hspace{{4mm}} B_y =  - w_1 \\cdot d_1 \\cdot \\dfrac{{d_1}}{{3d_2}} + w_2 \\cdot d_2 \\cdot \\dfrac{{1}}{{3}} + w_2 \\cdot d_3 \\cdot (1 + \\dfrac{{d_3}}{{2d_2}})}}$     
        
        ${{\hspace{{4mm}} B_y = {-f[1]*d[6]*(d[6]/(3*d[9]*2)) + (f[2]+10)*d[9]*2*(1/3)+(f[2]+10)*((d[6]/2)+1)*(1+(((d[6]/2)+1)/(2*d[9]*2))):.2f} \\text{{ N}}}}$     
        
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} X:}}$ 
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = A_x = 0 }}$     
                
        $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} Y:}}$  
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = B_y + A_y - F_1 - F_2 - F_3 = 0 }}$     
       
        ${{\hspace{{4mm}} A_y =  F_1 + F_2 + F_3 - B_y}}$     
        
        ${{\hspace{{4mm}} A_y = \\dfrac{{w_1 \\cdot d_1}}{{2}} + \\dfrac{{w_2 \\cdot d_2}}{{2}} + w_2 \\cdot d_3 + w_1 \\cdot d_1 \\cdot \\dfrac{{d_1}}{{3d_2}} - w_2 \\cdot d_2 \\cdot \\dfrac{{1}}{{3}} - w_2 \\cdot d_3 \\cdot (1 + \\dfrac{{d_3}}{{2d_2}})}}$     
        
        ${{\hspace{{4mm}} A_y = {(f[1]*d[6]/2)+(((f[2]+10)*(d[9]*2)))/2+(f[2]+10)*(1+(d[6]/2))-(-f[1]*d[6]*(d[6]/(3*d[9]*2)) + (f[2]+10)*d[9]*2*(1/3)+(f[2]+10)*((d[6]/2)+1)*(1+(((d[6]/2)+1)/(2*d[9]*2)))):.2f} \\text{{ N}}}}$     
        """,
        calculos='operations'
        ),
    

    #=================================================  FUERZAS DISTRIBUIDAS =========================================================
    #-------------------------------------------------       Vigas    --------------------------------------------
    #-------------------------------------------------       Nivel Medio   ---------------------------------------------------
    #-------------------------------------------------       Code: 71200#1    --------------------------------------------------
    
    Questionary(#1_1
        code = 7120011,
        no_pregunta = 1,
        complexity = M,
        topic = FD,
        subtopic = "Vigas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Encuentre las reacciones en los apoyos teniendo en cuenta que $W_1 = {m[0]:.0f} \\dfrac{{kN}}{{m}}$, $W_2 = {m[0]+5:.0f}\\dfrac{{kN}}{{m}}$, $W_3 = {m[2]:.0f}\\dfrac{{kN}}{{m}}$, $F={f[0]:.0f} \\text{{ kN}}$ y $d_0 = {d[0]:.0f} \\text{{ m}}$, $d_1 = {d[3]:.0f}\\text{{ m}}$ y $d_2 = {d[6]:.0f}\\text{{ m}}$. Adicionalmente, considere que la fuerza $F$ esta siendo aplicada en centro de su sección.",
        no_answers = 3,
        a1_name = "Reacción $A_x$ $[kN]$",
        a2_name = "Reacción $A_y$ $[kN]$",
        a3_name = "Reacción $B_y$ $[kN]$",
        answer1 = lambda f, a, calc, c, d, m: 0,
        answer2 = lambda f, a, calc, c, d, m: np.round(((m[0]*d[0])/2)+(m[0]*d[3])+((m[0]+5-m[0])*d[3]/2)+(m[2]*d[6])+f[0]-(((m[0]*d[0])/2)*(2*d[0]/3)+(m[0]*d[3])*(d[0]+(d[3]/2))+((m[0]+5-m[0])*(d[3]/2))*(d[0]+(2*d[3]/3))+f[0]*(d[0]+d[3]+((d[3]/2)/2))+((m[2]*d[6])*(d[0]+d[3]+(d[3]/2)+(d[6]/2))))/(d[0]+d[3]+(d[3]/2)+d[6]),2),
        answer3 = lambda f, a, calc, c, d, m: np.round((((m[0]*d[0])/2)*(2*d[0]/3)+(m[0]*d[3])*(d[0]+(d[3]/2))+((m[0]+5-m[0])*(d[3]/2))*(d[0]+(2*d[3]/3))+f[0]*(d[0]+d[3]+((d[3]/2)/2))+((m[2]*d[6])*(d[0]+d[3]+(d[3]/2)+(d[6]/2))))/(d[0]+d[3]+(d[3]/2)+d[6]),2),
        ayuda1 = FD1,
        ayuda2 = FD2,      
        ayuda3 = FD4,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una fuerza distribuida es una carga que actúa sobre una superficie o a lo largo de un segmento, en lugar de estar concentrada en un solo punto. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. División de fuerza distribuida: }}$

        En el ejercicio se muestra una fuerza distribuida que puede dividirse en 3 distribuciones más simples, cuyos centroides son conocidos y comunes, como triángulos y rectángulos.      
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Puntualización de las fuerzas: }}$
        
        Teniendo en cuenta la configuración mostrada, se puede determinar la ubicación de las tres fuerzas.
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"""
        La magnitud de cada una de las fuerzas se calcula de la siguiente forma:
        
        ${{\hspace{{4mm}} F_1 = \\dfrac{{W_1 \\cdot d_0}}{{2}} }}$    
        ${{\hspace{{4mm}} F_1 = {(m[0]*d[0])/2:.2f} \\text{{ kN}}}}$    
          
        ${{\hspace{{4mm}} F_2 = W_1 \\cdot d_1 }}$    
        ${{\hspace{{4mm}} F_2 = {m[0]*d[3]:.2f} \\text{{ kN}}}}$    
         
        ${{\hspace{{4mm}} F_3 = \\dfrac{{(W_2-W_1) \\cdot d_1}}{{2}} }}$    
        ${{\hspace{{4mm}} F_3 = {(m[0]+5-m[0])*d[3]/2:.2f} \\text{{ kN}}}}$    
            
        ${{\hspace{{4mm}} F_4 = W_3 \\cdot d_2 }}$    
        ${{\hspace{{4mm}} F_4 = {m[2]*d[6]:.2f} \\text{{ kN}}}}$    
          

        $\\textbf{{\\small 3. Cálculo de las reacciones en los apoyos: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = A_x = 0 }}$     
        ${{\hspace{{4mm}} A_x = 0 }}$

        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$      
        ${{\hspace{{4mm}} \\sum{{M_A}} = -F_1 \\cdot \\dfrac{{2d_0}}{{3}} - F_2 \\cdot (d_0 + \\dfrac{{d_1}}{{2}}) - F_3 \\cdot (d_0 + \\dfrac{{2d_1}}{{3}}) - F_4 \\cdot (d_0 + \\dfrac{{3 \\cdot d_1}}{{2}} + \\dfrac{{d_2}}{{2}}) - F(d_0 + \\dfrac{{5 \\cdot d_1}}{{4}}) + B_y \\cdot (d_0 + \\dfrac{{3 \\cdot d_1}}{{2}} + d_2) = 0 }}$      
        ${{\hspace{{4mm}} B_y = \\dfrac{{F_1 \\cdot \\dfrac{{2d_0}}{{3}} + F_2 \\cdot (d_0 + \\dfrac{{d_1}}{{2}}) + F_3 \\cdot (d_0 + \\dfrac{{2d_1}}{{3}}) + F_4 \\cdot (d_0 + \\dfrac{{3 \\cdot d_1}}{{2}} + \\dfrac{{d_2}}{{2}}) + F(d_0 + \\dfrac{{5 \\cdot d_1}}{{4}})}}{{d_0 + \\dfrac{{3 \\cdot d_1}}{{2}} + d_2}}}}$       
        ${{\hspace{{4mm}} B_y ={(((m[0]*d[0])/2)*(2*d[0]/3)+(m[0]*d[3])*(d[0]+(d[3]/2))+((m[0]+5-m[0])*(d[3]/2))*(d[0]+(2*d[3]/3))+f[0]*(d[0]+d[3]+((d[3]/2)/2))+((m[2]*d[6])*(d[0]+d[3]+(d[3]/2)+(d[6]/2))))/(d[0]+d[3]+(d[3]/2)+d[6]):.2f} \\text{{ kN}}}}$      

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$       
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + B_y - F_1 - F_2 - F_3 - F_4 = 0}}$       
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y = F_1 + F_2 + F_3 + F_4 - B_y}}$             
        ${{\hspace{{4mm}} A_y = {((m[0]*d[0])/2)+(m[0]*d[3])+((m[0]+5-m[0])*d[3]/2)+(m[2]*d[6])+f[0]-(((m[0]*d[0])/2)*(2*d[0]/3)+(m[0]*d[3])*(d[0]+(d[3]/2))+((m[0]+5-m[0])*(d[3]/2))*(d[0]+(2*d[3]/3))+f[0]*(d[0]+d[3]+((d[3]/2)/2))+((m[2]*d[6])*(d[0]+d[3]+(d[3]/2)+(d[6]/2))))/(d[0]+d[3]+(d[3]/2)+d[6]):.2f} \\text{{ kN}}}}$
        """,
        calculos='operations'
    ),

    Questionary(#2_1
        code = 7120011,
        no_pregunta = 2,
        complexity = M,
        topic = FD,
        subtopic = "Vigas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"La carga distribuida sobre la viga se describe mediante la función $y = c \\cdot \\sqrt{{x}}$, determine la fuerza generada por esta carga, y la posición sobre la viga donde se aplica dicha fuerza. Considere que $d_0 = {d[0]:.0f} \\text{{ m}}$ y $c = {d[3]:.0f}$.",
        no_answers = 2,
        a1_name = "Fuerza total $[N]$",
        a2_name = "Centroide de la carga distribuida $[m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(2*d[3]*(d[0])**(3/2)/3,2),
        answer2 = lambda f, a, calc, c, d, m: np.round(3*d[0]/5,2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = FD5,
        ayuda2 = FD6,      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una fuerza distribuida es una carga que actúa sobre una superficie o a lo largo de un segmento, en lugar de estar concentrada en un solo punto. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Fuerza: }}$

        La fuerza corresponde al área bajo la curva de la integral.
        
        ${{\hspace{{4mm}} F = \\int_{0}^{d[0]} {d[3]:.0f}\\sqrt{{x}} \\text{{ }}dx }}$     
        
        ${{\hspace{{4mm}} F = {d[3]:.0f}\\left[ \\dfrac{{2}}{{3}} x^{{3/2}} \\right]_{0}^{d[0]} }}$          
        
        ${{\hspace{{4mm}} F = {(2*d[3]*(d[0])**(3/2))/3:.2f} \\text{{ N}} }}$

        $\\textbf{{\\small 2. Centroide: }}$

        El centroide se calcula con la siguiente expresión: $\\dfrac{{\\int x \\cdot dA \\text{{ }}}}{{\\int dA \\text{{ }}}}$

        ${{\hspace{{4mm}} \\bar{{x}} = \\dfrac{{\\int_{0}^{d[0]} x \\cdot {d[3]:.0f}\\sqrt{{x}} \\text{{ }} dx}}{{\\int_{0}^{d[0]} {d[3]:.0f}\\sqrt{{x}} \\text{{ }}}} }}$      
        
        ${{\hspace{{4mm}} \\bar{{x}} = \\dfrac{{{d[3]:.0f}\\left[ \\dfrac{2}{5} x^{{5/2}} \\right]_{0}^{d[0]}}}{{{d[3]:.0f}\\left[ \\dfrac{2}{3} x^{{3/2}} \\right]_{0}^{d[0]}}} }}$            
        
        ${{\hspace{{4mm}} \\bar{{x}} = {(3*d[0])/5}  \\text{{ m}} }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
   

    #=================================================  FUERZAS DISTRIBUIDAS =========================================================
    #-------------------------------------------------       Vigas    --------------------------------------------
    #-------------------------------------------------       Nivel Díficil   ---------------------------------------------------
    #-------------------------------------------------       Code: 71300#1    --------------------------------------------------

    Questionary(#1_1
        code = 7130011,
        no_pregunta = 1,
        complexity = D,
        topic = FD,
        subtopic = "Vigas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Encuentre las reacciones en los apoyos. Considere que la primera carga distribuida se comporta como la función $y = c \\cdot x^3$ y sus unidades son $\\dfrac{{kN}}{{m}}$, $c = {d[9]:.0f}$, $F = {f[0]:.0f} \\text{{ kN}}$, $W_1 = {m[0]:.0f} \\dfrac{{kN}}{{m}}$ y $d_0 = {d[0]:.0f} \\text{{ m}}$, $d_1 = {d[3]:.0f} \\text{{ m}}$ y $d_2 = {d[6]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Reacción $A_x$ $[kN]$",
        a2_name = "Reacción $A_y$ $[kN]$",
        a3_name = "Reacción $B_y$ $[kN]$",
        answer1 = lambda f, a, calc, c, d, m: np.round(0,2),
        answer2 = lambda f, a, calc, c, d, m: np.round((f[0])+((d[9]*d[0]**4)/4)+(m[0]*d[6])-((d[9]*d[0]**5)/5+f[0]*(d[0]+d[3])+m[0]*d[6]*(d[0]+d[3]+d[6]/2))/(d[0]+d[3]+d[6]),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(((d[9]*d[0]**5)/5+f[0]*(d[0]+d[3])+m[0]*d[6]*(d[0]+d[3]+d[6]/2))/(d[0]+d[3]+d[6]),2),
        ayuda1 = FD1,
        ayuda2 = FD2,      
        ayuda3 = FD4,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una fuerza distribuida es una carga que actúa sobre una superficie o a lo largo de un segmento, en lugar de estar concentrada en un solo punto. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Fuerzas y centroides: }}$

        Teniendo en cuenta la configuración mostrada, se puede determinar la magnitud de las cargas distribuidas y su ubicación sobre la viga.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\underline{{Carga \\text{{ }} distribuida \\text{{ }} con \\text{{ }} función:}}$ 

        ${{\hspace{{4mm}} F_1 = \\int_{0}^{d[0]} {d[9]:.0f} \\cdot x^3 \\text{{}} dx }}$       
        ${{\hspace{{4mm}} F_1 = {(d[9]*d[0]**4)/4} \\text{{ kN}} }}$ 

        ${{\hspace{{4mm}} \\bar{{x_1}} = \\dfrac{{\\int_{0}^{d[0]} x \\cdot cx^3 \\text{{}} dx}}{{\\int_{0}^{d[0]} c \\cdot x^3 \\text{{}} dx}} }}$           
        ${{\hspace{{4mm}} \\bar{{x_1}} = {(4*d[0])/5} \\text{{ m}}}}$

        $\\underline{{Carga \\text{{ }} distribuida \\text{{ }} uniforme:}}$ 

        ${{\hspace{{4mm}} F_2 = W_1 \\cdot d_2 }}$      
        ${{\hspace{{4mm}} F_2 = {m[0]*d[6]} \\text{{ kN}}}}$     

        ${{\hspace{{4mm}} \\bar{{x_2}} = \\dfrac{{d_2}}{{2}} }}$       
        ${{\hspace{{4mm}} \\bar{{x_2}} = {d[6]/2} \\text{{ m}}}}$

        $\\textbf{{\\small 2. Cálculo de las reacciones en los apoyos: }}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = A_x = 0 }}$     
        ${{\hspace{{4mm}} A_x = 0 }}$

        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$   

        ${{\hspace{{4mm}} -F_1 \\cdot \\bar{{x_1}} - F_2 \\cdot (d_0 + d_1 + \\bar{{x_2}}) - F(d_0 + d_1) + B_y \\cdot (d_0 + d_1 + d_2) = 0 }}$      
        
        ${{\hspace{{4mm}} B_y = \\dfrac{{F_1 \\cdot \\bar{{x_1}} + F_2 \\cdot (d_0 + d_1 + \\bar{{x_2}}) + F(d_0 + d_1)}}{{(d_0 + d_1 + d_2)}}}}$     
        
        ${{\hspace{{4mm}} B_y ={((d[9]*d[0]**5)/5+f[0]*(d[0]+d[3])+m[0]*d[6]*(d[0]+d[3]+d[6]/2))/(d[0]+d[3]+d[6]):.2F} \\text{{ kN}}}}$     

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$       
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + B_y - F_1 - F_2 - F = 0}}$      
        ${{\hspace{{4mm}} A_y = F_1 + F_2 + F - B_y}}$     
        ${{\hspace{{4mm}} A_y = {(f[0])+((d[9]*d[0]**4)/4)+(m[0]*d[6])-((d[9]*d[0]**5)/5+f[0]*(d[0]+d[3])+m[0]*d[6]*(d[0]+d[3]+d[6]/2))/(d[0]+d[3]+d[6]):.2f} \\text{{ kN}}}}$
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ), 
    
    Questionary(#2_1
        code = 7130021,
        no_pregunta = 2,
        complexity = D,
        topic = FD,
        subtopic = "Vigas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Encuentre las reacciones en los apoyos. Considere que $W_1 = {m[0]:.0f} \\dfrac{{kN}}{{m}}$, $W_2 = {m[0]-3:.0f}\\dfrac{{kN}}{{m}}$, $W_3 = {m[0]-1:.0f}\\dfrac{{kN}}{{m}}$ y $d_0 = {d[0]:.0f} \\text{{ m}}$, $d_1 = {d[3]:.0f} \\text{{ m}}$, $d_2 = {d[6]:.0f} \\text{{ m}}$, $d_3 = {d[9]:.0f} \\text{{ m}}$ y $d_4 = {d[12]:.0f} \\text{{ m}}$.",
        no_answers = 3,
        a1_name = "Reacción $A_x$ $[kN]$",
        a2_name = "Reacción $A_y$ $[kN]$",
        a3_name = "Reacción $B_y$ $[kN]$",
        answer1 = lambda f, a, calc, c, d, m: np.round(0,2),
        answer2 = lambda f, a, calc, c, d, m: np.round((m[0]-3)*(d[0]+d[3]+d[6]+d[9]+d[12])+(3*d[0])+(3*d[3]/2)+(m[0]-1-(m[0]-3))*d[9]/2+(m[0]-1-(m[0]-3))*d[12]/2-(((((m[0]-3)*(d[0]+d[3]+d[6]+d[9]+d[12]))*((d[0]+d[3]+d[6]+d[9]+d[12])/2))+(((3)*d[0])*(d[0]/2))+(((3)*d[3]/2)*(d[0]+(d[3]/3)))+(((m[0]-1-(m[0]-3))*d[9]/2)*(d[0]+d[3]+d[6]+((2*d[9])/3)))+(((m[0]-1-(m[0]-3))*d[12]/2)*(d[0]+d[3]+d[6]+d[9]+(d[12]/3))))/(d[0]+d[3]+d[6]+d[9]+d[12])),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(((((m[0]-3)*(d[0]+d[3]+d[6]+d[9]+d[12]))*((d[0]+d[3]+d[6]+d[9]+d[12])/2))+(((3)*d[0])*(d[0]/2))+(((3)*d[3]/2)*(d[0]+(d[3]/3)))+(((m[0]-1-(m[0]-3))*d[9]/2)*(d[0]+d[3]+d[6]+((2*d[9])/3)))+(((m[0]-1-(m[0]-3))*d[12]/2)*(d[0]+d[3]+d[6]+d[9]+(d[12]/3))))/(d[0]+d[3]+d[6]+d[9]+d[12]),2),
        ayuda1 = FD3,
        ayuda2 = FD7,      
        ayuda3 = FD4,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una fuerza distribuida es una carga que actúa sobre una superficie o a lo largo de un segmento, en lugar de estar concentrada en un solo punto. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. División de fuerza distribuida: }}$

        En el ejercicio se muestra una fuerza distribuida que puede dividirse en 3 distribuciones más simples, cuyos centroides son conocidos y comunes, como triángulos y rectángulos.      
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Puntualización de las fuerzas y centroides: }}$
        
        Teniendo en cuenta la configuración mostrada, se puede determinar la ubicación de las fuerzas.
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"""
        $\\underline{{Fuerza \\text{{ }} 1:}}$ 

        ${{\hspace{{4mm}} F_1 = W_2 \\cdot (d_0 + d_1 + d_2 + d_3 + d_4) }}$     
        ${{\hspace{{4mm}} F_1 = {(m[0]-3)*(d[0]+d[3]+d[6]+d[9]+d[12])} \\text{{ kN}}}}$     
        ${{\hspace{{4mm}} \\bar{{x_1}} = \\dfrac{{(d_0 + d_1 + d_2 + d_3 + d_4)}}{{2}} }}$     
        ${{\hspace{{4mm}} \\bar{{x_1}} = {(d[0]+d[3]+d[6]+d[9]+d[12])/2:.2f} \\text{{ m}}}}$

        $\\underline{{Fuerza \\text{{ }} 2:}}$ 

        ${{\hspace{{4mm}} F_2 = (W_1 - W_2) \\cdot d_0 }}$     
        ${{\hspace{{4mm}} F_2 = {(3)*d[0]} \\text{{ kN}}}}$      
        ${{\hspace{{4mm}} \\bar{{x_2}} = \\dfrac{{d_0}}{{2}} }}$      
        ${{\hspace{{4mm}} \\bar{{x_2}} = {d[0]/2:.2f} \\text{{ m}}}}$

        $\\underline{{Fuerza \\text{{ }} 3:}}$ 

        ${{\hspace{{4mm}} F_3 = \\dfrac{{(W_1 - W_2) \\cdot d_1}}{{2}} }}$      
        ${{\hspace{{4mm}} F_3 = {(3)*d[3]/2} \\text{{ kN}}}}$        
        ${{\hspace{{4mm}} \\bar{{x_3}} = \\dfrac{{d_1}}{{3}} }}$       
        ${{\hspace{{4mm}} \\bar{{x_3}} = {d[3]/3:.2f} \\text{{ m}}}}$

        $\\underline{{Fuerza \\text{{ }} 4:}}$ 

        ${{\hspace{{4mm}} F_4 = \\dfrac{{(W_3 - W_2) \\cdot d_3}}{{2}} }}$       
        ${{\hspace{{4mm}} F_4 = {(m[0]-1-(m[0]-3))*d[9]/2} \\text{{ kN}}}}$        
        ${{\hspace{{4mm}} \\bar{{x_4}} = \\dfrac{{2 \\cdot d_3}}{{3}} }}$      
        ${{\hspace{{4mm}} \\bar{{x_4}} = {(2*d[9])/3:.2f} \\text{{ m}}}}$  

        $\\underline{{Fuerza \\text{{ }} 5:}}$ 

        ${{\hspace{{4mm}} F_5 = \\dfrac{{(W_3 - W_2) \\cdot d_4}}{{2}} }}$       
        ${{\hspace{{4mm}} F_5 = {(m[0]-1-(m[0]-3))*d[12]/2} \\text{{ kN}}}}$       
        ${{\hspace{{4mm}} \\bar{{x_5}} = \\dfrac{{d_4}}{{3}} }}$     
        ${{\hspace{{4mm}} \\bar{{x_5}} = {d[12]/3:.2f} \\text{{ m}}}}$

        $\\textbf{{\\small 3. Cálculo de las reacciones en los apoyos:}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = A_x = 0 }}$     
        ${{\hspace{{4mm}} A_x = 0 }}$

        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$
        ${{\hspace{{4mm}} \\sum{{M_A}} = -F_1 \\cdot \\bar{{x_1}} - F_2 \\cdot \\bar{{x_2}} - F_3 \\cdot (d_0 + \\bar{{x_3}}) - F_4 \\cdot (d_0 + d_1 + d_2 + \\bar{{x_4}}) - F_5 \\cdot (d_0 + d_1 + d_2 + d_3 + \\bar{{x_5}}) + B_y \\cdot (d_0 + d_1 + d_2 + d_3 + d_4) = 0 }}$
        
        ${{\hspace{{4mm}} B_y = \\dfrac{{F_1 \\cdot \\bar{{x_1}} + F_2 \\cdot \\bar{{x_2}} + F_3 \\cdot (d_0 + \\bar{{x_3}}) + F_4 \\cdot (d_0 + d_1 + d_2 + \\bar{{x_4}}) + F_5 \\cdot (d_0 + d_1 + d_2 + d_3 + \\bar{{x_5}})}}{{d_0 + d_1 + d_2 + d_3 + d_4}}}}$     
        ${{\hspace{{4mm}} B_y ={((((m[0]-3)*(d[0]+d[3]+d[6]+d[9]+d[12]))*((d[0]+d[3]+d[6]+d[9]+d[12])/2))+(((3)*d[0])*(d[0]/2))+(((3)*d[3]/2)*(d[0]+(d[3]/3)))+(((m[0]-1-(m[0]-3))*d[9]/2)*(d[0]+d[3]+d[6]+((2*d[9])/3)))+(((m[0]-1-(m[0]-3))*d[12]/2)*(d[0]+d[3]+d[6]+d[9]+(d[12]/3))))/(d[0]+d[3]+d[6]+d[9]+d[12]):.2f} \\text{{ kN}}}}$      
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$       
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + B_y - F_1 - F_2 - F_3 - F_4 - F_5 = 0}}$      
        ${{\hspace{{4mm}} A_y = F_1 + F_2 + F_3 + F_4 + F_5 - B_y}}$      
        ${{\hspace{{4mm}} A_y = {(m[0]-3)*(d[0]+d[3]+d[6]+d[9]+d[12])+(3*d[0])+(3*d[3]/2)+(m[0]-1-(m[0]-3))*d[9]/2+(m[0]-1-(m[0]-3))*d[12]/2-(((((m[0]-3)*(d[0]+d[3]+d[6]+d[9]+d[12]))*((d[0]+d[3]+d[6]+d[9]+d[12])/2))+(((3)*d[0])*(d[0]/2))+(((3)*d[3]/2)*(d[0]+(d[3]/3)))+(((m[0]-1-(m[0]-3))*d[9]/2)*(d[0]+d[3]+d[6]+((2*d[9])/3)))+(((m[0]-1-(m[0]-3))*d[12]/2)*(d[0]+d[3]+d[6]+d[9]+(d[12]/3))))/(d[0]+d[3]+d[6]+d[9]+d[12])):.2f} \\text{{ kN}}}}$
        """,
        calculos='operations'
        ),


    #=================================================  FUERZAS DISTRIBUIDAS =========================================================
    #-------------------------------------------------       Presión hidrostática    --------------------------------------------
    #-------------------------------------------------       Nivel Fácil   ---------------------------------------------------
    #-------------------------------------------------       Code: 72100#1    --------------------------------------------------
    
    Questionary(#1_1
        code = 7210011,
        no_pregunta = 1,
        complexity = F,
        topic = FD,
        subtopic = "Presión hidrostática",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza hidrostática resultante que actúa sobre la presa y su ubicación medida desde la base. Considere que el ancho de la presa $a = {d[0]:.0f} \\text{{ m}}$, la densidad del agua $\\rho = 1000 \\dfrac{{kg}}{{m^3}}$, la aceleración debida a la gravedad $g = 9,81 \\dfrac{{m}}{{s^2}}$ y $d_1 = {d[0]+5:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Magnitud fuerza hidrostática $|F_R|$ $[kN]$",
        a2_name = "Ubicación fuerza hidrostática $(\\bar{{y}})$ $[m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((9810*(d[0]+5))*((d[0]+5)*(d[0])))/2000, 2),
        answer2 = lambda f, a, calc, c, d, m: np.round((1/3)*(d[0]+5), 2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = PH1,
        ayuda2 = PH2,
        ayuda3 = PH3,
        respuesta_P1 = lambda fa, a, calc, c, d, m: f"""
        La presión hidrostática es la presión ejercida por un fluido en reposo. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Distribución de la fuerza hidrostática: }}$

        En este caso, la presión hidrostática se distribuye de forma lineal, aumentando con la profundidad.
        """,
        respuesta_P2 = lambda fa, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Cálculo de la fuerza hidrostática resultante:}}$

        La fuerza resultante debida a una distribución lineal (triangular) de presión hidrostática sobre una superficie se calcula mediante:    

        $F_R = \\dfrac{{P \\cdot d_1 \\cdot a}}{{2}}$     
        
        ${{\hspace{{4mm}} P = \\rho \\cdot g \\cdot d_1 }}$      
        
        ${{\hspace{{4mm}} P = 1000 \\dfrac{{kg}}{{m^3}} \\cdot 9,81 \\dfrac{{m}}{{s^2}} \\cdot {d[0]+5:.0f} \\text{{ m}} }}$      
        
        ${{\hspace{{4mm}} P = {9810*(d[0]+5):.2f}  \\dfrac{{N}}{{m^2}} }}$ 

        ${{\hspace{{4mm}} F_R = \\dfrac{{P \\cdot h \\cdot a}}{{2}}}}$      
        
        ${{\hspace{{4mm}} F_R = {((9810*(d[0]+5))*((d[0]+5)*(d[0])))/2000:.2f} \\text{{ kN}} }}$ 

        $\\textbf{{\\small 3. Ubicación de la fuerza hidrostática resultante desde la base:}}$

        La presión hidrostática se distribuye de forma triangular, por lo tanto, su ubicación desde la base es a $\\dfrac{{1}}{{3}}$ de la distancia $d_1$:

        ${{\hspace{{4mm}} \\bar{{y}} = \\dfrac{{1}}{{3}}d_1}}$        
        
        ${{\hspace{{4mm}} \\bar{{y}} = {(1/3)*(d[0]+5):.2f} \\text{{ m}} }}$ 
        """,
        respuesta_P3 = lambda fa, a, calc, c, d, m: f"",
        calculos = 'operations',
        ),

    Questionary(#2_1
        code = 7210021,
        no_pregunta = 2,
        complexity = F,
        topic = FD,
        subtopic = "Presión hidrostática",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"""
        Considere la presa de concreto mostrada en la figura. Para determinar su seguridad frente al volcamiento, calcule el momento resistente $(M_R)$ generado por el peso de la presa, y el momento actuante $(M_A)$ producido por la fuerza hidrostática del agua con respecto al punto $A$. Utilice los siguientes datos: el ancho de la presa $a = {d[3]:.0f} \\text{{ m}}$, la densidad del agua $\\rho_a = 1000 \\dfrac{{kg}}{{m^3}}$, la densidad del concreto $\\rho = 2500 \\dfrac{{kg}}{{m^3}}$, la aceleración debida a la gravedad $g = 9,81 \\dfrac{{m}}{{s^2}}$, $d_1 = {d[0]+5:.0f} \\text{{ m}}$ y $d_2 = {d[0]:.0f} \\text{{ m}}$.
        
        La presa será segura frente al volcamiento si el momento resistente es mayor que el momento actuante. De lo contrario, se considerará insegura.
        """,
        no_answers = 2,
        a1_name = "Momento resistente $(M_R)$ $[kN \\cdot m]$",
        a2_name = "Momento actuante $(M_A)$ $[kN \\cdot m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((2500*9.81*(d[0]+5)*(d[0])*(d[3])/2000)*((2/3)*(d[0])), 2),
        answer2 = lambda f, a, calc, c, d, m: np.round((((9810*(d[0]+5))*((d[0]+5)*(d[3])))/2000)*((1/3)*(d[0]+5)), 2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = PH1,
        ayuda2 = PH2,
        ayuda3 = PH3,
        respuesta_P1 = lambda fa, a, calc, c, d, m: f"""
        La presión hidrostática es la presión ejercida por un fluido en reposo. Para determinar si una presa es segura a volcamiento se puede comparar el momento resistente generado por la presa de concreto y el momento actuante producido por el agua. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Definición de las fuerzas actuantes: }}$

        En este caso, las fuerzas actuantes son el peso de la presa $(w)$ y la fuerza hidrostática del agua.
        """,
        respuesta_P2 = lambda fa, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Cálculo del momento resistente:}}$

        Primero, se calcula el peso de la presa de concreto:

        $W = \\rho_c \\cdot g \\cdot \\dfrac{{d_1 \\cdot d_2 \\cdot a}}{{2}}$   
        $W = {2500*9.81*(d[0]+5)*(d[0])*(d[3])/2000:.2f} \\text{{ kN}}$ 

        Luego, se halla la ubicación de esta fuerza con respecto al punto A, la cual se encuentra a $\\dfrac{{2}}{{3}}$ de la distancia $d_2$:

        ${{\hspace{{4mm}} \\bar{{x_c}} = \\dfrac{{2}}{{3}}d_2}}$        
        
        ${{\hspace{{4mm}} \\bar{{x_c}} = {(2/3)*(d[0]):.2f} \\text{{ m}} }}$ 

        Finalmente, se cálcula el momento resistente $(M_R)$:

        ${{\hspace{{4mm}} M_R = W \\cdot \\bar{{x_c}}}}$        
        
        ${{\hspace{{4mm}} M_R = {(2500*9.81*(d[0]+5)*(d[0])*(d[3])/2000)*((2/3)*(d[0])):.2f} \\text{{ kN}} \\cdot \\text{{m}} }}$ 

        
        $\\textbf{{\\small 2. Cálculo del momento actuante:}}$

        Primero, se calcula la fuerza hidrostática $(F_H)$:

        $F_H = \\dfrac{{P \\cdot d_1 \\cdot a}}{{2}}$     
        
        ${{\hspace{{4mm}} P = \\rho \\cdot g \\cdot d_1 }}$      
        
        ${{\hspace{{4mm}} P = 1000 \\dfrac{{kg}}{{m^3}} \\cdot 9,81 \\dfrac{{m}}{{s^2}} \\cdot {d[0]+5:.0f} \\text{{ m}} }}$      
        
        ${{\hspace{{4mm}} P = {9810*(d[0]+5):.2f}  \\dfrac{{N}}{{m^2}} }}$ 

        ${{\hspace{{4mm}} F_H = \\dfrac{{P \\cdot h \\cdot a}}{{2}}}}$      
        
        ${{\hspace{{4mm}} F_H = {((9810*(d[0]+5))*((d[0]+5)*(d[3])))/2000:.2f} \\text{{ kN}} }}$ 

        Luego, se halla la ubicación de esta fuerza con respecto al punto A, la cual se encuentra a $\\dfrac{{1}}{{3}}$ de la distancia $d_1$:

        ${{\hspace{{4mm}} \\bar{{y_a}} = \\dfrac{{1}}{{3}}d_1}}$        
        
        ${{\hspace{{4mm}} \\bar{{y_a}} = {(1/3)*(d[0]+5):.2f} \\text{{ m}} }}$ 

        Finalmente, se cálcula el momento actuante $(M_A)$:

        ${{\hspace{{4mm}} M_A = F_H \\cdot \\bar{{y_a}}}}$        
        
        ${{\hspace{{4mm}} M_A = {(((9810*(d[0]+5))*((d[0]+5)*(d[3])))/2000)*((1/3)*(d[0]+5)):.2f} \\text{{ kN}} \\cdot \\text{{m}}}}$
        """,
        respuesta_P3 = lambda fa, a, calc, c, d, m: f"",
        calculos = 'operations',
        ),

    Questionary(#3_1
        code = 7210031,
        no_pregunta = 3,
        complexity = F,
        topic = FD,
        subtopic = "Presión hidrostática",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Considere la presa de concreto mostrada en la figura. Determine la dimensión $d_2$ mínima para impedir que la presa se voltee alrededor de $A$. Utilice los siguientes datos: el ancho de la presa $a = {d[3]:.0f} \\text{{ m}}$, la densidad del agua $\\rho_a = 1000 \\dfrac{{kg}}{{m^3}}$, la densidad del concreto $\\rho_c = 2500 \\dfrac{{kg}}{{m^3}}$, la aceleración debida a la gravedad $g = 9,81 \\dfrac{{m}}{{s^2}}$ y $d_1 = {d[0]+5:.0f} \\text{{ m}}$.",
        no_answers = 1,
        a1_name = "$d_2$ $[m]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(math.sqrt(((((9810*(d[0]+5))*((d[0]+5)*(d[3])))/2000)*((1/3)*(d[0]+5))*3)/((d[0]+5)*24.525*d[3])), 2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = PH2,
        ayuda2 = PH3,
        ayuda3 = PH4,
        respuesta_P1 = lambda fa, a, calc, c, d, m: f"""
        La presión hidrostática es la presión ejercida por un fluido en reposo. Para determinar si una presa es segura a volcamiento se puede comparar el momento resistente generado por la presa de concreto y el momento actuante producido por el agua. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Definición de las fuerzas actuantes: }}$

        En este caso, las fuerzas actuantes son el peso de la presa $(w)$ y la fuerza hidrostática del agua.
        """,
        respuesta_P2 = lambda fa, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Sumatoria de momentos alrededor de A:}}$

        $\\underline{{Fuerzas \\text{{ }} actuantes:}}$  

        Peso de la presa de concreto ($W$):

        $W = \\rho_c \\cdot g \\cdot \\dfrac{{d_1 \\cdot d_2 \\cdot a}}{{2}}$  

        Fuerza hidrostática $(F_H)$:

        $F_H = \\dfrac{{P \\cdot d_1 \\cdot a}}{{2}}$     
        
        ${{\hspace{{4mm}} P = \\rho \\cdot g \\cdot d_1 }}$      
        
        ${{\hspace{{4mm}} P = 1000 \\dfrac{{kg}}{{m^3}} \\cdot 9,81 \\dfrac{{m}}{{s^2}} \\cdot {d[0]+5:.0f} \\text{{ m}} }}$      
        
        ${{\hspace{{4mm}} P = {9810*(d[0]+5):.2f}  \\dfrac{{N}}{{m^2}} }}$ 

        ${{\hspace{{4mm}} F_H = \\dfrac{{P \\cdot h \\cdot a}}{{2}}}}$      
        
        ${{\hspace{{4mm}} F_H = {((9810*(d[0]+5))*((d[0]+5)*(d[3])))/2000:.2f} \\text{{ kN}} }}$ 

        
        $\\underline{{Ubicación \\text{{ }} de \\text{{ }} las \\text{{ }} fuerzas \\text{{ }} con \\text{{ }} respecto \\text{{ }} a \\text{{ }} A:}}$  

        Ubicación del peso de la presa de concreto ($\\bar{{x_c}}$):

        ${{\hspace{{4mm}} \\bar{{x_c}} = \\dfrac{{2}}{{3}}d_2}}$        

        Ubicación de la fuerza hidrostática ($\\bar{{y_a}}$):

        ${{\hspace{{4mm}} \\bar{{y_a}} = \\dfrac{{1}}{{3}}d_1}}$        
        
        ${{\hspace{{4mm}} \\bar{{y_a}} = {(1/3)*(d[0]+5):.2f} \\text{{ m}} }}$ 


        $\\underline{{Sumatoria \\text{{ }} de \\text{{ }} momentos:}}$  

        ${{\hspace{{4mm}} \\sum{{M_A}} = W \\cdot \\bar{{x_c}} - F_H \\cdot \\bar{{y_a}} = 0}}$

        ${{\hspace{{4mm}} \\sum{{M_A}} = (\\rho_c \\cdot g \\cdot \\dfrac{{d_1 \\cdot d_2 \\cdot a}}{{2}}) \\cdot \\left(\\dfrac{{2}}{{3}}d_2\\right) - \\left(\\dfrac{{P \\cdot h \\cdot a}}{{2}}\\right) \\cdot \\dfrac{{1}}{{3}}d_1 = 0}}$
       
        
        $\\underline{{Despeje \\text{{ }} de \\text{{ }} la \\text{{ }} distancia:}}$ 
     
        ${{\hspace{{4mm}} d_2 = \\sqrt{{\\dfrac{{F_H}}{{a \\cdot \\rho_c \\cdot g}} }} }}$     

        ${{\hspace{{4mm}} d_2 = {math.sqrt(((((9810*(d[0]+5))*((d[0]+5)*(d[3])))/2000)*((1/3)*(d[0]+5))*3)/((d[0]+5)*24.525*d[3])):.2f} \\text{{ m}}}}$
        """,
        respuesta_P3 = lambda fa, a, calc, c, d, m: f"",
        calculos = 'operations',
        ),

    Questionary(#4_1
        code = 7210041,
        no_pregunta = 4,
        complexity = F,
        topic = FD,
        subtopic = "Presión hidrostática",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza hidrostática resultante que actúa sobre la cara de la presa. Considere que el ancho de la presa $a = {d[3]:.0f} \\text{{ m}}$, la densidad del agua $\\rho = 1000 \\dfrac{{kg}}{{m^3}}$, la aceleración debida a la gravedad $g = 9,81 \\dfrac{{m}}{{s^2}}$, $d_1 = {d[0]+5:.0f} \\text{{ m}}$ y $d_2 = {d[0]:.0f} \\text{{ m}}$.",
        no_answers = 1,
        a1_name = "Magnitud fuerza hidrostática $|F_R|$ $[kN]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((9810*(d[0]+5))*(Calculations.magnitude(d[0],d[0]+5)*(d[3])))/2000, 2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = PH1,
        ayuda2 = PH2,
        ayuda3 = PH3,
        respuesta_P1 = lambda fa, a, calc, c, d, m: f"""
        La presión hidrostática es la presión ejercida por un fluido en reposo. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Distribución de la fuerza hidrostática: }}$

        La fuerza hidrostática $(F_R)$ tiene dos componentes (vertical $(W)$ y horizontal $(F_H)$), debido a que la cara de la presa en contacto con el agua es inclinada. La fuerza resultante puede determinarse como una distribución triangular o calculando cada componente por separado.
        """,
        respuesta_P2 = lambda fa, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Cálculo de la fuerza hidrostática resultante:}}$

        Para este caso, se usará la distribución triangular de presiones:

        ${{\hspace{{4mm}} F_R = \\dfrac{{P \\cdot \\sqrt{{(d_1)^2+(d_2)^2}} \\cdot a}}{{2}}}}$        
        
        ${{\hspace{{4mm}} P = \\rho \\cdot g \\cdot d_1 }}$      
        
        ${{\hspace{{4mm}} P = 1000 \\dfrac{{kg}}{{m^3}} \\cdot 9,81 \\dfrac{{m}}{{s^2}} \\cdot {d[0]+5:.0f} \\text{{ m}} }}$      
        
        ${{\hspace{{4mm}} P = {9810*(d[0]+5):.2f}  \\dfrac{{N}}{{m^2}} }}$ 
        
        ${{\hspace{{4mm}} F_R = {((9810*(d[0]+5))*(Calculations.magnitude(d[0],d[0]+5)*(d[3])))/2000:.2f} \\text{{ kN}} }}$ 
        """,
        respuesta_P3 = lambda fa, a, calc, c, d, m: f"",
        calculos = 'operations',
        ),

    Questionary(#5_1
        code = 7210051,
        no_pregunta = 5,
        complexity = F,
        topic = FD,
        subtopic = "Presión hidrostática",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"El túnel semicircular pasa bajo un cuerpo de agua que tiene $d_1 = {d[0]+5} \\text{{ m}}$ de profundidad. Determine la fuerza hidrostática vertical que actúa por metro de longitud. Considere que el diámetro del túnel $d_2 = {d[0]+3:.0f} \\text{{ m}}$, la densidad del agua $\\rho = 1000 \\dfrac{{kg}}{{m^3}}$ y la aceleración debida a la gravedad $g = 9,81 \\dfrac{{m}}{{s^2}}$.",
        no_answers = 1,
        a1_name = "Fuerza hidrostática vertical $|F_V|$ $[kN/m]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((9.81*(d[0]+3)*((d[0]+5)-((d[0]+3)/2)))+(9.81*((d[0]+3)*((d[0]+3)/2)-((math.pi*((d[0]+3)/2)**2)/2))), 2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = PH1,
        ayuda2 = PH2,
        ayuda3 = PH3,
        respuesta_P1 = lambda fa, a, calc, c, d, m: f"""
        La presión hidrostática es la presión ejercida por un fluido en reposo. La fuerza hidrostática vertical hace referencia al peso del agua que está sobre la estructura. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Diagrama de la fuerza hidrostática vertical: }}$

        En la siguiente figura se presenta el diagrama utilizado para el cálculo de la fuerza hidrostática vertical.
        """,
        respuesta_P2 = lambda fa, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Cálculo de la fuerza hidrostática vertical:}}$

        Para este caso, se usará la distribución triangular de presiones:

        ${{\hspace{{4mm}} F_V = W_1 + W_2}}$        
        
        ${{\hspace{{4mm}} W_1 = \\rho \\cdot g \\cdot d_2 \\cdot \\left(d_1-\\dfrac{{d_2}}{{2}}\\right)}}$  

        ${{\hspace{{4mm}} W_1 = {9.81*(d[0]+3)*((d[0]+5)-((d[0]+3)/2)):.2f} \\dfrac{{kN}}{{m}}}}$ 

        ${{\hspace{{4mm}} W_2 = \\rho \\cdot g \\cdot \\left(d_2 \\cdot \\dfrac{{d_2}}{{2}}-\\dfrac{{\\pi \\cdot \\left(\\dfrac{{d_2}}{{2}}\\right)^2}}{{2}}\\right)}}$  
            
        ${{\hspace{{4mm}} W_2 = {9.81*((d[0]+3)*((d[0]+3)/2)-((math.pi*((d[0]+3)/2)**2)/2)):.2f} \\dfrac{{kN}}{{m}}}}$ 
        
        
        ${{\hspace{{4mm}} F_V = {(9.81*(d[0]+3)*((d[0]+5)-((d[0]+3)/2)))+(9.81*((d[0]+3)*((d[0]+3)/2)-((math.pi*((d[0]+3)/2)**2)/2))):.2f} \\dfrac{{kN}}{{m}} }}$ 
        """,
        respuesta_P3 = lambda fa, a, calc, c, d, m: f"",
        calculos = 'operations',
        ),
    

    # #=================================================  FUERZAS DISTRIBUIDAS =========================================================
    # #-------------------------------------------------       Presión hidrostática    --------------------------------------------
    # #-------------------------------------------------       Nivel Medio   ---------------------------------------------------
    # #-------------------------------------------------       Code: 72200#1    --------------------------------------------------
    Questionary(#1_1
        code = 7220011,
        no_pregunta = 1,
        complexity = M,
        topic = FD,
        subtopic = "Presión hidrostática",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza hidrostática que actúa sobre la compuerta AB, la cual tiene un ancho de $a = {d[0]:.2f} \\text{{ m}}$. Considere $d_1 = {d[3]:.0f} \\text{{ m}}$,  $d_2 = {d[6]:.0f}  \\text{{ m}}$, $d_3 = {d[9]:.0f}  \\text{{ m}}$, la densidad del agua $\\rho_1 = 1000 \\dfrac{{kg}}{{m^3}}$ y la aceleración debida a la gravedad $g = 9,81 \\dfrac{{m}}{{s^2}}$.",
        no_answers = 1,
        a1_name = "Magnitud fuerza hidrostática $|F_R|$ $[kN]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(d[0]*9810*Calculations.magnitude(d[9],d[6])*(1/2)*(2*d[3]+d[6])*(1/1000),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = PH1,
        ayuda2 = PH2,
        ayuda3 = PH3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        La presión hidrostática es la presión ejercida por un fluido en reposo. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. División de fuerza distribuida: }}$

        Dada la configuración de la compuerta, la presión hidrostática generada se puede dividir en 2 distribuciones más simples, cuyos centroides son comunes, como triángulos y rectángulos.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        Donde, según profundidad se puede obtener los valores de $p_1$ y $p_2$ :
        
        ${{\hspace{{4mm}} p_1 = \\rho \\cdot g \\cdot d_1 }}$     
        ${{\hspace{{4mm}} p_2 = \\rho \\cdot g \\cdot (d_1+d_2) }}$     
                
        $\\textbf{{\\small 2. Puntualización de las fuerzas: }}$
        
        Con las nuevas distribuciones se puede encontrar la magnitud de las presiones correspondientes a cada figura
        
        ${{\hspace{{4mm}} F_1 (Rectángulo) = p_1 \\cdot \\sqrt{{(d_2)^2 + (d_3)^2}} \\cdot a}}$     
        
        ${{\hspace{{4mm}} F_2 (Triángulo) = \\dfrac{{(p_2 - p_1) \\cdot \\sqrt{{(d_2)^2 + (d_3)^2}}}}{{2}} \\cdot a}}$         
                   
        $\\textbf{{\\small 3. Magnitud de fuerza resultante: }}$
        
        Ahora bien, la fuerza resultante sera la sumatoria de las dos fuerzas encontradas:
        
        ${{\hspace{{4mm}} F_R = F_1 + F_2 }}$     
        
        ${{\hspace{{4mm}} F_R = p_1 \\cdot \\sqrt{{(d_2)^2 + (d_3)^2}} \\cdot a + \\dfrac{{(p_2 - p_1) \\cdot \\sqrt{{(d_2)^2 + (d_3)^2}}}}{{2}} \\cdot a}}$     
        
        ${{\hspace{{4mm}} F_R = \\rho \\cdot g \\cdot d_1 \\cdot \\sqrt{{(d_2)^2 + (d_3)^2}} \\cdot a + \\dfrac{{(\\rho \\cdot g \\cdot (d_1+d_2) - \\rho \\cdot g \\cdot d_1) \\cdot \\sqrt{{(d_2)^2 + (d_3)^2}} \\cdot a}}{{2}} }}$     

        ${{\hspace{{4mm}} F_R = \\dfrac{{(2 \\rho \\cdot g \\cdot d_1 \\cdot \\sqrt{{(d_2)^2 + (d_3)^2}} \\cdot a + \\rho \\cdot g \\cdot d_2 \\cdot \\sqrt{{(d_2)^2 + (d_3)^2}} \\cdot a}}{{2}} }}$     
        
        ${{\hspace{{4mm}} F_R = \\dfrac{{\\rho \\cdot g \\cdot \\sqrt{{(d_2)^2 + (d_3)^2}} \\cdot a}}{{2}} \\cdot (2d_1+d_2)}}$     
       
        ${{\hspace{{4mm}} F_R = {d[0]*9810*Calculations.magnitude(d[9],d[6])*(1/2)*(2*d[3]+d[6]):.2f} \\text{{ N}}}}$ 
       
        ${{\hspace{{4mm}} F_R = {d[0]*9810*Calculations.magnitude(d[9],d[6])*(1/2)*(2*d[3]+d[6])*(1/1000):.2f} \\text{{ kN}}}}$ 
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
   
    Questionary(#2_1
        code = 7220021,
        no_pregunta = 2,
        complexity = M,
        topic = FD,
        subtopic = "Presión hidrostática",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza hidrostática que actúa sobre la presa, la cual tiene un ancho $ a = {d[0]:.0f} \\text{{ m}}$ y una forma parabólica descrita por la ecuación $ f(X) = {((d[3]+8)/50):.2f} \\cdot X^2$. Considere $d_1=f(d_2)$, $d_2 = {3+(d[6]/2):.2f}  \\text{{ m}}$, la densidad del agua $\\rho_1 = 1000 \\dfrac{{kg}}{{m^3}}$ y la aceleración debida a la gravedad $g = 9,81 \\dfrac{{m}}{{s^2}}$.",
        no_answers = 1,
        a1_name = "Magnitud fuerza hidrostática $|F_R|$ [kN]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude((981/100)*d[0]*((d[3]+8)/50)*(2/3)*pow(3+(d[6]/2),3),(981/100)*(1/2)*d[0]*pow(((d[3]+8)/50)*pow(3+(d[6]/2),2),2)),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = PH1,
        ayuda2 = PH2,
        ayuda3 = PH3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        La presión hidrostática es la presión ejercida por un fluido en reposo. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. División de fuerza distribuida: }}$

        Dada la configuración de la presa, se puede obtener una presión hidrostática y una fuerza vertical originada por el peso del agua.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Puntualización de las fuerzas: }}$
        
        Primero, se halla la distancia $d_1$ aplicando la ecuación de la parábola:

        ${{\hspace{{4mm}} d_1 =  f(X) = {((d[3]+8)/50):.2f} \\cdot X^2 }}$          
        ${{\hspace{{4mm}} d_1 = {((d[3]+8)/50)*(3+(d[6]/2))**2:.2f} \\text{{m}}}}$ 

        $\\underline{{Fuerza \\hspace{{2mm}} vertical:}}$ 
               
        ${{\hspace{{4mm}} W_1 = \\rho_a \\cdot g \\cdot a \\cdot (d_1 \\cdot d_2 - \\int_{{0}}^{{d_2}} {((d[3]+8)/50):.2f} \\cdot X^2\\,dx)}}$           
        ${{\hspace{{4mm}} W_1 = \\rho_a \\cdot g \\cdot a \\cdot (d_1 \\cdot d_2 - {((d[3]+8)/50):.2f} \\cdot \\dfrac{{(d_2)^3}}{{3}} )}}$       
        ${{\hspace{{4mm}} W_1 = {(1000*9.81*2*((d[3]+8)/50)*pow(3+(d[6]/2),2)*(3+(d[6]/2))*d[0]*(1/3)):.2f} \\text{{ N}}}}$  
        
        $\\underline{{Fuerza \\hspace{{2mm}} de \\hspace{{2mm}} presión:}}$ 
        
        ${{\hspace{{4mm}} F_P = a \\cdot \\dfrac{{p_1 \\cdot d_1}}{{2}}}}$     
        ${{\hspace{{4mm}} F_P = a \\cdot \\dfrac{{\\rho_a \\cdot g \\cdot d_1 \\cdot d_1}}{{2}}}}$      
        ${{\hspace{{4mm}} F_P = {1000*9.81*((d[3]+8)/50)*pow(3+(d[6]/2),2)*((d[3]+8)/50)*pow(3+(d[6]/2),2)*d[0]*(1/2):.2f} \\text{{ N}}}}$
                              
        $\\textbf{{\\small 3. Magnitud de fuerza resultante: }}$
        
        Ahora bien, la fuerza resultante sera la sumatoria de las dos fuerzas encontradas:
        
        ${{\hspace{{4mm}} F_R = \\sqrt{{(w_1)^2 + (F_P)^2}}}}$     
       
        ${{\hspace{{4mm}} F_R = {Calculations.magnitude(9810*d[0]*((d[3]+8)/50)*(2/3)*pow(3+(d[6]/2),3),9810*(1/2)*d[0]*pow(((d[3]+8)/50)*pow(3+(d[6]/2),2),2)):.2f} \\text{{ N}}}}$     
        
        ${{\hspace{{4mm}} F_R = {Calculations.magnitude((981/100)*d[0]*((d[3]+8)/50)*(2/3)*pow(3+(d[6]/2),3),(981/100)*(1/2)*d[0]*pow(((d[3]+8)/50)*pow(3+(d[6]/2),2),2)):.2f} \\text{{ kN}}}}$     
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    Questionary(#3_1
        code = 7220031,
        no_pregunta = 3,
        complexity = M,
        topic = "Fuerzas distribuidas",
        subtopic = "Presión hidrostática",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Un pantano de agua dulce se drena al océano mediante una compuerta de marea automática con un ancho $ a = {d[0]:.0f} \\text{{ m}}$. Determine el nivel del océano $d_2$, tal que, la compuerta se abra. Considere $d_1 = {4 + d[3]*(1/4):.2f} \\text{{ m}}$, $d_3 = {1 + d[6]*(1/4):.2f} \\text{{ m}}$, la densidad del agua del pantano $\\rho_p = {1000 + d[9]*(1/2):.2f} \\dfrac{{kg}}{{m^3}}$, la densidad del agua salada $\\rho_o = {1020 + d[12]:.2f} \\dfrac{{kg}}{{m^3}}$ y la aceleración debida a la gravedad $g = 9,81 \\dfrac{{m}}{{s^2}}$.",
        no_answers = 1,
        a1_name = "$d_2$ $[m]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((1000+d[9]*(1/4))/(1020+d[12]))*(4+d[3]*(1/4)) - (((1000+d[9]*(1/4))*(1+d[6]*(1/4)))/((1020+d[12])*3)) + (1/3)*(1+d[6]*(1/4)),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = PH1,
        ayuda2 = PH2,
        ayuda3 = PH5,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        La presión hidrostática es la presión ejercida por un fluido en reposo. La fuerza hidrostática vertical hace referencia al peso del agua que está sobre la estructura. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Representación de ejercicio: }}$

        Debido a la configuración de la compuerta, se generan fuerzas asociadas a la presión hidrostática tanto en el lado del océano como en el del pantano. Además, no se considera la reacción en el bloque $B$, ya que el análisis corresponde a la situación en la que la compuerta se encuentra abierta.
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        Donde $p_1$, $p_2$, $p_3$ y $p_4$ se determinan mediante:
        
        ${{\hspace{{4mm}} p_1 = \\rho_p \\cdot g \\cdot (d_1 - d_3) }}$     
        ${{\hspace{{4mm}} p_2 = \\rho_p \\cdot g \\cdot d_1 }}$     
        ${{\hspace{{4mm}} p_3 = \\rho_o \\cdot g \\cdot (d_2 - d_3) }}$     
        ${{\hspace{{4mm}} p_4 = \\rho_o \\cdot g \\cdot d_2 }}$     
                
        $\\textbf{{\\small 2. Puntualización de las fuerzas: }}$
        
        Con base en la configuración mostrada, se pueden identificar cuatro fuerzas resultantes. No se considera la reacción en el bloque $B$, ya que la situación de análisis es cuando la compuerta se encuentra abierta.    
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"""
        Las magnitudes de cada fuerza son:
        
        ${{\hspace{{4mm}} F_{{P1}} = a \\cdot p_1 \\cdot d_3}}$     
        
        ${{\hspace{{4mm}} F_{{P2}} = a \\cdot \\dfrac{{ d_3 \\cdot (p_2 - p_1)}}{{2}}}}$         
        
        ${{\hspace{{4mm}} F_{{O1}} = a \\cdot p_3 \\cdot d_3}}$     
        
        ${{\hspace{{4mm}} F_{{O2}} = a \\cdot \\dfrac{{ d_3 \\cdot (p_4 - p_3)}}{{2}}}}$         
        
                   
        $\\textbf{{\\small 3. Condición de equilibrio: }}$
        
       Para que la compuerta pueda abrirse, se requiere que el nivel del océano sea, al menos, tal que la sumatoria de momentos respecto al punto $A$ sea igual a cero. A partir de esta condición, se procede a resolver."
        
        ${{\hspace{{4mm}} \\sum{{M_A}} = F_{{P1}} \\cdot \\dfrac{{d_3}}{{2}} + F_{{P2}} \\cdot \\dfrac{{2d_3}}{{3}} - F_{{O1}} \\cdot \\dfrac{{d_3}}{{2}} - F_{{O2}} \\cdot \\dfrac{{2d_3}}{{3}} = 0}}$     
       
        ${{\hspace{{4mm}} a \\cdot p_3 \\cdot d_3 \\cdot \\dfrac{{d_3}}{{2}} + a \\cdot \\dfrac{{ d_3 \\cdot (p_4 - p_3)}}{{2}} \\cdot \\dfrac{{2d_3}}{{3}} = a \\cdot p_1 \\cdot d_3 \\cdot \\dfrac{{d_3}}{{2}} + a \\cdot \\dfrac{{ d_3 \\cdot (p_2 - p_1)}}{{2}} \\cdot \\dfrac{{2d_3}}{{3}} }}$     
        
        ${{\hspace{{4mm}} \\rho_o \\cdot g \\cdot (d_2 - d_3) \\cdot \\dfrac{{1}}{{2}} + \\dfrac{{\\rho_o \\cdot g \\cdot d_2 - \\rho_o \\cdot g \\cdot (d_2 - d_3)}}{{3}} = \\rho_p \\cdot g \\cdot (d_1 - d_3) \\cdot \\dfrac{{1}}{{2}} + \\dfrac{{\\rho_p \\cdot g \\cdot d_1 - \\rho_p \\cdot g \\cdot (d_1 - d_3)}}{{3}}}}$     
        
        ${{\hspace{{4mm}} \\rho_o \\cdot (d_2 - d_3) \\cdot \\dfrac{{1}}{{2}} + \\dfrac{{\\rho_o \\cdot d_3}}{{3}} = \\rho_p \\cdot (d_1 - d_3) \\cdot \\dfrac{{1}}{{2}} + \\dfrac{{\\rho_p \\cdot d_3}}{{3}}}}$     
        
        ${{\hspace{{4mm}} \\rho_o \\cdot d_2 \\cdot \\dfrac{{1}}{{2}} = \\rho_p \\cdot (d_1 - d_3) \\cdot \\dfrac{{1}}{{2}} + \\dfrac{{\\rho_p \\cdot d_3}}{{3}} + \\dfrac{{\\rho_o \\cdot d_3}}{{6}}}}$     
        
        ${{\hspace{{4mm}} d_2  = \\dfrac{{\\rho_p}}{{\\rho_o}} \\cdot d_1 - \\dfrac{{\\rho_p \\cdot d_3}}{{3 \\cdot \\rho_o}} + \\dfrac{{d_3}}{{3}}}}$     
        
        ${{\hspace{{4mm}} d_2  = {((1000+d[9]*(1/4))/(1020+d[12]))*(4+d[3]*(1/4)) - (((1000+d[9]*(1/4))*(1+d[6]*(1/4)))/((1020+d[12])*3)) + (1/3)*(1+d[6]*(1/4)):.2f} \\text{{ m}}}}$         
        """,
        calculos='operations'
        ),

    #=================================================  FUERZAS DISTRIBUIDAS =========================================================
    #-------------------------------------------------       Presión hidrostática    --------------------------------------------
    #-------------------------------------------------       Nivel Díficil   ---------------------------------------------------
    #-------------------------------------------------       Code: 72300#1    --------------------------------------------------
    
    Questionary(#1_1
        code = 7230011,
        no_pregunta = 1,
        complexity = D,
        topic = FD,
        subtopic = "Presión hidrostática",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"La presa de “gravedad” de concreto es mantenida en su lugar por su propio peso. Determine la dimensión $d_3$ más pequeña que impide que la presa se voltee alrededor de su extremo $A$. Considere $d_1 = {d[0] + d[3]*2:.0f} \\text{{ m}}$,  $d_2 = {d[3]/2:.1f}  \\text{{ m}}$, la densidad del agua $\\rho_a = 1000 \\dfrac{{kg}}{{m^3}}$, la densidad del concreto $\\rho_c = {2400+m[0]:.0f} \\dfrac{{kg}}{{m^3}}$ y la aceleración debida a la gravedad $g = 9,81 \\dfrac{{m}}{{s^2}}$.",
        no_answers = 1,
        a1_name = "Dimensión $d_3$ $[m]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((-((((2400+m[0])*9.81*(d[0]+d[3]*2)*d[3]*0.5)/2)+((1000*9.81*(d[0]+d[3]*2)*d[3]*0.5)/2))+math.sqrt(((((2400+m[0])*9.81*(d[0]+d[3]*2)*d[3]*0.5)/2)+((1000*9.81*(d[0]+d[3]*2)*d[3]*0.5)/2))**2-4*((((2400+m[0])*9.81*(d[0]+d[3]*2))/6)+((1000*9.81*(d[0]+d[3]*2))/3))*(((2400+m[0])*9.81*(d[0]+d[3]*2)*d[3]*0.5*((0.5*d[3])/2))-((1000*9.81*(d[0]+d[3]*2)**3))/6)))/(2*((((2400+m[0])*9.81*(d[0]+d[3]*2))/6)+((1000*9.81*(d[0]+d[3]*2))/3))),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = PH1,
        ayuda2 = PH2,
        ayuda3 = PH3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        La presión hidrostática es la presión aplicada por un fluido en reposo debido a su propio peso. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Representación de ejercicio: }}$
        Dado a la configuración de la compuerta se puede obtener una presión hidrostática y tres fuerzas verticales dado al peso del agua y de la presa.        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
         $\\textbf{{\\small 2. Puntualización de las fuerzas: }}$
        Asumiendo un ancho "a" de 1m
        
        $\\underline{{Fuerzas \\hspace{{2mm}} verticales:}}$ 
                
        ${{\hspace{{4mm}} W_1 = \\rho_a \\cdot g \\cdot a \\cdot \\dfrac{{d_1 \\cdot d_3}}{{2}}}}$     
        ${{\hspace{{4mm}} W_2 = \\rho_c \\cdot g \\cdot a \\cdot \\dfrac{{d_1 \\cdot d_3}}{{2}}}}$         
        ${{\hspace{{4mm}} W_3 = \\rho_c \\cdot g \\cdot a \\cdot d_1 \\cdot d_2}}$         
        
        $\\underline{{Fuerza \\hspace{{2mm}} de \\hspace{{2mm}} presión:}}$ 
        
        ${{\hspace{{4mm}} F_P = a \\cdot \\dfrac{{\\rho_a \\cdot g \\cdot d_1 \\cdot d_1}}{{2}}}}$     
                   
        $\\textbf{{\\small 3. Condición de equilibrio: }}$
        
        Para garantizar que la presa no gire alrededor de su extremo $A$, es necesario que se cumpla que la sumatoria de momentos respecto al punto $A$ sea igual a cero:
        
        ${{\hspace{{4mm}} \\sum{{M_A}} = W_3 \\cdot \\dfrac{{d_2}}{{2}} + W_2 \\cdot \\left(d_2+\\dfrac{{d_3}}{{3}}\\right) + W_1 \\cdot \\left(d_2+\\dfrac{{2d_3}}{{3}}\\right) - F_P \\cdot \\dfrac{{d_1}}{{3}} = 0}}$     
        
        Reemplazando, se llega  la ecuación cuadrática:
        
        ${{\hspace{{4mm}} (d_3)^2 \\left(\\dfrac{{\\rho_c \\cdot g \\cdot d_1}}{{6}}+\\dfrac{{\\rho_a \\cdot g \\cdot d_1}}{{3}}\\right) + d_3 \\left(\\dfrac{{\\rho_c \\cdot g \\cdot d_1 \\cdot d_2}}{{2}} + \\dfrac{{\\rho_a \\cdot g \\cdot d_1 \\cdot d_2}}{{2}} \\right) + \\left(w_3 \\cdot \\dfrac{{d_2}}{{3}} - \\dfrac{{\\rho_a \\cdot g \\cdot d_1 \\cdot d_1}}{{2}} \\cdot \\dfrac{{d_1}}{{3}} \\right)= 0 }}$     
        
        Dando como resultado:
        
        ${{\hspace{{4mm}} d_3 = {(-((((2400+m[0])*9.81*(d[0]+d[3]*2)*d[3]*0.5)/2)+((1000*9.81*(d[0]+d[3]*2)*d[3]*0.5)/2))+math.sqrt(((((2400+m[0])*9.81*(d[0]+d[3]*2)*d[3]*0.5)/2)+((1000*9.81*(d[0]+d[3]*2)*d[3]*0.5)/2))**2-4*((((2400+m[0])*9.81*(d[0]+d[3]*2))/6)+((1000*9.81*(d[0]+d[3]*2))/3))*(((2400+m[0])*9.81*(d[0]+d[3]*2)*d[3]*0.5*((0.5*d[3])/2))-((1000*9.81*(d[0]+d[3]*2)**3))/6)))/(2*((((2400+m[0])*9.81*(d[0]+d[3]*2))/6)+((1000*9.81*(d[0]+d[3]*2))/3))):.2f} \\text{{ m}}}}$
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),


    #=================================================  FUERZAS DISTRIBUIDAS =========================================================
    #-------------------------------------------------        Empuje de suelo  --------------------------------------------
    #-------------------------------------------------       Nivel Fácil   ---------------------------------------------------
    #-------------------------------------------------       Code: 73100#1    --------------------------------------------------
    
    Questionary(#1_1
        code = 7310011,
        no_pregunta = 1,
        complexity = F,
        topic = FD,
        subtopic = "Empuje de suelo",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la fuerza para la cual debe diseñarse el anclaje, de manera que no se produzca volcamiento alrededor del punto $A$. Considere que el peso específico del concreto es $\\gamma_c = {19+d[0]*(1/2):.2f} \\dfrac{{kN}}{{m^3}}$, el peso específico del suelo es $\\gamma_s = {15+d[3]*(1/2):.2f} \\dfrac{{kN}}{{m^3}}$, el coeficiente de presión lateral de tierra $k = {(12+d[6])*(1/50):.2f}$, $d_1 = {1+d[9]*(1/4):.2f} \\text{{ m}}$,  $d_2 = {(100+d[12])/100:.2f}  \\text{{ m}}$, $d_3 = {1+d[15]*(1/10):.2f}  \\text{{ m}}$ y $d_4 = {4+d[9]*(1/2):.2f} \\text{{ m}}$.",
        no_answers = 1,
        a1_name = "Fuerza del anclaje $F_a$ [kN]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((12+d[6])*(1/300)*(15+d[3]*(1/2))*(pow(4+d[9]*(1/2) + (100+ d[12])*(1/100),3)) - (19+d[0]*(1/2))*(100+d[12])*(1/100)*((100+d[12])*(1/100) + 4 + d[9]*(1/2))*(1+d[15]*(1/10) + (1/200)*(100+d[12])) - (19+d[0]*(1/2))*(100+d[12])*(1/100)*(1/2)*(pow((1+d[15]*(1/10)),2)))/(1+d[9]*(1/4)),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = ES1,
        ayuda2 = ES2,
        ayuda3 = ES3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El empuje de suelo es la fuerza que el terreno ejerce sobre una estructura en contacto con él, por ejemplo, un muro de contención. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Representación de ejercicio: }}$

        En la configuración del muro de contención mostrado, se identifican las siguientes fuerzas: la fuerza resultante del empuje del suelo, la fuerza ejercida por el anclaje y dos fuerzas verticales del peso propio del muro de contención.  
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Puntualización de las fuerzas: }}$
        
        Asumiendo un ancho "a" de 1m:
        
        $\\underline{{Fuerzas \\hspace{{2mm}} verticales:}}$ 
                
        ${{\hspace{{4mm}} W_1 = \\gamma_c \\cdot a \\cdot d_2 \\cdot (d_2 + d_4)}}$     
        ${{\hspace{{4mm}} W_2 = \\gamma_c \\cdot a \\cdot d_2 \\cdot d_3}}$         
        
        $\\underline{{Fuerza \\hspace{{2mm}} de \\hspace{{2mm}} presión:}}$ 
        
        ${{\hspace{{4mm}} F_P = k \\cdot a \\cdot \\dfrac{{\\gamma_s \\cdot (d_4 + d_2)^2}}{{2}}}}$  
           
        $\\textbf{{\\small 3. Estabilidad al volcamiento: }}$
        
        La fuerza mínima ejercida por el anclaje para asegurar que no exista volcamiento alrededor del punto $A$ se despeja de la sumatoria de momentos en $A$:
        
        ${{\hspace{{4mm}} \\sum{{M_A}} = F_P \\cdot \\dfrac{{d_4 + d_2}}{{3}} - F_a \\cdot d_1  - W_1 \\cdot \\left(d_3 + \\dfrac{{d_2}}{{2}}\\right) - W_2 \\cdot \\dfrac{{d_3}}{{2}} = 0}}$     
       
        ${{\hspace{{4mm}} F_a \\cdot d_1 = F_P \\cdot \\dfrac{{d_4 + d_2}}{{3}} - W_1 \\cdot \\left(d_3 + \\dfrac{{d_2}}{{2}}\\right) - W_2 \\cdot \\dfrac{{d_3}}{{2}}}}$     
        
        ${{\hspace{{4mm}} F_a \\cdot d_1 =  k \\cdot a \\cdot \\dfrac{{\\gamma_s \\cdot (d_4 + d_2)^3}}{{6}} -  \\gamma_c \\cdot a \\cdot d_2 \\cdot (d_2 + d_4) \\cdot \\left(d_3 + \\dfrac{{d_2}}{{2}}\\right) - \\gamma_c \\cdot a \\cdot d_2 \\cdot \\dfrac{{(d_3)^2}}{{2}}}}$     
        
        ${{\hspace{{4mm}} F_a \\cdot {1+d[9]*(1/4):.2f} \\text{{ m}} =  {(12+d[6])*(1/300)*(15+d[3]*(1/2))*(pow(4+d[9]*(1/2) + (100+ d[12])*(1/100),3)):.2f} \\text{{ kN}} \\cdot \\text{{ m}} - {(19+d[0]*(1/2))*(100+d[12])*(1/100)*((100+d[12])*(1/100)+ 4 + d[9]*(1/2))*(1+d[15]*(1/10) + (1/200)*(100+d[12])):.2f} \\text{{ kN}} \\cdot \\text{{ m}} - {(19+d[0]*(1/2))*(100+d[12])*(1/100)*(1/2)*(pow((1+d[15]*(1/10)),2)):.2f} \\text{{ kN}} \\cdot \\text{{ m}}}}$     
        
        ${{\hspace{{4mm}} F_a =  {((12+d[6])*(1/300)*(15+d[3]*(1/2))*(pow(4+d[9]*(1/2) + (100+ d[12])*(1/100),3)) - (19+d[0]*(1/2))*(100+d[12])*(1/100)*((100+d[12])*(1/100) + 4 + d[9]*(1/2))*(1+d[15]*(1/10) + (1/200)*(100+d[12])) - (19+d[0]*(1/2))*(100+d[12])*(1/100)*(1/2)*(pow((1+d[15]*(1/10)),2)))/(1+d[9]*(1/4)):.2f} \\text{{ kN}} }}$     
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

     Questionary(#2_1
        code = 7310011,
        no_pregunta = 2,
        complexity = F,
        topic = FD,
        subtopic = "Empuje de suelo",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza de presión de tierra que actúa sobre el muro de contención  y su ubicación medida desde la base. Considere que el ancho del muro $a = {d[0]:.0f} \\text{{ m}}$, el peso específico del suelo es $\\gamma_s = {14+d[3]*(1/2):.2f} \\dfrac{{kN}}{{m^3}}$,  el coeficiente de presión lateral de tierra $k = {(12+d[6])*(1/50):.2f}$ y $d_1 = {((100+d[12])/100)+3.5:.2f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Magnitud fuerza de presión de tierra $|F_P|$ $[kN]$",
        a2_name = "Ubicación fuerza de presión de tierra $(\\bar{{y}})$ $[m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(0.5*(14+d[3]*0.5)*((12+d[6])*(1/50))*d[0]*(((100+d[12])/100)+3.5)**2, 2),
        answer2 = lambda f, a, calc, c, d, m: np.round((1/3)*(((100+d[12])/100)+3.5), 2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = ES1,
        ayuda2 = ES2,
        ayuda3 = "",
        respuesta_P1 = lambda fa, a, calc, c, d, m: f"""
        El empuje de suelo es la fuerza que el terreno ejerce sobre una estructura en contacto con él, por ejemplo, un muro de contención. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Representación de ejercicio: }}$

        Se identifica la fuerza de presión de tierra:  
        """,
        respuesta_P2 = lambda fa, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Cálculo de la fuerza de presión de tierra: }}$d
          
        ${{\hspace{{4mm}} F_P = \\dfrac{{k \\cdot a \\cdot \\gamma_s \\cdot (d_1)^2}}{{2}}}}$  
        ${{\hspace{{4mm}} F_P = {0.5*(14+d[3]*0.5)*((12+d[6])*(1/50))*d[0]*(((100+d[12])/100)+3.5)**2:.2f} \\text{{ kN}}}}$  

        $\\textbf{{\\small 3. Ubicación de la fuerza de presión de tierra desde la base:}}$

        La fuerza de presión de tierra se distribuye de forma triangular, por lo tanto, su ubicación desde la base es a $\\dfrac{{1}}{{3}}$ de la distancia $d_1$:

        ${{\hspace{{4mm}} \\bar{{y}} = \\dfrac{{1}}{{3}}d_1}}$        
        
        ${{\hspace{{4mm}} \\bar{{y}} = {(1/3)*(((100+d[12])/100)+3.5):.2f} \\text{{ m}} }}$ 
        """,
        respuesta_P3 = lambda fa, a, calc, c, d, m: f"",
        calculos = 'operations',
        ),
    

    #=================================================  FUERZAS DISTRIBUIDAS =========================================================
    #-------------------------------------------------        Empuje de suelo  --------------------------------------------
    #-------------------------------------------------       Nivel medio   ---------------------------------------------------
    #-------------------------------------------------       Code: 73200#1    --------------------------------------------------
    Questionary(#1_1
        code = 7320011,
        no_pregunta = 1,
        complexity = M,
        topic = FD,
        subtopic = "Empuje de suelo",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la distancia $d_2$ que se necesita para asegurar que no exista volcamiento alrededor del punto $A$. Considere que el peso específico del concreto es $\\gamma_c = {20+d[0]*(1/2):.2f} \\dfrac{{kN}}{{m^3}}$, el peso específico del suelo es $\\gamma_s = {15+d[3]*(1/2):.2f} \\dfrac{{kN}}{{m^3}}$, el coeficiente de presión lateral de tierra $k = {(12+d[6])*(1/50):.2f}$, $d_1 = {(100+d[12])/100:.2f}  \\text{{ m}}$ y $d_3 = {3+d[9]*(1/2):.2f} \\text{{ m}}$.",
        no_answers = 1,
        a1_name = "Dimensión $d_2$ $[m]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((-(-(20+d[0]*(1/2))*((100+d[12])/100)*(((100+d[12])/100)+(3+d[9]*0.5)))-math.sqrt((-(20+d[0]*(1/2))*((100+d[12])/100)*(((100+d[12])/100)+(3+d[9]*0.5)))**2-4*(-((20+d[0]*(1/2))*((100+d[12])/100))/2)*(((-(20+d[0]*0.5)*((100+d[12])/100)*(((100+d[12])/100)+(3+d[9]*0.5))*((100+d[12])/100)/2))+(((((100+d[12])/100)+(3+d[9]*0.5))**3)*(1/6)*((12+d[6])*(1/50))*(15+d[3]*0.5)))))/(2*(-((20+d[0]*(1/2))*((100+d[12])/100))/2)),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = ES1,
        ayuda2 = ES2,
        ayuda3 = ES3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El empuje de suelo es la fuerza que el terreno ejerce sobre una estructura en contacto con él, por ejemplo, un muro de contención. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Representación de ejercicio: }}$

        En la configuración del muro de contención mostrado, se identifican las siguientes fuerzas: la fuerza resultante del empuje del suelo y cuatro fuerzas verticales del peso propio del muro de contención.  
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Puntualización de las fuerzas: }}$
        
        Asumiendo un ancho "a" de 1m:
        
        $\\underline{{Fuerzas \\hspace{{2mm}} verticales:}}$ 
                
        ${{\hspace{{4mm}} W_1 = \\gamma_c \\cdot a \\cdot d_1 \\cdot (d_3 + d_1)}}$     
        ${{\hspace{{4mm}} W_2 = \\gamma_c \\cdot a \\cdot d_1 \\cdot d_2}}$         
        
        $\\underline{{Fuerza \\hspace{{2mm}} de \\hspace{{2mm}} presión:}}$ 
        
        ${{\hspace{{4mm}} F_P = k \\cdot a \\cdot \\dfrac{{\\gamma_s \\cdot (d_1 + d_3)^2}}{{2}}}}$  
           
        $\\textbf{{\\small 3. Estabilidad al volcamiento: }}$
        
        Ahora bien, la distancia minima de $d_2$ para asegurar que no exista volcamiento alrededor del punto $A$ se puede despejar de la sumatoria de momentos en $A$, igualándola a cero:
        
        ${{\hspace{{4mm}} \\sum{{M_A}} = F_P \\cdot \\dfrac{{d_1 + d_3}}{{3}} - W_1 \\cdot \\left(d_2 + \\dfrac{{d_1}}{{2}}\\right) - W_2 \\cdot \\left(\\dfrac{{d_2}}{{2}}\\right) = 0}}$     
        
        Al realizar el despeje se obtiene que $d_2$ es:
        
        ${{\hspace{{4mm}} d_2 = {(-(-(20+d[0]*(1/2))*((100+d[12])/100)*(((100+d[12])/100)+(3+d[9]*0.5)))-math.sqrt((-(20+d[0]*(1/2))*((100+d[12])/100)*(((100+d[12])/100)+(3+d[9]*0.5)))**2-4*(-((20+d[0]*(1/2))*((100+d[12])/100))/2)*(((-(20+d[0]*0.5)*((100+d[12])/100)*(((100+d[12])/100)+(3+d[9]*0.5))*((100+d[12])/100)/2))+(((((100+d[12])/100)+(3+d[9]*0.5))**3)*(1/6)*((12+d[6])*(1/50))*(15+d[3]*0.5)))))/(2*(-((20+d[0]*(1/2))*((100+d[12])/100))/2)):.2f} \\text{{ m}}}}$
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
  

    #=================================================  FUERZAS DISTRIBUIDAS =========================================================
    #-------------------------------------------------       Empuje de suelo    --------------------------------------------
    #-------------------------------------------------       Nivel Díficil   ---------------------------------------------------
    #-------------------------------------------------       Code: 73300#1    --------------------------------------------------
 
    Questionary(#1_1
        code = 7330011,
        no_pregunta = 1,
        complexity = D,
        topic = FD,
        subtopic = "Empuje de suelo",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la distancia $d_4$ que se necesita para asegurar que no exista volcamiento alrededor del punto $A$. Considere que el peso específico del concreto es $\\gamma_c = {18+d[0]*(1/2):.2f} \\dfrac{{kN}}{{m^3}}$, el peso específico del suelo es $\\gamma_s = {15+d[3]*(1/2):.2f} \\dfrac{{kN}}{{m^3}}$, el coeficiente de presión lateral de tierra $k = {(12+d[6])*(1/50):.2f}$, $d_1 = {(3/2)+d[9]*(1/2):.2f} \\text{{ m}}$,  $d_2 = {(50+d[12])/100:.2f}  \\text{{ m}}$ y $d_3 = {(1/2) + d[15]*(1/20):.2f} \\text{{ m}}$.",
        no_answers = 1,
        a1_name = "Distancia $d_4$ [m]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((-(-(18+d[0]*(1/2))*((50+d[12])/100)*(((3/2)+d[9]*(1/2))+((50+d[12])/100))-(18+d[0]*(1/2))*((((3/2)+d[9]*(1/2))*(((1/2) + d[15]*(1/20))-((50+d[12])/100)))/2)-(18+d[0]*(1/2))*(((1/2) + d[15]*(1/20))-((50+d[12])/100))*((50+d[12])/100))-(math.sqrt(((-(18+d[0]*(1/2))*((50+d[12])/100)*(((3/2)+d[9]*(1/2))+((50+d[12])/100))-(18+d[0]*(1/2))*((((3/2)+d[9]*(1/2))*(((1/2) + d[15]*(1/20))-((50+d[12])/100)))/2)-(18+d[0]*(1/2))*(((1/2) + d[15]*(1/20))-((50+d[12])/100))*((50+d[12])/100)))**2-(4*(((-(18+d[0]*(1/2))*((50+d[12])/100)*(((3/2)+d[9]*(1/2))+((50+d[12])/100))*((1/2) + d[15]*(1/20))))+((18+d[0]*(1/2))*((50+d[12])/100)*(((3/2)+d[9]*(1/2))+((50+d[12])/100))*(((50+d[12])/100)/2))-((18+d[0]*(1/2))*((((3/2)+d[9]*(1/2))*(((1/2) + d[15]*(1/20))-((50+d[12])/100)))/2)*(2/3)*((((1/2) + d[15]*(1/20)))-(((50+d[12])/100))))-((18+d[0]*(1/2))*(((1/2) + d[15]*(1/20))-((50+d[12])/100))*((50+d[12])/100)*(((((1/2) + d[15]*(1/20)))-(((50+d[12])/100)))/2))+((15+d[3]*(1/2))*((12+d[6])*(1/50))*(1/2)*(((3/2)+d[9]*(1/2))+((50+d[12])/100))**2)*(1/3)*(((3/2)+d[9]*(1/2))+((50+d[12])/100)))*((-((18+d[0]*(1/2))*((50+d[12])/100))/2))))))/(2*((-((18+d[0]*(1/2))*((50+d[12])/100))/2))),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = ES1,
        ayuda2 = ES2,
        ayuda3 = ES3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El empuje de suelo es la fuerza que el terreno ejerce sobre una estructura en contacto con él, por ejemplo, un muro de contención. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Representación de ejercicio: }}$

        En la configuración del muro de contención mostrado, se identifican las siguientes fuerzas: la fuerza resultante del empuje del suelo y cuatro fuerzas verticales del peso propio del muro de contención.  
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 2. Puntualización de las fuerzas: }}$
        
        Asumiendo un ancho "a" de 1m:
        
        $\\underline{{Fuerzas \\hspace{{2mm}} verticales:}}$ 
                
        ${{\hspace{{4mm}} W_1 = \\gamma_c \\cdot a \\cdot d_2 \\cdot (d_2 + d_1)}}$     
        ${{\hspace{{4mm}} W_2 = \\gamma_c \\cdot a \\cdot \\dfrac{{d_1 \\cdot (d_3 - d_2)}}{{2}}}}$         
        ${{\hspace{{4mm}} W_3 = \\gamma_c \\cdot a \\cdot d_2 \\cdot (d_3 - d_2)}}$         
        ${{\hspace{{4mm}} W_4 = \\gamma_c \\cdot a \\cdot d_4 \\cdot d_2}}$         
        
        $\\underline{{Fuerza \\hspace{{2mm}} de \\hspace{{2mm}} presión:}}$ 
        
        ${{\hspace{{4mm}} F_P = k \\cdot a \\cdot \\dfrac{{\\gamma_s \\cdot (d_1 + d_2)^2}}{{2}}}}$  
           
        $\\textbf{{\\small 3. Estabilidad al volcamiento: }}$
        
        Ahora bien, la distancia minima de $d_4$ para asegurar que no exista volcamiento alrededor del punto $A$ se puede despejar de la sumatoria de momentos en $A$, igualándola a cero:
        
        ${{\hspace{{4mm}} \\sum{{M_A}} = F_P \\cdot \\dfrac{{d_1 + d_2}}{{3}} - W_1 \\cdot \\left(d_4 + d_3 - \\dfrac{{d_2}}{{2}}\\right) - W_2 \\cdot \\left(d_4 + \\dfrac{{2(d_3 - d_2)}}{{3}}\\right) - W_3 \\cdot  \\left(d_4 + \\dfrac{{d_3 - d_2}}{{2}}\\right) - W_4 \\cdot \\dfrac{{d_4}}{{2}} = 0}}$     
        
        Al realizar el despeje se obtiene que $d_4$ es:
       
        ${{\hspace{{4mm}} d_4 = {(-(-(18+d[0]*(1/2))*((50+d[12])/100)*(((3/2)+d[9]*(1/2))+((50+d[12])/100))-(18+d[0]*(1/2))*((((3/2)+d[9]*(1/2))*(((1/2) + d[15]*(1/20))-((50+d[12])/100)))/2)-(18+d[0]*(1/2))*(((1/2) + d[15]*(1/20))-((50+d[12])/100))*((50+d[12])/100))-(math.sqrt(((-(18+d[0]*(1/2))*((50+d[12])/100)*(((3/2)+d[9]*(1/2))+((50+d[12])/100))-(18+d[0]*(1/2))*((((3/2)+d[9]*(1/2))*(((1/2) + d[15]*(1/20))-((50+d[12])/100)))/2)-(18+d[0]*(1/2))*(((1/2) + d[15]*(1/20))-((50+d[12])/100))*((50+d[12])/100)))**2-(4*(((-(18+d[0]*(1/2))*((50+d[12])/100)*(((3/2)+d[9]*(1/2))+((50+d[12])/100))*((1/2) + d[15]*(1/20))))+((18+d[0]*(1/2))*((50+d[12])/100)*(((3/2)+d[9]*(1/2))+((50+d[12])/100))*(((50+d[12])/100)/2))-((18+d[0]*(1/2))*((((3/2)+d[9]*(1/2))*(((1/2) + d[15]*(1/20))-((50+d[12])/100)))/2)*(2/3)*((((1/2) + d[15]*(1/20)))-(((50+d[12])/100))))-((18+d[0]*(1/2))*(((1/2) + d[15]*(1/20))-((50+d[12])/100))*((50+d[12])/100)*(((((1/2) + d[15]*(1/20)))-(((50+d[12])/100)))/2))+((15+d[3]*(1/2))*((12+d[6])*(1/50))*(1/2)*(((3/2)+d[9]*(1/2))+((50+d[12])/100))**2)*(1/3)*(((3/2)+d[9]*(1/2))+((50+d[12])/100)))*((-((18+d[0]*(1/2))*((50+d[12])/100))/2))))))/(2*((-((18+d[0]*(1/2))*((50+d[12])/100))/2))):.2f} \\text{{ m}}}}$
        """, 
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),


    #=================================================  FUERZAS INTERNAS =========================================================
    #-------------------------------------------------       Fuerzas internas    --------------------------------------------
    #-------------------------------------------------       Nivel Fácil   ---------------------------------------------------
    #-------------------------------------------------       Code: 8110011    --------------------------------------------------
    Questionary(#1_1
        code = 8110011,
        no_pregunta = 1,
        complexity = F,
        topic = FI,
        subtopic = FI,
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la fuerza cortante en los puntos $B$ y $D$, así como el momento flector en $B$. Considere $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[0]+d[3]:.0f}  \\text{{ m}}$, $d_3 = {d[6]+2:.0f} \\text{{ m}}$,  $d_4 = {d[6]:.0f}  \\text{{ m}}$, $F_1 = {f[0]:.0f}  \\text{{ kN}}$, $w_1 = {50+m[0]:.0f} \\dfrac{{kN}}{{m}}$ y $w_2 = {m[1]*(1/2):.2f} \\dfrac{{kN}}{{m}}$.",
        no_answers = 3,
        a1_name = "Fuerza cortante en $B$ ($V_B$) $[kN]$",
        a2_name = "Fuerza cortante en $D$ ($V_D$) $[kN]$",
        a3_name = "Momento flector en $B$ ($M_B$) [$kN \\cdot m$]",
        answer1 = lambda f, a, calc, c, d, m: np.round(((-(f[0]*(4/5)*(d[6]+2))+((d[0]+d[3])*(m[1]*0.5)*(d[0]+d[3])/2)+((((50+m[0])-(m[1]*0.5))*(d[0]+d[3])/2)*((2/3)*(d[0]+d[3]))))/(d[0]+d[3]))-(d[0]*((((d[0]+d[3])-d[0])*((50+m[0])-(m[1]*0.5))/(d[0]+d[3]))+(m[1]*0.5)))-0.5*d[0]*((50+m[0])-((((d[0]+d[3])-d[0])*((50+m[0])-(m[1]*0.5))/(d[0]+d[3]))+(m[1]*0.5))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((4/5)*f[0],2),
        answer3 = lambda f, a, calc, c, d, m: np.round((((-(f[0]*(4/5)*(d[6]+2))+((d[0]+d[3])*(m[1]*0.5)*(d[0]+d[3])/2)+((((50+m[0])-(m[1]*0.5))*(d[0]+d[3])/2)*((2/3)*(d[0]+d[3]))))/(d[0]+d[3]))*d[0]-(d[0]*((((d[0]+d[3])-d[0])*((50+m[0])-(m[1]*0.5))/(d[0]+d[3]))+(m[1]*0.5)))*(d[0]/2)-d[0]*((50+m[0])-((((d[0]+d[3])-d[0])*((50+m[0])-(m[1]*0.5))/(d[0]+d[3]))+(m[1]*0.5)))*(d[0]/3)),2),
        ayuda1 = FI1,
        ayuda2 = FI2,
        ayuda3 = FI3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Las fuerzas internas se definen como las fuerzas que actúan dentro de un elemento y se obtienen mediante un corte teórico en el cuerpo. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Fuerzas internas en B: }}$
        
        Se realiza el corte mostrado en la imagen para encontrar las fuerzas internas en $B$:
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        Se observa que la única reacción de interés para determinar el cortante y el momento flector es $A_y$, dado que, $A_x$ se relaciona con la fuerzas normales internas. El valor de $A_y$ se puede calcular haciendo equilibrio global, formulando la sumatoria de momentos en C:

        ${{\hspace{{4mm}} \\sum{{M_C}} = \\dfrac{{d_2 \\cdot (w_1 - w_2)}}{{2}} \\cdot \\dfrac{{2d_2}}{{3}} + w_2 \\cdot \\dfrac{{(d_2)^2}}{{2}} - \\dfrac{{4F_1}}{{5}} \\cdot d_3 - A_y \\cdot d_2 = 0 }}$     
        ${{\hspace{{4mm}} A_y = \\dfrac{{d_2 \\cdot (w_1 - w_2)}}{{3}} + w_2 \\cdot \\dfrac{{d_2}}{{2}} - \\dfrac{{4F_1 \\cdot d_3}}{{5d_2}}}}$     
        ${{\hspace{{4mm}} A_y = {(-(f[0]*(4/5)*(d[6]+2))+((d[0]+d[3])*(m[1]*0.5)*(d[0]+d[3])/2)+((((50+m[0])-(m[1]*0.5))*(d[0]+d[3])/2)*((2/3)*(d[0]+d[3]))))/(d[0]+d[3]):.2f} \\text{{ kN}}}}$     
        
        De igual manera, se contempla una nueva variable w', la cual, se puede determinar utilizando triángulos semejantes:
        ${{\hspace{{4mm}} \\dfrac{{w' - w_2}}{{d_2 - d_1}} = \\dfrac{{w_1 - w_2}}{{d_2}}}}$     
        ${{\hspace{{4mm}} w' = \\dfrac{{(d_2 - d_1) \\cdot (w_1 - w_2)}}{{d_2}} + w_2}}$      
        ${{\hspace{{4mm}} w' = {(((d[0]+d[3])-d[0])*((50+m[0])-(m[1]*0.5))/(d[0]+d[3]))+(m[1]*0.5):.2f} \\dfrac{{kN}}{{m}} }}$ 

        
        A partir de lo anterior, se calcula tanto la fuerza cortante como el momento flector en $B$:
        
        $\\underline{{Fuerza \\hspace{{2mm}} cortante:}}$
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y - \\dfrac{{d_1 \\cdot (w_1 - w')}}{{2}} - w' \\cdot d_1 - V_B = 0}}$     
        ${{\hspace{{4mm}} V_B = A_y - \\dfrac{{d_1 \\cdot (w_1 - w')}}{{2}} - w' \\cdot d_1}}$     
        ${{\hspace{{4mm}} V_B = {((-(f[0]*(4/5)*(d[6]+2))+((d[0]+d[3])*(m[1]*0.5)*(d[0]+d[3])/2)+((((50+m[0])-(m[1]*0.5))*(d[0]+d[3])/2)*((2/3)*(d[0]+d[3]))))/(d[0]+d[3]))-(d[0]*((((d[0]+d[3])-d[0])*((50+m[0])-(m[1]*0.5))/(d[0]+d[3]))+(m[1]*0.5)))-0.5*d[0]*((50+m[0])-((((d[0]+d[3])-d[0])*((50+m[0])-(m[1]*0.5))/(d[0]+d[3]))+(m[1]*0.5))):.2f} \\text{{ kN}} }}$     
        
        $\\underline{{Momento \\hspace{{2mm}} flector:}}$
        
        ${{\hspace{{4mm}} \\sum{{M_B}} = \\dfrac{{(d_1)^2 \\cdot (w_1 - w')}}{{3}} + w' \\cdot \\dfrac{{(d_1)^2}}{{2}} - A_y \\cdot d_1 + M_B = 0}}$     
        ${{\hspace{{4mm}} M_B = -\\dfrac{{(d_1)^2 \\cdot (w_1 - w')}}{{3}} - w' \\cdot \\dfrac{{(d_1)^2}}{{2}} + A_y \\cdot d_1}}$  
        ${{\hspace{{4mm}} M_B = {((-(f[0]*(4/5)*(d[6]+2))+((d[0]+d[3])*(m[1]*0.5)*(d[0]+d[3])/2)+((((50+m[0])-(m[1]*0.5))*(d[0]+d[3])/2)*((2/3)*(d[0]+d[3]))))/(d[0]+d[3]))*d[0]-(d[0]*((((d[0]+d[3])-d[0])*((50+m[0])-(m[1]*0.5))/(d[0]+d[3]))+(m[1]*0.5)))*(d[0]/2)-d[0]*((50+m[0])-((((d[0]+d[3])-d[0])*((50+m[0])-(m[1]*0.5))/(d[0]+d[3]))+(m[1]*0.5)))*(d[0]/3):.2f} \\text{{ kN}} \\cdot \\text{{ m}}}}$     
        
        $\\textbf{{\\small 2. Fuerzas internas en D: }}$
        
        Se realiza el corte mostrado en la imagen para encontrar las fuerzas internas en D:
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"""
        A partir de la configuración mostrada en la imagen, se calcula fuerza cortante en D:
        
        $\\underline{{Fuerza \\hspace{{2mm}} cortante:}}$
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = V_D - \\dfrac{{4F_1}}{{5}} = 0}}$     
        ${{\hspace{{4mm}} V_D = \\dfrac{{4F_1}}{{5}}}}$     
        ${{\hspace{{4mm}} V_D = {(4/5)*f[0]:.2f} \\text{{ kN}}}}$ 
        """,
        calculos='operations'
        ),

    Questionary(#2_1
        code = 8110021,
        no_pregunta = 2,
        complexity = F,
        topic = "Fuerzas internas",
        subtopic = "Fuerzas internas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"La viga fallará cuando el momento máximo sea $M_{{max}} = {m[0]*(1/5) + 80:.2f} \\text{{ kN}} \\cdot \\text{{ m}}$ o la fuerza cortante máxima sea $V_{{max}} = {d[0] + 30:.0f} \\text{{ kN}}$. Determine la máxima carga distribuida $w$ que la viga puede soportar. Considere $d_1 = {d[3]*(1/2)+5:.2f} \\text{{ m}}$",
        no_answers = 1,
        a1_name = "Carga distribuida $w$ $\\left[\\dfrac{{kN}}{{m}}\\right]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(3*(m[0]*(1/5) + 80)*(1/(pow(d[3]*(1/2)+5,2))),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = FI1,
        ayuda2 = FI2,
        ayuda3 = FI3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Las fuerzas internas se definen como las fuerzas que actúan dentro de un elemento y se obtienen mediante un corte teórico en el cuerpo. A continuación, se presenta la solución sugerida para el ejercicio:
        
        En este ejercicio se puede inferir que tanto el cortante máximo como el momento flector máximo de la viga en voladizo estan ubicados en su único apoyo, por tal motivo, se determinan las reacciones en el apoyo y se fija la condición suministrada:
        
        $\\textbf{{\\small 1. Reacciones en los apoyos: }}$
                
        ${{\hspace{{4mm}} \\sum{{F_x}} = A_x = 0}}$     
             
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y - \\dfrac{{w \\cdot d_1}}{{2}} = 0}}$     
        ${{\hspace{{4mm}} A_y = \\dfrac{{w \\cdot d_1}}{{2}} }}$     
             
        ${{\hspace{{4mm}} \\sum{{M_A}} = M_A - \\dfrac{{w \\cdot d_1}}{{2}} \\cdot \\dfrac{{2d_1}}{{3}} = 0}}$     
        ${{\hspace{{4mm}} M_A = \\dfrac{{w \\cdot (d_1)^2}}{{3}} }}$     
             
        Con dichas reacciones se realizan los siguientes diagramas:
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\textbf{{\\small 3. Evaluación de la condición de resistencia máxima: }}$     
        
        $\\underline{{Cortante \\hspace{{2mm}} máximo:}}$      
        
        ${{\hspace{{4mm}} V_{{max}} = A_y = \\dfrac{{w \\cdot d_1}}{{2}}}}$     
        ${{\hspace{{4mm}} w  = \\dfrac{{2V_{{max}}}}{{d_1}}  }}$     
        ${{\hspace{{4mm}} w  = {2*(d[0] + 30)*(1/(d[3]*(1/2)+5)):.2f} \\dfrac{{ kN}}{{m}}}}$     
                
        $\\underline{{Momento \\hspace{{2mm}} máximo:}}$  
        
        ${{\hspace{{4mm}} M_{{max}} = |M_max| = \\dfrac{{w \\cdot (d_1)^2}}{{3}} }}$     
        ${{\hspace{{4mm}} w = \\dfrac{{3M_{{max}}}}{{(d_1)^2}} }}$     
        ${{\hspace{{4mm}} w =  {3*(m[0]*(1/5) + 80)*(1/(pow(d[3]*(1/2)+5,2))):.2f} \\dfrac{{ kN}}{{m}}}}$     
        
        Finalmente, se selecciona la carga de menor magnitud, dado que, si selecciona la mayor, la viga fallará bajo la otra condición.
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    #=================================================  FUERZAS INTERNAS =========================================================
    #-------------------------------------------------       Fuerzas internas    --------------------------------------------
    #-------------------------------------------------       Nivel Medio    ---------------------------------------------------
    #-------------------------------------------------       Code: 8120011    --------------------------------------------------    
    Questionary(#1_1
        code = 8120011,
        no_pregunta = 1,
        complexity = M,
        topic = "Fuerzas internas",
        subtopic = "Fuerzas internas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine tanto la fuerza cortante como el momento flector en $C$. Considere $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$, $d_3 = {d[6]:.0f} \\text{{ m}}$, $F_1 = {f[0]:.0f}  \\text{{ kN}}$, $w_1 = {m[0]:.0f} \\dfrac{{kN}}{{m}}$ y $w_2 = {m[1]:.2f} \\dfrac{{kN}}{{m}}$.",
        no_answers = 2,
        a1_name = "Fuerza cortante en $C$ $(V_C)$ $[kN]$",
        a2_name = "Momento flector en $C$ $(M_C)$ $[kN \\cdot m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((m[1]*pow((2*d[3] + d[6]),2))*(1/6) + (1/2)*m[0]*d[0]*(2*d[3] + d[6] + d[0]*(1/3)) + f[0]*(d[3]+d[6]))/(d[0] + 2*d[3] + d[6]) - f[0] - m[0]*d[0]*(1/2) - d[3]*((2*m[1]*d[3])/(2*d[3] + d[6])),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-f[0]*d[3] + (((m[1]*pow((2*d[3] + d[6]),2))*(1/6) + (1/2)*m[0]*d[0]*(2*d[3] + d[6] + d[0]*(1/3)) + f[0]*(d[3]+d[6]))/(d[0] + 2*d[3] + d[6]))*(d[0] + 2*d[3]) - (2/3)*d[3]*((2*m[1]*d[3])/(2*d[3] + d[6]))*d[3] - m[0]*d[0]*(1/2)*(2*d[3] + d[0]*(1/3)),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = FI1,
        ayuda2 = FI2,
        ayuda3 = FI3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Las fuerzas internas se definen como las fuerzas que actúan dentro de un elemento y se obtienen mediante un corte teórico en el cuerpo. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Fuerzas internas en C: }}$
        
        Se realiza el corte mostrado en la imagen para encontrar las fuerzas internas en $C$:                     
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        Se observa que la reacción de interés para determinar la fuerza cortante y el momento flector en $C$ es $A_y$. Para determinar su valor, se realiza equilibrio global de la estructura aplicando la sumatoria de momentos respecto al punto $D$:

        ${{\hspace{{4mm}} \\sum{{M_D}} = \\dfrac{{w_2 \\cdot (2d_2 + d_3)^2}}{{6}} + \\dfrac{{w_1 \\cdot d_1}}{{2}} \\cdot (2d_2 + d_3 + \\dfrac{{d_1}}{{3}}) + F_1 \\cdot (d_2 + d_3) - A_y \\cdot (d_1 + 2d_2 + d_3) = 0 }}$     
       
        ${{\hspace{{4mm}} A_y = \\dfrac{{w_2 \\cdot (2d_2 + d_3)^2}}{{6 \\cdot (d_1 + 2d_2 + d_3)}} + \\dfrac{{w_1 \\cdot d_1}}{{2}} \\cdot \\dfrac{{2d_2 + d_3 + \\dfrac{{d_1}}{{3}}}}{{d_1 + 2d_2 + d_3}} + \\dfrac{{F_1 \\cdot (d_2 + d_3)}}{{d_1 + 2d_2 + d_3}}}}$     
        
        ${{\hspace{{4mm}} A_y = {((m[1]*pow((2*d[3] + d[6]),2))*(1/6) + (1/2)*m[0]*d[0]*(2*d[3] + d[6] + d[0]*(1/3)) + f[0]*(d[3]+d[6]))/(d[0] + 2*d[3] + d[6]):.2f} \\text{{ kN}}}}$     
        
        De igual manera, se contempla una nueva variable $w_2'$, la cual puede determinarse aplicando triángulos semejantes:
        
        ${{\hspace{{4mm}} \\dfrac{{w_2}}{{2d_2 + d_3}} = \\dfrac{{w_2'}}{{2d_2}}}}$     
        
        ${{\hspace{{4mm}} w_2' = \\dfrac{{2d_2 \\cdot w_2}}{{2d_2 + d_3}}}}$     
        
        ${{\hspace{{4mm}} w_2' = {(2*m[1]*d[3])/(2*d[3] + d[6]):.2f} \\dfrac{{kN}}{{m}}}}$     
        
        Después, se define el siguiente sistema equivalente, en el que se traslada la fuerza $F_1$ sobre la viga y se aplica el momento correspondiente ($M_1$):  
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"""
        Las fuerzas $F_2$ y $F_3$ y el momento par $M_1$ del sistema son:
        
        ${{\hspace{{4mm}} M_1 = F_1 \\cdot d_2}}$     
        ${{\hspace{{4mm}} M_1 = {f[0]*d[3]:.2f} \\text{{ kN}} \\cdot \\text{{ m}}}}$     
             
        ${{\hspace{{4mm}} F_2 = \\dfrac{{w_1 \\cdot d_1}}{{2}}}}$     
        ${{\hspace{{4mm}} F_2 = {m[0]*d[0]*(1/2):.2f} \\text{{ kN}} }}$     
             
        ${{\hspace{{4mm}} F_3 = w_2' \\cdot d_2}}$     
        ${{\hspace{{4mm}} F_3 = {d[3]*((2*m[1]*d[3])/(2*d[3] + d[6])):.2f} \\text{{ kN}} }}$     
             
                
        $\\underline{{Fuerza \\hspace{{2mm}} cortante:}}$
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y - F_1 - F_2 - F_3 - V_C = 0}}$     
        ${{\hspace{{4mm}} V_C = A_y - F_1 - F_2 - F_3}}$     
        ${{\hspace{{4mm}} V_C = {((m[1]*pow((2*d[3] + d[6]),2))*(1/6) + (1/2)*m[0]*d[0]*(2*d[3] + d[6] + d[0]*(1/3)) + f[0]*(d[3]+d[6]))/(d[0] + 2*d[3] + d[6]) - f[0] - m[0]*d[0]*(1/2) - d[3]*((2*m[1]*d[3])/(2*d[3] + d[6])):.2f} \\text{{ kN}}}}$     
        
        $\\underline{{Momento \\hspace{{2mm}} flector:}}$
        
        ${{\hspace{{4mm}} \\sum{{M_C}} = \\dfrac{{2d_2 \\cdot F_3}}{{3}} + F_2 \\cdot \\left(2d_2 + \\dfrac{{d_1}}{{3}}\\right) - A_y \\cdot (d_1 + 2d_2) + M_1 + M_C = 0}}$     
        
        ${{\hspace{{4mm}} M_C = - M_1 + A_y \\cdot (d_1 + 2d_2) - \\dfrac{{2d_2 \\cdot F_3}}{{3}} - F_2 \\cdot \\left(2d_2 + \\dfrac{{d_1}}{{3}}\\right)}}$     
        
        ${{\hspace{{4mm}} M_C = {-f[0]*d[3] + (((m[1]*pow((2*d[3] + d[6]),2))*(1/6) + (1/2)*m[0]*d[0]*(2*d[3] + d[6] + d[0]*(1/3)) + f[0]*(d[3]+d[6]))/(d[0] + 2*d[3] + d[6]))*(d[0] + 2*d[3]) - (2/3)*d[3]*((2*m[1]*d[3])/(2*d[3] + d[6]))*d[3] - m[0]*d[0]*(1/2)*(2*d[3] + d[0]*(1/3)):.2f} \\text{{ kN}} \\cdot \\text{{ m}}}}$     
        """,
        calculos='operations'
        ),

    # Questionary(#2_1
    #     code = 8120021,
    #     no_pregunta = 2,
    #     complexity = M,
    #     topic = "Fuerzas internas",
    #     subtopic = "Fuerzas internas",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"La viga fallará cuando el momento máximo sea $M_{{max}} = {m[0]:.0f} \\text{{ kN}} \\cdot \\text{{ m}}$ o la fuerza cortante máxima sea $V_{{max}} = {d[0] + 2 :.0f} \\text{{ kN}}$. Determine la máxima carga distribuida $w$ que la viga puede soportar. Considere $d_1 = {3 + d[3]*(1/5):.2f} \\text{{ m}}$ y  $d_2 = {5 + d[6]*(1/5):.2f}  \\text{{ m}}$.",
    #     no_answers = 1,
    #     a1_name = "Carga distribuida $w$ $\\left[\\dfrac{{kN}}{{m}}\\right]$",
    #     a2_name = "",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round((d[0] + 2)/((3 + d[3]*(1/5))*(1/2) + ((5 + d[6]*(1/5))/(6 + d[3]*(2/5)))*(3 + d[3]*(1/5) + (1/3)*(5 + d[6]*(1/5))) - (1/2)*(5 + d[6]*(1/5))),2),
    #     answer2 = lambda f, a, calc, c, d, m: 0,
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = FI1,
    #     ayuda2 = FI2,
    #     ayuda3 = FI3,
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     Las fuerzas internas se definen como las fuerzas que actúan dentro de un elemento y se obtienen mediante un corte teórico en el cuerpo. A continuación, se presenta la solución sugerida para el ejercicio:


    #     $\\textbf{{\\small 1. Reacciones en los apoyos: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{F_x}} = R_{{Ax}} = 0}}$     
             
    #     ${{\hspace{{4mm}} \\sum{{M_A}} = R_{{By}} \\cdot d_1 - w \\cdot \\dfrac{{(d_1)^2}}{{2}} - \\dfrac{{w \\cdot d_2}}{{2}} \\cdot (d_1 + \\dfrac{{d_2}}{{3}}) = 0}}$     
    #     ${{\hspace{{4mm}} R_{{By}} =  w \\cdot \\dfrac{{d_1}}{{2}} + \\dfrac{{w \\cdot d_2}}{{2d_1}} \\cdot (d_1 + \\dfrac{{d_2}}{{3}}) }}$     
             
    #     ${{\hspace{{4mm}} \\sum{{F_y}} = R_{{Ay}} + R_{{By}} - w \\cdot d_1 - \\dfrac{{w \\cdot d_2}}{{2}} = 0}}$     
    #     ${{\hspace{{4mm}} R_{{Ay}} = w \\cdot d_1 + \\dfrac{{w \\cdot d_2}}{{2}} - R_{{By}}}}$     
    #     ${{\hspace{{4mm}} R_{{Ay}} = w \\cdot d_1 + \\dfrac{{w \\cdot d_2}}{{2}} -  w \\cdot \\dfrac{{d_1}}{{2}} - \\dfrac{{w \\cdot d_2}}{{2d_1}} \\cdot (d_1 + \\dfrac{{d_2}}{{3}})}}$     
    #     ${{\hspace{{4mm}} R_{{Ay}} = \\dfrac{{w \\cdot d_2}}{{2}} + w \\cdot \\dfrac{{d_1}}{{2}} - \\dfrac{{w \\cdot d_2}}{{2d_1}} \\cdot (d_1 + \\dfrac{{d_2}}{{3}})}}$     
        
    #     Con las reacciones se realizan los siguientes diagramas:
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"""
    #     Tal que, solo es necesario tener prente las ecuaciones del tramo $A$-$B$ para calcular el momento máximo (puesto se ubica en $x = d_1$), dado que el valor del cortante máximo es $|R_{{Ay}} - w \\cdot d_1|$:
        
    #     $\\textbf{{\\small 2. Fuerzas internas en tramo A-B: }}$
        
    #     Se hace el corte mostrado en la imagen para encontrar las ecuaciones de las fuerzas internas en el tramo $A$-$B$:
    #     """,
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"""
    #     $\\underline{{Fuerza \\hspace{{2mm}} cortante:}}$
        
    #     ${{\hspace{{4mm}} \\sum{{F_y}} = R_{{Ay}} - w \\cdot x - V_1 = 0}}$     
    #     ${{\hspace{{4mm}} V_1 = R_{{Ay}} - w \\cdot x}}$     
        
    #     $\\underline{{Momento \\hspace{{2mm}} flector:}}$
        
    #     ${{\hspace{{4mm}} \\sum{{M_x}} = w \\cdot \\dfrac{{x^2}}{{2}} - R_{{Ay}} \\cdot x + M_1 = 0}}$     
    #     ${{\hspace{{4mm}} M_1 = R_{{Ay}} \\cdot x - w \\cdot \\dfrac{{x^2}}{{2}}}}$     
        
    #     El valor máximo de momento flector es:
        
    #     ${{\hspace{{4mm}} M_{{max}} = R_{{Ay}} \\cdot d_1 - w \\cdot \\dfrac{{(d_1)^2}}{{2}} }}$     
        
    #     $\\textbf{{\\small 3. Evaluación de la condición de resistencia máxima: }}$     
        
    #     $\\underline{{Cortante \\hspace{{2mm}} máximo:}}$      
        
    #     ${{\hspace{{4mm}} V_{{max}} = |R_{{Ay}} - w \\cdot d_1| = |\\dfrac{{w \\cdot d_2}}{{2}} + w \\cdot \\dfrac{{d_1}}{{2}} - \\dfrac{{w \\cdot d_2}}{{2d_1}} \\cdot (d_1 + \\dfrac{{d_2}}{{3}}) - w \\cdot d_1|}}$     
    #     ${{\hspace{{4mm}} V_{{max}} = |\\dfrac{{w \\cdot d_2}}{{2}} - w \\cdot \\dfrac{{d_1}}{{2}} - \\dfrac{{w \\cdot d_2}}{{2d_1}} \\cdot (d_1 + \\dfrac{{d_2}}{{3}})|}}$     
    #     ${{\hspace{{4mm}} V_{{max}} = w \\cdot (\\dfrac{{d_1}}{{2}} + \\dfrac{{d_2}}{{2d_1}} \\cdot (d_1 + \\dfrac{{d_2}}{{3}}) - \\dfrac{{d_2}}{{2}})}}$     
    #     ${{\hspace{{4mm}} w  = \\dfrac{{V_{{max}}}}{{\\dfrac{{d_1}}{{2}} + \\dfrac{{d_2}}{{2d_1}} \\cdot (d_1 + \\dfrac{{d_2}}{{3}}) - \\dfrac{{d_2}}{{2}}}}}}$     
    #     ${{\hspace{{4mm}} w  = {(d[0] + 2)/((3 + d[3]*(1/5))*(1/2) + ((5 + d[6]*(1/5))/(6 + d[3]*(2/5)))*(3 + d[3]*(1/5) + (1/3)*(5 + d[6]*(1/5))) - (1/2)*(5 + d[6]*(1/5))):.2f} \\dfrac{{ kN}}{{m}}}}$     
                
    #     $\\underline{{Momento \\hspace{{2mm}} máximo:}}$  
        
    #     ${{\hspace{{4mm}} M_{{max}} = |R_{{Ay}} \\cdot d_1 - w \\cdot \\dfrac{{(d_1)^2}}{{2}} |}}$     
    #     ${{\hspace{{4mm}} M_{{max}} = |(\\dfrac{{w \\cdot d_2}}{{2}} + w \\cdot \\dfrac{{d_1}}{{2}} - \\dfrac{{w \\cdot d_2}}{{2d_1}} \\cdot (d_1 + \\dfrac{{d_2}}{{3}})) \\cdot d_1 - w \\cdot \\dfrac{{(d_1)^2}}{{2}} |}}$     
    #     ${{\hspace{{4mm}} M_{{max}} = \\dfrac{{w \\cdot d_2}}{{2}} \\cdot (d_1 + \\dfrac{{d_2}}{{3}}) - \\dfrac{{w \\cdot d_2 \\cdot d_1}}{{2}} }}$     
    #     ${{\hspace{{4mm}} M_{{max}} = w \\cdot (\\dfrac{{d_2}}{{2}} \\cdot (d_1 + \\dfrac{{d_2}}{{3}}) - \\dfrac{{d_2 \\cdot d_1}}{{2}} ) }}$     
    #     ${{\hspace{{4mm}} w = \\dfrac{{M_{{max}}}}{{\\dfrac{{d_2}}{{2}} \\cdot (d_1 + \\dfrac{{d_2}}{{3}}) - \\dfrac{{d_2 \\cdot d_1}}{{2}}}} }}$     
    #     ${{\hspace{{4mm}} w =  {(m[0])/((5 + d[6]*(1/5))*(1/2)*(3 + d[3]*(1/5) + (1/3)*(5 + d[6]*(1/5))) - (5 + d[6]*(1/5))*(3 + d[3]*(1/5))*(1/2)):.2f} \\dfrac{{ kN}}{{m}}}}$     
        
        
    #     Finalmente, se selecciona la carga de menor magnitud, dado que, si selecciona la mayor, la viga fallará bajo la otra condición.
    #     """,
    #     calculos='operations'
    #     ),

    Questionary(#3_1
        code = 8120031,
        no_pregunta = 3,
        complexity = M,
        topic = "Fuerzas internas",
        subtopic = "Fuerzas internas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la distancia $d_2$ de la viga colocada simétricamente en los apoyos, de manera que el momento flector interno en el centro de la viga sea cero. Considere $d_1 = {d[0]:.0f} \\text{{ m}}$ y  $w = {m[0]:.2f}  \\dfrac{{N}}{{m}}$.",
        no_answers = 1,
        a1_name = "Distancia $d_2$ [m]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(d[0] + d[0]*math.sqrt(3),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = FI1,
        ayuda2 = FI2,
        ayuda3 = FI3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Las fuerzas internas se definen como las fuerzas que actúan dentro de un elemento y se obtienen mediante un corte teórico en el cuerpo. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Identificar fuerzas aplicadas sobre viga: }}$          
        Antes de analizar la condición suministrada, se deben identificar todas las fuerzas externas y reacciones que actúan sobre la viga. Dado que no existen fuerzas en la dirección horizontal y que la viga está dispuesta simétricamente, se representa la carga distribuida y las reacciones verticales en los apoyos de la siguiente forma:
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        ${{\hspace{{4mm}} F_1 = \\dfrac{{w \\cdot (d_2 - d_1)}}{{4}}}}$     
             
        ${{\hspace{{4mm}} F_2 = w \\cdot d_1}}$     
                   
        ${{\hspace{{4mm}} \\sum{{F_y}} = 2R - 2F_1 - F_2 = 0}}$     
        ${{\hspace{{4mm}} R = F_1 + \\dfrac{{F_2}}{{2}} }}$     
        
        $\\textbf{{\\small 2. Fuerzas internas en el centro de la viga: }}$
        
        Se realiza el corte mostrado en la imagen y luego se determina cuál es el valor de $d_2$, tal que el momento flector interno en el centro de la viga sea cero:
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"""
        ${{\hspace{{4mm}} \\sum{{M_c}} = \\dfrac{{F_2 \\cdot d_1}}{{8}} + F_1 \\cdot (\\dfrac{{d_2 - d_1}}{{6}} + \\dfrac{{d_1}}{{2}}) - \\dfrac{{R \\cdot d_1}}{{2}} + M_c = 0}}$     
        
        ${{\hspace{{4mm}} \\dfrac{{F_2 \\cdot d_1}}{{8}} + F_1 \\cdot \\dfrac{{d_2}}{{6}} + F_1 \\cdot \\dfrac{{d_1}}{{3}} - (F_1 + \\dfrac{{F_2}}{{2}}) \\cdot \\dfrac{{d_1}}{{2}} = 0}}$     
        
        ${{\hspace{{4mm}} F_1 \\cdot \\dfrac{{d_2}}{{6}} - F_1 \\cdot \\dfrac{{d_1}}{{6}} - \\dfrac{{F_2 \\cdot d_1}}{{8}} = 0}}$     
        
        ${{\hspace{{4mm}} \\dfrac{{w \\cdot (d_2 - d_1) \\cdot d_2}}{{24}}  - \\dfrac{{w \\cdot (d_2 - d_1) \\cdot d_1}}{{24}} - \\dfrac{{w \\cdot (d_1)^2}}{{8}} = 0}}$     
        
        ${{\hspace{{4mm}} \\dfrac{{(d_2)^2}}{{24}}  - \\dfrac{{d_2 \\cdot d_1}}{{12}} - \\dfrac{{(d_1)^2}}{{12}} = 0}}$     
        
        ${{\hspace{{4mm}} (d_2)^2  - 2 \\cdot d_2 \\cdot d_1 - 2 \\cdot (d_1)^2 = 0}}$     
        
        La solución es:
        ${{\hspace{{4mm}} d_2 = d_1 \\pm d_1 \\cdot \\sqrt{{3}}}}$     
        
        Tomando el resultado positivo:
        
        ${{\hspace{{4mm}} d_2 = {d[0] + d[0]*math.sqrt(3):.2f} \\text{{ m}}}}$   
        """,
        calculos='operations'
        ),

    #  Questionary(#4_1
    #     code = 8120041,
    #     no_pregunta = 4,
    #     complexity = M,
    #     topic = "Fuerzas internas",
    #     subtopic = "Fuerzas internas",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine las magnitudes de las fuerzas $F_1$ y $F_2$ aplicadas sobre la viga, sabiendo que el momento flector interno en el punto $A$ es $M_A = {-(180 + m[0]*(1/5)):.2f} \\text{{ N}} \\cdot \\text{{ m}}$ y en el punto $B$ es $M_B ={-(135+m[0]*(1/5)):.2f} \\text{{ N}} \\cdot \\text{{ m}}$. Considere $d_1 = {(20+d[0])*(1/100):.2f} \\text{{ m}}$, $d_2 = {(40+d[3])*(1/100):.2f} \\text{{ m}}$, $d_3 = {(70+d[6])*(1/100):.2f} \\text{{ m}}$, y  $w = {(38+d[9])*(1/2):.2f}  \\dfrac{{N}}{{m}}$.",
    #     no_answers = 2,
    #     a1_name = "Fuerza $F_1$ $[N]$",
    #     a2_name = "Fuerza $F_2$ $[N]$",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(((1/2)*((38+d[9])*(1/2))*pow((60+d[3]+d[0])*(1/100),2) + ((45/((20 + d[0])*(1/100))) - (1/2)*((38 + d[9])*(1/2))*(20+d[0])*(1/100) - ((38 + d[9])*(1/2))*(40 + d[3])*(1/100))*((130 + d[0] + d[6] + d[9])*(1/100)) - (180 + m[0]*(1/5)))/((70 + d[6])*(1/100)),2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round(((45/((20 + d[0])*(1/100))) - (1/2)*((38 + d[9])*(1/2))*(20+d[0])*(1/100) - ((38 + d[9])*(1/2))*(40 + d[3])*(1/100)) - ((1/2)*((38+d[9])*(1/2))*pow((60+d[3]+d[0])*(1/100),2) + ((45/((20 + d[0])*(1/100))) - (1/2)*((38 + d[9])*(1/2))*(20+d[0])*(1/100) - ((38 + d[9])*(1/2))*(40 + d[3])*(1/100))*((130 + d[0] + d[6] + d[9])*(1/100)) - (180 + m[0]*(1/5)))/((70 + d[6])*(1/100)),2),
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = FI1,
    #     ayuda2 = FI2,
    #     ayuda3 = FI3,
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     Las fuerzas internas se definen como las fuerzas que actúan dentro de un elemento y se obtienen mediante un corte teórico en el cuerpo. A continuación, se presenta la solución sugerida para el ejercicio:
        
    #     $\\textbf{{\\small 1. Identificar las fuerzas aplicadas sobre la viga - Punto A: }}$

    #     Primero, dado que el momento flector suministrado en el punto $A$ corresponde al valor justo en el apoyo de tercer grado, se infiere que la reacción en momento en dicho apoyo es igual en magnitud pero de signo opuesto, es decir, $M_R = -M_A$. A partir de esto, al aplicar la condición de equilibrio de momentos para toda la estructura, se puede plantear la siguiente ecuación:
         
    #     ${{\hspace{{4mm}} \\sum{{M_A}} = M_R - w \\cdot \\dfrac{{(d_1 + d_2)^2}}{{2}} - F_1 \\cdot (d_1 + d_2) - F_2 \\cdot (d_1 + d_2 + d_3) = 0 }}$          
    #     ${{\hspace{{4mm}} w \\cdot \\dfrac{{(d_1 + d_2)^2}}{{2}} + F_1 \\cdot (d_1 + d_2) + F_2 \\cdot (d_1 + d_2 + d_3) = - M_A }}$         
                 
    #     $\\textbf{{\\small 2. Identificar las fuerzas aplicadas sobre la viga - Punto B: }}$
        
    #     Se realiza el corte en la ubicación mostrada en la imagen para obtener la ecuación del momento flector en el punto $B$ (Teniendo en cuenta que el valor que nos dan de $M_B$ es negativo):
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"""
    #     En esta ecuación, la única incógnita es el valor de $R_y$, ya que no existe ninguna fuerza externa en la dirección horizontal, por lo tanto, no se considera reacción en $X$. El valor de $R_y$ puede determinarse aplicando equilibrio global:

    #     ${{\hspace{{4mm}} \\sum{{F_y}} = R_y - w \\cdot (d_1 + d_2) - F_1 - F_2 = 0}}$     
    #     ${{\hspace{{4mm}} R_y = w \\cdot (d_1 + d_2) + F_1 + F_2}}$     
        
    #     Se obtiene la siguiente ecuación a partir de la sumatoria de momentos en $B$ con el corte realizado:
        
    #     ${{\hspace{{4mm}} \\sum{{M_B}} = M_R - |M_B| - R_y \\cdot d_1 + \\dfrac{{w \\cdot (d_1)^2}}{{2}} = 0}}$     
    #     ${{\hspace{{4mm}} - (M_A +|M_B|) - (w \\cdot (d_1 + d_2) + F_1 + F_2) \\cdot d_1 + \\dfrac{{w \\cdot (d_1)^2}}{{2}} = 0}}$     
    #     ${{\hspace{{4mm}} - \\dfrac{{(M_A + |M_B|)}}{{d_1}} - \\dfrac{{w \\cdot d_1}}{{2}} - w \\cdot d_2 - F_1 = F_2}}$     
        
    #     $\\textbf{{\\small 3. Despeje fuerzas F1 y F2: }}$
        
    #     La ecuación obtenida en el segundo apartado se puede integrar en la de primer apartado, de forma que se logra obtener el resultado de $F_1$:
        
    #     ${{\hspace{{4mm}} w \\cdot \\dfrac{{(d_1 + d_2)^2}}{{2}} + F_1 \\cdot (d_1 + d_2) + (- \\dfrac{{(M_A + |M_B|)}}{{d_1}} - \\dfrac{{w \\cdot d_1}}{{2}} - w \\cdot d_2 - F_1) \\cdot (d_1 + d_2 + d_3) = - M_A }}$         
    #     ${{\hspace{{4mm}} F_1 \\cdot d_3 = w \\cdot \\dfrac{{(d_1 + d_2)^2}}{{2}} - (\\dfrac{{(M_A + |M_B|)}}{{d_1}} + \\dfrac{{w \\cdot d_1}}{{2}} + w \\cdot d_2) \\cdot (d_1 + d_2 + d_3) + M_A }}$         
    #     ${{\hspace{{4mm}} F_1 = {((1/2)*((38+d[9])*(1/2))*pow((60+d[3]+d[0])*(1/100),2) + ((45/((20 + d[0])*(1/100))) - (1/2)*((38 + d[9])*(1/2))*(20+d[0])*(1/100) - ((38 + d[9])*(1/2))*(40 + d[3])*(1/100))*((130 + d[0] + d[6] + d[9])*(1/100)) - (180 + m[0]*(1/5)))/((70 + d[6])*(1/100)):.2f} \\text{{ N}} }}$     
        
    #     Y se determina $F_2$ con la ecuación del segundo apartado:
        
    #     ${{\hspace{{4mm}} F_2 = {((45/((20 + d[0])*(1/100))) - (1/2)*((38 + d[9])*(1/2))*(20+d[0])*(1/100) - ((38 + d[9])*(1/2))*(40 + d[3])*(1/100)) - ((1/2)*((38+d[9])*(1/2))*pow((60+d[3]+d[0])*(1/100),2) + ((45/((20 + d[0])*(1/100))) - (1/2)*((38 + d[9])*(1/2))*(20+d[0])*(1/100) - ((38 + d[9])*(1/2))*(40 + d[3])*(1/100))*((130 + d[0] + d[6] + d[9])*(1/100)) - (180 + m[0]*(1/5)))/((70 + d[6])*(1/100)):.2f} \\text{{ N}} }}$     
    #     """,
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    Questionary(#5_1
        code = 8120051,
        no_pregunta = 5,
        complexity = M,
        topic = FI,
        subtopic = "Fuerzas internas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las magnitudes de la fuerza cortante y el momento flector que actúan sobre la columna en el punto $B$, debido a las fuerzas $F_1 = {f[0]:.0f} \\text{{ kN}}$ y $F_2 = {f[1]:.0f} \\text{{ kN}}$. Considere que $d_0 = {d[0]/4:.2f} \\text{{ m}}$, $d_1 = {d[3]/4:.2f} \\text{{ m}}$ y $d_2 = {d[6]/4:.2f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Fuerza cortante en $B$ $[kN]$",
        a2_name = "Momento en $B$ $[kN \\cdot m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[0]+f[1],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-1*((f[0]+f[1])*(d[0]/4)-(f[0]*((d[0]+d[3])/4)+f[1]*((d[0]+d[3]+d[6])/4))),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = FI1,
        ayuda2 = FI2,      
        ayuda3 = FI3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Las fuerzas internas se definen como las fuerzas que actúan dentro de un elemento y se obtienen mediante un corte teórico en el cuerpo. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Cálculo de las reacciones: }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$            
        ${{\hspace{{4mm}} R_y = 0 \\text{{ kN}}}}$

        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_x}} = -R_x + F_1 + F_2 = 0}}$          
        ${{\hspace{{4mm}} R_x = (F_1 + F_2) \\text{{ kN}} }}$         
        ${{\hspace{{4mm}} R_x = {f[0]+f[1]:.2f} \\text{{ kN}} }}$

        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{M_A}} = M_R - F_1(d_0 + d_1) - F_2(d_0 + d_1 + d_2) = 0 }}$           
        ${{\hspace{{4mm}} M_R = (F_1(d_0 + d_1) + F_2(d_0 + d_1 + d_2)) \\text{{ }} kN \\cdot m }}$           
        ${{\hspace{{4mm}} M_R = {f[0]*((d[0]+d[3])/4)+f[1]*((d[0]+d[3]+d[6])/4):.2f}\\text{{ }} kN \\cdot m }}$

        $\\textbf{{\\small 2. Cortante y Momento flector en B: }}$
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"""
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{F_x}} = V_B - R_x}}$       
        ${{\hspace{{4mm}} V_B = R_x}}$            
        ${{\hspace{{4mm}} V_B = {(f[0]+f[1])} \\text{{ kN}} }}$  

        ${{\hspace{{4mm}} \\sum{{M_B}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{M_B}} = M_B + M_R - R_X(d_0+d_1) }}$          
        ${{\hspace{{4mm}} M_B = R_X \\cdot d_0 - M_R}}$          
        ${{\hspace{{4mm}} M_B = {((f[0]+f[1])*(d[0]/4)-(f[0]*((d[0]+d[3])/4)+f[1]*((d[0]+d[3]+d[6])/4))):.2f}\\text{{ }} kN \\cdot m }}$   
        ${{\hspace{{4mm}} |M_B| = {-1*((f[0]+f[1])*(d[0]/4)-(f[0]*((d[0]+d[3])/4)+f[1]*((d[0]+d[3]+d[6])/4))):.2f}\\text{{ }} kN \\cdot m }}$ 
        """,
        calculos='operations'
    ),

    Questionary(#6_1
        code = 8120061,
        no_pregunta = 6,
        complexity = M,
        topic = FI,
        subtopic = "Fuerzas internas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine las magnitudes de la fuerza cortante y el momento flector inmediatamente después del punto $C$. Considere que la fuerza $F = {f[0]:.0f} \\text{{ kN}}$, el momento $M = {m[0]:.0f} \\text{{ }} kN \\cdot m$, $d_0 = {d[0]:.0f} \\text{{ m}}$ y $d_1 = {d[3]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Fuerza cortante $[kN]$",
        a2_name = "Momento flector $[kN \\cdot m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(-1*((f[0]*d[3]-m[0])/(d[0]+d[3])-f[0]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((f[0]*d[3]-m[0])/(d[0]+d[3])*d[0]+m[0],2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = FI1,
        ayuda2 = FI2,      
        ayuda3 = FI3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Las fuerzas internas se definen como las fuerzas que actúan dentro de un elemento y se obtienen mediante un corte teórico en el cuerpo. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Reacciones: }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$             
        ${{\hspace{{4mm}} A_x = 0 \\text{{ kN}}}}$

        ${{\hspace{{4mm}} \\sum{{M_B}} = 0 }}$              
        ${{\hspace{{4mm}} \\sum{{M_B}} = F \\cdot d_1 - A_y \cdot (d_0 + d_1) - M = 0 }}$                
        ${{\hspace{{4mm}} A_y = \\dfrac{{F \\cdot d_1 - M}}{{(d_0 + d_1)}}}}$                  
        ${{\hspace{{4mm}} A_y = {(f[0]*d[3]-m[0])/(d[0]+d[3]):.2f} \\text{{ kN}} }}$

        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$                  
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + B_y - F = 0}}$            
        ${{\hspace{{4mm}} B_y = F - A_y}}$            
        ${{\hspace{{4mm}} B_y = {f[0]-((f[0]*d[3]-m[0])/(d[0]+d[3])):.2f} \\text{{ kN}} }}$

        
        $\\textbf{{\\small 2. Cortante y Momento flector en C: }}$
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"""
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y - F - V_C(x) = 0 }}$           
        ${{\hspace{{4mm}} V_C(x) = A_y - F \\text{{ kN}} }}$           
        ${{\hspace{{4mm}} V_C(x) = {(f[0]*d[3]-m[0])/(d[0]+d[3])-f[0]:.2f} \\text{{ kN}} }}$          
        ${{\hspace{{4mm}} |V_C(x)| = {-1*((f[0]*d[3]-m[0])/(d[0]+d[3])-f[0]):.2f} \\text{{ kN}} }}$

        ${{\hspace{{4mm}} \\sum{{M}} = 0 }}$               
        ${{\hspace{{4mm}} \\sum{{M}} = M_C(x) - A_y \cdot d_0 - M= 0 }}$             
        ${{\hspace{{4mm}} M_C(x) = A_y \cdot d_0 + M \\text{{ }}}}$                   
        ${{\hspace{{4mm}} M_C = |M_C(x)| = {(f[0]*d[3]-m[0])/(d[0]+d[3])*d[0]+m[0]:.2f} \\text{{ }} kN \\cdot m }}$ 
        """,
        calculos='operations'
        ),
   



    # #=================================================  FUERZAS INTERNAS =========================================================
    #-------------------------------------------------       Fuerzas internas    --------------------------------------------
    #-------------------------------------------------       Nivel Díficil    ---------------------------------------------------
    #-------------------------------------------------       Code: 8130011    --------------------------------------------------
    Questionary(#1_1
        code = 8130011,
        no_pregunta = 1,
        complexity = D,
        topic = "Fuerzas internas",
        subtopic = "Fuerzas internas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la distancia $d_1$, de manera que el momento flector interno máximo en el tramo $AB$ tenga la misma magnitud (valor absoluto) que el momento flector en el punto $B$. Considere los siguientes datos: $d_2 = {d[0]:.0f} \\text{{ m}}$ y $w = {m[0]:.2f} \\dfrac{{N}}{{m}}$.",     
        no_answers = 1,
        a1_name = "Distancia $d_1$ $[m]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(d[0] + d[0]*math.sqrt(3),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = FI4,
        ayuda2 = FI2,
        ayuda3 = FI3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Las fuerzas internas se pueden definir como las fuerzas que actuan dentro de un elemento en respuesta a la aplicación de fuerzas externas. A continuación, se muestra una solución del ejercicio: 
        
        $\\textbf{{\\small 1. Reacciones en los apoyos: }}$
        
        ${{\hspace{{4mm}} \\sum{{M_A}} = B_y \\cdot d_1 - \\dfrac{{w \\cdot (d_2)^2}}{{2}} = 0 }}$     
        ${{\hspace{{4mm}} B_y = \\dfrac{{w \\cdot (d_2)^2}}{{2d_1}} }}$     
             
        ${{\hspace{{4mm}} \\sum{{F_y}} = B_y + A_y - w \\cdot d_2 = 0}}$     
        ${{\hspace{{4mm}} A_y = w \\cdot d_2 - B_y}}$     
        ${{\hspace{{4mm}} A_y = \\dfrac{{w \\cdot d_2}}{{2d_1}} \\cdot (2d_1 - d_2)  }}$     
                
        $\\textbf{{\\small 2. Fuerzas internas en tramo AB: }}$
        
        Se hace el corte mostrado en la imagen :        
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        $\\underline{{Ecuación\\hspace{{2mm}} de \\hspace{{2mm}} cortante:}}$    
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y - w \\cdot x - V_1 = 0}}$     
        ${{\hspace{{4mm}} V_1 = A_y - w \\cdot x }}$     
             
        $\\underline{{Ecuación\\hspace{{2mm}} de \\hspace{{2mm}} momento:}}$    
                    
        ${{\hspace{{4mm}} \\sum{{M_x}} = \\dfrac{{w \\cdot x^2}}{{2}} - A_y \\cdot x + M_1 = 0}}$     
        ${{\hspace{{4mm}} M_1 = A_y \\cdot x - \\dfrac{{w \\cdot x^2}}{{2}}}}$     
        
        $\\textbf{{\\small 3. Momento flector máximo: }}$
        
        El momento máximo en el tramo AB se encontrará justamente cuando $V_1 = 0$, es decir :
        
        ${{\hspace{{4mm}} V_1 = A_y - w \\cdot x = 0}}$     
        ${{\hspace{{4mm}} x = \\dfrac{{A_y}}{{w}}}}$     
                
        Del cuál, se obtiene el valor de momento flector máximo:
        
        ${{\hspace{{4mm}} M_{{max}} = A_y \\cdot \\dfrac{{A_y}}{{w}} - \\dfrac{{w \\cdot (\\dfrac{{A_y}}{{w}})^2}}{{2}}}}$     
        ${{\hspace{{4mm}} M_{{max}} = \\dfrac{{(A_y)^2}}{{2w}}}}$     
        ${{\hspace{{4mm}} M_{{max}} = \\dfrac{{w}}{{8 \\cdot (d_1)^2}} \\cdot (2d_1 \\cdot d_2 - (d_2)^2)^2}}$     
        
        $\\textbf{{\\small 4. Momento flector en B: }}$
        
        Se determina cual es el momento flector en $B$, reemplazando en la ecuación de momento la distancia $d_1$:

        ${{\hspace{{4mm}} M_B = A_y \\cdot d_1 - \\dfrac{{w \\cdot (d_1)^2}}{{2}}}}$     
        ${{\hspace{{4mm}} M_B = \\dfrac{{w}}{{2}} \\cdot (2d_1 \\cdot d_2 - (d_2)^2 - (d_1)^2) }}$     
        ${{\hspace{{4mm}} M_B = - \\dfrac{{w}}{{2}} \\cdot (d_2 - d_1)^2}}$     
        
        
        $\\textbf{{\\small 5. Despeje de d1: }}$
        
        ${{\hspace{{4mm}} |M_B| = |M_{{max}}| }}$     
        ${{\hspace{{4mm}} \\dfrac{{w}}{{2}} \\cdot (d_2 - d_1)^2 = \\dfrac{{w}}{{8 \\cdot (d_1)^2}} \\cdot (2d_1 \\cdot d_2 - (d_2)^2)^2 }}$     
        ${{\hspace{{4mm}} 4 \\cdot (d_1)^2 \\cdot (d_2 - d_1)^2 = (2d_1 \\cdot d_2 - (d_2)^2)^2 }}$     
        ${{\hspace{{4mm}} 2 \\cdot d_1 \\cdot (d_2 - d_1) = 2d_1 \\cdot d_2 - (d_2)^2 }}$     
        ${{\hspace{{4mm}} d_1 = \\dfrac{{d_2}}{{\\sqrt{{2}}}}}}$     
        ${{\hspace{{4mm}} d_1 = {d[0]/(math.sqrt(2)) :.2f} \\text{{ m}}}}$   
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),
    
    Questionary(#2_1
        code = 8130021,
        no_pregunta = 2,
        complexity = D,
        topic = FI,
        subtopic = "Fuerzas internas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza cortante y el momento flector a la distancia $x = {d[0]:.0f} \\text{{ m}}$ medida desde el apoyo $B$ hacia la izquierda. Considere que $W_1 = {f[0]+7:.0f} \\text{{ }} \\dfrac{{kN}}{{m}}$, $W_2 = {f[0]:.0f} \\text{{ }} \\dfrac{{kN}}{{m}}$ y $d_0 = {d[0]+3:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Fuerza cortante $[kN]$",
        a2_name = "Momento flector $[kN \\cdot m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(abs(((((f[0]+7)-(f[0]))/(d[0]+3))*d[0])*0.5*(d[0])+(f[0]*d[0])-((((7*(d[0]+3))/2)/3)+((f[0]*(d[0]+3))/2))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(abs(((((7*(d[0]+3))/2)/3)+((f[0]*(d[0]+3))/2))*d[0]-f[0]*d[0]*d[0]/2-((((f[0]+7)-(f[0]))/(d[0]+3))*d[0])*(d[0]**2)/6),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = FI1,
        ayuda2 = FI2,      
        ayuda3 = FI3,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Las fuerzas internas se definen como las fuerzas que actúan dentro de un elemento y se obtienen mediante un corte teórico en el cuerpo. A continuación, se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Reacción en el apoyo B: }}$

        Dado que el punto en el cual se solicita la fuerza cortante y el momento flector es con respecto al apoyo $B$, se considera la sección de la viga ubicada a la izquierda de dicho punto. Por lo tanto, únicamente es de interés conocer la reacción en el apoyo $B$.       
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        ${{\hspace{{4mm}} F_1 =  \\dfrac{{(W_1 - W_2) * d_0}}{{2}}}}$         
        ${{\hspace{{4mm}} F_1 =  {(7*(d[0]+3))/2:.2f} \\text {{ kN}} }}$      

        ${{\hspace{{4mm}} F_2 = W_2 * d_0  }}$            
         ${{\hspace{{4mm}} F_2 =  {f[0]*(d[0]+3):.2f} \\text {{ kN}} }}$


        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$        
        ${{\hspace{{4mm}} \\sum{{M_A}} = -F_1 \\cdot \\dfrac{{d_0}}{{3}} - F_2 \\cdot \\dfrac{{d_0}}{{2}} + B_y \\cdot d_0 = 0 }}$           
        ${{\hspace{{4mm}} B_y \\cdot d_0 = F_1 \\cdot \\dfrac{{d_0}}{{3}} + F_2 \\cdot \\dfrac{{d_0}}{{2}}}}$              
        ${{\hspace{{4mm}} B_y = \\dfrac{{F_1}}{{3}} + \\dfrac{{F_2}}{{2}} }}$     
        ${{\hspace{{4mm}} B_y = {(((7*(d[0]+3))/2)/3)+((f[0]*(d[0]+3))/2):.2f} \\text {{ kN}} }}$              

        $\\textbf{{\\small 2. Cálculo de la fuerza cortante y el momento flector: }}$  
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"""
        Se contempla una nueva variable W', la cual, se puede determinar utilizando triángulos semejantes:

        ${{\hspace{{4mm}} \\dfrac{{W_1 - W_2}}{{d_0}} = \\dfrac{{W'}}{{x}}}}$     
        ${{\hspace{{4mm}} W' = \\left(\\dfrac{{W_1 - W_2}}{{d_0}}\\right) x}}$      
        ${{\hspace{{4mm}} W' = {(((f[0]+7)-(f[0]))/(d[0]+3))*d[0]:.2f} \\dfrac{{kN}}{{m}} }}$ 

        
        A partir de lo anterior, se calcula tanto la fuerza cortante como el momento flector:
        
        $\\underline{{Fuerza \\hspace{{2mm}} cortante:}}$
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = V + B_y - W_2 \\cdot x - \\dfrac{{W' \\cdot x}}{{2}} = 0}}$     
        ${{\hspace{{4mm}} V =  W_2 \\cdot x + \\dfrac{{W' \\cdot x}}{{2}} - B_y}}$     
        ${{\hspace{{4mm}} V = {((((f[0]+7)-(f[0]))/(d[0]+3))*d[0])*0.5*(d[0])+(f[0]*d[0])-((((7*(d[0]+3))/2)/3)+((f[0]*(d[0]+3))/2)):.2f} \\text{{ kN}} }}$     
        
        $\\underline{{Momento \\hspace{{2mm}} flector:}}$
        
        ${{\hspace{{4mm}} \\sum{{M}} = -M + B_y \\cdot x - W_2 \\cdot \\dfrac{{x^2}}{{2}} - W' \\cdot \\dfrac{{x^2}}{{6}}= 0}}$     
        ${{\hspace{{4mm}} M = B_y \\cdot x - W_2 \\cdot \\dfrac{{x^2}}{{2}} - W' \\cdot \\dfrac{{x^2}}{{6}} }}$  
        ${{\hspace{{4mm}} M = {((((7*(d[0]+3))/2)/3)+((f[0]*(d[0]+3))/2))*d[0]-f[0]*d[0]*d[0]/2-((((f[0]+7)-(f[0]))/(d[0]+3))*d[0])*(d[0]**2)/6:.2f} \\text{{ kN}} \\cdot \\text{{ m}}}}$     


        """,
        calculos='operations'
        ), 

    Questionary(#3_1
        code = 8130031,
        no_pregunta = 3,
        complexity = D,
        topic = FI,
        subtopic = "Fuerzas internas",
        version = 1,
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza cortante y el momento flector a la distancia $x = {d[0]+d[3]-0.5:.2f} \\text{{ m}}$ medida desde el apoyo $A$. Considere que $W_1 = {f[0]:.0f} \\text{{ }} \\dfrac {{N}}{{m}}$, $W_2 = {f[1]:.0f} \\text{{ }} \\dfrac {{N}}{{m}}$, $F = {f[2]:.0f} \\text{{ }} N$, $d_0 = {d[0]:.0f} \\text{{ m}}$, $d_1 = {d[3]:.0f} \\text{{ m}}$, $d_2 = {d[6]:.0f} \\text{{ m}}$ y $d_3 = {d[9]:.0f} \\text{{ m}}$.",
        no_answers = 2,
        a1_name = "Fuerza cortante a la distancia $x$ $[N]$",
        a2_name = "Momento flector a la distancia $x$ $[N \\cdot m]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(f[2]+f[1]*d[9]/2,2),
        answer2 = lambda f, a, calc, c, d, m: np.round(abs(f[1]*d[9]*0.5*(d[6]+(d[9]/3)+0.5))+f[2]*0.5,2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = FI2,
        ayuda2 = FI3,      
        ayuda3 = FI5,
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Las fuerzas internas se definen como las fuerzas que actúan dentro de un elemento y se obtienen mediante un corte teórico en el cuerpo. A continuación, se presenta la solución sugerida para el ejercicio:
        
        La forma más sencilla de solucionar este ejercicio es seleccionar la sección derecha de la viga, dado que, esto evita tener que hallar las reacciones en el empotramiento.
              
        $\\textbf{{\\small 1. Cálculo de la fuerza cortante y el momento flector: }}$
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"""
        
        La distancia $d$ es equivalente a :

        ${{\hspace{{4mm}} d = d_0+d_1+d_2+d_3-x }}$          
        ${{\hspace{{4mm}} d = {d[0]+d[3]+d[6]+d[9]-(d[0]+d[3]-0.5):.2f} \\text{{ N}} }}$          

        $\\underline{{Fuerza \\hspace{{2mm}} cortante:}}$

        ${{\hspace{{4mm}} \\sum{{F_y}}=V-\\dfrac{{W_2 \\cdot d_3}}{{2}}-F=0 }}$            
        ${{\hspace{{4mm}} V=\\dfrac{{W_2 \\cdot d_3}}{{2}}+F }}$    
        ${{\hspace{{4mm}} V={f[1]*d[9]*0.5+f[2]:.2f} \\text{{ N}} }}$

        $\\underline{{Momento \\hspace{{2mm}} flector:}}$

        ${{\hspace{{4mm}} \\sum{{M}}=-M-\\dfrac{{W_2 \\cdot d_3}}{{2}} \\cdot \\left(0,5+d_2+\\dfrac{{d_3}}{{3}}\\right)-F \\cdot 0,5=0 }}$   
        ${{\hspace{{4mm}} M=-\\dfrac{{W_2 \\cdot d_3}}{{2}} \\cdot \\left(0,5+d_2+\\dfrac{{d_3}}{{3}}\\right) -  F \\cdot 0,5}}$   
        ${{\hspace{{4mm}} M={-f[1]*d[9]*0.5*(d[6]+(d[9]/3)+0.5)-f[2]*0.5:.2f} \\text{{ }} N \\cdot m }}$            
        ${{\hspace{{4mm}} |M|={abs(-f[1]*d[9]*0.5*(d[6]+(d[9]/3)+0.5)-f[2]*0.5):.2f} \\text{{ }} N \\cdot m }}$
        """,
        respuesta_P3 = lambda f, a, calc, c, d, m: f"""
        """,
        calculos='operations'
        ),

    ]