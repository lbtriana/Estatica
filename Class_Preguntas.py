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
        pregunta = lambda f, a, calc, c, d, m: f"Determine el momento en el punto A de la fuerza $F_1$ y $F_2$. Considere que $F_1 = {f[0]:.0f} \\text{{ lb}}$, $F_2 = {f[1]:.0f} \\text{{ lb}}$, $\\alpha_1 = {a[0]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ ft}}$,  $X_2 = {d[3]:.0f}  \\text{{ ft}}$ y $X_3 = {d[6]:.0f} \\text{{ ft}}$.",
        no_answers = 2,
        a1_name = "Momento en A de la fuerza F1 [$lb \\cdot ft$]",
        a2_name = "Momento en A de la fuerza F2 [$lb \\cdot ft$]",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(-f[0]*d[0],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-f[1]*calc['sin1']*(d[0]+d[3]),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector posición $\\overrightarrow{{r}}$. A continuación, se presenta la solución sugerida para el ejercicio:  

        $\\textbf{{\\small 1. Descomposición de las fuerzas F1 y F2:}}$

        $\\underline{{Fuerza \\hspace{{2mm}} F_1 :}}$ La fuerza $F_1$ solo tiene componente en Y y es igual a su magnitud. 

        $\\underline{{Fuerza  \\hspace{{2mm}} F_2 :}}$ 

        ${{\hspace{{4mm}} F_2x = |\\overrightarrow{{F_2}}| \\cdot \\cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ lb}}}}}}$     
        ${{\hspace{{4mm}} F_2y = |\\overrightarrow{{F_2}}| \\cdot \\sin(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ lb}}}}}}$    

        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        En este caso, los vectores posición solo tienen componente en la dirección X, y son equivalentes a la magnitud de las distancias de A al punto de acción de la fuerza:      
        
        ${{\hspace{{4mm}} r_1 \\text{{ = }} X_1 = {d[0]:.0f}{{ \\text{{ ft}}}}}}$     
        ${{\hspace{{4mm}} r_2 \\text{{ = }} X_1 + X_2 = {(d[0]+d[3]):.0f}{{ \\text{{ ft}}}}}}$     

        Ahora solo es necesario operar utilizando la ecuación de momento según las componentes necesarias y denotando el signo acorde a la regla de la mano de derecha: 

        $\\textbf{{\\small 3. Cálculo del momento en el punto A:}}$ 

        $\\underline{{Momento \\hspace{{2mm}} de \\hspace{{2mm}} la \\hspace{{2mm}} fuerza \\hspace{{2mm}} F1:}}$

        Teniendo en cuenta que el vector posición y la fuerza $F_1$ ya son perpendiculares entre sí, y que, por la regla de la mano de derecha el momento es negativo (en sentido horario):

        ${{\hspace{{4mm}} M_1 = - |\\overrightarrow{{r_1}}| \\cdot |\\overrightarrow{{F_1}}| = -{d[0]:.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[0]:.0f}{{\\text{{ lb }}}}}}$     
        ${{\hspace{{4mm}} M_1 = {-f[0]*d[0]:.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}$     

        $\\underline{{Momento \\hspace{{2mm}} de \\hspace{{2mm}} la \\hspace{{2mm}} fuerza \\hspace{{2mm}} F2:}}$

        En el momento de la fuerza F2, la componente de la fuerza que es perpendicular al vector posición es $F2_y$, y por la regla de la mano de derecha el momento es negativo: 

        ${{\hspace{{4mm}} M_2 = \\overrightarrow{{r_2}} X \\overrightarrow{{F_2}} = -r_2 \\cdot\\hspace{{1mm}} F_2y = - {(d[3]+d[0]):.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['sin1']:.2f}{{\\text{{ lb}}}}}}$      
        ${{\hspace{{4mm}} M_2 = {-(f[1]*calc['sin1']*(d[0]+d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ft}}}}}}$  
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
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de las fuerzas $F_1$ y $F_2$, si en el punto D el momento que ejerce la fuerza $F1$ es ${m[0]:.0f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}$, y el momento que ejerce la fuerza $F2$ es ${m[1]:.0f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}$. Considere que $\\alpha_1 = {a[0]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ ft}}$,  $X_2 = {d[3]:.0f}  \\text{{ ft}}$ y $X_3 = {d[6]:.0f} \\text{{ ft}}$.",
        no_answers = 2,
        a1_name = "Fuerza $F_1 [lb]$",
        a2_name = "Fuerza $F_2 [lb]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((m[0])/(d[3]+d[6]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((m[1])/(d[6]*calc['sin1']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular un momento en un punto en especifico, primero se obtiene las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, se identifica la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector posición $\\overrightarrow{{r}}$. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Determinación del vector posición asociado a cada fuerza: }}$ 
        
        En este caso, los vectores posición solo tienen componente en la dirección X y son equivalentes a la magnitud de las distancias de D al punto de acción de la fuerza. 

        ${{\hspace{{4mm}} r_1 = X_2 + X_3 = {d[3] + d[6]:.0f}{{\\text{{ ft}}}}}}$       
        ${{\hspace{{4mm}} r_2 = X_3 = {(d[6]):.0f}{{\\text{{ ft}}}}}}$      
        
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

        ${{\hspace{{4mm}} F_1 = ( \\dfrac{{{m[0]:.0f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}{{{d[3]+d[6]:.0f}{{\\text{{ ft}}}}}} ) }}$      

        ${{\hspace{{4mm}} F_1  = {(m[0])/(d[3]+d[6]):.2f}{{\\text{{ lb}}}}}}$      
        
        $\\underline{{Fuerza  \\hspace{{2mm}} F_2 :}}$ 
        
        Se desarrolla el mismo procedimiento que con la fuerza $F_1$, se define la ecuación de momento en D de la fuerza F2 y se verifica su sentido con la regla de la mano de derecha el momento es positivo (en sentido antihorario).
        
        ${{\hspace{{4mm}} M2_D  = \\overrightarrow{{r2}} X \\overrightarrow{{F2}} = |\\overrightarrow{{r2}}| \\cdot |\\overrightarrow{{F2}}| \\cdot sen(\\alpha_1)}}$   

        ${{\hspace{{4mm}} F_2 = \\dfrac{{M_{{2D}}}}{{r_2 \\cdot sen(\\alpha_1)}}}}$      

        ${{\hspace{{4mm}} F_2 = ( \\dfrac{{{m[1]:.0f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}{{{d[6]*calc['sin1']:.2f}{{\\text{{ ft}}}}}} ) }}$      

        ${{\hspace{{4mm}} F_2  = {(m[1])/(d[6]*calc['sin1']):.2f}{{\\text{{ lb}}}}}}$      
        
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
        pregunta = lambda f, a, calc, c, d, m: f"Determine el momento en el punto B de la fuerza $F1$ y $F2$, y el momento en C de la fuerza $F2$. Considere que $F_1 = {f[0]:.0f} \\text{{ lb}}$, $F_2 = {f[1]:.0f} \\text{{ lb}}$, $\\alpha_1 = {a[0]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ ft}}$,  $X_2 = {d[3]:.0f}  \\text{{ ft}}$ y $X_3 = {d[6]:.0f} \\text{{ ft}}$.",
        no_answers = 3,
        a1_name = "Momento en B de la fuerza $F1$ [$lb \\cdot ft$]",
        a2_name = "Momento en B de la fuerza $F2$ [$lb \\cdot ft$]",
        a3_name = "Momento en C de la fuerza $F2$ [$lb \\cdot ft$]",
        answer1 = lambda f, a, calc, c, d, m: np.round(-f[0]*d[3],2),
        answer2 = lambda f, a, calc, c, d, m: np.round(-f[1]*calc['cos1']*(d[0]),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(-(f[1]*calc['cos1']*(d[0]+d[3])),2),
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector posición $\\overrightarrow{{r}}$. A continuación, se presenta la solución sugerida para el ejercicio:  

        $\\textbf{{\\small 1. Descomposición de las fuerzas F1 y F2:}}$

        $\\underline{{Fuerza \\hspace{{2mm}} F1:}}$ La fuerza $F1$ solo tiene componente en Y y es igual a su magnitud. 

        $\\underline{{Fuerza \\hspace{{2mm}} F2:}}$ 
        
        ${{\hspace{{4mm}} F_{{2x}} = |\\overrightarrow{{F_2}}| \\cdot sen(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ lb}}}}}}$       
        ${{\hspace{{4mm}} F_{{2y}} = |\\overrightarrow{{F_2}}| \\cdot cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ lb}}}}}}$          
        
        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

       En este caso, los vectores posición solo tienen componente en la dirección X y son equivalentes a la magnitud de las distancias de D al punto de acción de la fuerza: 

        ${{\hspace{{4mm}} r_{{1B}} = X_2 = {d[3]:.0f}{{ \\text{{ ft}}}}}}$      
        ${{\hspace{{4mm}} r_{{2B}} = X_1 = {d[0]:.0f}{{ \\text{{ ft}}}}}}$      
        ${{\hspace{{4mm}} r_{{2C}} = X_1 + X_2 = {d[0] +d[3]:.0f}{{ \\text{{ ft}}}}}}$       

        $\\textbf{{\\small 3. Cálculo de los momentos: }}$ 

        $\\underline{{Momento \\hspace{{2mm}} en \\hspace{{2mm}} B \\hspace{{2mm}} de \\hspace{{2mm}} la \\hspace{{2mm}} fuerza \\hspace{{2mm}} F_1:}}$ 

        Se tiene en cuenta que el vector posición y la fuerza $F_1$ son perpendiculares entre sí, y que, por la regla de la mano de derecha el momento es negativo (en sentido horario): 

        ${{\hspace{{4mm}} M_{{1B}} = -|\\overrightarrow{{r_{{1B}}}}| \\cdot |\\overrightarrow{{F1}}| = -{d[3]:.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[0]:.0f}{{\\text{{ lb}}}}}}$       
        ${{\hspace{{4mm}} M_{{1B}} = {-f[0]*d[3]:.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}$     

        $\\underline{{Momento \\hspace{{2mm}} en \\hspace{{2mm}} B \\hspace{{2mm}} de \\hspace{{2mm}} la \\hspace{{2mm}} fuerza \\hspace{{2mm}} F_2:}}$ 

        La componente de la fuerza $F_2$ que genera momento en el punto B es $F2_y$, la cual es perpendicular al vector posición $r_{{2B}}. Por la regla de la mano de derecha, el momento es negativo (en sentido horario): 

        ${{\hspace{{4mm}} M_{{2B}} = \\overrightarrow{{r_{{2B}}}} X \\overrightarrow{{F_2}} = r{{2B}} \\cdot\\hspace{{1mm}} F_{{2y}} = -{(d[0]):.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['cos1']:.2f}{{\\text{{ lb}}}}}}$      
        ${{\hspace{{4mm}} M_{{2B}} = {-(f[1]*calc['cos1']*(d[0])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$    
        
        $\\underline{{Momento \\hspace{{2mm}} en \\hspace{{2mm}} C \\hspace{{2mm}} de \\hspace{{2mm}} la \\hspace{{2mm}} fuerza \\hspace{{2mm}} F_2 :}}$ 

       De manera simular al punto B, el momento en C de la fuerza $F_2$ es generado por la componente perpendicular al vector posición, es decir, $F2_y$. Según la regla de la mano de derecha, el momento es negativo (en sentido horario):  
        
        ${{\hspace{{4mm}} M_{{2C}} = \\overrightarrow{{r_{{2C}}}} X \\overrightarrow{{F_2}} = r_{{2C}} \\cdot\\hspace{{1mm}} F_{{2y}} = -{(d[0]+d[3]):.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['cos1']:.2f}{{\\text{{ lb}}}}}}$      
        ${{\hspace{{4mm}} M_{{2C}} = {-(f[1]*calc['cos1']*(d[0]+d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$    
        
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
        pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza $F1$ y la distancia $X1$, si en el punto B el momento de $F_1$ es ${-m[0]:.2f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}$, y el momento de $F_2$ es ${-m[1]:.2f}{{\\text{{ ft}} \\cdot\\text{{ lb}}}}$. Considere que $\\alpha_1 = {a[0]:.0f}°$, $F_2 = {f[1]:.0f} \\text{{ lb}}$,  $X_2 = {d[3]:.0f}  \\text{{ ft}}$ y $X_3 = {d[6]:.0f} \\text{{ ft}}$.",
        no_answers = 2,
        a1_name = "Fuerza $F_1 [lb]$",
        a2_name = "Distancia $X_1 [ft]$",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((m[0])/d[3]),2),
        answer2 = lambda f, a, calc, c, d, m: np.round((m[1])/(f[1]*calc['cos1']),2),
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular un momento en un punto en especifico, primero se obtiene las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, se identifica la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector posición $\\overrightarrow{{r}}$. A continuación, se presenta la solución sugerida para el ejercicio:
        
        Para hallar la fuerza $F_1$ se define la ecuación del momento que esta ejerce en el punto B. Por otra parte, la distancia $X_1$ se calcula mediante la ecuación del momento que ejerce la fuerza $F_2$ en el punto B.
        
        $\\textbf{{\\small 1. Determinación del vector posición asociado a cada fuerza: }}$ 
        
        En este caso, los vectores posición solo tiene componente en X y son equivalentes a la magnitud de las distancias de B al punto de acción de la fuerza. 

        ${{\hspace{{4mm}} r_1 = X_2 = {d[3]:.0f}{{\\text{{ ft}}}}}}$    
        ${{\hspace{{4mm}} r_2 = X_1}}$
        
        $\\textbf{{\\small 2. Descomposición de las fuerzas F1 y F2: }}$
       
        $\\underline{{Fuerza \\hspace{{2mm}} F1 :}}$ La fuerza $F_1$ solo tiene componente en Y y es igual a su magnitud. 

        $\\underline{{Fuerza \\hspace{{2mm}} F2 :}}$ 

        ${{\hspace{{4mm}} F_{{2x}} = |\\overrightarrow{{F_2}}| \\cdot sen(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[1]*calc['sin1']:.2f}{{ \\text{{ lb}}}}}}$      
        ${{\hspace{{4mm}} F_{{2y}} = |\\overrightarrow{{F_2}}| \\cdot \\cos(\\alpha_1) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[1]*calc['cos1']:.2f}{{ \\text{{ lb}}}}}}$     
        
        $\\textbf{{\\small 3. Cálculo de la fuerza F1: }}$ 
        
        Se define la ecuación de momento en B de la fuerza F1. De acuedo con la regla de la mano de derecha el momento es negativo (sentido horario).
        
        ${{\hspace{{4mm}} M_{{1B}}  = \\overrightarrow{{r_1}} X \\overrightarrow{{F_1}} = - r_1 \\cdot |\\overrightarrow{{F_1}}| }}$ 

        ${{\hspace{{4mm}} F1 = -\\dfrac{{M_{{1d}}}}{{r_1}}}}$ 

        ${{\hspace{{4mm}} F1 = -( \\dfrac{{{-m[0]:.0f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}{{{d[3]:.0f}{{\\text{{ ft}}}}}} ) }}$    

        ${{\hspace{{4mm}} F1  = {(m[0])/d[3]:.2f}{{\\text{{ lb}}}}}}$     
        
        $\\textbf{{\\small 4. Cálculo de la distancia X1: }}$ 
        
       Se define la ecuación de momento en B de la fuerza $F_2$. Según la regla de la mano de derecha el momento es negativo (sentido horario).
        
        ${{\hspace{{4mm}} M_{{2B}}  = \\overrightarrow{{r_2}} X \\overrightarrow{{F_2}} = -r_2 \\cdot |\\overrightarrow{{F_2}}| \\cdot \\cos(\\alpha_1)}}$     

        ${{\hspace{{4mm}} X_1 = r2 = - \\dfrac{{M_{{2B}}}}{{F_2 \\cdot \\cos(\\alpha_1)}}}}$      

        ${{\hspace{{4mm}} X_1 = -( \\dfrac{{{-m[1]:.0f}{{\\text{{ lb}} \\cdot\\text{{ ft}}}}}}{{{f[1]*calc['cos1']:.2f}{{ \\text{{ lb}}}}}} ) }}$  

        ${{\hspace{{4mm}} X_1  = {(m[1])/(f[1]*calc['cos1']):.2f}{{\\text{{ ft}}}}}}$    
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    # Questionary(#5_1
    #     code = 2110051,
    #     no_pregunta = 5,
    #     complexity = F,
    #     topic = MO,
    #     subtopic = M2D,
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Calcule el momento alrededor del origen $\\textit{{O}}$ de la fuerza $\\overrightarrow{{F}} = [ {c[0]:.0f}\\hat{{i}} + ( {c[3]:.0f} ) \\hat{{j}} ] {{ \\text{{ kN}}}}$ que actua en un punto A. Evalue cuando el vector posición es  $ \\overrightarrow{{r_a}} = [ {d[2]:.0f}\\hat{{i}} + {d[5]:.0f}\\hat{{j}} ]{{ \\text{{ m}}}}$ ; $\\overrightarrow{{r_b}} = [( {d[8]:.0f} )\\hat{{i}} + {d[11]:.0f}\\hat{{j}} ]{{ \\text{{ m}}}}$.",
    #     no_answers = 2,
    #     a1_name = "Momento usando $\\overrightarrow{{r_a}}$ [kN \\cdot m]",
    #     a2_name = "Momento usando $\\overrightarrow{{r_b}}$ [kN \\cdot m]",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(d[2]*c[3]-d[5]*c[0],2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round(d[8]*c[3]-d[11]*c[0],2),
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
    #     ayuda2 = "Recordar que los signos de los componentes de r y F son importantes para determinar la dirección correcta del momento.",      
    #     ayuda3 = "",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. A continuación, se presenta la solución sugerida:  

    #     En el ejercicio planteado hay que notar que se suministra las componentes de la Fuerza y del Vector posición tal que se puede resolver haciendo el producto cruz. 
        
    #     Sin embargo, como se esta trabajando en 2 dimensiones el momento solo va a tener una componente con vector unitario $\\hat{{k}}$ que es perpendicular al plano y su obtenicón sera multiplicando las componentes perpendiculares entre si del Vector Fuerza y vector Posición. Tal que:
        
    #     ${{\hspace{{4mm}} M = \\overrightarrow{{r_x}} \\cdot \\overrightarrow{{F_y}} - \\overrightarrow{{r_y}} \\cdot \\overrightarrow{{F_x}}}}$
        
    #     A partir de lo anterior, se puede facilmente encontrar el momento asociado a cada Vector posición otorgado por el enunciado:
        
    #     $\\textbf{{\\small 1. Momento usando \\overrightarrow{{r_a}}:}}$
        
    #     ${{\hspace{{4mm}} M = \\overrightarrow{{r_x}} \\cdot \\overrightarrow{{F_y}} - \\overrightarrow{{r_y}} \\cdot \\overrightarrow{{F_x}} = ( {d[2]:.0f}{{ \\text{{ m}}}} \\cdot {c[3]:.0f}{{ \\text{{ kN }}}} ) - ( {d[5]:.0f}{{ \\text{{ m}}}} \\cdot {c[0]:.0f}{{ \\text{{ kN}}}} ) }}$     
    #     ${{\hspace{{4mm}} M = {d[2]*c[3]-d[5]*c[0]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$    
        
    #     $\\textbf{{\\small 2. Momento usando \\overrightarrow{{r_b}}:}}$
        
    #     ${{\hspace{{4mm}} M = \\overrightarrow{{r_x}} \\cdot \\overrightarrow{{F_y}} - \\overrightarrow{{r_y}} \\cdot \\overrightarrow{{F_x}} = ( {d[8]:.0f}{{ \\text{{ m}}}} \\cdot {c[3]:.0f}{{ \\text{{ kN}}}} ) - ( {d[11]:.0f}{{ \\text{{ m}}}} \\cdot {c[0]:.0f}{{ \\text{{ kN}}}} ) }}$     
    #     ${{\hspace{{4mm}} M = {d[8]*c[3]-d[11]*c[0]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$            
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),
    
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
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
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
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
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

    # Questionary(#5_1
    #     code = 2120051,
    #     no_pregunta = 5,
    #     complexity = M,
    #     topic = MO,
    #     subtopic = M2D,
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Calcule la suma de momentos alrededor del origen $\\textit{{O}}$ de las fuerza $\\overrightarrow{{F_1}} = [ {c[0]:.0f}\\hat{{i}} + ( {c[3]:.0f} ) \\hat{{j}} ] {{ \\text{{ kN}}}}$ que actua en un punto A con vector posición \\overrightarrow{{r_a}} = [ {d[2]:.0f}\\hat{{i}} + ( {d[5]:.0f} )\\hat{{j}} ]{{ \\text{{ m}}}}$ y la fuerza $\\overrightarrow{{F_2}} = [ {c[4]:.0f}\\hat{{i}} + ( {c[1]:.0f} ) \\hat{{j}} ] {{ \\text{{ kN}}}}$ que actua en un punto B, con vector posición  $\\overrightarrow{{r_b}} = [( {d[8]:.0f} )\\hat{{i}} + {d[11]:.0f}\\hat{{j}} ]{{ \\text{{ m}}}}$.",
    #     no_answers = 2,
    #     a1_name = "Momento en el origen [kN \\cdot m]",
    #     a2_name = "",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round((d[2]*c[3]-d[5]*c[0]) + (d[8]*c[1]-d[11]*c[4]),2),
    #     answer2 = lambda f, a, calc, c, d, m: 0,
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
    #     ayuda2 = "Recordar que los signos de los componentes de r y F son importantes para determinar la dirección correcta del momento.",      
    #     ayuda3 = "",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. A continuación, se presenta la solución sugerida:  

    #     En el ejercicio planteado hay que notar que otorga las componentes de la Fuerza y del Vector posición tal que se puede resolver haciendo el producto cruz. 
        
    #     Sin embargo, como se esta trabajando en 2 dimensiones el momento solo va a tener una componente con vector unitario $\\hat{{k}}$ que es perpendicular al plano y su obtenicón sera multiplicando las componentes perpendiculares entre si del Vector Fuerza y vector Posición. Tal que:
        
    #     $\\textbf{{\\small 1. Momento causado por \\overrightarrow{{F_1}}:}}$
        
    #     ${{\hspace{{4mm}} M_1 = \\overrightarrow{{r_x}} \\cdot \\overrightarrow{{F1_y}} - \\overrightarrow{{r_y}} \\cdot \\overrightarrow{{F1_x}} = ( {d[2]:.0f}{{ \\text{{ m }}}}\\cdot {c[3]:.0f}{{ \\text{{ kN }}}} ) - ( {d[5]:.0f}{{ \\text{{ m }}}}\\cdot {c[0]:.0f}{{ \\text{{ kN}}}} )}}$     
    #     ${{\hspace{{4mm}} M_1 = {(d[2]*c[3]-d[5]*c[0]):.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$    
        
    #     $\\textbf{{\\small 2. Momento causado por \\overrightarrow{{F_2}}:}}$
        
    #     ${{\hspace{{4mm}} M_2 = \\overrightarrow{{r_x}} \\cdot \\overrightarrow{{F2_y}} - \\overrightarrow{{r_y}} \\cdot \\overrightarrow{{F2_x}} = ( {d[8]:.0f}{{ \\text{{ m }}}} \\cdot {c[1]:.0f}{{ \\text{{ kN }}}} ) - ( {d[11]:.0f}{{ \\text{{ m}}}}\\cdot {c[4]:.0f}{{ \\text{{ kN}}}} )}}$     
    #     ${{\hspace{{4mm}} M_2 = {(d[8]*c[1]-d[11]*c[4]):.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$
        
    #     $\\textbf{{\\small 3. Sumatoria de momentos:}}$ 
        
    #     ${{\hspace{{4mm}} M_O = M_1 + M_2 = {(d[2]*c[3]-d[5]*c[0]):.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}} + {(d[8]*c[1]-d[11]*c[4]):.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$      
    #     ${{\hspace{{4mm}} M_O = {(d[2]*c[3]-d[5]*c[0]) + (d[8]*c[1]-d[11]*c[4]):.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$      
                   
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    
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
        pregunta = lambda f, a, calc, c, d, m: f"Si el trabajador ubicado en B ejerce una fuerza  $F_2 = {f[1]:.0f} \\text{{ lb}}$ sobre su cuerda, determine la magnitud de la fuerza $F_1$ que debe aplicar el trabajador en C para evitar que el poste gire. Se sabe que $\\alpha_1 = {a[0]:.0f}°$, $\\alpha_2 = {a[4]:.0f}°$, $Y_1 = {d[0]:.0f} \\text{{ ft}}$ y $Y_2 = {d[3]:.0f}  \\text{{ ft}}$.",
        no_answers = 1,
        a1_name = "Fuerza $F_1$ $[lb]$",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[1]*calc['cos5']*(d[0]+d[3]))/(d[0]*calc['sin1']),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Para que el poste no gire, es necesario que la suma de momentos en el punto A sea igual a cero, garantizando así que el sistema está en equilibrio. A continuación, se presenta la solución sugerida para el ejercicio:
        
        $\\textbf{{\\small 1. Descomposición de las fuerzas:}}$

        $\\underline{{Fuerza  \\hspace{{2mm}} F1:}}$ 
        
        ${{\hspace{{4mm}} |F_{{1x}}| = |\\overrightarrow{{F_1}}| \\cdot \\sin(\\alpha_1)}}$       
        ${{\hspace{{4mm}} |F_{{1y}}| = |\\overrightarrow{{F_1}}| \\cdot \\cos(\\alpha_1)}}$       

        $\\underline{{Fuerza  \\hspace{{2mm}} F2:}}$ 

        ${{\hspace{{4mm}} |F_{{2x}}| = |\\overrightarrow{{F_2}}| \\cdot \\cos(\\alpha_2) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos5']:.2f} = {f[1]*calc['cos5']:.2f}{{ \\text{{ lb}}}}}}$      
        ${{\hspace{{4mm}} |F_{{2y}}| = |\\overrightarrow{{F_2}}| \\cdot \\sin(\\alpha_2) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin5']:.2f} = {f[1]*calc['sin5']:.2f}{{ \\text{{ lb}}}}}}$      

        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        ${{\hspace{{4mm}} r_1 \\text{{ = }} Y_1 = {d[0]:.0f}{{ \\text{{ ft}}}}}}$     
        ${{\hspace{{4mm}} r_2 \\text{{ = }} Y_1 + Y_2 = {(d[0]+d[3]):.0f}{{ \\text{{ ft}}}}}}$  
        
        $\\textbf{{\\small 3. Cálculo de los momentos generados por F1 y F2:}}$ 

        $\\underline{{Momento \\hspace{{2mm}} Fuerza \\hspace{{2mm}} F1:}}$ 

        La componente perpendicular al vector posición asociado $r_1$ es $F_{{1x}}$. Por la Regla de la mano de derecha el momento es negativo (sentido horario).

        ${{\hspace{{4mm}} M_{{1A}} = - r_1 \\cdot |\\overrightarrow{{F_1}}| \\cdot \\sin(\\alpha_1) = - {d[0]:.0f}{{ \\text{{ ft}}}} \\cdot |\\overrightarrow{{F_1}}| \\cdot {calc['sin1']:.2f}}}$
        
        $\\underline{{Momento \\hspace{{2mm}} Fuerza \\hspace{{2mm}} F2:}}$ 

        La componente de la fuerza que es perpendicular al vector posición es $F_{{2x}}$. De acuerdo con la regla de la mano de derecha el momento es positivo (sentido antihorario). 

        ${{\hspace{{4mm}} M_{{2A}} = \\overrightarrow{{r_2}} X \\overrightarrow{{F_2}} = r2 \\cdot\\hspace{{1mm}} F2_y = {(d[0]+d[3]):.0f}{{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['cos5']:.2f}{{\\text{{ lb}}}}}}$     
        ${{\hspace{{4mm}} M_{{2A}} = {(f[1]*calc['cos5']*(d[0]+d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$    
        
        $\\textbf{{\\small 4. Sumatoria de momentos en A: }}$ 

        Se plantea la condición de equilibrio al igualar la sumatoria de momentos en A a 0.
        
        ${{\hspace{{4mm}} \\sum M_A = M_{{1A}} + M_{{2A}} = 0}}$      

        ${{\hspace{{4mm}} - {d[0]:.0f}{{ \\text{{ ft}}}} \\cdot |\\overrightarrow{{F_1}}| \\cdot {calc['sin1']:.2f} + {(f[1]*calc['cos5']*(d[0]+d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} = 0}}$

        ${{\hspace{{4mm}} {d[0]*calc['sin1']:.2f}{{ \\text{{ ft}}}} \\cdot |\\overrightarrow{{F_1}}| = {(f[1]*calc['sin5']*(d[0]+d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$     

        ${{\hspace{{4mm}} |\\overrightarrow{{F_1}}| = \\dfrac{{{(f[1]*calc['cos5']*(d[0]+d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}{{{d[0]*calc['sin1']:.2f}{{ \\text{{ ft}}}}}}}}$     

        ${{\hspace{{4mm}} |\\overrightarrow{{F_1}}| = {(f[1]*calc['cos5']*(d[0]+d[3]))/(d[0]*calc['sin1']):.2f}{{ \\text{{ lb}}}}}}$     
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
        pregunta = lambda f, a, calc, c, d, m: f"Si el trabajador ubicado en B ejerce una fuerza  $F_2 = {f[1]:.0f} \\text{{ lb}}$ sobre su cuerda, y el que está ubicado en C realiza otra fuerza $F_1 = {f[0]:.0f} \\text{{ lb}}$, determine la magnitud la distancia en la que la fuerza F1 se debe aplicar para evitar quer gire el poste.  $\\alpha_1 = {a[0]:.0f}°$, $\\alpha_2 = {a[4]:.0f}°$ y $X_2 = {d[3]:.0f}  \\text{{ ft}}$.",
        no_answers = 1,
        a1_name = "Distancia X1 [ft]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((f[1]*calc['cos5']*(d[3]))/(f[0]*calc['sin1']-f[1]*calc['cos5'])),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
        ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
        ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector. A continuación, vamos a resolver el ejercicio usando esta definición:  

        Inicialmente, observamos que para que la condición del enunciado se cumpla es necesario que la suma de momentos en A sea igual a cero.
        
        $\\textbf{{\\small 1. Descomposición de las fuerzas:}}$

        $\\underline{{Fuerza  \\hspace{{2mm}} F1 :}}$ 
        
        ${{\hspace{{4mm}} |F1_x| = |\\overrightarrow{{F1}}| \\cdot \\sin(\\alpha_1) = {f[0]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[0]*calc['sin1']:.2f}{{ \\text{{ lb}}}}}}$             
        ${{\hspace{{4mm}} |F1_y| = |\\overrightarrow{{F1}}| \\cdot \\cos(\\alpha_1) = {f[0]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[0]*calc['cos1']:.2f}{{ \\text{{ lb}}}}}}$            

        $\\underline{{Fuerza  \\hspace{{2mm}} F2 :}}$ 

        ${{\hspace{{4mm}} |F2_x| = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_2) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos5']:.2f} = {f[1]*calc['cos5']:.2f}{{ \\text{{ lb}}}}}}$      
        ${{\hspace{{4mm}} |F2_y| = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_2) = {f[1]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin5']:.2f} = {f[1]*calc['sin5']:.2f}{{ \\text{{ lb}}}}}}$      

        $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

        ${{\hspace{{4mm}} r1 \\text{{ = }} X_1 }}$     
        ${{\hspace{{4mm}} r2 \\text{{ = }} X_1 + X_2 = X_1 + {(d[3]):.0f}{{ \\text{{ ft}}}}}}$  
        
        $\\textbf{{\\small 3.1 Momento de la fuerza F1: }}$ 

        Para calcular el momento de F1 en A vemos que la componente perpendicular al vector posición asociado r1 es $F1_x$, y que por la $\\textit{{Regla de la mano de derecha}}$ el momento sera negativo. Tal que: 

        ${{\hspace{{4mm}} M1_A = - r1 \\cdot |\\overrightarrow{{F1}}| \\cdot \\sin(\\alpha_1) = - X_1 \\cdot {f[0]*calc['sin1']:.2f}{{ \\text{{ lb}}}}}}$
        
        $\\textbf{{\\small 3.2 Momento de la fuerza F2: }}$ 

        En el momento de la fuerza F2, notamos que la componente de la fuerza que es perpendicular al vector posición es $F2_x$, y por la $\\textit{{Regla de la mano de derecha}}$ el momento es positivo. Tal que podemos considerar: 

        ${{\hspace{{4mm}} M2_A = \\overrightarrow{{r_2}} X \\overrightarrow{{F2}} = r2 \\cdot\\hspace{{1mm}} F2_x = ( X_1 + {(d[3]):.0f} ){{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]*calc['cos5']:.2f}{{\\text{{ lb}}}}}}$     
        ${{\hspace{{4mm}} M2_A = ( X_1 \\cdot\\hspace{{1mm}}{f[1]*calc['cos5']:.2f}{{\\text{{ lb}}}} + {(f[1]*calc['cos5']*(d[3])):.2f} ) {{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$    
        
        $\\textbf{{\\small 4. Sumatoria de momentos en A: }}$ 

        Hacemos sumatoria de momentos en A y la igualamos a cero: 
        
        ${{\hspace{{4mm}} \\sum M_A = M1_A + M2_A = 0}}$      
        ${{\hspace{{4mm}} - X_1 \\cdot {f[0]*calc['sin1']:.2f}{{ \\text{{ lb}}}} + X_1 \\cdot\\hspace{{1mm}}{f[1]*calc['cos5']:.2f}{{\\text{{ lb}}}} +{(f[1]*calc['cos5']*(d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} = 0}}$         
        ${{\hspace{{4mm}} X_1 \\cdot ({f[0]*calc['sin1']:.2f}{{ \\text{{ lb}}}} - {f[1]*calc['cos5']:.2f}{{\\text{{ lb}}}}) = {(f[1]*calc['cos5']*(d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$     
        ${{\hspace{{4mm}} X_1 = \\dfrac{{{(f[1]*calc['cos5']*(d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}{{{f[0]*calc['sin1']-f[1]*calc['cos5']:.2f}{{\\text{{ lb}}}}}}}}$     
        ${{\hspace{{4mm}} X_1 = {(f[1]*calc['cos5']*(d[3]))/(f[0]*calc['sin1']-f[1]*calc['cos5']):.2f}{{ \\text{{ ft}}}}}}$     
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    # Questionary(#3_1
    #     code = 2130031,
    #     no_pregunta = 3,
    #     complexity = D,
    #     topic = MO,
    #     subtopic = M2D,
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Si el trabajador ubicado en B ejerce una fuerza  $F_2 = {f[1]:.0f} \\text{{ lb}}$ sobre su cuerda, y el que está ubicado en C realiza otra fuerza $F_1 = {f[0]:.0f} \\text{{ lb}}$. Calcular el ángulo asociado a la fuerza F2 para evitar que gire el poste. Considerar $\\alpha_1 = {a[0]:.0f}°$, $X_1 = {d[0]:.0f} \\text{{ ft}}$  y $X_2 = {d[3]:.0f}  \\text{{ ft}}$.",
    #     no_answers = 1,
    #     a1_name = "Ángulo $\\alpha_2 [°]",
    #     a2_name = "",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.arccosine((d[0]*f[0]*calc['sin1'])/(f[1]*(d[0]+d[3]))),2),
    #     answer2 = lambda f, a, calc, c, d, m: 0,
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
    #     ayuda2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación.",      
    #     ayuda3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 2 dimensiones es más fácil calcular el momento como la multiplicación de las componentes de la fuerza perpendiculares a las componentes del vector. A continuación, vamos a resolver el ejercicio usando esta definición:  

    #     Inicialmente, se observa que para que la condición del enunciado se cumpla es necesario que la suma de momentos en A sea igual a cero.
        
    #     $\\textbf{{\\small 1. Descomposición de las fuerzas:}}$

    #     $\\underline{{Fuerza  \\hspace{{2mm}} F1 :}}$ 
        
    #     ${{\hspace{{4mm}} |F1_x| = |\\overrightarrow{{F1}}| \\cdot \\sin(\\alpha_1) = {f[0]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['sin1']:.2f} = {f[0]*calc['sin1']:.2f}{{ \\text{{ lb}}}}}}$             
    #     ${{\hspace{{4mm}} |F1_y| = |\\overrightarrow{{F1}}| \\cdot \\cos(\\alpha_1) = {f[0]:.0f}{{\\text{{ lb }} \\cdot\\hspace{{1mm}}}}{calc['cos1']:.2f} = {f[0]*calc['cos1']:.2f}{{ \\text{{ lb}}}}}}$            

    #     $\\underline{{Fuerza  \\hspace{{2mm}} F2 :}}$ 

    #     ${{\hspace{{4mm}} |F2_x| = |\\overrightarrow{{F2}}| \\cdot \\cos(\\alpha_2) = {f[1]:.0f}{{\\text{{ lb }}}} \\cdot \\cos(\\alpha_2) }}$      
    #     ${{\hspace{{4mm}} |F2_y| = |\\overrightarrow{{F2}}| \\cdot \\sin(\\alpha_2) = {f[1]:.0f}{{\\text{{ lb }}}} \\cdot \\sin(\\alpha_2) }}$      

    #     $\\textbf{{\\small 2. Obtención del vector posición:}}$ 

    #     ${{\hspace{{4mm}} r1 \\text{{ = }} X_1 = {d[0]:.0f}{{ \\text{{ ft}}}}}}$     
    #     ${{\hspace{{4mm}} r2 \\text{{ = }} X_1 + X_2 = {(d[0]+d[3]):.0f}{{ \\text{{ ft}}}}}}$      
        
    #     $\\textbf{{\\small 3.1 Momento de la fuerza F1: }}$ 

    #     Para calcular el momento de F1 en A vemos que la componente perpendicular al vector posición asociado r1 es $F1_x$, y que por la Regla de la mano de derecha el momento sera negativo (Sentido horario). Tal que: 

    #     ${{\hspace{{4mm}} M1_A = - r1 \\cdot |\\overrightarrow{{F1}}| \\cdot \\sin(\\alpha_1) = - {d[0]:.0f}{{ \\text{{ ft}}}} \\cdot {f[0]*calc['sin1']:.2f}{{ \\text{{ lb}}}}}}$     
    #     ${{\hspace{{4mm}} M1_A = - {d[0]*f[0]*calc['sin1']:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$     
        
    #     $\\textbf{{\\small 3.2 Momento de la fuerza F2: }}$ 

    #     En el momento de la fuerza F2, notamos que la componente de la fuerza que es perpendicular al vector posición r2 es $F2_x$, y por la Regla de la mano de derecha el momento es positivo (Sentido antihorario). Tal que podemos considerar: 

    #     ${{\hspace{{4mm}} M2_A = \\overrightarrow{{r_2}} X \\overrightarrow{{F2}} = r2 \\cdot\\hspace{{1mm}} F2_x = {(d[0] + d[3]):.0f} {{ \\text{{ ft}}}} \\cdot\\hspace{{1mm}}{f[1]:.0f}{{\\text{{ lb }}}} \\cdot \\cos(\\alpha_2)}}$     
    #     ${{\hspace{{4mm}} M2_A = ( \\cos(\\alpha_2)\\cdot\\hspace{{1mm}}{(f[1]*(d[0]+d[3])):.2f} ) {{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$    
        
    #     $\\textbf{{\\small 4. Sumatoria de momentos en A: }}$ 

    #     Hacemos sumatoria de momentos en A y la igualamos a cero: 
        
    #     ${{\hspace{{4mm}} \\sum M_A = M1_A + M2_A = 0}}$      
    #     ${{\hspace{{4mm}}  - {d[0]*f[0]*calc['sin1']:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} + ( \\cos(\\alpha_2)\\cdot\\hspace{{1mm}}{(f[1]*(d[0]+d[3])):.2f} ) {{\\text{{ lb}} \\cdot \\text{{ ft}}}} = 0}}$         
    #     ${{\hspace{{4mm}} ( \\cos(\\alpha_2)\\cdot\\hspace{{1mm}}{(f[1]*(d[0]+d[3])):.2f} ) {{\\text{{ lb}} \\cdot \\text{{ ft}}}} = {d[0]*f[0]*calc['sin1']:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} }}$     
    #     ${{\hspace{{4mm}} \\cos(\\alpha_2) = ( \\dfrac{{{d[0]*f[0]*calc['sin1']:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}{{{(f[1]*(d[0]+d[3])):.2f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}} ) }}$     
    #     ${{\hspace{{4mm}} \\alpha_2 = arcocoseno ( \\dfrac{{{d[0]*f[0]*calc['sin1']:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}{{{(f[1]*(d[0]+d[3])):.2f} {{\\text{{ lb}} \\cdot \\text{{ ft}}}}}} ) }}$
    #     ${{\hspace{{4mm}} \\alpha_2 = {Calculations.arccosine((d[0]*f[0]*calc['sin1'])/(f[1]*(d[0]+d[3]))):.2f}°}}     
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    # Questionary(#4_1
    #     code = 2130041,
    #     no_pregunta = 4,
    #     complexity = D,
    #     topic = MO,
    #     subtopic = M2D,
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Calcule la componente en X de una fuerza $\\overrightarrow{{F_1}}$ que tiene como componente en Y, $\\overrightarrow{{F1_y}} = {c[3]:.0f}{{ \\text{{ kN}}}}$, sí la suma de momentos alrededor del origen $\\textit{{O}}$ debe ser igual a cero. Considere que la fuerza $F_1$ actua en un punto A con vector posición \\overrightarrow{{r_a}} = [ {d[2]:.0f}\\hat{{i}} + {(d[3]):.0f}\\hat{{j}} ]{{ \\text{{ m}}}}$ y existe una segunda fuerza $\\overrightarrow{{F_2}} = [ {c[4]:.0f}\\hat{{i}} + ( {c[1]:.0f} ) \\hat{{j}} ] {{ \\text{{ kN}}}}$ que actua en un punto B, con vector posición  $\\overrightarrow{{r_b}} = [( {d[8]:.0f} )\\hat{{i}} + {d[11]:.0f}\\hat{{j}} ]{{ \\text{{ m}}}}$.",
    #     no_answers = 2,
    #     a1_name = "Componente en X de $F_1$ [kN \\cdot m]",
    #     a2_name = "",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round((d[2]*c[3] + d[8]*c[1] - d[11]*c[4])/(d[3]),2),
    #     answer2 = lambda f, a, calc, c, d, m: 0,
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}} se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
    #     ayuda2 = "Recordar que los signos de los componentes de r y F son importantes para determinar la dirección correcta del momento.",      
    #     ayuda3 = "",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. A continuación, se presenta la solución sugerida:  

    #     Para este ejercicio es necesario plantear la sumatoria de fuerzas igualda a cero, para finalizar despejando $\\overrightarrow{{F1_x}}$:
        
    #     $\\textbf{{\\small 1. Momento causado por \\overrightarrow{{F_1}}:}}$
        
    #     ${{\hspace{{4mm}} M_1 = \\overrightarrow{{r_x}} \\cdot \\overrightarrow{{F1_y}} - \\overrightarrow{{r_y}} \\cdot \\overrightarrow{{F1_x}} = ( {d[2]:.0f}{{ \\text{{ m }}}} \\cdot {c[3]:.0f}{{ \\text{{ kN }}}} ) - ( {d[3]:.0f}{{ \\text{{ m }}}} \\cdot \\overrightarrow{{F1_x}} )}}$     
    #     ${{\hspace{{4mm}} M_1 = {d[2]*c[3]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}} - ( {d[3]:.0f}{{ \\text{{ m }}}} \\cdot \\overrightarrow{{F1_x}} ) }}$    
        
    #     $\\textbf{{\\small 2. Momento causado por \\overrightarrow{{F_2}}:}}$
        
    #     ${{\hspace{{4mm}} M_2 = \\overrightarrow{{r_x}} \\cdot \\overrightarrow{{F2_y}} - \\overrightarrow{{r_y}} \\cdot \\overrightarrow{{F2_x}} = ( {d[8]:.0f}{{ \\text{{ m }}}}  \\cdot {c[1]:.0f}{{ \\text{{ kN }}}} )  - ( {d[11]:.0f}{{ \\text{{ m }}}} \\cdot {c[4]:.0f}{{ \\text{{ kN}}}} )}}$     
    #     ${{\hspace{{4mm}} M_2 = {d[8]*c[1]-d[11]*c[4]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}$
        
    #     $\\textbf{{\\small 3. Sumatoria de momentos:}}$ 
        
    #     ${{\hspace{{4mm}} M_O = M_1 + M_2 = ( {d[2]*c[3]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}} - ( {d[3]:.0f}{{ \\text{{ m }}}} \\cdot \\overrightarrow{{F1_x}} )  ) + ( {d[8]*c[1]-d[11]*c[4]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}} ) = 0 }}$      
    #     ${{\hspace{{4mm}} ( {d[3]:.0f}{{ \\text{{ m }}}} \\cdot \\overrightarrow{{F1_x}} ) = ( {d[2]*c[3]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}} ) + ( {d[8]*c[1]-d[11]*c[4]:.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}} )}}$      
    #     ${{\hspace{{4mm}} \\overrightarrow{{F1_x}} = \\dfrac{{{(d[2]*c[3] + d[8]*c[1] - d[11]*c[4]):.2f}{{\\text{{ kN}} \\cdot\\text{{ m}}}}}}{{{d[3]:.0f}{{ \\text{{ m }}}}}}}}$          
    #     ${{\hspace{{4mm}} \\overrightarrow{{F1_x}} = {(d[2]*c[3] + d[7]*c[1] - d[11]*c[4])/(d[3]):.2f}{{ \\text{{ kN}}}}}}$
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),


    #========================================================  MOMENTO  =========================================================
    #--------------------------------------------     Momento en un punto en 3D      --------------------------------------------
    #-------------------------------------------------       Nivel facil    ---------------------------------------------------
    #-------------------------------------------------       Code: 2210011    ---------------------------------------------------

    # Questionary(#1_1
    #     code = 2210011,
    #     no_pregunta = 1,
    #     complexity = F,
    #     topic = MO,
    #     subtopic = M3D,
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine el momento en el origen de la fuerza $F_1$, y expreselo en vector cartesiano. Considere que $F_1 = [ {d[9]:.0f}\\hat{{i}} + {d[12]:.0f} \\hat{{j}} + ( {d[1]:.0f} ) \\hat{{k}} ] \\text{{ lb}}$, $d_1 = {d[3]:.0f} \\text{{ ft}}$,  $d_2 = {d[0]:.0f}  \\text{{ ft}}$ y $d_3 = {d[6]:.0f} \\text{{ ft}}$.",
    #     no_answers = 3,
    #     a1_name = "Componente $\\hat{{i}}$ del momento en el origen [$lb \\cdot ft$]",
    #     a2_name = "Componente $\\hat{{j}}$ del momento en el origen [$lb \\cdot ft$]",
    #     a3_name = "Componente $\\hat{{k}}$ del momento en el origen [$lb \\cdot ft$]",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(d[3]*d[1]+d[6]*d[12],2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round(-(d[0]*d[1])-d[6]*d[9],2),
    #     answer3 = lambda f, a, calc, c, d, m: np.round((d[0]*d[12])-(d[3]*d[9]),2),
    #     ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
    #     ayuda2 = "Recordar que los signos de los componentes de $\\overrightarrow{{r}}$  y $\\overrightarrow{{F}}$ son importantes para determinar la dirección correcta del momento; recordando que el vector momento no solo indicamagnitud, sino también el eje alrededor del cual se produce la rotación el cual es perpendicular tanto al vector $\\overrightarrow{{r}}$ como $\\overrightarrow{{F}}$.",      
    #     ayuda3 = "Se puede dividir el problema en componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$, y resolver de manera independiente las componentes del momento.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones es más fácil calcular el momento resolviendo producto cruz y dividiendo el ejercicios en determinar las componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$. A continuación, se presenta la solución sugerida para el ejercicio:      

    #     $\\textbf{{\\small 1. Obtención del vector posición:}}$       
        
    #     ${{\hspace{{4mm}} r_x = d_2 = {d[0]:.0f}{{ \\text{{ ft}}}}}}$     
    #     ${{\hspace{{4mm}} r_y = d_1 = {d[3]:.0f}{{ \\text{{ ft}}}}}}$      
    #     ${{\hspace{{4mm}} r_z = - d_3 = {-d[6]:.0f}{{ \\text{{ ft}}}}}}$        

    #     $\\textbf{{\\small 2. Calculo del momento en el origen: }}$  
        
    #     $\\underline{{Componente \\hspace{{2mm}} \\hat{{i}} :}}$
        
    #     $\\underline{{Componente \\hspace{{2mm}} \\hat{{i}} :}}$
        
    #     Haciendo Producto Cruz, la componente \\hat{{i}} del momento se puede calcular como:
        
    #     ${{\hspace{{4mm}} M_i = r_y \\cdot F_z - r_z \\cdot F_y = {d[3]:.0f}{{ \\text{{ ft}}}} \\cdot ( {d[1]:.0f} ){{ \\text{{ lb}}}} - ( {-d[6]:.0f}{{ \\text{{ ft}}}} ) \\cdot {d[12]:.0f}{{ \\text{{ lb}}}}}}$       
    #     ${{\hspace{{4mm}} M_i = ( {d[3]*d[1]:.0f} ){{ \\text{{ lb}}}} \\cdot {{ \\text{{ ft}}}} - ( {-( d[6]*d[12]) :.0f} ) {{ \\text{{ lb}}}} \\cdot {{ \\text{{ ft}}}}}}$     
    #     ${{\hspace{{4mm}} M_i = {d[3]*d[1]+d[6]*d[12]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$       
        
    #     $\\underline{{Componente \\hspace{{2mm}} \\hat{{j}} :}}$
        
    #     Haciendo Producto Cruz, la componente \\hat{{j}} del momento se puede calcular como:
        
    #     ${{\hspace{{4mm}} M_j = - ( r_x \\cdot F_z - r_z \\cdot F_x ) = -( {d[0]:.0f}{{ \\text{{ ft}}}} \\cdot ( {d[1]:.0f} ){{ \\text{{ lb}}}} - ( {-d[6]:.0f}{{ \\text{{ ft}}}} ) \\cdot {d[9]:.0f}{{ \\text{{ lb}}}} )}}$       
    #     ${{\hspace{{4mm}} M_j = ( {-(d[0]*d[1]):.0f} ){{ \\text{{ lb}}}} \\cdot {{ \\text{{ ft}}}} - ( {d[6]*d[9]:.0f} ) {{ \\text{{ lb}}}} \\cdot {{ \\text{{ ft}}}} }}$     
    #     ${{\hspace{{4mm}} M_j = {-(d[0]*d[1])-d[6]*d[9]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$      
        
    #     $\\underline{{Componente \\hspace{{2mm}} \\hat{{k}} :}}$
        
    #     Haciendo Producto Cruz, la componente \\hat{{k}} del momento se puede calcular como:
        
    #     ${{\hspace{{4mm}} M_k =  r_x \\cdot F_y - r_y \\cdot F_x  = {d[0]:.0f}{{ \\text{{ ft}}}} \\cdot {d[12]:.0f} {{ \\text{{ lb}}}} - {d[3]:.0f}{{ \\text{{ ft}}}} \\cdot {d[9]:.0f}{{ \\text{{ lb}}}}}}$       
    #     ${{\hspace{{4mm}} M_k =  {(d[0]*d[12]):.0f}{{ \\text{{ lb}}}} \\cdot {{ \\text{{ ft}}}} - {d[3]*d[9]:.0f} {{ \\text{{ lb}}}} \\cdot {{ \\text{{ ft}}}} }}$      
    #     ${{\hspace{{4mm}} M_k = {(d[0]*d[12])-d[3]*d[9]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$    
        
    #     Finalmente, se puede decir que el momento que causa $F_1$ en el origen es  $ [ {d[3]*d[1]+d[6]*d[12]:.0f}\\hat{{i}} + ( {-(d[0]*d[1])-d[6]*d[9]:.0f}) \\hat{{j}} + ({(d[0]*d[12])-d[3]*d[9]:.0f})\\hat{{k}} ]{{ \\text{{ lb}}}} \\cdot {{ \\text{{ ft}}}}$
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    # Questionary(#2_1
    #     code = 2210021,
    #     no_pregunta = 2,
    #     complexity = F,
    #     topic = MO,
    #     subtopic = M3D,
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de $d_1$ y $d_2$  si el momento en el origen que causa $F_1$ es de $ [ {-m[0]:.0f}\\hat{{i}} + ( {-m[1]:.0f}) \\hat{{j}} + ({ (f[1]*m[1]+m[0]*f[0])/(-f[2]):.0f})\\hat{{k}} ]{{ \\text{{ lb}}}} \\cdot {{ \\text{{ ft}}}}$. Considere que $F_1 = [ {f[0]:.0f}\\hat{{i}} + {f[1]:.0f} \\hat{{j}} + ( {-f[2]:.0f} ) \\hat{{k}} ] \\text{{ lb}}$ y $d_3 = {d[6]:.0f} \\text{{ ft}}$.",
    #     no_answers = 2,
    #     a1_name = "d_1 [ft]",
    #     a2_name = "d_2 [ft]",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round((-m[0]-d[6]*f[1])/(-f[2]),2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round((m[1]-d[6]*f[0])/(-f[2]),2),
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
    #     ayuda2 = "Recordar que los signos de los componentes de $\\overrightarrow{{r}}$  y $\\overrightarrow{{F}}$ son importantes para determinar la dirección correcta del momento; recordando que el vector momento no solo indicamagnitud, sino también el eje alrededor del cual se produce la rotación el cual es perpendicular tanto al vector $\\overrightarrow{{r}}$ como $\\overrightarrow{{F}}$.",      
    #     ayuda3 = "Para encontrar incognitas, primero mira que datos tienes y como se relacionan.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones es más fácil calcular el momento resolviendo producto cruz y dividiendo el ejercicios en determinar las componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$. A continuación, se presenta la solución sugerida para el ejercicio:      

    #     $\\textbf{{\\small 1. Obtención del vector posición:}}$       
        
    #     ${{\hspace{{4mm}} r_x = d_2}}$     
    #     ${{\hspace{{4mm}} r_y = d_1}}$      
    #     ${{\hspace{{4mm}} r_z = - d_3 = {-d[6]:.0f}{{ \\text{{ ft}}}}}}$         

    #     $\\textbf{{\\small 2. Expresión de ecuaciones de la componentes de momento: }}$  
        
    #     ${{\hspace{{4mm}} M_i = d_1 \\cdot F_z - (-d_3) \\cdot F_y }}$     
    #     ${{\hspace{{4mm}} M_j = - (d_2 \\cdot F_z - (-d_3) \\cdot F_x)}}$     
    #     ${{\hspace{{4mm}} M_k = d_2 \\cdot F_y - d_1 \\cdot F_x }}$     
        
    #     De lo cual sencillamente se puede resolver para $d_1$ y $d_2$ de la siguiente manera:
        
    #     $\\underline{{Despejar \\hspace{{2mm}} d_1 \\hspace{{2mm}} de \\hspace{{2mm}} ecuación \\hspace{{2mm}} 1:}}$        
    #     ${{\hspace{{4mm}} {-m[0]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} = d_1 \\cdot ( {-f[2]:.0f} ){{ \\text{{ lb}}}} - ( {-d[6]:.0f}{{ \\text{{ ft}}}}) \\cdot {f[1]:.0f}{{ \\text{{ lb}}}}}}$       
    #     ${{\hspace{{4mm}} {-m[0]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} -  {d[6]*f[1]:.0f} {{\\text{{ lb}} \\cdot \\text{{ ft}}}} = d_1 \\cdot ( {-f[2]:.0f} ){{ \\text{{ lb}}}}}}$       
    #     ${{\hspace{{4mm}} d_1 = \\dfrac{{{-m[0]-d[6]*f[1]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}{{( {-f[2]:.0f} ){{ \\text{{ lb}}}}}}}}$      
    #     ${{\hspace{{4mm}} d_1 = {(-m[0]-d[6]*f[1])/(-f[2]):.2f}{{\\text{{ ft}}}} }}$     
        
    #     $\\underline{{Despejar \\hspace{{2mm}} d_2 \\hspace{{2mm}} de \\hspace{{2mm}} ecuación \\hspace{{2mm}} 2:}}$       
    #     ${{\hspace{{4mm}} {-m[1]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} = - (d_2 \\cdot ( {-f[2]:.0f} ){{ \\text{{ lb}}}} - ({-d[6]:.0f}{{ \\text{{ ft}}}}) \\cdot {f[0]:.0f}{{ \\text{{ lb}}}} )}}$       
    #     ${{\hspace{{4mm}} {m[1]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} - {d[6]*f[0]:.0f}{{ \\text{{ lb}}}} = d_2 \\cdot ( {-f[2]:.0f} ){{ \\text{{ lb}}}}}}$       
    #     ${{\hspace{{4mm}} d_2 = \\dfrac{{{m[1]-d[6]*f[0]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}{{( {-f[2]:.0f} ){{ \\text{{ lb}}}}}}}}$      
    #     ${{\hspace{{4mm}} d_2 = {(m[1]-d[6]*f[0])/(-f[2]):.2f}{{ \\text{{ ft}}}} }}$    

    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    # Questionary(#3_1
    #     code = 2210021,
    #     no_pregunta = 3,
    #     complexity = F,
    #     topic = MO,
    #     subtopic = M3D,
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de las componentes $\\hat{{i}}$ y $\\hat{{j}}$ de $F_1$ si el momento en el origen que causa esta fuerza es de $ [ {-m[0]:.0f}\\hat{{i}} + ( {-m[1]:.0f}) \\hat{{j}} + ({ (d[0]*(-m[0])-m[1]*d[3])/(d[6]):.0f})\\hat{{k}} ]{{ \\text{{ lb}}}} \\cdot {{ \\text{{ ft}}}}$. Considere que la componente $\\hat{{k}}$ de $F_1$ tiene un valor de ${-f[2]:.0f}\\text{{ lb}}$; y que $d_1 = {d[3]:.0f} \\text{{ ft}}$,  $d_2 = {d[0]:.0f}  \\text{{ ft}}$ y $d_3 = {d[6]:.0f} \\text{{ ft}}$.",
    #     no_answers = 2,
    #     a1_name = "Componente $\\hat{{i}}$ de $F_1$ [lb]",
    #     a2_name = "Componente $\\hat{{j}}$ de $F_1$ [lb]",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round((m[1]+d[0]*f[2])/(d[6]),2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round((-m[0]+d[3]*f[2])/(d[6]),2),
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
    #     ayuda2 = "Recordar que los signos de los componentes de $\\overrightarrow{{r}}$  y $\\overrightarrow{{F}}$ son importantes para determinar la dirección correcta del momento; recordando que el vector momento no solo indicamagnitud, sino también el eje alrededor del cual se produce la rotación el cual es perpendicular tanto al vector $\\overrightarrow{{r}}$ como $\\overrightarrow{{F}}$.",      
    #     ayuda3 = "Para encontrar incognitas, primero mira que datos tienes y como se relacionan.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones es más fácil calcular el momento resolviendo producto cruz y dividiendo el ejercicios en determinar las componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$. A continuación, se presenta la solución sugerida para el ejercicio:      

    #     $\\textbf{{\\small 1. Obtención del vector posición:}}$       
        
    #     ${{\hspace{{4mm}} r_x = d_2 = {d[0]:.0f}{{ \\text{{ ft}}}}}}$     
    #     ${{\hspace{{4mm}} r_y = d_1 = {d[3]:.0f}{{ \\text{{ ft}}}}}}$     
    #     ${{\hspace{{4mm}} r_z = - d_3 = {-d[6]:.0f}{{ \\text{{ ft}}}}}}$         

    #     $\\textbf{{\\small 2. Expresión de ecuaciones de la componentes de momento: }}$  
        
    #     ${{\hspace{{4mm}} M_i = d_1 \\cdot F_z - (-d_3) \\cdot F_y }}$     
    #     ${{\hspace{{4mm}} M_j = - (d_2 \\cdot F_z - (-d_3) \\cdot F_x)}}$     
    #     ${{\hspace{{4mm}} M_k = d_2 \\cdot F_y - d_1 \\cdot F_x }}$     
        
    #     De lo cual sencillamente se puede resolver para $F_x$ y $F_y$ de la siguiente manera:
        
    #     $\\underline{{Despejar \\hspace{{2mm}} F_x \\hspace{{2mm}} de \\hspace{{2mm}} ecuación \\hspace{{2mm}} 2:}}$       
    #     ${{\hspace{{4mm}} {-m[1]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} = - ({d[0]:.0f}{{ \\text{{ ft}}}} \\cdot ( {-f[2]:.0f} ){{ \\text{{ lb}}}} - ({-d[6]:.0f}{{ \\text{{ ft}}}}) \\cdot F_x )}}$       
    #     ${{\hspace{{4mm}} {m[1]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} + {d[0]*f[2]:.0f}{{ \\text{{ ft}}}} \\cdot \\text{{ lb}} = {d[6]:.0f}{{ \\text{{ ft}}}} \\cdot F_x}}$       
    #     ${{\hspace{{4mm}} F_x = \\dfrac{{{m[1]+d[0]*f[2]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}{{( {d[6]:.0f} ){{ \\text{{ ft}}}}}}}}$      
    #     ${{\hspace{{4mm}} F_x = {(m[1]+d[0]*f[2])/(d[6]):.2f}{{\\text{{ lb}}}}}}$     
        
    #     $\\underline{{Despejar \\hspace{{2mm}} F_y \\hspace{{2mm}} de \\hspace{{2mm}} ecuación \\hspace{{2mm}} 1:}}$        
    #     ${{\hspace{{4mm}} {-m[0]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} = {d[3]:.0f}{{ \\text{{ ft}}}} \\cdot ( {-f[2]:.0f} ){{ \\text{{ lb}}}} - ( {-d[6]:.0f}{{ \\text{{ ft}}}}) \\cdot F_y}}$       
    #     ${{\hspace{{4mm}} {-m[0]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} +  {d[3]*f[2]:.0f} {{\\text{{ lb}} \\cdot \\text{{ ft}}}} = {d[6]:.0f}{{ \\text{{ ft}}}} \\cdot F_y}}$       
    #     ${{\hspace{{4mm}} F_y = \\dfrac{{{-m[0]+d[3]*f[2]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}{{( {d[6]:.0f} ){{ \\text{{ ft}}}}}}}}$      
    #     ${{\hspace{{4mm}} F_y = {(-m[0]+d[3]*f[2])/(d[6]):.2f}{{\\text{{ lb}}}} }}$     
           
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    # Questionary(#4_1
    #     code = 2210041,
    #     no_pregunta = 4,
    #     complexity = F,
    #     topic = MO,
    #     subtopic = M3D,
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de los momentos en el punto A de las fuerza $F_1$ y $F_2$. Considere $F_1 = [ {f[0]:.0f}\\hat{{i}} + {f[1]:.0f} \\hat{{j}} + ( {-f[2]:.0f} ) \\hat{{k}} ] \\text{{ lb}}$, $F_2 = [ {-f[3]:.0f}\\hat{{i}} + {f[4]:.0f} \\hat{{j}} + ( {f[5]:.0f} ) \\hat{{k}} ] \\text{{ lb}}$ $d_1 = {d[3]:.0f} \\text{{ ft}}$,  $d_2 = {d[0]:.0f}  \\text{{ ft}}$ y $d_3 = {d[6]:.0f} \\text{{ ft}}$.",
    #     no_answers = 2,
    #     a1_name = "Momento en A causado por $F_1$ [$lb \\cdot ft$]",
    #     a2_name = "Momento en A causado por $F_2$ [$lb \\cdot ft$]",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D(d[6]*f[1],-d[6]*f[0],0),2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round(Calculations.magnitude3D(0,-d[0]*f[5],-d[0]*f[4]),2),
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
    #     ayuda2 = "Recordar que los signos de los componentes de $\\overrightarrow{{r}}$  y $\\overrightarrow{{F}}$ son importantes para determinar la dirección correcta del momento; recordando que el vector momento no solo indicamagnitud, sino también el eje alrededor del cual se produce la rotación el cual es perpendicular tanto al vector $\\overrightarrow{{r}}$ como $\\overrightarrow{{F}}$.",      
    #     ayuda3 = "Se puede dividir el problema en componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$, y resolver de manera independiente las componentes del momento.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones es más fácil calcular el momento resolviendo producto cruz y dividiendo el ejercicios en determinar las componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$. A continuación, se presenta la solución sugerida para el ejercicio:      

    #     $\\textbf{{\\small 1. Obtención del vector posición:}}$   
        
    #     $\\underline{{Vector Posición \\hspace{{2mm}} r1: }}$         
        
    #     ${{\hspace{{4mm}} r1_x = 0 {{ \\text{{ ft}}}}}}$     
    #     ${{\hspace{{4mm}} r1_y = 0 {{ \\text{{ ft}}}}}}$     
    #     ${{\hspace{{4mm}} r1_z = - d_3 = {-d[6]:.0f}{{ \\text{{ ft}}}}}}$        
        
    #     $\\underline{{Vector Posición \\hspace{{2mm}} r2: }}$
        
    #     ${{\hspace{{4mm}} r2_x = - d_2 = {-d[0]:.0f}{{ \\text{{ ft}}}}}}$     
    #     ${{\hspace{{4mm}} r2_y = 0 {{ \\text{{ ft}}}}}}$     
    #     ${{\hspace{{4mm}} r2_z = 0 {{ \\text{{ ft}}}}}}$       

    #     $\\textbf{{\\small 2. Calculo del momento en A de F_1: }}$  
        
    #     $\\underline{{Componente \\hspace{{2mm}} \\hat{{i}} :}}$
        
    #     Haciendo Producto Cruz, la componente \\hat{{i}} del momento se puede calcular como:
        
    #     ${{\hspace{{4mm}} M1_i = r_y \\cdot F_z - r_z \\cdot F_y = 0 {{ \\text{{ ft}}}} \\cdot ( {-f[2]:.0f} ){{ \\text{{ lb}}}} - ( {-d[6]:.0f}{{ \\text{{ ft}}}} ) \\cdot {f[1]:.0f}{{ \\text{{ lb}}}}}}$          
    #     ${{\hspace{{4mm}} M1_i = {d[6]*f[1]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$       
        
    #     $\\underline{{Componente \\hspace{{2mm}} \\hat{{j}} :}}$
        
    #     Haciendo Producto Cruz, la componente \\hat{{j}} del momento se puede calcular como:
        
    #     ${{\hspace{{4mm}} M1_j = - ( r_x \\cdot F_z - r_z \\cdot F_x ) = -( 0 {{ \\text{{ ft}}}} \\cdot ( {-f[2]:.0f} ){{ \\text{{ lb}}}} - ( {-d[6]:.0f}{{ \\text{{ ft}}}} ) \\cdot {f[0]:.0f}{{ \\text{{ lb}}}} )}}$           
    #     ${{\hspace{{4mm}} M1_j = {-d[6]*f[0]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$      
        
    #     $\\underline{{Componente \\hspace{{2mm}} \\hat{{k}} :}}$
        
    #     Haciendo Producto Cruz, la componente \\hat{{k}} del momento se puede calcular como:
        
    #     ${{\hspace{{4mm}} M1_k =  r_x \\cdot F_y - r_y \\cdot F_x  = 0 {{ \\text{{ ft}}}} \\cdot {f[1]:.0f} {{ \\text{{ lb}}}} - 0 {{ \\text{{ ft}}}} \\cdot {f[0]:.0f}{{ \\text{{ lb}}}}}}$         
    #     ${{\hspace{{4mm}} M1_k = 0 {{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$     
        
    #     $\\underline{{Magnitud \\hspace{{2mm}} del \\hspace{{2mm}} momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_1:}}$
        
    #     ${{\hspace{{4mm}} |M_1| = \\sqrt{{ ({d[6]*f[1]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}})^{{2}} + ({-d[6]*f[0]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}})^{{2}} }} }}$     
    #     ${{\hspace{{4mm}} |M_1| = {Calculations.magnitude3D(d[6]*f[1],-d[6]*f[0],0)}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$     
        
    #     $\\textbf{{\\small 3. Calculo del momento en A de F_2: }}$  
        
    #     $\\underline{{Componente \\hspace{{2mm}} \\hat{{i}} :}}$
        
    #     Haciendo Producto Cruz, la componente \\hat{{i}} del momento se puede calcular como:
        
    #     ${{\hspace{{4mm}} M2_i = r_y \\cdot F_z - r_z \\cdot F_y = 0 {{ \\text{{ ft}}}} \\cdot ( {f[5]:.0f} ){{ \\text{{ lb}}}} - 0 \\cdot {f[4]:.0f}{{ \\text{{ lb}}}}}}$          
    #     ${{\hspace{{4mm}} M2_i = 0 {{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$       
        
    #     $\\underline{{Componente \\hspace{{2mm}} \\hat{{j}} :}}$
        
    #     Haciendo Producto Cruz, la componente \\hat{{j}} del momento se puede calcular como:
        
    #     ${{\hspace{{4mm}} M2_j = - ( r_x \\cdot F_z - r_z \\cdot F_x ) = -( {-d[0]:.0f} {{ \\text{{ ft}}}} \\cdot ( {f[5]:.0f} ){{ \\text{{ lb}}}} - 0 {{ \\text{{ ft}}}} \\cdot ( {-f[3]:.0f}{{ \\text{{ lb}}}} ) )}}$           
    #     ${{\hspace{{4mm}} M2_j = {d[0]*f[5]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$      
        
    #     $\\underline{{Componente \\hspace{{2mm}} \\hat{{k}} :}}$
        
    #     Haciendo Producto Cruz, la componente \\hat{{k}} del momento se puede calcular como:
        
    #     ${{\hspace{{4mm}} M2_k =  r_x \\cdot F_y - r_y \\cdot F_x  = {-d[0]:.0f} {{ \\text{{ ft}}}} \\cdot {f[4]:.0f} {{ \\text{{ lb}}}} - 0 {{ \\text{{ ft}}}} \\cdot ( {-f[3]:.0f}{{ \\text{{ lb}}}} )}}$    
    #     ${{\hspace{{4mm}} M2_k = {-d[0]*f[4]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}}}}$     
        
    #     $\\underline{{Magnitud \\hspace{{2mm}} del \\hspace{{2mm}} momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_1:}}$
        
    #     ${{\hspace{{4mm}} |M_2| = \\sqrt{{ ({d[0]*f[5]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}})^{{2}} + ({-d[0]*f[4]:.0f}{{\\text{{ lb}} \\cdot \\text{{ ft}}}})^{{2}} }} }}$
    #     ${{\hspace{{4mm}} |M_2| = {Calculations.magnitude3D(0,d[0]*f[5],d[0]*f[4])}{{\\text{{ lb}} \\cdot \\text{{ ft}}}} }}$       
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),


    #========================================================  MOMENTO  =========================================================
    #--------------------------------------------     Momento en un punto en 3D      --------------------------------------------
    #-------------------------------------------------       Nivel medio    ---------------------------------------------------
    #-------------------------------------------------       Code: 2220011    --------------------------------------------------
    
    # Questionary(#1_1
    #     code = 2220011,
    #     no_pregunta = 1,
    #     complexity = M,
    #     topic = MO,
    #     subtopic = M3D,
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Calcule la suma de momentos que causan las tres fuerzas en el Origen, y expreselo en vector cartesiano. Considere que $F_1 = [{f[0]:.0f}\\hat{{i}} + {f[1]:.0f} \\hat{{j}} + ({-f[2]:.0f})\\hat{{k}}]\\text{{ N}}$, $F_2 = [({-f[3]:.0f})\\hat{{i}} + {f[4]:.0f} \\hat{{j}} + {f[5]:.0f}\\hat{{k}}]\\text{{ N}}$, $F_3 = [{f[6]:.0f}\\hat{{i}} + (({-f[7]:.0f})\\hat{{j}} + {f[8]:.0f})\\hat{{k}}]\\text{{ N}}$, $d_1 = {d[3]:.0f} \\text{{ m}}$,  $d_2 = {d[0]:.0f}  \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
    #     no_answers = 3,
    #     a1_name = "Componente $\\hat{{i}}$ del momento en el origen [$N \\cdot m$]",
    #     a2_name = "Componente $\\hat{{j}}$ del momento en el origen [$N \\cdot m$]",
    #     a3_name = "Componente $\\hat{{k}}$ del momento en el origen [$N \\cdot m$]",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(d[3]*(-f[2]) + d[3]*(f[5]) + d[3]*f[8] - d[6]*(-f[7]),2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round(d[0]*f[2] + d[6]*f[6]-d[0]*f[8],2),
    #     answer3 = lambda f, a, calc, c, d, m: np.round(d[0]*f[1]-d[3]*f[0] + d[3]*f[3] - d[0]*f[7]-d[3]*f[6],2),
    #     ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
    #     ayuda2 = "Recordar que los signos de los componentes de $\\overrightarrow{{r}}$  y $\\overrightarrow{{F}}$ son importantes para determinar la dirección correcta del momento; recordando que el vector momento no solo indicamagnitud, sino también el eje alrededor del cual se produce la rotación el cual es perpendicular tanto al vector $\\overrightarrow{{r}}$ como $\\overrightarrow{{F}}$.",      
    #     ayuda3 = "Se puede dividir el problema en componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$, y resolver de manera independiente las componentes del momento.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones es más fácil calcular el momento resolviendo producto cruz y dividiendo el ejercicio en determinar las componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$. A continuación, se presenta la solución sugerida para el ejercicio:      

    #     $\\textbf{{\\small 1. Calculo del momento en el origen causado por F_1: }}$  
        
    #     ${{\hspace{{4mm}} M_1 = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_1 = ({d[3]:.0f}{{\\text{{ m}}}} \\cdot ({-f[2]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[1]:.0f} {{\\text{{ N}}}})\\hat{{i}} - ({d[0]:.0f}{{\\text{{ m}}}} \\cdot ({-f[2]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[0]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ({d[0]:.0f}{{\\text{{ m}}}} \\cdot {f[1]:.0f} {{\\text{{ N}}}} - {d[3]:.0f}{{\\text{{ m}}}} \\cdot {f[0]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_1 = [ ({d[3]*(-f[2]):.0f})\\hat{{i}} + ({d[0]*f[2]:.0f})\\hat{{j}} + ({d[0]*f[1]-d[3]*f[0]:.0f})\\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$ 
        
    #     $\\textbf{{\\small 2. Calculo del momento en el origen causado por F_2: }}$  
        
    #     ${{\hspace{{4mm}} M_2 = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_2 = ({d[3]:.0f}{{\\text{{ m}}}} \\cdot {f[5]:.0f} {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[4]:.0f} {{\\text{{ N}}}})\\hat{{i}} - ( 0 {{\\text{{ m}}}} \\cdot ({f[5]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot ({-f[3]:.0f}) {{\\text{{ N}}}})\\hat{{j}} + ( 0 {{\\text{{ m}}}} \\cdot {f[4]:.0f} {{\\text{{ N}}}} - {d[3]:.0f}{{\\text{{ m}}}} \\cdot ({-f[3]:.0f}) {{\\text{{ N}}}})\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_2 = [ ({d[3]*(f[5]):.0f})\\hat{{i}} + 0\\hat{{j}} + ({d[3]*f[3]:.0f})\\hat{{k}} ] {{ \\text{{ N}} \\cdot \\text{{ m}}}} }}$
        
    #     $\\textbf{{\\small 3. Calculo del momento en el origen causado por F_3: }}$  
        
    #     ${{\hspace{{4mm}} M_3 = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_3 = ({d[3]:.0f}{{\\text{{ m}}}} \\cdot {f[8]:.0f}{{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}})\\hat{{i}} - ({d[0]:.0f}{{\\text{{ m}}}} \\cdot {f[8]:.0f} {{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ({d[0]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}} - {d[3]:.0f}{{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_3 = [ ({d[3]*f[8] + d[6]*f[7]:.0f})\\hat{{i}} - ({d[0]*f[8]-d[6]*f[6]:.0f})\\hat{{j}} - ({d[0]*(f[7])+d[3]*f[6]:.0f})\\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$
        
    #     $\\textbf{{\\small 4. Sumatoria de momentos en el origen: }}$

    #     ${{\hspace{{4mm}} \\sum{{M_O}} = [({d[3]*(-f[2]):.0f} + {d[3]*(f[5]):.0f} + {d[3]*f[8] - d[6]*(-f[7]):.0f})\\hat{{i}} + ({d[0]*f[2]:.0f} + 0 + ({d[6]*f[6]-d[0]*f[8]:.0f}))\\hat{{j}} + ({d[0]*f[1]-d[3]*f[0]:.0f} + {d[3]*f[3]:.0f} + {d[0]*(-f[7])-d[3]*f[6]:.0f})\\hat{{k}}]{{\\text{{ N}} \\cdot \\text{{ m}}}} }}$      
    #     ${{\hspace{{4mm}} \\sum{{M_O}} = [({d[3]*(-f[2]) + d[3]*(f[5]) + d[3]*f[8] - d[6]*(-f[7]):.2f})\\hat{{i}} + ({d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f})\\hat{{j}} + ({d[0]*f[1]-d[3]*f[0] + d[3]*f[3] - d[0]*f[7]-d[3]*f[6]:.2f})\\hat{{k}}] {{\\text{{ N}} \\cdot \\text{{ m}}}} }}$      
              
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),  
    # Questionary(#2_1
    #     code = 2220021,
    #     no_pregunta = 2,
    #     complexity = M,
    #     topic = MO,
    #     subtopic = M3D,
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine las componentes  $\\hat{{j}}$ y $\\hat{{k}}$ de la fuerza $F_2$ si la sumatoria de momentos en A y en B deben ser iguales. Considere que la componente $\\hat{{k}}$ de $F_2 = {-f[3]:0f} \\text{{ N}}$; Asuma $F_1 = [{f[0]:.0f}\\hat{{i}} + {f[1]:.0f} \\hat{{j}} + ({-f[2]:.0f})\\hat{{k}}]\\text{{ N}}$, $F_3 = [{f[6]:.0f}\\hat{{i}} + ({-f[7]:.0f})\\hat{{j}} + {f[8]:.0f}\\hat{{k}}]\\text{{ N}}$, $d_1 = {d[3]:.0f} \\text{{ m}}$,  $d_2 = {d[0]:.0f}  \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
    #     no_answers = 2,
    #     a1_name = "Componente $\\hat{{j}}$ de la fuerza $F_2$ [N]",
    #     a2_name = "Componente $\\hat{{k}}$ de la fuerza $F_2$ [N]",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(f[2]-f[8],2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round(f[7]-f[1],2),
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
    #     ayuda2 = "Recordar que los signos de los componentes de $\\overrightarrow{{r}}$  y $\\overrightarrow{{F}}$ son importantes para determinar la dirección correcta del momento; recordando que el vector momento no solo indicamagnitud, sino también el eje alrededor del cual se produce la rotación el cual es perpendicular tanto al vector $\\overrightarrow{{r}}$ como $\\overrightarrow{{F}}$.",      
    #     ayuda3 = "Se puede dividir el problema en componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$, y resolver de manera independiente las componentes del momento.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones es más fácil calcular el momento resolviendo producto cruz y dividiendo el ejercicio en determinar las componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$. 
        
    #     En este caso, también se va a descomponer el problema en obtener las componentes de los momentos en A y en B, para luego igualarlas con el fin de despejar los terminos que se buscan. A continuación, se presenta la solución sugerida para el ejercicio:      

    #     $\\textbf{{\\small 1. Calculo del momento en A: }}$
        
    #     En este caso, se puede evidenciar que las unicas fuerzas que causan momento seran $F_1$ y $F_3$ :
        
    #     $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_1 :}}$  
        
    #     ${{\hspace{{4mm}} M_{{A1}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_{{A1}} = ( 0 {{\\text{{ m}}}} \\cdot ({-f[2]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[1]:.0f} {{\\text{{ N}}}})\\hat{{i}} - ({d[0]:.0f}{{\\text{{ m}}}} \\cdot ({-f[2]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[0]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ({d[0]:.0f}{{\\text{{ m}}}} \\cdot {f[1]:.0f} {{\\text{{ N}}}} - 0{{\\text{{ m}}}} \\cdot {f[0]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_{{A1}} = [ 0 \\hat{{i}} + {d[0]*f[2]:.0f}\\hat{{j}} + {d[0]*f[1]:.0f} \\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$      
        
    #     $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_3 :}}$  
        
    #     ${{\hspace{{4mm}} M_{{A3}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_{{A3}} = ( 0 {{\\text{{ m}}}} \\cdot {f[8]:.0f}{{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}})\\hat{{i}} - ({d[0]:.0f}{{\\text{{ m}}}} \\cdot {f[8]:.0f} {{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ({d[0]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_{{A3}} = [ {d[6]*f[7]:.0f}\\hat{{i}} - ({d[0]*f[8] - d[6]*f[6]:.0f})\\hat{{j}} - ({d[0]*(f[7]):.0f})\\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$    
        
    #     $\\underline{{Sumatoria \\hspace{{2mm}} momentos \\hspace{{2mm}} en \\hspace{{2mm}} A :}}$ 
         
    #     ${{\hspace{{4mm}} \\sum{{M_A}} = [ ( 0 + {d[6]*(f[7]):.0f})\\hat{{i}} + ({d[0]*f[2]:.0f} + ({d[6]*f[6]-d[0]*f[8]:.0f}))\\hat{{j}} + ({d[0]*f[1]:.0f} - {d[0]*(f[7]):.0f})\\hat{{k}}]{{\\text{{N}} \\cdot \\text{{ m}}}} }}$     
    #     ${{\hspace{{4mm}} \\sum{{M_A}} = [({d[6]*f[7]:.2f})\hat{{i}} + ({d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f})\\hat{{j}} + ({d[0]*f[1] - d[0]*f[7]:.2f})\\hat{{k}}] {{\\text{{ N}} \\cdot \\text{{ m}}}} }}$     
        
    #     $\\textbf{{\\small 2. Calculo del momento en B: }}$
        
    #     En B, es evidente que las unicas fuerzas que causan momento son $F_2$ y $F_3$ :
        
    #     $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_2 :}}$  
        
    #     ${{\hspace{{4mm}} M_{{B2}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_{{B2}} = ( 0 {{\\text{{ m}}}} \\cdot F2_z - 0 {{\\text{{ m}}}} \\cdot F2_y )\\hat{{i}} - ( {-d[0]:.0f} {{\\text{{ m}}}} \\cdot F2_z - 0 {{\\text{{ m}}}} \\cdot ({-f[3]:.0f}) {{\\text{{ N}}}})\\hat{{j}} + ( {-d[0]:.0f} {{\\text{{ m}}}} \\cdot  F2_y - 0 {{\\text{{ m}}}} \\cdot ({-f[3]:.0f}) {{\\text{{ N}}}})\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_{{B2}} =  0 {{ \\text{{ N}} \\cdot \\text{{ m }}}} \\hat{{i}} + {d[0]:.0f} {{\\text{{ m}}}} \\cdot F2_z \\hat{{j}} - {d[0]:.0f} {{\\text{{ m}}}} \\ cdot F2_y \\hat{{k}}  }}$
        
    #     $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_3 :}}$  
        
    #     ${{\hspace{{4mm}} M_{{B3}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_{{B3}} = ( 0 {{\\text{{ m}}}} \\cdot {f[8]:.0f}{{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}})\\hat{{i}} - ( 0 {{\\text{{ m}}}} \\cdot {f[8]:.0f} {{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ( 0 {{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_{{B3}} = [ {d[6]*f[7]:.0f}\\hat{{i}} + {d[6]*f[6]:.0f}\\hat{{j}} - 0 \\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$    
        
    #     $\\underline{{Sumatoria \\hspace{{2mm}} momentos \\hspace{{2mm}} en \\hspace{{2mm}} B :}}$
           
    #     ${{\hspace{{4mm}} \\sum{{M_B}} = [({d[6]*f[7]:.2f} {{\\text{{ N}} \\cdot \\text{{ m}}}})\\hat{{i}} + ({d[6]*f[6]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[0]:.0f} {{\\text{{ m}}}} \\cdot F2_z ) \\hat{{j}} - ({d[0]:.2f}{{\\text{{ m}}}} \\cdot F2_y)\\hat{{k}}] }}$    
        
    #     $\\textbf{{\\small 3. Despeje de $F2_y$ y $F2_z$: }}$
        
    #     Para cumplir la condición de que tanto el momento en B y el momento en A sean iguales, se observa que es necesario que sus compenentes asi lo sean. Tal que:
        
    #     ${{\hspace{{4mm}} 1.  ({d[6]*f[7]:.2f} {{\\text{{ N}} \\cdot \\text{{ m}}}})\\hat{{i}} = ({d[6]*f[7]:.2f} {{\\text{{ N}} \\cdot \\text{{ m}}}})\\hat{{i}} }}$      
    #     ${{\hspace{{4mm}} 2.  ({d[6]*f[6]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[0]:.0f} {{\\text{{ m}}}} \\cdot F2_z ) \\hat{{j}} = ({d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}})\\hat{{j}} }}$      
    #     ${{\hspace{{4mm}} 3.  - ({d[0]:.2f}{{\\text{{ m}}}} \\cdot F2_y)\\hat{{k}} = ({d[0]*f[1] - d[0]*f[7]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}})\\hat{{k}} }}$     
        
    #     De lo cual, se encuentran utiles las ecuaciones 2 y 3 para obtener los valores de $F2_z$ y $F2_y$ :
        
    #     $\\underline{{Despeje \\hspace{{2mm}} para \\hspace{{2mm}} F2_z :}}$

    #     De la ecuación 2 se obtiene:  
        
    #     ${{\hspace{{4mm}} ({d[6]*f[6]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[0]:.0f} {{\\text{{ m}}}} \\cdot F2_z ) \\hat{{j}} = ({d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}})\\hat{{j}} }}$      
    #     ${{\hspace{{4mm}} ({d[0]:.2f} {{\\text{{ m}}}} \\cdot F2_z ) = {d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[6]*f[6]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$      
    #     ${{\hspace{{4mm}} F2_z = \\dfrac{{{d[0]*f[2] - d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}}}{{{d[0]:.2f} {{\\text{{ m}}}}}} }}$           
    #     ${{\hspace{{4mm}} F2_z = {f[2]-f[8]:.2f}{{\\text{{ N}}}}}} $ 
        
    #     \\underline{{Despeje \\hspace{{2mm}} para \\hspace{{2mm}} F2_y :}}$ 

    #     De la ecuación 3 se obtiene 
        
    #     ${{\hspace{{4mm}} - ({d[0]:.2f}{{\\text{{ m}}}} \\cdot F2_y)\\hat{{k}} = ({d[0]*f[1] - d[0]*f[7]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}})\\hat{{k}} }}$            
    #     ${{\hspace{{4mm}} F2_y = \\dfrac{{{d[0]*f[7] - d[0]*f[1]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}}}{{{d[0]:.2f} {{\\text{{ m}}}}}} }}$           
    #     ${{\hspace{{4mm}} F2_y = {f[7]-f[1]:.2f}{{\\text{{ N}}}}}} $ 
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),
    # Questionary(#3_1
    #     code = 2220031,
    #     no_pregunta = 3,
    #     complexity = M,
    #     topic = MO,
    #     subtopic = M3D,
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine las componentes  $\\hat{{j}}$ y $\\hat{{k}}$ de una cuarta fuerza $F_4$, que es aplicada sobre el tramo OA, y esta a ${(d[3]/3):.2f}{{\\text{{ m}}}}$ si la sumatoria de momentos en A y en B deben ser iguales. Considere que la componente $\\hat{{k}}$ de $F_4 = {f[9]:0f} \\text{{ N}}$; Asuma que $F_1 = [{f[0]:.0f}\\hat{{i}} + {f[1]:.0f} \\hat{{j}} + ({-f[2]:.0f})\\hat{{k}}]\\text{{ N}}$, $F_2 = [({-f[3]:.0f})\\hat{{i}} + {f[4]:.0f} \\hat{{j}} + {f[5]:.0f}\\hat{{k}}]\\text{{ N}}$, $F_3 = [{f[6]:.0f}\\hat{{i}} + ({-f[7]:.0f})\\hat{{j}} + {f[8]:.0f}\\hat{{k}}]\\text{{ N}}$, $d_1 = {d[3]:.0f} \\text{{ m}}$,  $d_2 = {d[0]:.0f}  \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
    #     no_answers = 2,
    #     a1_name = "Componente $\\hat{{j}}$ de la fuerza $F_4$ [N]",
    #     a2_name = "Componente $\\hat{{k}}$ de la fuerza $F_4$ [N]",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(f[7]- f[1] - f[4],2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round(f[2]- f[8] - f[5],2),
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
    #     ayuda2 = "Recordar que los signos de los componentes de $\\overrightarrow{{r}}$  y $\\overrightarrow{{F}}$ son importantes para determinar la dirección correcta del momento; recordando que el vector momento no solo indicamagnitud, sino también el eje alrededor del cual se produce la rotación el cual es perpendicular tanto al vector $\\overrightarrow{{r}}$ como $\\overrightarrow{{F}}$.",      
    #     ayuda3 = "Se puede dividir el problema en componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$, y resolver de manera independiente las componentes del momento.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones es más fácil calcular el momento resolviendo producto cruz y dividiendo el ejercicio en determinar las componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$. 
        
    #     En este caso, también se va a descomponer el problema en obtener las componentes de los momentos en A y en B, para luego igualarlas con el fin de despejar los terminos que se buscan. A continuación, se presenta la solución sugerida para el ejercicio:      

    #     $\\textbf{{\\small 1. Calculo del momento en A: }}$
        
    #     En este caso, se puede evidenciar que las unicas fuerzas que causarían momento seran $F_1$, $F_3$ y $F_4$ :
        
    #     $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_1 :}}$  
        
    #     ${{\hspace{{4mm}} M_{{A1}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_{{A1}} = ( 0 {{\\text{{ m}}}} \\cdot ({-f[2]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[1]:.0f} {{\\text{{ N}}}})\\hat{{i}} - ({d[0]:.0f}{{\\text{{ m}}}} \\cdot ({-f[2]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[0]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ({d[0]:.0f}{{\\text{{ m}}}} \\cdot {f[1]:.0f} {{\\text{{ N}}}} - 0{{\\text{{ m}}}} \\cdot {f[0]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_{{A1}} = [ 0 \\hat{{i}} + {d[0]*f[2]:.0f}\\hat{{j}} + {d[0]*f[1]:.0f} \\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$      
        
    #     $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_3 :}}$  
        
    #     ${{\hspace{{4mm}} M_{{A3}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_{{A3}} = ( 0 {{\\text{{ m}}}} \\cdot {f[8]:.0f}{{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}})\\hat{{i}} - ({d[0]:.0f}{{\\text{{ m}}}} \\cdot {f[8]:.0f} {{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ({d[0]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_{{A3}} = [ {d[6]*f[7]:.0f}\\hat{{i}} - ({d[0]*f[8] - d[6]*f[6]:.0f})\\hat{{j}} - ({d[0]*(f[7]):.0f})\\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$    
        
    #     $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_4 :}}$  
        
    #     ${{\hspace{{4mm}} M_{{A4}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_{{A4}} = ( ({-2*(d[3]/3):.2f}) {{\\text{{ m}}}} \\cdot F4_z - 0 {{\\text{{ m}}}} \\cdot F4_y)\\hat{{i}} - ( 0 {{\\text{{ m}}}} \\cdot F4_z - 0 {{\\text{{ m}}}} \\cdot {f[9]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ( 0 {{\\text{{ m}}}} \\cdot F4_y - ({-2*(d[3]/3):.2f}) {{\\text{{ m}}}} \\cdot {f[9]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_{{A4}} =  ( ({-2*(d[3]/3):.2f}) {{\\text{{ m}}}} \\cdot F4_z )\\hat{{i}} + 0{{\\text{{ N}} \\cdot \\text{{ m}}}} \\hat{{j}} + {2*(d[3]/3)*f[9]:2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} \\hat{{k}} }}$    
        
    #     $\\underline{{Sumatoria \\hspace{{2mm}} momentos \\hspace{{2mm}} en \\hspace{{2mm}} A :}}$ 
         
    #     ${{\hspace{{4mm}} \\sum{{M_A}} =  ( 0 {{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[6]*(f[7]):.0f}{{\\text{{N}} \\cdot \\text{{ m}}}} - {2*(d[3]/3):.2f} {{\\text{{ m}}}} \\cdot F4_z )\\hat{{i}} + ({d[0]*f[2]:.0f} + ({d[6]*f[6]-d[0]*f[8]:.0f}) + 0){{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{j}} + ({d[0]*f[1]:.0f} - {d[0]*(f[7]) + 2*(d[3]/3)*f[9]:.0f}){{\\text{{ N}} \\cdot \\text{{ m}}}} \\hat{{k}} }}$     
    #     ${{\hspace{{4mm}} \\sum{{M_A}} = ({d[6]*f[7]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {2*(d[3]/3):.2f} {{\\text{{ m}}}} \\cdot F4_z)\\hat{{i}} + {d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{j}} + {d[0]*f[1] - d[0]*f[7] + 2*(d[3]/3)*f[9]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{k}}  }}$     
        
    #     $\\textbf{{\\small 2. Calculo del momento en B: }}$
        
    #     En B, es evidente que las unicas fuerzas que causan momento son $F_2$, $F_3$ Y $F_4$:
        
    #     $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_2 :}}$  
        
    #     ${{\hspace{{4mm}} M_{{B2}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_{{B2}} = ( 0 {{\\text{{ m}}}} \\cdot {f[5]:.0f}{{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[4]:.0f}{{\\text{{ N}}}} )\\hat{{i}} - ( {-d[0]:.0f} {{\\text{{ m}}}} \\cdot {f[5]}{{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot ({-f[3]:.0f}) {{\\text{{ N}}}})\\hat{{j}} + ( {-d[0]:.0f} {{\\text{{ m}}}} \\cdot {f[4]:.0f}{{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot ({-f[3]:.0f}) {{\\text{{ N}}}})\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_{{B2}} = [ 0 \\hat{{i}} + {d[0]*f[5]:.0f}\\hat{{j}} - {d[0]*f[4]:.0f} \\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}} }}$
        
    #     $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_3 :}}$  
        
    #     ${{\hspace{{4mm}} M_{{B3}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_{{B3}} = ( 0 {{\\text{{ m}}}} \\cdot {f[8]:.0f}{{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}})\\hat{{i}} - ( 0 {{\\text{{ m}}}} \\cdot {f[8]:.0f} {{\\text{{ N}}}} - {d[6]:.0f}{{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ( 0 {{\\text{{ m}}}} \\cdot ({-f[7]:.0f}) {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {f[6]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_{{B3}} = [ {d[6]*f[7]:.0f}\\hat{{i}} + {d[6]*f[6]:.0f}\\hat{{j}} + 0 \\hat{{k}} ]{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$    
        
    #     $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_4 :}}$  
        
    #     ${{\hspace{{4mm}} M_{{B4}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_{{B4}} = ( ({-2*(d[3]/3):.2f}) {{\\text{{ m}}}} \\cdot F4_z - 0 {{\\text{{ m}}}} \\cdot F4_y)\\hat{{i}} - ( ({-d[0]:.0f}) {{\\text{{ m}}}} \\cdot F4_z - 0 {{\\text{{ m}}}} \\cdot {f[9]:.0f} {{\\text{{ N}}}})\\hat{{j}} + ( ({-d[0]:.0f}) {{\\text{{ m}}}} \\cdot F4_y - ({-2*(d[3]/3):.2f}) {{\\text{{ m}}}} \\cdot {f[9]:.0f} {{\\text{{ N}}}})\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_{{B4}} =  ( {-2*(d[3]/3):.2f} {{\\text{{ m}}}} \\cdot F4_z )\\hat{{i}} + {d[0]:.0f} {{\\text{{ m}}}} \\cdot F4_z \\hat{{j}} + ({(2*(d[3]/3)*f[9]):2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[0]:.0f}{{\\text{{ m}}}} \\cdot F4_y )\\hat{{k}} }}$    
        
    #     $\\underline{{Sumatoria \\hspace{{2mm}} momentos \\hspace{{2mm}} en \\hspace{{2mm}} B :}}$

    #     ${{\hspace{{4mm}} \\sum{{M_B}} =  ( 0 {{\\text{{N}} \\cdot \\text{{ m}}}} + {d[6]*(f[7]):.0f}{{\\text{{N}} \\cdot \\text{{ m}}}} - {2*(d[3]/3):.2f} {{\\text{{ m}}}} \\cdot F4_z )\\hat{{i}} + ({d[0]*f[5]:.0f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[6]*f[6]:.0f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[0]:.0f} {{\\text{{ m}}}} \\cdot F4_z)\\hat{{j}} + (0 {{\\text{{ N}} \\cdot \\text{{ m}}}} + {(2*(d[3]/3)*f[9]):2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[0]:.0f}{{\\text{{ m}}}}\\cdot F4_y - {d[0]*f[4]:.0f}{{\\text{{ N}} \\cdot \\text{{ m}}}}) \\hat{{k}} }}$     
    #     ${{\hspace{{4mm}} \\sum{{M_B}} = ({d[6]*f[7]:.2f}{{\\text{{N}} \\cdot \\text{{ m}}}} - {2*(d[3]/3):.2f} {{\\text{{ m}}}} \\cdot F4_z)\\hat{{i}} + ({d[0]*f[5] + d[6]*f[6]:.0f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[0]:.2f} {{\\text{{ m}}}} \\cdot F4_z ) \\hat{{j}} + ({(2*(d[3]/3)*f[9] - d[0]*f[4]):2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[0]:.2f}{{\\text{{ m}}}}\\cdot F4_y)\\hat{{k}} }}$    
        
    #     $\\textbf{{\\small 3. Despeje de F4_y y F4_z: }}$
        
    #     Para cumplir la condición de que tanto el momento en B y el momento en A sean iguales, se observa que es necesario que sus compenentes asi lo sean. Tal que:
        
    #     ${{\hspace{{4mm}} 1.  ({d[6]*f[7]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {2*(d[3]/3):.2f} {{\\text{{ m}}}} \\cdot F4_z)\\hat{{i}} = ({d[6]*f[7]:.2f}{{\\text{{N}} \\cdot \\text{{ m}}}} - {2*(d[3]/3):.2f} {{\\text{{ m}}}} \\cdot F4_z)\\hat{{i}} }}$      
    #     ${{\hspace{{4mm}} 2.  ({d[0]*f[5] + d[6]*f[6]:.0f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[0]:.2f} {{\\text{{ m}}}} \\cdot F4_z )\\hat{{j}} =  {d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{j}}}}$      
    #     ${{\hspace{{4mm}} 3.  ({(2*(d[3]/3)*f[9] - d[0]*f[4]):2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[0]:.2f}{{\\text{{ m}}}}\\cdot F4_y)\\hat{{k}} =  {d[0]*f[1] - d[0]*f[7] + 2*(d[3]/3)*f[9]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{k}} }}$     
        
    #     De lo cual, se encuentran utiles las ecuaciones 2 y 3 para obtener los valores de $F4_z$ y $F4_y$ :
        
    #     $\\underline{{Despeje \\hspace{{2mm}} para \\hspace{{2mm}} F4_z :}}$  
        
    #     De la ecuación 2 se obtiene:
        
    #     ${{\hspace{{4mm}} ({d[0]*f[5] + d[6]*f[6]:.0f}{{\\text{{ N}} \\cdot \\text{{ m}}}} + {d[0]:.2f} {{\\text{{ m}}}} \\cdot F4_z )\\hat{{j}} =  {d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{j}}}}$      
    #     ${{\hspace{{4mm}} {d[0]:.2f} {{\\text{{ m}}}} \\cdot F4_z  = {d[0]*f[2] + d[6]*f[6]-d[0]*f[8]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[0]*f[5] + d[6]*f[6]:.0f}{{\\text{{ N}} \\cdot \\text{{ m}}}}}}$      
    #     ${{\hspace{{4mm}} F4_z = \\dfrac{{{d[0]*f[2] -d[0]*f[8] - d[0]*f[5] :.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}}}{{{d[0]:.2f} {{\\text{{ m}}}}}} }}$           
    #     ${{\hspace{{4mm}} F4_z = {f[2]-f[8] -f[5]:.2f}{{\\text{{ N}}}}}} $ 
        
    #     \\underline{{Despeje \\hspace{{2mm}} de \\hspace{{2mm}} por \\hspace{{2mm}} F4_y :}}$
        
    #     De la ecuación 3 se obtiene:  
        
    #     ${{\hspace{{4mm}} ({(2*(d[3]/3)*f[9] - d[0]*f[4]):2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[0]:.2f}{{\\text{{ m}}}}\\cdot F4_y)\\hat{{k}} = {d[0]*f[1] - d[0]*f[7] + 2*(d[3]/3)*f[9]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{k}} }}$         
    #     ${{\hspace{{4mm}} {d[0]:.2f}{{\\text{{ m}}}}\\cdot F4_y = {(2*(d[3]/3)*f[9] - d[0]*f[4]):2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} - {d[0]*f[1] - d[0]*f[7] + 2*(d[3]/3)*f[9]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} }}$       
    #     ${{\hspace{{4mm}} F4_y = \\dfrac{{{d[0]*f[7] - d[0]*f[1] - d[0]*f[4]:.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}}}}{{{d[0]:.2f} {{\\text{{ m}}}}}} }}$           
    #     ${{\hspace{{4mm}} F4_y = {f[7]-f[1]:.0f}{{\\text{{ N}}}}}} $ 
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),
        
    #========================================================  MOMENTO  =========================================================
    #--------------------------------------------     Momento en un punto en 3D      --------------------------------------------
    #-------------------------------------------------       Nivel Dificil   ---------------------------------------------------
    #-------------------------------------------------       Code: 2230011    --------------------------------------------------
    # Questionary(#1_1
    #     code = 2230011,
    #     no_pregunta = 1,
    #     complexity = D,
    #     topic = MO,
    #     subtopic = M3D,
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine la fuerza $F_1$ aplicado sobre el aguilón OA a una distancia $d_1$, sabiendo que la estructura no gira respecto al origen. Así mismo, calcule la tension $T_{{AC}}. Considere la tensión del cable  ABde magnitud ${f[0]:.2f}{{\\text{{ N}}}}$. Asuma $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$, $d_3 = {d[6]:.0f} \\text{{ m}}$, $d_4 = {d[9]:.0f} \\text{{ m}}$,  $d_5 = {d[12]:.0f}  \\text{{ m}}$ y  $d_6 = {d[15]:.0f} \\text{{ m}}$..",
    #     no_answers = 2,
    #     a1_name = "Magnitud de Fuerza $F_1$ [N]",
    #     a2_name = "Magnitud de Tension $T_{{AC}}$ [N]",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round((((d[3]+d[0])*((f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))) + ((d[3]+d[0])*((d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])))*(((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))/((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))))))/d[0],2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round(((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))/((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))),2),
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza.",
    #     ayuda2 = "Recordar que los signos de los componentes de $\\overrightarrow{{r}}$  y $\\overrightarrow{{F}}$ son importantes para determinar la dirección correcta del momento; recordando que el vector momento no solo indicamagnitud, sino también el eje alrededor del cual se produce la rotación el cual es perpendicular tanto al vector $\\overrightarrow{{r}}$ como $\\overrightarrow{{F}}$.",      
    #     ayuda3 = "Se puede dividir el problema en componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$, y resolver de manera independiente las componentes del momento.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. En 3 dimensiones es más fácil calcular el momento resolviendo producto cruz y dividiendo el ejercicio en determinar las componentes $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$. A continuación, se presenta la solución sugerida para el ejercicio:   
        
    #     $\\textbf{{\\small 1. Calculo de componentes de cada tensión: }}$    
        
    #     Antes de empezar a calcular momentos, para poder aplicar producto cruz, hay que hallar las componentes de ambas tensiones según el Vector Unitario asociado a cada una: 
        
    #     $\\underline{{Componentes\\hspace{{2mm}} de \\hspace{{2mm}}T_{{AB}}:}}$
        
    #     ${{\hspace{{4mm}} \\overrightarrow{{T_{{AB}}}} = |\\overrightarrow{{T_{{AB}}}}| \\cdot \\lambda_{{AB}}}}$    
    #     ${{\hspace{{4mm}} \\overrightarrow{{T_{{AB}}}} = {f[0]:.2f}{{\\text{{ N}}}} \\cdot [ ( {(d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} )\\hat{{i}} + ( {-(d[0]+d[3])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} )\\hat{{j}} + ( {(d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} )\\hat{{k}}]}}$    
    #     ${{\hspace{{4mm}} \\overrightarrow{{T_{{AB}}}} = [ ( {(f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} )\\hat{{i}} +  ( {(-f[0]*(d[0]+d[3]))/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} )\\hat{{j}} + ( {(f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} )\\hat{{k}}] {{\\text{{ N}}}}}}$     
        
    #     $\\underline{{Componentes\\hspace{{2mm}} de \\hspace{{2mm}}T_{{AC}}:}}$
        
    #     ${{\hspace{{4mm}} \\overrightarrow{{T_{{AC}}}} = |\\overrightarrow{{T_{{AC}}}}| \\cdot \\lambda_{{AC}}}}$    
    #     ${{\hspace{{4mm}} \\overrightarrow{{T_{{AC}}}} = |\\overrightarrow{{T_{{AC}}}}| \\cdot [ ( {(-d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f} )\\hat{{i}} +  ( {-(d[0]+d[3])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f} )\\hat{{j}} + ( {(d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f} )\\hat{{k}}]}}$       

    #     $\\textbf{{\\small 2. Calculo del momento en el origen: }}$ 
        
    #     $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} F_1 :}}$ 
        
    #     ${{\hspace{{4mm}} M_{{F_1}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_{{F_1}} = (-F_1 \\cdot {d[0]:.0f}{{\\text{{ m}}}})\\hat{{i}} + 0 {{\\text{{N}} \\cdot \\text{{ m}}}}\\hat{{j}} + 0 {{\\text{{N}} \\cdot \\text{{ m}}}}\\hat{{k}} }}$      
        
    #     $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} T_{{AB}} :}}$  
        
    #     ${{\hspace{{4mm}} M_{{T_{{AB}}}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_{{T_{{AB}}}} = ({(d[3]+d[0]) :.0f}{{\\text{{ m}}}} \\cdot {(f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot ({-(f[0]*(d[0]+d[3]))/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} ) {{\\text{{ N}}}} )\\hat{{i}} - ( 0 {{\\text{{ m}}}} \\cdot  {(f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} {{\\text{{ N}}}} - 0 {{\\text{{ m}}}} \\cdot {(f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} {{\\text{{ N}}}})\\hat{{j}} + ( 0 {{\\text{{ m}}}} \\cdot ({(-f[0]*(d[0]+d[3]))/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f}){{\\text{{ N}}}} - {d[3]+d[0]:.0f}{{\\text{{ m}}}} \\cdot {(f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])):.2f} {{\\text{{ N}}}})\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_{{T_{{AB}}}} = [ {(d[3]+d[0])*((f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}\\hat{{i}} + 0 \\hat{{j}} - {(d[3]+d[0])*((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}\\hat{{k}} ] {{ \\text{{N}} \\cdot \\text{{ m}}}} }}$     
        
    #     $\\underline{{Momento \\hspace{{2mm}} causado \\hspace{{2mm}} por \\hspace{{2mm}} T_{{AC}} :}}$  
        
    #     ${{\hspace{{4mm}} M_{{T_{{AC}}}} = (r_y \\cdot F_z - r_z \\cdot F_y)\\hat{{i}} - (r_x \\cdot F_z - r_z \\cdot F_x)\\hat{{j}} + (r_x \\cdot F_y - r_y \\cdot F_x)\\hat{{k}} }}$       
    #     ${{\hspace{{4mm}} M_{{T_{{AC}}}} = ({(d[3]+d[0]) :.0f}{{\\text{{ m}}}} \\cdot T_{{AC}} \\cdot {(d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f}  - 0 {{\\text{{ m}}}} \\cdot T_{{AC}} \\cdot ({-(d[0]+d[3])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f}) )\\hat{{i}} - ( 0 {{\\text{{ m}}}} \\cdot  T_{{AC}} \\cdot {(d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f} - 0 {{\\text{{ m}}}} \\cdot T_{{AC}} \\cdot ( {(-d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f} ))\\hat{{j}} + ( 0 {{\\text{{ m}}}} \\cdot T_{{AC}} \\cdot ({(-(d[0]+d[3]))/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f}) - {d[3]+d[0]:.0f}{{\\text{{ m}}}} \\cdot T_{{AC}} \\cdot  ( {(-d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])):.2f} ))\\hat{{k}}}}$       
    #     ${{\hspace{{4mm}} M_{{T_{{AC}}}} = {(d[3]+d[0])*((d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}} \\hat{{i}} + 0 {{ \\text{{N}} \\cdot \\text{{ m}}}} \\hat{{j}} + {(d[3]+d[0])*((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}}\\hat{{k}}  }}$      
        
    #     $\\underline{{Sumatoria \\hspace{{2mm}} momentos \\hspace{{2mm}} en \\hspace{{2mm}} Origen :}}$
        
    #     ${{\hspace{{4mm}} \\sum{{M_O}} = ({(d[3]+d[0])*((f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}{{\\text{{N}} \\cdot \\text{{ m}}}} + {(d[3]+d[0])*((d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}} - F_1 \\cdot {d[0]:.0f}{{\\text{{ m}}}})\\hat{{i}} + 0 \\hat{{j}} + ({(d[3]+d[0])*((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}} -{(d[3]+d[0])*((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}{{ \\text{{N}} \\cdot \\text{{ m}}}})\\hat{{k}} = 0\\hat{{i}} + 0\\hat{{j}} + 0\\hat{{k}}}}$      
        
    #     $\\textbf{{\\small 3. Despeje de T_{{AC}} y F_1: }}$
        
    #     Para cumplir la condición de que tanto el momento en B y el momento en A sean iguales, se observa que es necesario que sus compenentes asi lo sean. Tal que:
        
    #     ${{\hspace{{4mm}} 1.  ({(d[3]+d[0])*((f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}{{\\text{{N}} \\cdot \\text{{ m}}}} + {(d[3]+d[0])*((d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}} - F_1 \\cdot {d[0]:.0f}{{\\text{{ m}}}})\\hat{{i}} = 0{{\\text{{N}} \\cdot \\text{{ m}}}} \\hat{{i}} }}$      
    #     ${{\hspace{{4mm}} 2.  0{{\\text{{N}} \\cdot \\text{{ m}}}} \\hat{{j}} =  0 {{\\text{{N}} \\cdot \\text{{ m}}}}\\hat{{j}}}}$      
    #     ${{\hspace{{4mm}} 3.  ({(d[3]+d[0])*((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}} - {(d[3]+d[0])*((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}{{ \\text{{N}} \\cdot \\text{{ m}}}})\\hat{{k}} =  0 {{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{k}} }}$     
        
    #     De lo cual, se encuentran utiles las ecuaciones 1 y 3 para obtener los valores de $F_1$ y $T_{{AC}}$ :
        
    #     $\\underline{{Despeje \\hspace{{2mm}} para \\hspace{{2mm}} T_{{AC}} :}}$  
        
    #     De la ecuación 3 se obtiene:
        
    #     ${{\hspace{{4mm}} ({(d[3]+d[0])*((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}} - {(d[3]+d[0])*((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}{{ \\text{{N}} \\cdot \\text{{ m}}}})\\hat{{k}} =  0 {{\\text{{ N}} \\cdot \\text{{ m}}}}\\hat{{k}} }}$      
    #     ${{\hspace{{4mm}} {(d[3]+d[0])*((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot T_{{AC}}  = {(d[3]+d[0])*((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}{{ \\text{{N}} \\cdot \\text{{ m}}}}}}$      
    #     ${{\hspace{{4mm}} T_{{AC}} = {((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))/((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ N}}}}}} $ 
        
    #     \\underline{{Despeje \\hspace{{2mm}} de \\hspace{{2mm}} por \\hspace{{2mm}} F_1 :}}$
        
    #     Con el dato obtenido anteriormente, de la ecuación 1 se obtiene:  
        
    #     ${{\hspace{{4mm}} ({(d[3]+d[0])*((f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9]))):.2f}{{\\text{{N}} \\cdot \\text{{ m}}}} + {(d[3]+d[0])*((d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ m}}}} \\cdot{((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))/((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))):.2f}{{\\text{{ N}}}}  - F_1 \\cdot {d[0]:.0f}{{\\text{{ m}}}})\\hat{{i}} = 0{{\\text{{N}} \\cdot \\text{{ m}}}} \\hat{{i}} }}$      
    #     ${{\hspace{{4mm}} F_1 \\cdot {d[0]:.0f}{{\\text{{ m}}}} = {((d[3]+d[0])*((f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))) + ((d[3]+d[0])*((d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])))*(((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))/((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))))):.2f}{{\\text{{ N}} \\cdot \\text{{ m}}}} }}$       
    #     ${{\hspace{{4mm}} F_1 = {(((d[3]+d[0])*((f[0]*d[6])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))) + ((d[3]+d[0])*((d[15])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15])))*(((f[0]*d[9])/(Calculations.magnitude3D(d[0]+d[3],d[6],d[9])))/((d[12])/(Calculations.magnitude3D(d[0]+d[3],d[12],d[15]))))))/d[0]:.2f}{{\\text{{ N}}}}}} $     
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),
   
   
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
        pregunta = lambda f, a, calc, c, d, m: f"Determine las reacciones en los apoyos A y D (Indique el signo de la dirección de las fuerzas). Considere $F_1 = {f[0]:.0f} \\text{{ lb}}$, $F_2 = {f[1]:.0f} \\text{{ lb}}$,  $d_1 = {d[0]:.0f} \\text{{ ft}}$,  $d_2 = {d[3]:.0f}  \\text{{ ft}}$ y $d_3 = {d[6]:.0f} \\text{{ ft}}$.",
        no_answers = 3,
        a1_name = "Reacción $A_x$ [lb]",
        a2_name = "Reacción $A_y$ [lb]",
        a3_name = "Reacción $D_y$ [lb]",
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
         ${{\hspace{{4mm}} \\sum{{M_A}} = - {f[0]:.0f} \\text{{ lb}} \\cdot {d[0]:.0f} \\text{{ ft}} - {f[1]:.0f} \\text{{ lb}} \\cdot {d[0] + d[3]:.0f} \\text{{ ft}} + D_y \\cdot {2*d[0] + d[3]:.0f} \\text{{ ft}} = 0}}$     
        ${{\hspace{{4mm}} D_y \\cdot {2*d[0] + d[3]:.0f} \\text{{ ft}} = {f[0]*d[0]:.0f} \\text{{ lb}} \\cdot \\text{{ ft}} + {f[1]*(d[0] + d[3]):.0f} \\text{{ lb}} \\cdot \\text{{ ft}}}}$     
        ${{\hspace{{4mm}} D_y = \\dfrac{{ {f[0]*d[0]+f[1]*(d[0] + d[3]):.0f} \\text{{ lb}} \\cdot \\text{{ ft}} }}{{ {2*d[0] + d[3]:.0f} \\text{{ ft}} }} }}$      
        ${{\hspace{{4mm}} D_y = {(f[0]*d[0]+f[1]*(d[0] + d[3]))/(2*d[0] + d[3]):.2f} \\text{{ lb}} }}$     
        
        $\\textbf{{\\small 3. Condición de equilibrio - Sumatoria de fuerzas en Y: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + D_y - F_1 - F_2 = 0}}$     
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y +  {(f[0]*d[0]+f[1]*(d[0] + d[3]))/(2*d[0] + d[3]):.0f} \\text{{ lb}} - {f[0]:.0f} \\text{{ lb}}  - {f[1]:.0f} \\text{{ lb}} = 0}}$      
        ${{\hspace{{4mm}} A_y = {f[0]:.0f} \\text{{ lb}}  + {f[1]:.0f} \\text{{ lb}} - {(f[0]*d[0]+f[1]*(d[0] + d[3]))/(2*d[0] + d[3]):.0f} \\text{{ lb}} }}$     
        ${{\hspace{{4mm}} A_y = {f[0] + f[1] - ((f[0]*d[0]+f[1]*(d[0] + d[3]))/(2*d[0] + d[3])) :.2f} \\text{{ lb}} }}$   
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
        pregunta = lambda f, a, calc, c, d, m: f"Determine las fuerzas internas de los miembros AC, AD y BC (Use negativo si el elemento esta en compresión y positivo si el elemento esta tensión). Considere $F_1 = {f[0]:.0f} \\text{{ lb}}$, $d_1 = {d[0]:.0f} \\text{{ ft}}$, $\\alpha_1 = {(a[2]/7):.2f}°$ y $\\alpha_2 = {(a[1]/4):.2f}°$.",
        no_answers = 3,
        a1_name = "Fuerza en AC [lb]",
        a2_name = "Fuerza en AD [lb]",
        a3_name = "Fuerza en BC [lb]",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.sine((a[2]/7))))- (f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7)))))*((Calculations.cosine((a[1]/4)))/(Calculations.sine((a[2]/7)))),2),
        answer3 = lambda f, a, calc, c, d, m: np.round((-f[0] + (Calculations.sine((a[1]/4)))*(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))))/(Calculations.sine((a[1]/4))), 2),
        ayuda1 = C3,
        ayuda2 = C6,    
        ayuda3 = "",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre si por puntos llamados nodos, formando triángulos. El metodo de los nodos es una técnica para determinar fuerzas internas utilizando el principio de que cada nodo está en equilibrio. A continuación, se presenta la solución sugerida para el ejercicio: 
        
        $\\textbf{{\\small 1. Cálculo de las reacciones en los apoyos: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$               
        ${{\hspace{{4mm}} \\sum{{F_x}} = A_x + F_1= 0}}$     
        ${{\hspace{{4mm}} A_x = {-f[0]:.0f} \\text{{ lb}} }}$         
              
        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{M_A}} = - F_1 \\cdot \\left(\\dfrac{{d_1}}{{tan(\\alpha_2)}}\\right) + B_y \\cdot (2 \\cdot d_1 ) = - {f[0]:.0f} \\text{{ lb}} \\cdot {(d[0])/(Calculations.tangent((a[1]/4))):.0f} \\text{{ ft}} + B_y \\cdot {2*d[0]:.0f} \\text{{ ft}} = 0}}$     
        ${{\hspace{{4mm}} B_y \\cdot {2*d[0]:.0f} \\text{{ ft}} = {f[0]*((d[0])/(Calculations.tangent((a[1]/4)))):.0f} \\text{{ lb}} \\cdot \\text{{ ft}} }}$         
        ${{\hspace{{4mm}} B_y = {(f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]):.2f} \\text{{ lb}} }}$     
             
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + B_y = A_y +  {(f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]):.2f} \\text{{ lb}} = 0}}$     
        ${{\hspace{{4mm}} A_y = {-((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0])) :.2f} \\text{{ lb}} }}$
        
        $\\textbf{{\\small 2. Nodo A: }}$

        En el nodo A se pueden determinar las fuerzas internas $F_{{AD}}$ y $F_{{AC}}$. Para ello, se define un sistema de ecuaciones utilizando la sumatoria de fuerzas en los ejes estándar. Alternativamente, se puede cambiar el sistema de referencia, alineando uno de los nuevos ejes de forma que sea perpendicular a una de las fuerzas desconocidas.
    
        A continuación, se presenta la solución utilizando el primer método, en el cual se resolverá el sistema de ecuaciones mediante sustitución:

        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{AD}} \\cdot \\cos(\\alpha_1) + F{{AC}} \\cdot \\sin(\\alpha_2) - |A_x| = F_{{AD}} \\cdot {Calculations.cosine((a[2]/7)):.2f} + F_{{AC}} \\cdot {Calculations.sine((a[1]/4)):.2f} - {f[0]:.0f} \\text{{ lb}}  = 0 }}$     
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = F_{{AD}} \\cdot \\sin(\\alpha_1) + F{{AC}} \\cdot \\cos(\\alpha_2) - |A_y| = F_{{AD}} \\cdot {Calculations.sine((a[2]/7)):.2f} + F_{{AC}} \\cdot {Calculations.cosine((a[1]/4)):.2f} - {((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0])) :.2f} \\text{{ lb}} = 0 }}$      
        
        De la ecuación 2, se despeja $F_{{AD}}$ en términos de $F_{{AC}}$:
        
        ${{\hspace{{4mm}} F_{{AD}} \\cdot {Calculations.sine((a[2]/7)):.2f} + F_{{AC}} \\cdot {Calculations.cosine((a[1]/4)):.2f} - {((f[0]*d[3])/(2*d[0])) :.2f} \\text{{ lb}} = 0 }}$      
        ${{\hspace{{4mm}} F_{{AD}} = {((f[0]*d[3])/(2*d[0]*Calculations.sine((a[2]/7)))):.2f} \\text{{ lb}} - F_{{AC}} \\cdot {(Calculations.cosine((a[1]/4)))/(Calculations.sine((a[2]/7))):.2f} }}$ 
        
        Se reemplaza en la ecuación 1:     
              
        ${{\hspace{{4mm}} F_{{AD}} \\cdot {Calculations.cosine((a[2]/7)):.2f} + F_{{AC}} \\cdot {Calculations.sine((a[1]/4)):.2f} - {f[0]:.0f} \\text{{ lb}} = 0 }}$      
        ${{\hspace{{4mm}} ({((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))) :.2f} \\text{{ lb}} - F_{{AC}} \\cdot {(Calculations.cosine((a[1]/4)))/(Calculations.sine((a[2]/7))):.2f} ) \\cdot {Calculations.cosine((a[2]/7)):.2f} + F_{{AC}} \\cdot {Calculations.sine((a[1]/4)):.2f} = {f[0]:.0f} \\text{{ lb}}}}$       
        ${{\hspace{{4mm}} F_{{AC}} \\cdot ({Calculations.sine((a[1]/4)) - (Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))):.2f}) = {f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))):.2f} \\text{{ lb}}}}$      
        ${{\hspace{{4mm}} F_{{AC}} = {(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))):.2f} \\text{{ lb}} }}$       
              
        Se calcula $F_{{AD}}$:
        
        ${{\hspace{{4mm}} F_{{AD}} = {((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.sine((a[2]/7)))):.2f} \\text{{ lb}} - F_{{AC}} \\cdot {(Calculations.cosine((a[1]/4)))/(Calculations.sine((a[2]/7))):.2f}}}$      
        ${{\hspace{{4mm}} F_{{AD}} = {((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.sine((a[2]/7)))):.2f} \\text{{ lb}} - {(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7)))))*(Calculations.cosine((a[1]/4)))/(Calculations.sine((a[2]/7))):.2f} \\text{{ lb}} }}$     
        ${{\hspace{{4mm}} F_{{AD}} = {((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.sine((a[2]/7))))- (f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7)))))*(Calculations.cosine((a[1]/4)))/(Calculations.sine((a[2]/7))):.2f} \\text{{ lb}} }}$     
        
        $\\textbf{{\\small 3. Nodo C: }}$

        Para el nodo C, se obtienen las siguientes ecuaciones:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{CB}} \\cdot \\sin(\\alpha_2) + ({-(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))):.2f} \\text{{ lb}} ) \\cdot \\sin(\\alpha_2) + F_1 = F_{{CB}} \\cdot {Calculations.sine((a[1]/4)):.2f} + ( {-(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))):.2f} \\text{{ lb}} ) \\cdot {Calculations.sine((a[1]/4)):.2f} + {f[0]:.0f} \\text{{ lb}} = 0 }}$      
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = F_{{CB}} \\cdot \\cos(\\alpha_2) + ({-(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))):.2f} \\text{{ lb}} ) \\cdot \\cos(\\alpha_2) + F_{{CD}} = F_{{CB}} \\cdot {Calculations.cosine((a[1]/4)):.2f} + ( {-(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))):.2f} \\text{{ lb}} ) \\cdot {Calculations.cosine((a[1]/4)):.2f} + F_{{CD}} = 0 }}$      
        
        Dada la pregunta del ejercicio, solo se necesita despejar F_{{CB}} de la primera ecuación:
        
        ${{\hspace{{4mm}} F_{{CB}} \\cdot {Calculations.sine((a[1]/4)):.2f} + ( {-(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))):.2f} \\text{{ lb}} ) \\cdot {Calculations.sine((a[1]/4)):.2f} + {f[0]:.0f} \\text{{ lb}} = 0 }}$      
        ${{\hspace{{4mm}} F_{{CB}} \\cdot {Calculations.sine((a[1]/4)):.2f} = {-f[0] + (Calculations.sine((a[1]/4)))*(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))):.2f} \\text{{ lb}}}}$      
        ${{\hspace{{4mm}} F_{{CB}} = {(-f[0] + (Calculations.sine((a[1]/4)))*(f[0] - ((f[0]*((d[0])/(Calculations.tangent((a[1]/4)))))/(2*d[0]*Calculations.tangent((a[2]/7)))))/(Calculations.sine((a[1]/4)) - ((Calculations.cosine((a[1]/4)))/(Calculations.tangent((a[2]/7))))))/(Calculations.sine((a[1]/4))):.2f} \\text{{ lb}}}}$      
        
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
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuántos elementos de fuerza cero tiene la armadura Baltimore mostrada?.",
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
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre sí por puntos llamados nodos, formando triángulos. Un elemento de fuerza cero se define como un miembro de la armadura que no experimenta ninguna fuerza axial (Tension o compresión). A continuación, se presenta la solución sugerida para el ejercicio: 
          
        Inicialmente, para resolver el problema es necesario notar que la cercha es simétrica en geometría y carga. Esto implica que las fuerzas internas y las reacciones se distribuyen de forma simétrica; por ejemplo, $F_{{AF}} = F_{{EI}}$.
        
        Además, se debe tener en cuenta que si hay tres elementos conectados en un nodo, donde dos de ellos son colineales y no hay cargas externas aplicadas en el nodo, el tercer miembro va a ser de fuerza cero. Esto nos permite identificar que los elementos $FB, GB, HD, ID$ y $KC$ son de fuerza cero.
        
        Una vez identificados los anteriores elementos de fuerza cero, si se realiza la sumatoria de fuerzas en los nodos B y D, se encontrará que los elementos $BJ$ y $DL$ también son de fuerza cero.    
        
        En resumen, se identifican un total de 7 elementos de fuerza cero: $FB, GB, HD, ID, KC, BJ$ y $DL$.       
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
        pregunta = lambda f, a, calc, c, d, m: f"Determine las fuerzas internas de los miembros AB, FD y CE de la armadura Gambrel presentada (Use negativo si el elemento esta en compresión y positivo si el elemento esta tensión). Considere $F_1 = {f[0]:.0f} \\text{{ lb}}$, $F_2 = {f[1]:.0f} \\text{{ lb}}$, $F_3 = {f[2]:.0f} \\text{{ lb}}$, $d_1 = {d[0]:.0f} \\text{{ ft}}$, $d_2 = {d[3]:.0f}  \\text{{ ft}}$,  $d_3 = {d[6]:.0f} \\text{{ ft}}$ y $d_4 = {d[9]:.0f}  \\text{{ ft}}$.",
        no_answers = 3,
        a1_name = "Fuerza en AB [lb]",
        a2_name = "Fuerza en DF [lb]",
        a3_name = "Fuerza en CE [lb]",
        answer1 = lambda f, a, calc, c, d, m: np.round(-((f[1] + (f[0]/2))/((d[6])/(Calculations.magnitude(d[0],d[6])))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(((f[0]/2) + ((f[1] + (f[0]/2))*(d[0]/d[3])))/(((d[9] + d[6])/(Calculations.magnitude(d[3],d[9])))),2),
        answer3 = lambda f, a, calc, c, d, m: np.round(((f[1] + (f[0]/2))/(d[6]))*(d[0]), 2),
        ayuda1 = "La armadura Gambrel se caracteriza por ser una estructura simétrica. ¿Qué nos dice esto respecto a las reacciones y a las fuerzas de cada elemento?",
        ayuda2 = "Uno de los metodos para analizar fuerzas en elementos de cerchas es el Método de los nodos. Este consiste en evaluar el equilibrio en cada nodo. Para analizar mejor un nodo es importante dibujar un diagrama de cuerpo libre claro y detallado con cada fuerza involucrada",      
        ayuda3 = "Un miembro en compresión empuja o genera una fuerza sobre el nodo (la fuerza entra al nodo); un miembro a tensión jala o genera una fuerza hacia afuera del nodo (la fuerza sale del nodo)",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre si por puntos llamados nodos, formando triángulos. El metodo de nodos es una técnica para determinar fuerzas internas utilizando el principio de que cada nodo está en equilibrio bajo las fuerzas que actúan sobre él. A continuación, se presenta la solución sugerida para el ejercicio: 
        
        $\\textbf{{\\small 1. Cálculo de las reacciones en los apoyos: }}$
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$               
        ${{\hspace{{4mm}} \\sum{{F_x}} = H_x = 0}}$             
              
        Ahora bien, dado que la cercha es simétrica, se sabe que $H_y$ = $A_y$, tal que, se podrá obtener el siguiente resultado de la sumatoria de fuerzas en Y: 
             
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + H_y - (2F_3 + 2F_2 + F_1) = 2A_y - {2*f[2] + 2*f[1] + f[0]:.0f} \\text{{ lb}} = 0}}$     
        ${{\hspace{{4mm}} H_y = A_y = {f[2] + f[1] + (f[0]/2):.0f} \\text{{ lb}} }}$
        
        $\\textbf{{\\small 2. Nodo A: }}$

        En el nodo A se puede obtener las siguientes ecuaciones:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{BC}} - F_{{AB}} \\cdot \\dfrac{{d_1}}{{sqrt{{(d_1)^{{2}} + (d_3)^{{2}}}}}} = F_{{BC}} - F_{{AB}} \\cdot {(d[0])/(Calculations.magnitude(d[0],d[6])):.2f} = 0 }}$     
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = A_y - F_3 - F_{{AB}} \\cdot \\dfrac{{d_3}}{{sqrt{{(d_1)^{{2}} + (d_3)^{{2}}}}}}= {f[2] + f[1] + (f[0]/2):.0f} \\text{{ lb}} - {f[2]:0f} \\text{{ lb}} - F_{{AB}} \\cdot {(d[6])/(Calculations.magnitude(d[0],d[6])):.2f} = 0 }}$      
        
        De la ecuación 2, podemos obtener F_{{AB}}:
        
        ${{\hspace{{4mm}} {f[2] + f[1] + (f[0]/2):.0f} \\text{{ lb}} - {f[2]:0f} \\text{{ lb}} - F_{{AB}} \\cdot {(d[6])/(Calculations.magnitude(d[0],d[6])):.2f}= 0}}$      
        ${{\hspace{{4mm}} F_{{AB}} \\cdot {(d[6])/(Calculations.magnitude(d[0],d[6])):.2f} = {f[1] + (f[0]/2):.0f} \\text{{ lb}}}}$      
        ${{\hspace{{4mm}} F_{{AB}} = {(f[1] + (f[0]/2))/((d[6])/(Calculations.magnitude(d[0],d[6]))):.2f} \\text{{ lb}}}}$      
        
        Ahora bien, uno se da cuenta, que en el nodo C, solo estan involucradas las fuerzas $F_{{AC}}$ y $F_{{CE}}, siendo que, el elemento BC es de fuerza cero. Tal que, se puede sacar $F_{{CE}}$ calculando $F_{{AC}}$ en la ecuación 1 del nodo A, reemplazando el dato de $F_{{AB}}$ obtenido anteriormente:
              
        ${{\hspace{{4mm}} F_{{BC}} - {(f[1] + (f[0]/2))/((d[6])/(Calculations.magnitude(d[0],d[6]))):.2f} \\text{{ lb}} \\cdot {(d[0])/(Calculations.magnitude(d[0],d[6])):.2f} = 0}}$      
        ${{\hspace{{4mm}} F_{{CE}} = F_{{BC}} = {((f[1] + (f[0]/2))/(d[6]))*(d[0]):.2f} \\text{{ lb}} }}$       
        
        $\\textbf{{\\small 3. Nodo B: }}$

        Como la cercha es simétrica se podrá resolver para el nodo B, y calcular el resutlado de $F_{{BD}}$, que va a ser el mismo que $F_{{DF}}$:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{AB}} \\cdot \\dfrac{{d_1}}{{sqrt{{(d_1)^{{2}} + (d_3)^{{2}}}}}} - F_{{BE}} \\cdot \\dfrac{{d_2}}{{sqrt{{(d_2)^{{2}} + (d_3)^{{2}}}}}} - F_{{BD}} \\cdot \\dfrac{{d_2}}{{sqrt{{(d_2)^{{2}} + (d_4)^{{2}}}}}} = {((f[1] + (f[0]/2))/(d[6]))*(d[0]):.2f} \\text{{ lb}}  - F_{{BE}} \\cdot {(d[3])/(Calculations.magnitude(d[3],d[6])):.2f} - F_{{BD}} \\cdot {(d[3])/(Calculations.magnitude(d[3],d[9])):.2f} = 0}}$      
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = - F_2 + F_{{AB}} \\cdot \\dfrac{{d_3}}{{sqrt{{(d_1)^{{2}} + (d_3)^{{2}}}}}} + F_{{BE}} \\cdot \\dfrac{{d_3}}{{sqrt{{(d_2)^{{2}} + (d_3)^{{2}}}}}} - F_{{BD}} \\cdot \\dfrac{{d_4}}{{sqrt{{(d_2)^{{2}} + (d_4)^{{2}}}}}} = - {f[1]:.0f}\\text{{ lb}} + {(f[1] + (f[0]/2)):.2f} \\text{{ lb}}  + F_{{BE}} \\cdot {(d[6])/(Calculations.magnitude(d[3],d[6])):.2f} - F_{{BD}} \\cdot {(d[9])/(Calculations.magnitude(d[3],d[9])):.2f}  = 0 }}$      
        
        Donde, se observa como de la primera ecuación se puede despejar $F_{{BE}}$ en terminos de $F_{{BD}}$, para luego hacer la sustitución en la segunda ecuación y resolver para $F_{{BD}}:
        
        ${{\hspace{{4mm}} {(f[1] + (f[0]/2))*(d[0]/d[6]):.2f} \\text{{ lb}}  - F_{{BE}} \\cdot {(d[3])/(Calculations.magnitude(d[3],d[6])):.2f} - F_{{BD}} \\cdot {(d[3])/(Calculations.magnitude(d[3],d[9])):.2f} = 0}}$      
        ${{\hspace{{4mm}} F_{{BE}} \\cdot {(d[3])/(Calculations.magnitude(d[3],d[6])):.2f} = {(f[1] + (f[0]/2))*(d[0]/d[6]):.2f} \\text{{ lb}}  - F_{{BD}} \\cdot {(d[3])/(Calculations.magnitude(d[3],d[9])):.2f}}}$      
        ${{\hspace{{4mm}} F_{{BE}} = {((f[1] + (f[0]/2))*((d[0]*(Calculations.magnitude(d[3],d[6])))/(d[6]*d[3]))):.2f} \\text{{ lb}} - F_{{BD}} \\cdot {(Calculations.magnitude(d[3],d[6]))/(Calculations.magnitude(d[3],d[9])):.2f}}}$     
        
        Finalmente:
        ${{\hspace{{4mm}} {(f[0]/2):.2f} \\text{{ lb}} + F_{{BE}} \\cdot {(d[6])/(Calculations.magnitude(d[3],d[6])):.2f} - F_{{BD}} \\cdot {(d[9])/(Calculations.magnitude(d[3],d[9])):.2f} = 0 }}$      
        ${{\hspace{{4mm}} F_{{BD}} \\cdot {(d[9])/(Calculations.magnitude(d[3],d[9])):.2f} =  {(f[0]/2):.2f} \\text{{ lb}} + ({((f[1] + (f[0]/2))*((d[0]*(Calculations.magnitude(d[3],d[6])))/(d[6]*d[3]))):.2f} \\text{{ lb}} - F_{{BD}} \\cdot {(Calculations.magnitude(d[3],d[6]))/(Calculations.magnitude(d[3],d[9])):.2f}) \\cdot {(d[6])/(Calculations.magnitude(d[3],d[6])):.2f}}}$      
        ${{\hspace{{4mm}} F_{{BD}} \\cdot {(d[9])/(Calculations.magnitude(d[3],d[9])):.2f} =  {(f[0]/2) + ((f[1] + (f[0]/2))*(d[0]/d[3])):.2f} \\text{{ lb}} - F_{{BD}} \\cdot {(d[6])/(Calculations.magnitude(d[3],d[9])):.2f} }}$      
        ${{\hspace{{4mm}} F_{{BD}} \\cdot {((d[9] + d[6])/(Calculations.magnitude(d[3],d[9]))):.2f} = {(f[0]/2) + ((f[1] + (f[0]/2))*(d[0]/d[3])):.2f} \\text{{ lb}}}}$      
        ${{\hspace{{4mm}} F_{{DF}} = F_{{BD}} = {((f[0]/2) + ((f[1] + (f[0]/2))*(d[0]/d[3])))/(((d[9] + d[6])/(Calculations.magnitude(d[3],d[9])))):.2f} \\text{{ lb}}}}$      
        
                        
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
        pregunta = lambda f, a, calc, c, d, m: f"Si la fuerza máxima que cualquier elemento puede soportar es de ${f[0] + 25:0f} \\text{{ N}}$ en tensión y de ${f[0]:0f}\\text{{ N}}$ en compresión, calcule cual es la fuerza $F_1$ máxima que puede ser soportada en el nudo E. Considere $d_1 = {d[0]:.0f} \\text{{ m}}$ y $\\alpha_1 = {(a[1]/3):.2f}°$ .",
        no_answers = 1,
        a1_name = "F_1 [N]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round((f[0])*(Calculations.sine((a[1]/3))),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "Uno de los metodos para analizar fuerzas en elementos de cerchas es el Método de los nodos. Este consiste en evaluar el equilibrio en cada nodo.",
        ayuda2 = "Para analizar mejor un nodo es importante dibujar un diagrama de cuerpo libre claro y detallado con cada fuerza involucrada",      
        ayuda3 = "Un miembro en compresión empuja o genera una fuerza sobre el nodo (la fuerza entra al nodo); un miembro a tensión jala o genera una fuerza hacia afuera del nodo (la fuerza sale del nodo)",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre si por puntos llamados nodos, formando triángulos. El metodo de nodos es una técnica para determinar fuerzas internas utilizando el principio de que cada nodo está en equilibrio bajo las fuerzas que actúan sobre él. A continuación, se presenta la solución sugerida para el ejercicio: 
        
        $\\textbf{{\\small 1. Cálculo de las reacciones en los apoyos: }}$     
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$               
        ${{\hspace{{4mm}} \\sum{{F_x}} = C_x = 0}}$             
              
        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{M_A}} = C_y \\cdot d_1 - F_1 \\cdot 2d_1 = 0}}$     
        ${{\hspace{{4mm}} C_y = 2F_1 }}$     
             
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + C_y - F_1 = 0}}$     
        ${{\hspace{{4mm}} A_y = -F_1 }}$     
        
        Ahora bien, al observar la configuración de la cercha y las reacciones en los apoyos, se puede intuir que $F_{{AB}} = F_{{ED}}$; $F_{{AC}} = F_{{EC}}$; y $F_{{BC}} = F_{{DC}}$. Tal que, solo será necesario realmente evaluar 4 fuerzas internas:

        $\\textbf{{\\small 2. Nodo A: }}$     
        
        En el nodo A se puede obtener las siguientes ecuaciones:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{AB}} \\cdot \\cos(\\alpha_1) - F_{{AC}} =  F_{{AB}} \\cdot {Calculations.cosine((a[1]/3)):.2f} - F_{{AC}} = 0 }}$     
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = F_{{AB}} \\cdot \\sin(\\alpha_1) - F_1 = F_{{AB}} \\cdot {Calculations.sine((a[1]/3)):.2f} - F_1 = 0 }}$     
        
        De lo cual, se usa la ecuación 2. para determinar $F_{{AB}}$:
        ${{\hspace{{4mm}} F_{{AB}} \\cdot {Calculations.sine((a[1]/3)):.2f} - F_1 = 0 }}$     
        ${{\hspace{{4mm}} F_{{AB}} = F_1 \\cdot {1/(Calculations.sine((a[1]/3))):.2f}}}$     
        
        Se obtiene $F_{{AC}}$ de la ecuación 1.:
        
        ${{\hspace{{4mm}} F_{{AB}} \\cdot {Calculations.cosine((a[1]/3)):.2f} - F_{{AC}} = 0 }}$     
        ${{\hspace{{4mm}} F_{{AC}} = F_1 \\cdot {1/(Calculations.tangent((a[1]/3))):.2f}}}$     
        
        $\\textbf{{\\small 3. Nodo B: }}$     
        
        En el nodo B se puede obtener las siguientes ecuaciones:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{BD}} - F_{{AB}} \\cdot \\cos(\\alpha_1) - F_{{BC}} \\cdot \\cos(\\alpha_1) = F_{{BD}} - F_{{AB}} \\cdot {Calculations.cosine((a[1]/3)):.2f} - F_{{BC}} \\cdot {Calculations.cosine((a[1]/3)):.2f} = 0 }}$     
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = F_{{BC}} \\cdot \\sin(\\alpha_1) - F_{{AB}} \\cdot \\sin(\\alpha_1) = F_{{BC}} \\cdot {Calculations.sine((a[1]/3)):.2f} - F_{{AB}} \\cdot {Calculations.sine((a[1]/3)):.2f} = 0 }}$     
        
        De lo cual, se define de la ecuación 2:
        ${{\hspace{{4mm}} F_{{BC}} \\cdot {Calculations.sine((a[1]/3)):.2f} - F_{{AB}} \\cdot {Calculations.sine((a[1]/3)):.2f} = 0 }}$     
        ${{\hspace{{4mm}} F_{{BC}} = F_{{AB}} = F_1 \\cdot {1/(Calculations.sine((a[1]/3))):.2f}}}$     
        
        Se obtiene $F_{{BD}}$ de la ecuación 1.:
        
        ${{\hspace{{4mm}} F_{{BD}} - F_{{AB}} \\cdot {Calculations.cosine((a[1]/3)):.2f} - F_{{BC}} \\cdot {Calculations.cosine((a[1]/3)):.2f} = 0 }}$     
        ${{\hspace{{4mm}} F_{{BD}} =  F_1 \\cdot {2/(Calculations.tangent((a[1]/3))):.2f}}}$     
        
        $\\textbf{{\\small 4. Evaluación de la condición de resistencia máxima: }}$     
        
        $\\underline{{Elementos \\hspace{{2mm}} de \\hspace{{2mm}} Tensión:}}$      
        
        Los elementos de tensión encontrados fueron el AB y el BD, tal que, estas fuerzas deben ser menor o igual a ${f[0]+ 25:0f} \\text{{ N}}$. Dado que, el elemento BD tiene que resistir más o igual fuerza AB, se va a evaluar en este:
        
        ${{\hspace{{4mm}} F_{{BD}} = F_1 \\cdot {2/(Calculations.tangent((a[1]/3))):.2f} = {f[0]+ 25:0f} \\text{{ N}} }}$     
        ${{\hspace{{4mm}} F_1 = {((f[0]+ 25)/2)*(Calculations.tangent((a[1]/3))):2f} \\text{{ N}}}}$     
        
        $\\underline{{Elementos \\hspace{{2mm}} de \\hspace{{2mm}} Compresión:}}$  
        
        Los elementos de compresión encontrados fueron el AC y el BC, tal que, estas fuerzas deben ser menor o igual a ${f[0]:0f} \\text{{ N}}$. Dado que, el elemento BC tiene que resistir más o igual fuerza que AC, se va a evaluar en este:
        
        ${{\hspace{{4mm}} F_{{BC}} = F_1 \\cdot {1/(Calculations.sine((a[1]/3))):.2f} = {f[0]:0f} \\text{{ N}} }}$     
        ${{\hspace{{4mm}} F_1 = {(f[0])*(Calculations.sine((a[1]/3))):2f} \\text{{ N}}}}$     
        
        Finalmente, se selecciona la respuesta menor, siendo que, si seleccionará la mayor, el otro elemento no resistiría y la estructura fallaría.
            
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
        pregunta = lambda f, a, calc, c, d, m: f"¿Cuantos elementos de fuerza cero tiene la armadura Fink mostrada?.",
        no_answers = 1,
        a1_name = "Número de elementos de fuerza cero",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(7,2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "Uno de los metodos para analizar fuerzas en elementos de cerchas es el Método de los nodos. Este consiste en evaluar el equilibrio en cada nodo. Para analizar mejor un nodo es importante dibujar un diagrama de cuerpo libre claro y detallado con cada fuerza involucrada",
        ayuda2 = "Revisar si los elementos son colineales o perpendiculares entre ellos, y donde se aplican las fuerzas externas en la armadura puede darnos un indicio a encontrar un elemento de fuerza cero.",      
        ayuda3 = "Un miembro en compresión empuja o genera una fuerza sobre el nodo (la fuerza entra al nodo); un miembro a tensión jala o genera una fuerza hacia afuera del nodo (la fuerza sale del nodo)",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre si por puntos llamados nodos, formando triángulos. Un elemento de fuerza cero se define como un miembro de la armadura que no experimenta ninguna fuerza axial (Tension o compresión). A continuación, se presenta la solución sugerida para el ejercicio: 

        Primero, se debe tener presente el hecho de que si hay tres elementos conectados en un nodo, donde dos de ellos son colineales y no se presentan cargas externas aplicadas en el nodo, el tercer miembro va a ser de fuerza cero.
        Siendo que, esto puede ser aplicado en los nodos B, J y N para evidenciar que los elementos BC, JI y NM son elementos de fuerza cero.
        
        Del mismo modo, teniendo en cuenta que estos elementos son de fuerza cero, se logra utilizar el mismo concepto en los nodos C, I y M para corroborar que los elementos CD, IL y ML son de fuerza cero.
        
        Por otro lado, al ser IL y ML elementos de fuerza cero, se puede dar cuenta evaluando el nodo L que el elemento LK es de fuerza cero.  
        
        Finalmente, se consigue contar un total de 7 elementos de fuerza cero.
        
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
        pregunta = lambda f, a, calc, c, d, m: f"Determine las fuerzas internas de los miembros DC, HC y DH de la armadura presentada (Use negativo si el elemento esta en compresión y positivo si el elemento esta tensión). Considere $F_1 = {f[0]:.0f} \\text{{ lb}}$, $F_2 = {f[1]:.0f} \\text{{ lb}}$, $F_3 = {f[2]:.0f} \\text{{ lb}}$, $F_4 = {f[2]:.0f} \\text{{ lb}}$, $d_1 = {d[0]:.0f} \\text{{ ft}}$ y $d_2 = {d[3]:.0f}  \\text{{ ft}}$.",
        no_answers = 3,
        a1_name = "Fuerza en DC [lb]",
        a2_name = "Fuerza en HC [lb]",
        a3_name = "Fuerza en DH [lb]",
        answer1 = lambda f, a, calc, c, d, m: np.round(-(f[3]*d[3]+f[2]*2*d[3])/((d[0]*d[3])/(Calculations.magnitude(d[0],d[3]))),2),
        answer2 = lambda f, a, calc, c, d, m: np.round(f[3] + 2*f[2],2),
        answer3 = lambda f, a, calc, c, d, m: np.round((f[3]+f[2]*2)*(d[3]/d[0]) - f[1], 2),
        ayuda1 = "Uno de los metodos para analizar fuerzas en elementos de cerchas es el Método de secciones. Este se basa en el principio de que si la armadura esta en equilibrio así mismo lo estará cualquier parte de ella.",
        ayuda2 = "Uno de los metodos para analizar fuerzas en elementos de cerchas es el Método de los nodos. Este consiste en evaluar el equilibrio en cada nodo. Para analizar mejor un nodo es importante dibujar un diagrama de cuerpo libre claro y detallado con cada fuerza involucrada",      
        ayuda3 = "Un miembro en compresión empuja o genera una fuerza sobre el nodo (la fuerza entra al nodo); un miembro a tensión jala o genera una fuerza hacia afuera del nodo (la fuerza sale del nodo)",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre si por puntos llamados nodos, formando triángulos. A continuación, se presenta la solución sugerida para el ejercicio: 
        
        $\\textbf{{\\small 1. Cálculo de las reacciones en los apoyos: }}$     
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$               
        ${{\hspace{{4mm}} \\sum{{F_x}} = A_x - F_3 - F_4 = 0}}$             
        ${{\hspace{{4mm}} A_x = F_3 + F_4 = {f[2] + f[3] :.0f} \\text{{ lb}}}}$         
             
        ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$     
        ${{\hspace{{4mm}} \\sum{{M_A}} = F_4 \\cdot d_2 + F_3 \\cdot 2d_2 + F_1 \\cdot d_1 - F_y \\cdot 2d_1 = 0}}$     
        ${{\hspace{{4mm}} F_y = \\dfrac{{F_4 \\cdot d_2 + F_3 \\cdot 2d_2 + F_1 \\cdot d_1}}{{2d_1}} = {(f[3]*d[3]+f[2]*2*d[3]+f[0]*d[0])/(2*d[0]):.2f}}}$     
             
        ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
        ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + F_y - F_1 - F_2 = 0}}$     
        ${{\hspace{{4mm}} A_y = F_1 + F_2 - F_y = {f[0] + f[1] - (f[3]*d[3]+f[2]*2*d[3]+f[0]*d[0])/(2*d[0]) :.2f}}}$     
        
        $\\textbf{{\\small 2. Condición de equilibrio de armadura seccionada: }}$     
        
        En la armadura mostrada, se realiza un corte donde se obtiene solo la parte compuesta por nodos FEDGH, teniendo solo a las reacciones en F y las fuerzas $F_1$, $F_2$, $F_{{DC}}$, $F_{{HC}}$ y $F_{{HI}}$ como fuerzas involucradas. A partir de las cuales, se utilizan las ecuaciones de equilibrio para encontrar las fuerzas deseadas:
        
        $\\underline{{Despeje \\hspace{{2mm}} de \\hspace{{2mm}} F_{{DC}}:}}$    
        
        ${{\hspace{{4mm}} \\sum{{M_H}} = F_1 \\cdot d_1 - F_y \\cdot 2d_1 - F_{{DC}} \\cdot  \\dfrac{{d_1}}{{sqrt{{(d_1)^{{2}} + (d_2)^{{2}}}}}}  \\cdot d_2 = {f[0]*d[0]:.2f} \\text{{ lb}} \\cdot \\text{{ ft}} - {(f[3]*d[3]+f[2]*2*d[3]+f[0]*d[0]):.2f} \\text{{ lb}} \\cdot \\text{{ ft}} - F_{{DC}} \\cdot {(d[0]*d[3])/(Calculations.magnitude(d[0],d[3])):.2f} \\text{{ ft}} = 0 }}$      
        ${{\hspace{{4mm}} F_{{DC}} \\cdot {(d[0]*d[3])/(Calculations.magnitude(d[0],d[3])):.2f} \\text{{ ft}} = {- (f[3]*d[3]+f[2]*2*d[3]):.2f} \\text{{ lb}} \\cdot \\text{{ ft}} }}$      
        ${{\hspace{{4mm}} F_{{DC}} = {-(f[3]*d[3]+f[2]*2*d[3])/((d[0]*d[3])/(Calculations.magnitude(d[0],d[3]))):.2f} \\text{{ lb}}  }}$       
        
        $\\underline{{Despeje \\hspace{{2mm}} de \\hspace{{2mm}} F_{{HC}}:}}$     
        Teniendo en cuenta que F_{{DC}} está en compresión :
        
        ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{HC}} - F_{{DC}} \\cdot \\dfrac{{d_1}}{{sqrt{{(d_1)^{{2}} + (d_2)^{{2}}}}}} = F_{{HC}} - {f[3] + 2*f[2]:.2f} \\text{{ lb}} = 0 }}$     
        ${{\hspace{{4mm}} F_{{HC}} = {f[3] + 2*f[2]:.2f} \\text{{ lb}} }}$     
        
        $\\textbf{{\\small 3. Nodo D: }}$ 
        
        Para encontrar la fuerza $F_{{DH}}$, se puede evaluar el nodo D:
        
        ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{DH}} - F_2 + F_{{DC}} \\cdot \\dfrac{{d_2}}{{sqrt{{(d_1)^{{2}} + (d_2)^{{2}}}}}} = F_{{DH}} - {f[1]:.2f} \\tex{{ lb}} + {(f[3]+f[2]*2)*(d[3]/d[0])} \\tex{{ lb}} = 0 }}$      
        ${{\hspace{{4mm}} F_{{DH}} =  {f[1] - (f[3]+f[2]*2)*(d[3]/d[0]):.2f} \\tex{{ lb}} }}$     
                        
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
        pregunta = lambda f, a, calc, c, d, m: f"Si la fuerza máxima que cualquier elemento puede soportar es de ${f[0] + 35:0f} \\text{{ N}}$ en tensión y de ${f[0]:0f}\\text{{ N}}$ en compresión, calcule cual es la fuerza $F_1$ máxima que puede ser soportada en el nudo E. Considere $d_1 = {d[0]:.0f} \\text{{ m}}$ .",
        no_answers = 1,
        a1_name = "F_1 [N]",
        a2_name = "",
        a3_name = "",
        answer1 = lambda f, a, calc, c, d, m: np.round(((f[0] + 35)*(3*(d[0]/2)))/(Calculations.magnitude((d[0]/2), (3/2)*d[0])),2),
        answer2 = lambda f, a, calc, c, d, m: 0,
        answer3 = lambda f, a, calc, c, d, m: 0,
        ayuda1 = "Uno de los metodos para analizar fuerzas en elementos de cerchas es el Método de los nodos. Este consiste en evaluar el equilibrio en cada nodo.",
        ayuda2 = "Para analizar mejor un nodo es importante dibujar un diagrama de cuerpo libre claro y detallado con cada fuerza involucrada",      
        ayuda3 = "Un miembro en compresión empuja o genera una fuerza sobre el nodo (la fuerza entra al nodo); un miembro a tensión jala o genera una fuerza hacia afuera del nodo (la fuerza sale del nodo)",
        respuesta_P1 = lambda f, a, calc, c, d, m: f"""
        Una cercha es una estructura compuesta por elementos rectos que se conectan entre si por puntos llamados nodos, formando triángulos. El metodo de nodos es una técnica para determinar fuerzas internas utilizando el principio de que cada nodo está en equilibrio bajo las fuerzas que actúan sobre él. A continuación, se presenta la solución sugerida para el ejercicio: 
        
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
        
        En el nodo E se puede obtener las siguientes ecuaciones:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{EC}} \\cdot \\dfrac{{{d[0]/2:.2f}}}{{{Calculations.magnitude((d[0]/2), (3/2)*d[0]):.2f}}} - \\dfrac{{1}}{{3}} \\cdot F_1 =  0 }}$     
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = F_1 + F_{{ED}} - F_{{EC}} \\cdot \\dfrac{{{(3/2)*d[0]:.2f}}}{{{Calculations.magnitude((d[0]/2), (3/2)*d[0]):.2f}}} = 0 }}$     
        
        De lo cual, se usa la ecuación 2. para determinar $F_{{EC}}$:
        ${{\hspace{{4mm}} F_{{EC}} \\cdot \\dfrac{{{d[0]/2:.2f}}}{{{Calculations.magnitude((d[0]/2), (3/2)*d[0]):.2f}}} = \\dfrac{{1}}{{3}} \\cdot F_1 }}$     
        ${{\hspace{{4mm}} F_{{EC}} = F_1 \\cdot {(Calculations.magnitude((d[0]/2), (3/2)*d[0]))/(3*(d[0]/2)):.2f}}}$     
        
        Se obtiene $F_{{ED}}$ de la ecuación 1.:
        
        ${{\hspace{{4mm}} F_{{ED}} = F_{{EC}} \\cdot \\dfrac{{{(3/2)*d[0]:.2f}}}{{{Calculations.magnitude((d[0]/2), (3/2)*d[0]):.2f}}} - F_1 }}$     
        ${{\hspace{{4mm}} F_{{ED}} = 0 }}$     
        
        $\\textbf{{\\small 3. Nodo A: }}$     
        
        Del nodo A se puede obtener las siguientes ecuaciones:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = \\dfrac{{1}}{{3}} \\cdot F_1 - F_{{AD}} \\cdot {Calculations.cosine(45):.2f} - F_{{AB}} \\cdot {Calculations.cosine(45):.2f} = 0 }}$     
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = F_{{AB}} \\cdot {Calculations.sine(45):.2f} - F_{{AD}} \\cdot {Calculations.sine(45):.2f} = 0 }}$     
        
        De lo cual, se define de la ecuación 2:
        ${{\hspace{{4mm}} F_{{AD}} = F_{{AB}} }}$     
        
        Se obtiene $F_{{AB}}$ y $F_{{AD}}$ de la ecuación 1.:
        
        ${{\hspace{{4mm}} F_{{AD}} = F_{{AB}} = F_1 \\cdot {1/(6*Calculations.cosine(45)):.2f} }}$         
        
        $\\textbf{{\\small 4. Nodo D: }}$     
        
        Del nodo D se puede obtener las siguientes ecuaciones:
        
        ${{\hspace{{4mm}} 1. \\sum{{F_x}} = F_{{DA}} \\cdot {Calculations.cosine(45):.2f} - F_{{DC}} \\cdot {Calculations.cosine(45):.2f} = 0 }}$     
        ${{\hspace{{4mm}} 2. \\sum{{F_y}} = F_{{DA}} \\cdot {Calculations.cosine(45):.2f} + F_{{DC}} \\cdot {Calculations.cosine(45):.2f} - F_{{DB}} = 0 }}$     
        
        De lo cual, se define de la ecuación 2:
        ${{\hspace{{4mm}} F_{{DC}} = F_{{DA}} = F_1 \\cdot {1/(6*Calculations.cosine(45)):.2f} }}$     
        
        Se obtiene $F_{{DB}}$ de la ecuación 1.:
        
        ${{\hspace{{4mm}} F_{{DB}} = 2 \\cdot F_{{DA}} \\cdot {Calculations.cosine(45):.2f} }}$       
        ${{\hspace{{4mm}} F_{{DB}} = F_1  \\cdot {(1/3):.2f} }}$     
        
        Por otro lado, se puede dar cuenta uno que $F_{{DC}} = F_{{BC}}$ .
        
        $\\textbf{{\\small 5. Evaluación de la condición de resistencia máxima: }}$     
        
        $\\underline{{Elementos \\hspace{{2mm}} de \\hspace{{2mm}} Tensión:}}$      
        
        Los elementos de tensión encontrados fueron el EC y el DB, tal que, estas fuerzas deben ser menor o igual a ${f[0] + 35:0f} \\text{{ N}}$. Dado que, el elemento EC tiene que resistir más fuerza que DB, se va a evaluar en este:
        
        ${{\hspace{{4mm}} F_{{EC}} = F_1 \\cdot {(Calculations.magnitude((d[0]/2), (3/2)*d[0]))/(3*(d[0]/2)):.2f} = {f[0] + 35:0f} \\text{{ N}} }}$     
        ${{\hspace{{4mm}} F_1 = {((f[0] + 35)*(3*(d[0]/2)))/(Calculations.magnitude((d[0]/2), (3/2)*d[0])):2f} \\text{{ N}}}}$     
        
        $\\underline{{Elementos \\hspace{{2mm}} de \\hspace{{2mm}} Compresión:}}$    
        
        Los elementos de compresión encontrados fueron el AD, el AB, el DC y el BC, tal que, estas fuerzas deben ser menor o igual a ${f[0]:0f} \\text{{ N}}$. Dado que, todos estos elementos tienen fuerza interna de igual magnitud, se puede evaluar de la siguiente manera:
        
        ${{\hspace{{4mm}} F_{{AD}} = F_{{AB}} = F_{{DC}} = F_{{BC}} = F_1 \\cdot {1/(6*Calculations.cosine(45)):.2f} = {f[0]:0f} \\text{{ N}} }}$     
        ${{\hspace{{4mm}} F_1 = {(f[0])*(6*Calculations.sine(45)):2f} \\text{{ N}}}}$     
        
        Finalmente, se selecciona la respuesta menor, siendo que, si seleccionará la mayor, el otro elemento no resistiría y la estructura fallaría.
            
        """,   
        respuesta_P2 = lambda f, a, calc, c, d, m: f"",
        respuesta_P3 = lambda f, a, calc, c, d, m: f"",
        calculos='operations'
        ),

    #-------------------------------------------------         Marcos      --------------------------------------------
    #-------------------------------------------------       Nivel Fácil   ---------------------------------------------------
    #-------------------------------------------------       Code: 5210011    --------------------------------------------------

    # Questionary(#1_1
    #     code = 5210011,
    #     no_pregunta = 1,
    #     complexity = F,
    #     topic = "Armaduras",
    #     subtopic = "Marcos",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine la fuerza sobre el elemento BD y las componentes de la reacción en C (Utilice el signo para indicar dirección). Considere $F_1 = {f[0]:.0f} \\text{{ N}}$,  $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
    #     no_answers = 3,
    #     a1_name = "Reacción $C_x$ [N]",
    #     a2_name = "Reacción $C_y$ [N]",
    #     a3_name = "Fuerza BD [N]",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(-(f[0]*(d[3] + d[6])*d[3])/(d[0]*d[6]),2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round(-(f[0]*(d[3] + d[6]))/(d[6]),2),
    #     answer3 = lambda f, a, calc, c, d, m: np.round((f[0]*(d[3] + d[6])*(Calculations.magnitude(d[0],d[3])))/(d[0]*d[6]), 2),
    #     ayuda1 = "Para visualizar mejor el ejercicio, puede ayudar desensamblar o despiezar los elementos del marco y dibujar un diagrama de cuerpo libre para cada uno.",
    #     ayuda2 = "Cada elemento debe cumplir las condiciones de equilibrio, es decir, la sumatoria de fuerzas en cualquier dirección debe ser cero y que los momentos respecto a cualquier punto debe ser cero.",      
    #     ayuda3 = "",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     Los armazones son estructuras estacionarias en las cuales, al menos un elemento esta sometido a la acción de varias fuerzas. A continuación, se presenta la solución sugerida para el ejercicio:
        
    #     Se puede intuir, desde un inicio que las fuerzas que solicita el ejercicio se pueden encontrar analizando el elemento ABC (recordando que la fuerza del elemento BD esta dirigida a lo largo de BD): 
        
    #     $\\textbf{{\\small 1. Condición de equilibrio - Momento en C: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = F_1 \\cdot (d_2 + d_3) - F_{{BD}} \\cdot \\dfrac{{d_1}}{{sqrt{{(d_1)^{{2}} + (d_2)^{{2}}}}}} \\cdot d_3 = 0  }}$      
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = {f[0]:.0f} \\text{{ N}} \\cdot {d[3] + d[6]:.0f} \\text{{ m}} - F_{{BD}} \\cdot {(d[0]*d[6])/(Calculations.magnitude(d[0],d[3])) :.2f} \\text{{ m}} = 0 }}$     
    #     ${{\hspace{{4mm}} F_{{BD}} \\cdot {(d[0]*d[6])/(Calculations.magnitude(d[0],d[3])) :.2f} \\text{{ m}} = {f[0]*(d[3] + d[6]):.0f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
    #     ${{\hspace{{4mm}} F_{{BD}} = {(f[0]*(d[3] + d[6])*(Calculations.magnitude(d[0],d[3])))/(d[0]*d[6]):.2f} \\text{{ N}} }}$      
        
    #     $\\textbf{{\\small 2. Condición de equilibrio - Sumatoria de fuerzas en X: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{BD}} \\cdot \\dfrac{{d_2}}{{sqrt{{(d_1)^{{2}} + (d_2)^{{2}}}}}} + C_x = 0  }}$      
    #     ${{\hspace{{4mm}} \\sum{{F_x}} = {(f[0]*(d[3] + d[6])*(Calculations.magnitude(d[0],d[3])))/(d[0]*d[6]):.2f} \\cdot {(d[3])/(Calculations.magnitude(d[0],d[3])):.2f} \\text{{ N}} + C_x = 0 }}$     
    #     ${{\hspace{{4mm}} C_x = {-(f[0]*(d[3] + d[6])*d[3])/(d[0]*d[6]):.2f} \\text{{ N}} }}$      
        
    #     $\\textbf{{\\small 3. Condición de equilibrio - Sumatoria de fuerzas en Y: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{BD}} \\cdot \\dfrac{{d_1}}{{sqrt{{(d_1)^{{2}} + (d_2)^{{2}}}}}} + C_y - F_1 = 0  }}$      
    #     ${{\hspace{{4mm}} \\sum{{F_y}} = {(f[0]*(d[3] + d[6])*(Calculations.magnitude(d[0],d[3])))/(d[0]*d[6]):.2f} \\cdot {(d[0])/(Calculations.magnitude(d[0],d[3])):.2f} \\text{{ N}} + C_y - {f[0]:.0f} \\text{{ N}}= 0 }}$     
    #     ${{\hspace{{4mm}} C_y = {-(f[0]*(d[3] + d[6]))/(d[6]) + f[0]:.2f} \\text{{ N}} }}$       
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    # Questionary(#1_2
    #     code = 5210012,
    #     no_pregunta = 1,
    #     complexity = F,
    #     topic = "Armaduras",
    #     subtopic = "Marcos",
    #     version = 2,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine la componente vertical en A y ambas componentes de la reacción en C (Utilice el signo para indicar dirección). Considere $F_1 = {f[0]:.0f} \\text{{ N}}$,  $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$, $d_3 = {d[6]:.0f} \\text{{ m}}$ y $d_4 = {d[0]*(3/5):.2f} \\text{{ m}}$ .",
    #     no_answers = 3,
    #     a1_name = "Reacción $B_x$ [N]",
    #     a2_name = "Reacción $B_y$ [N]",
    #     a3_name = "Reacción $A_y$ [N]",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(-f[0]*(2/5)*(d[0]/(d[6]+d[3])),2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round(f[0]*(3/5) + d[3]*f[0]*(2/(5*(d[6]+d[3]))),2),
    #     answer3 = lambda f, a, calc, c, d, m: np.round(f[0]*(2/5) + d[3]*f[0]*(2/(5*(d[6]+d[3]))), 2),
    #     ayuda1 = "Para visualizar mejor el ejercicio, puede ayudar desensamblar o despiezar los elementos del marco y dibujar un diagrama de cuerpo libre para cada uno.",
    #     ayuda2 = "Cada elemento debe cumplir las condiciones de equilibrio, es decir, la sumatoria de fuerzas en cualquier dirección debe ser cero y que los momentos respecto a cualquier punto debe ser cero.",      
    #     ayuda3 = "",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     Los armazones son estructuras estacionarias en las cuales, al menos un elemento esta sometido a la acción de varias fuerzas. A continuación, se presenta la solución sugerida para el ejercicio: 
        
    #     $\\textbf{{\\small 1. Condición de equilibrio global - Momento en A: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{M_A}} = F_1 \\cdot (d_1 - d_4) + B_x \\cdot (d_3 + d_2) = 0  }}$      
    #     ${{\hspace{{4mm}} B_x \\cdot {d[6] + d[3] :.0f} \\text{{ m}} = {-f[0]*(2/5)*d[0]:.2f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
    #     ${{\hspace{{4mm}} B_x = {-f[0]*(2/5)*(d[0]/(d[6]+d[3])):.2f} \\text{{ N}} }}$      
        
    #     $\\textbf{{\\small 2. Condición de equilibrio elemento BCD - Momento en C: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = B_y \\cdot d_1 - F_1 \\cdot d_4 - B_x \\cdot d_2 = 0  }}$      
    #     ${{\hspace{{4mm}} B_y \\cdot {d[0]:.0f} \\text{{ m}} = {f[0]*(3/5)*d[0]:.2f} \\text{{ N}} \\cdot \\text{{ m}} + {d[3]*f[0]*(2/5)*(d[0]/(d[6]+d[3])):.2f} \\text{{ N}} \\cdot \\text{{ m}}}}$      
    #     ${{\hspace{{4mm}} B_y= {f[0]*(3/5) + d[3]*f[0]*(2/(5*(d[6]+d[3]))):.2f} \\text{{ N}} }}$      
        
    #     $\\textbf{{\\small 3. Condición de equilibrio global - Sumatoria de fuerzas en Y: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{F_y}} = A_y + B_y - F_1 = 0  }}$       
    #     ${{\hspace{{4mm}} A_y = {f[0]*(2/5) + d[3]*f[0]*(2/(5*(d[6]+d[3]))):.2f} \\text{{ N}} }}$      
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    #========================================================  ARMADURAS  =========================================================
    #-------------------------------------------------         Marcos      --------------------------------------------
    #-------------------------------------------------       Nivel Medio   ---------------------------------------------------
    #-------------------------------------------------       Code: 5220011    --------------------------------------------------

    # Questionary(#1_1
    #     code = 5220011,
    #     no_pregunta = 1,
    #     complexity = M,
    #     topic = "Armaduras",
    #     subtopic = "Marcos",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine las componentes de la reacción en D y la componente vertical de la reacción en E (Utilice el signo para indicar dirección). Considere $F_1 = {f[0]:.0f} \\text{{ N}}$, $M_1 = {m[0]:.0f} \\text{{  N}} \\cdot \\text {{ m}}$,  $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
    #     no_answers = 3,
    #     a1_name = "Reacción $D_x$ [N]",
    #     a2_name = "Reacción $D_y$ [N]",
    #     a3_name = "Reacción $E_y$ [N]",
    #     answer1 = lambda f, a, calc, c, d, m: np.round((m[0] - ((m[0] - f[0]*d[3])/(d[6] + d[3]))*d[3])/d[0],2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round((m[0] - f[0]*d[3])/(d[6] + d[3]),2),
    #     answer3 = lambda f, a, calc, c, d, m: np.round(f[0] - (m[0] - f[0]*d[3])/(d[6] + d[3]), 2),
    #     ayuda1 = "Para encontrar reacciones, es util verficar el equilibrio global de la estructura.",
    #     ayuda2 = "Para visualizar mejor el ejercicio, puede ayudar desensamblar o despiezar los elementos del marco y dibujar un diagrama de cuerpo libre para cada uno.",      
    #     ayuda3 = "Cada elemento debe cumplir las condiciones de equilibrio, es decir, la sumatoria de fuerzas en cualquier dirección debe ser cero y que los momentos respecto a cualquier punto debe ser cero.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     Los armazones son estructuras estacionarias en las cuales, al menos un elemento esta sometido a la acción de varias fuerzas. A continuación, se presenta la solución sugerida para el ejercicio: 
        
    #     $\\textbf{{\\small 1. Condición de equilibrio global - Momento en E: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{M_E}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{M_E}} = F_1 \\cdot d_2 - D_y \\cdot (d_3 + d_2) - M_1 = 0  }}$      
    #     ${{\hspace{{4mm}} \\sum{{M_E}} = {f[0]:.0f} \\text{{ N}} \\cdot {d[3]:.0f} \\text{{ m}} - D_y \\cdot {d[6] + d[3] :.0f} \\text{{ m}} - {m[0]:.0f} \\text{{  N}} \\cdot \\text {{ m}} = 0 }}$     
    #     ${{\hspace{{4mm}} D_y \\cdot {d[6] + d[3] :.0f} \\text{{ m}} = {m[0] - f[0]*d[3]:.0f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
    #     ${{\hspace{{4mm}} D_y = {(m[0] - f[0]*d[3])/(d[6] + d[3]):.2f} \\text{{ N}} }}$      
        
    #     $\\textbf{{\\small 2. Condición de equilibrio global- Sumatoria de fuerzas en Y: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{F_y}} = {(m[0] - f[0]*d[3])/(d[6] + d[3]):.2f} \\text{{ N}} - {f[0]:.0f} \\text{{ N}} + E_y = 0  }}$       
    #     ${{\hspace{{4mm}} E_y = {f[0] - (m[0] - f[0]*d[3])/(d[6] + d[3]):.2f} \\text{{ N}} }}$      
        
    #     $\\textbf{{\\small 3. Condición de equilibrio Elemento ACD - Momento en C: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = {(m[0] - f[0]*d[3])/(d[6] + d[3]):.2f} \\text{{ N}} \\cdot {d[3]:.0f} \\text{{ m}} - {m[0]:.0f} \\text{{  N}} \\cdot \\text {{ m}} + D_x \\cdot {d[0]:.0f} \\text{{ m}} = 0  }}$      
    #     ${{\hspace{{4mm}} D_x \\cdot {d[0]:.0f} \\text{{ m}} = {m[0] - ((m[0] - f[0]*d[3])/(d[6] + d[3]))*d[3]:.2f} \\text{{ N}} \\cdot \\text {{ m}}}}$      
    #     ${{\hspace{{4mm}} D_x  = {(m[0] - ((m[0] - f[0]*d[3])/(d[6] + d[3]))*d[3])/d[0]:.2f} \\text{{ N}} }}$      
        
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    # Questionary(#2_1
    #     code = 5220021,
    #     no_pregunta = 2,
    #     complexity = M,
    #     topic = "Armaduras",
    #     subtopic = "Marcos",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine las componentes de las fuerzas ejercidas sobre el elemento ACEG en C. Considere $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$, $F_3 = {f[2]:.0f} \\text{{ N}}$  $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$ y $d_3 = {d[6]:.0f} \\text{{ m}}$.",
    #     no_answers = 2,
    #     a1_name = "Fuerza $C_x$ [N]",
    #     a2_name = "Fuerza $C_y$ [N]",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(-(f[2]*d[3]- d[0]*(f[0]+f[1]))/d[6],2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round(((f[2]*d[3] - d[0]*(f[0]+f[1])) + 2*f[0]*d[0] - f[2]*d[3])/d[0],2),
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "Para encontrar reacciones, es util verficar el equilibrio global de la estructura.",
    #     ayuda2 = "Para visualizar mejor el ejercicio, puede ayudar desensamblar o despiezar los elementos del marco y dibujar un diagrama de cuerpo libre para cada uno.",      
    #     ayuda3 = "Cada elemento debe cumplir las condiciones de equilibrio, es decir, la sumatoria de fuerzas en cualquier dirección debe ser cero y que los momentos respecto a cualquier punto debe ser cero.",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     Los armazones son estructuras estacionarias en las cuales, al menos un elemento esta sometido a la acción de varias fuerzas. A continuación, se presenta la solución sugerida para el ejercicio: 
        
    #     $\\textbf{{\\small 1. Condición de equilibrio global - Momento en D: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{M_D}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{M_D}} = F_1 \\cdot 2d_1 + F_2 \\cdot 2d_1 - 2F_3 \\cdot d_2 + E_x \\cdot 2d_3 = 0  }}$      
    #     ${{\hspace{{4mm}} \\sum{{M_D}} = {f[0]:.0f} \\text{{ N}} \\cdot {2*d[0]:.0f} \\text{{ m}} + {f[1]:.0f} \\cdot {2*d[0]:.0f} \\text{{ m}} - {2*f[2]:.0f} \\text{{  N}} \\cdot {d[3]:.0f} \\text {{ m}} + E_x \\cdot {2*d[6]:.0f} \\text{{ m}} = 0 }}$     
    #     ${{\hspace{{4mm}} E_x \\cdot {2*d[6]:.0f} \\text{{ m}} = {2*(f[2]*d[3]- d[0]*(f[0]+f[1])):.0f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
    #     ${{\hspace{{4mm}} E_x = {(f[2]*d[3] - d[0]*(f[0]+f[1]))/d[6]:.2f} \\text{{ N}} }}$      
        
    #     $\\textbf{{\\small 2. Condición de equilibrio Elemento ACEG- Sumatoria de fuerzas en X: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{F_x}} = {(f[2]*d[3]- d[0]*(f[0]+f[1]))/d[6]:.2f} \\text{{ N}} + C_x = 0  }}$       
    #     ${{\hspace{{4mm}} C_x = {-(f[2]*d[3]- d[0]*(f[0]+f[1]))/d[6]:.2f} \\text{{ N}} }}$      
        
    #     $\\textbf{{\\small 3. Condición de equilibrio Elemento ACEG - Momento en E: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{M_E}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{M_E}} = {(f[2]*d[3]- d[0]*(f[0]+f[1]))/d[6]:.2f} \\text{{ N}} \\cdot {d[6]:.0f} \\text{{ m}} + {f[0]:.0f} \\text{{ N}} \\cdot {2*d[0]:.0f} \\text{{ m}} - {f[2]:.0f} \\text{{  N}} \\cdot {d[3]:.0f} \\text {{ m}} - C_y \\cdot {d[0]:.0f} \\text{{ m}} = 0  }}$      
    #     ${{\hspace{{4mm}} C_y \\cdot {d[0]:.0f} \\text{{ m}} = {(f[2]*d[3]- d[0]*(f[0]+f[1])) + 2*f[0]*d[0] - f[2]*d[3]:.2f} \\text{{ N}} \\cdot \\text {{ m}}}}$      
    #     ${{\hspace{{4mm}} C_y  = {((f[2]*d[3] - d[0]*(f[0]+f[1])) + 2*f[0]*d[0] - f[2]*d[3])/d[0]:.2f} \\text{{ N}} }}$      
        
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    #========================================================  ARMADURAS  =========================================================
    #-------------------------------------------------         Marcos      --------------------------------------------
    #-------------------------------------------------       Nivel Difícil   ---------------------------------------------------
    #-------------------------------------------------       Code: 5220011    --------------------------------------------------

    # Questionary(#1_1
    #     code = 5230011,
    #     no_pregunta = 1,
    #     complexity = D,
    #     topic = "Armaduras",
    #     subtopic = "Marcos",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine las componentes de la fuerza ejercida sobre el segmento AB en B (Utilice el signo para indicar dirección). Considere $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$, $d_1 = {d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[3]:.0f}  \\text{{ m}}$, $d_3 = {d[6]:.0f} \\text{{ m}}$ y $d_4 = {d[9]:.0f} \\text{{ m}}$.",
    #     no_answers = 2,
    #     a1_name = "Fuerza $B_x$ [N]",
    #     a2_name = "Fuerza $B_y$ [N]",
    #     a3_name = "",
    #     answer1 = lambda f, a, calc, c, d, m: np.round((-((f[1]*d[3])/d[6]) - (f[0]/2))/(((2*d[3])/d[6]) + ((2*d[3] + d[0])/(d[9]*2))),2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round(((-((f[1]*d[3])/d[6]) - (f[0]/2))/(((2*d[3])/d[6]) + ((2*d[3] + d[0])/(d[9]*2))))*((2*d[3])/d[6]) + (f[1]*d[3])/d[6],2),
    #     answer3 = lambda f, a, calc, c, d, m: 0,
    #     ayuda1 = "Para visualizar mejor el ejercicio, puede ayudar desensamblar o despiezar los elementos del marco y dibujar un diagrama de cuerpo libre para cada uno.",
    #     ayuda2 = "Cada elemento debe cumplir las condiciones de equilibrio, es decir, la sumatoria de fuerzas en cualquier dirección debe ser cero y que los momentos respecto a cualquier punto debe ser cero.",      
    #     ayuda3 = "",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     Los armazones son estructuras estacionarias en las cuales, al menos un elemento esta sometido a la acción de varias fuerzas. A continuación, se presenta la solución sugerida para el ejercicio: 
        
    #     En este ejercicio, es valido aclarar que es necesario revisar ambos segmentos del Marco para dar con un sistema de ecuaciones que logre resolver el ejercicio. Asumiendo $B_y$ y $B_x$ positivos en AB y negativos en CB:
        
    #     $\\textbf{{\\small 1. Condición de equilibrio Elemento AB - Momento en A: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{M_A}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{M_A}} = B_y \\cdot d_3 - B_x \\cdot 2d_2 - F_2 \\cdot d_2 = 0  }}$      
    #     ${{\hspace{{4mm}} \\sum{{M_A}} = B_y \\cdot {d[6]:.0f} \\text{{ m}} - B_x \\cdot {2*d[3] :.0f} \\text{{ m}} - {f[1]:.0f} \\text{{  N}} \\cdot {d[3] :.0f} \\text {{ m}} = 0 }}$     
    #     ${{\hspace{{4mm}} B_y \\cdot {d[6]:.0f} \\text{{ m}} = B_x \\cdot {2*d[3] :.0f} \\text{{ m}} + {f[1]*d[3]:.0f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
    #     ${{\hspace{{4mm}} B_y = B_x \\cdot {(2*d[3])/d[6] :.2f} + {(f[1]*d[3])/d[6]:.2f} \\text{{ N}} }}$      
        
    #     $\\textbf{{\\small 2. Condición de equilibrio Elemento CB - Momento en C: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = B_y \\cdot 2d_4 + B_x \\cdot (2d_2 + d_1) + F_1 \\cdot d_4 = 0  }}$      
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = B_y \\cdot {2*d[9]:.0f} \\text{{ m}} + B_x \\cdot {2*d[3] + d[0]:.0f} \\text{{ m}} + {f[0]:.0f} \\text{{  N}} \\cdot {d[9]:.0f} \\text {{ m}} = 0 }}$     
    #     ${{\hspace{{4mm}} B_y \\cdot {2*d[9]:.0f} \\text{{ m}} = - B_x \\cdot {2*d[3] + d[0]:.0f} \\text{{ m}} + {f[0]*d[9]:.0f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
    #     ${{\hspace{{4mm}} B_y = - B_x \\cdot {(2*d[3] + d[0])/(d[9]*2):.2f} - {(f[0]/2):.2f} \\text{{ N}} }}$      
        
    #     $\\textbf{{\\small 3. Despeje de B_y y B_x: }}$
        
    #     Con las anteriores ecuaciones se hallar $B_x$:
        
    #     ${{\hspace{{4mm}} B_x \\cdot {(2*d[3])/d[6] :.2f} + {(f[1]*d[3])/d[6]:.2f} \\text{{ N}} = - B_x \\cdot {(2*d[3] + d[0])/(d[9]*2):.2f} - {(f[0]/2):.2f} \\text{{ N}}  }}$          
    #     ${{\hspace{{4mm}} B_x \\cdot {((2*d[3])/d[6]) + ((2*d[3] + d[0])/(d[9]*2)):.2f} = {-((f[1]*d[3])/d[6]) - (f[0]/2) :.2f} \\text{{ N}} }}$      
    #     ${{\hspace{{4mm}} B_x = {(-((f[1]*d[3])/d[6]) - (f[0]/2))/(((2*d[3])/d[6]) + ((2*d[3] + d[0])/(d[9]*2))):.2f} \\text{{ N}} }}$       
        
    #     Ahora, a partir de $B_x$ se puede encontrar $B_y$:
        
    #     ${{\hspace{{4mm}} B_y = B_x \\cdot {(2*d[3])/d[6] :.2f} + {(f[1]*d[3])/d[6]:.2f} \\text{{ N}} }}$      
    #     ${{\hspace{{4mm}} B_y = {((-((f[1]*d[3])/d[6]) - (f[0]/2))/(((2*d[3])/d[6]) + ((2*d[3] + d[0])/(d[9]*2))))*((2*d[3])/d[6]) + (f[1]*d[3])/d[6]:.2f} \\text{{ N}} }}$      
        
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),
    # Questionary(#1_2
    #     code = 5230012,
    #     no_pregunta = 1,
    #     complexity = D,
    #     topic = "Armaduras",
    #     subtopic = "Marcos",
    #     version = 2,
    #     pregunta = lambda f, a, calc, c, d, m: f"Determine la magnitud de la fuerza en el elemento FD y las componentes de la fuerza ejercida sobre el segmento ABC en el pasador C (Utilice el signo para indicar dirección). Considere $F_1 = {f[0]:.0f} \\text{{ N}}$, $d_1 = {2*d[0]:.0f} \\text{{ m}}$,  $d_2 = {d[0]:.0f}  \\text{{ m}}$, $d_3 = {2*d[3]:.0f} \\text{{ m}}$ y $d_4 = {d[3]:.0f} \\text{{ m}}$.",
    #     no_answers = 3,
    #     a1_name = "Fuerza $C_x$ [N]",
    #     a2_name = "Fuerza $C_y$ [N]",
    #     a3_name = "Fuerza $F_{{FD}}$ [N]",
    #     answer1 = lambda f, a, calc, c, d, m: np.round((3*f[0]*(d[0]/d[3])),2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round(2*f[0],2),
    #     answer3 = lambda f, a, calc, c, d, m: np.round((f[0]*3)/((2*d[3]/Calculations.magnitude(d[0], (2*d[3])))),2),
    #     ayuda1 = "Para visualizar mejor el ejercicio, puede ayudar desensamblar o despiezar los elementos del marco y dibujar un diagrama de cuerpo libre para cada uno.",
    #     ayuda2 = "Cada elemento debe cumplir las condiciones de equilibrio, es decir, la sumatoria de fuerzas en cualquier dirección debe ser cero y que los momentos respecto a cualquier punto debe ser cero.",      
    #     ayuda3 = "",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     Los armazones son estructuras estacionarias en las cuales, al menos un elemento esta sometido a la acción de varias fuerzas. A continuación, se presenta la solución sugerida para el ejercicio: 
              
    #     $\\textbf{{\\small 1. Condición de equilibrio global: }}$
        
    #     $\\underline{{Momento \\hspace{{2mm}} en \\hspace{{2mm}} C:}}$     
        
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = F_1 \\cdot (d_1 + d_2) - R_{{Ay}} \\cdot (d_1 + d_2) = 0  }}$      
    #     ${{\hspace{{4mm}} R_{{Ay}} = F_1 = {f[0]:.0f} \\text{{ N}} }}$      
        
    #     $\\underline{{Sumatoria \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} Y:}}$     
        
    #     ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{F_y}} = R_{{Ay}} + R_{{Cy}} - F_1 = 0  }}$      
    #     ${{\hspace{{4mm}} R_{{Cy}} = 0 }}$
        
    #     Ahora bien, el hecho de que $R_{{Cy}}$ sea cero, no implica que en el pasador C que conecta los elementos ABC y CDE no haya reacciones. Con eso en cuenta, podemos encontrar esas fuerzas:
        
    #     $\\textbf{{\\small 2. Condición de equilibrio Elemento ABC: }}$
        
    #     $\\underline{{Momento \\hspace{{2mm}} en \\hspace{{2mm}} C:}}$     
        
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = F_{{BD}} \\cdot \\dfrac{{d_4}}{{sqrt{{(d_2)^{{2}} + (d_4)^{{2}}}}}} \\cdot d_2 - R_{{Ay}} \\cdot (d_1 + d_2) = 0  }}$      
    #     ${{\hspace{{4mm}} \\sum{{M_C}} = F_{{BD}} \\cdot {d[0]*(d[3]/Calculations.magnitude(d[0],d[3])):.2f} \\text{{ m}} - {f[0]:.0f} \\text{{ N}} \\cdot {3*d[0]:.0f} \\text{{ m}} = 0 }}$     
    #     ${{\hspace{{4mm}} F_{{BD}} \\cdot {d[0]*(d[3]/Calculations.magnitude(d[0],d[3])):.2f} \\text{{ m}} = {f[0]*3*d[0]:.2f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
    #     ${{\hspace{{4mm}} F_{{BD}} = {(f[0]*3)/((d[3]/Calculations.magnitude(d[0],d[3]))):.2f} \\text{{ N}} }}$      
        
    #     $\\underline{{Sumatoria \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} Y:}}$     
        
    #     ${{\hspace{{4mm}} \\sum{{F_y}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{F_y}} = R_{{Ay}} - F_{{BD}} \\cdot \\dfrac{{d_4}}{{sqrt{{(d_2)^{{2}} + (d_4)^{{2}}}}}} + C_y = 0  }}$      
    #     ${{\hspace{{4mm}} C_y = F_{{BD}} \\cdot \\dfrac{{d_4}}{{sqrt{{(d_2)^{{2}} + (d_4)^{{2}}}}}} - R_{{Ay}}}}$      
    #     ${{\hspace{{4mm}} C_y = {(f[0]*3)/((d[3]/Calculations.magnitude(d[0],d[3]))):.2f} \\cdot {(d[3]/Calculations.magnitude(d[0],d[3])):.2f} \\text{{ N}}  - {f[0]:.0f} \\text{{ N}}}}$      
    #     ${{\hspace{{4mm}} C_y = {2*f[0]:.2f} \\text{{ N}}}}$      

    #     $\\underline{{Sumatoria \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} X:}}$     
        
    #     ${{\hspace{{4mm}} \\sum{{F_x}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{F_x}} = C_x - F_{{BD}} \\cdot \\dfrac{{d_2}}{{sqrt{{(d_2)^{{2}} + (d_4)^{{2}}}}}} = 0  }}$      
    #     ${{\hspace{{4mm}} C_x = F_{{BD}} \\cdot \\dfrac{{d_4}}{{sqrt{{(d_2)^{{2}} + (d_4)^{{2}}}}}} }}$      
    #     ${{\hspace{{4mm}} C_x = {(f[0]*3)/((d[3]/Calculations.magnitude(d[0],d[3]))):.2f} \\cdot {(d[0]/Calculations.magnitude(d[0],d[3])):.2f} \\text{{ N}}}}$      
    #     ${{\hspace{{4mm}} C_x = {3*f[0]*(d[0]/d[3]):.2f} \\text{{ N}}}}$           
        
    #     $\\textbf{{\\small 3. Condición de equilibrio Elemento EFG - Momento en E: }}$     
        
    #     ${{\hspace{{4mm}} \\sum{{M_G}} = 0 }}$          
    #     ${{\hspace{{4mm}} \\sum{{M_G}} = F_1 \\cdot (d_1 + d_2) - F_{{FD}} \\cdot \\dfrac{{d_3}}{{sqrt{{(d_3)^{{2}} + (d_4)^{{2}}}}}} \\cdot d_2 = 0  }}$      
    #     ${{\hspace{{4mm}} \\sum{{M_G}} = {f[0]:.0f} \\text{{ N}} \\cdot {3*d[0]:.0f} \\text{{ m}} - F_{{FD}} \\cdot {d[0]*((2*d[3])/Calculations.magnitude(d[0], (2*d[3]))):.2f} \\text{{ m}} = 0 }}$     
    #     ${{\hspace{{4mm}} F_{{FD}} \\cdot {d[0]*((2*d[3])/Calculations.magnitude(d[0], (2*d[3]))):.2f} \\text{{ m}} = {f[0]*3*d[0]:.2f} \\text{{ N}} \\cdot \\text{{ m}} }}$      
    #     ${{\hspace{{4mm}} F_{{FD}} = {(f[0]*3)/((2*d[3]/Calculations.magnitude(d[0], (2*d[3])))):.2f} \\text{{ N}} }}$      
        
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),

    #========================================================  SISTEMAS EQUIVALENTES  =========================================================
    #-------------------------------------------------       Sistemas equivalentes 2D-3D      --------------------------------------------
    #-------------------------------------------------       Nivel Medio   ---------------------------------------------------
    #-------------------------------------------------       Code: 4120011    --------------------------------------------------
    # Questionary(#1_1
    #     code = 4120011,
    #     no_pregunta = 1,
    #     complexity = M,
    #     topic = "Sistemas equivalentes",
    #     subtopic = "Sistemas equivalentes",
    #     version = 1,
    #     pregunta = lambda f, a, calc, c, d, m: f"Reemplace el sistema de fuerzas que actua sobre el poste por una sola fuerza resultante ubicada en el tramo AB. Determine las componentes de la fuerza (Use el signo para la dirección) y donde actua esta fuerza, medido desde el extremo B. Considere $F_1 = {f[0]:.0f} \\text{{ N}}$, $F_2 = {f[1]:.0f} \\text{{ N}}$, $F_3 = {f[2]:.0f} \\text{{ N}}$, $\\alpha_1 = {a[0]:.0f}°$, $d_1 = {d[0]/10:.2f} \\text{{ m}}$,  $d_2 = {(2*d[0])/10:.0f}  \\text{{ m}}$, $d_3 = {d[6]:.0f} \\text{{ m}}$, $d_4 = {d[9]:.0f}  \\text{{ m}}$ y $d_5 = {d[12]:.0f} \\text{{ m}}$.",
    #     no_answers = 3,
    #     a1_name = "Componente $F_{{Rx}}$ [N]",
    #     a2_name = "Componente $F_{{Ry}}$ [N]",
    #     a3_name = "Distancia desde el extremo B [m]",
    #     answer1 = lambda f, a, calc, c, d, m: np.round(f[0]*calc['cos1'] - f[1]*(4/5) - f[2],2),
    #     answer2 = lambda f, a, calc, c, d, m: np.round(f[1]*(3/5) - f[0]*calc['sin1'],2),
    #     answer3 = lambda f, a, calc, c, d, m: np.round((f[0]*calc['sin1']*(2*(d[0]/10)) + f[1]*(4/5)*d[12] + f[1]*(3/5)*(d[0]/20) + f[2]*(d[12] + d[9]))/(-f[0]*calc['cos1'] + f[1]*(4/5) + f[2]), 2),
    #     ayuda1 = "La fuerza resultante será igual a la suma de todas las fuerzas en el sistema, y que el momento de la fuerza resultante es igual a la suma de los momentos originales desde cualquier punto.",
    #     ayuda2 = "Para determinar la ubicación de la fuerza resultante con respecto a un punto de referencia, utilizamos la condición de que el momento producido por la fuerza resultante respecto a ese punto debe ser igual al momento de las fuerzas originales del sistema respecto al mismo punto.",      
    #     ayuda3 = "",
    #     respuesta_P1 = lambda f, a, calc, c, d, m: f"""
    #     En un sistema equivalente se esta buscando reducir un sistema complejo a un sistema de fuerzas y momentos que producen mismo efecto rotacional y traslacional. A continuación, se presenta la solución sugerida para el ejercicio:
        
    #     $\\textbf{{\\small 1. Determinar fuerza resultante: }}$
        
    #     $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} X:}}$  
        
    #     ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{Rx}}}}$          
    #     ${{\hspace{{4mm}} F_{{Rx}} = F_1 \\cdot \\cos(\\alpha_1) - F_2 \\cdot \\dfrac{{4}}{{5}} - F_3 = {f[0]*calc['cos1']:.2f} \\text{{ N}} - {f[1]*(3/5):.2f} \\text{{ N}}  - {f[2]:.0f} \\text{{ N}}}}$          
    #     ${{\hspace{{4mm}} F_{{Rx}} = {f[0]*calc['cos1'] - f[1]*(4/5) - f[2]:.2f} \\text{{ N}} }}$          
        
    #     $\\underline{{Sumatoria \\hspace{{2mm}} de \\hspace{{2mm}} fuerzas \\hspace{{2mm}} en \\hspace{{2mm}} Y:}}$  
        
    #     ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{Ry}}}}$          
    #     ${{\hspace{{4mm}} F_{{Ry}} = F_2 \\cdot \\dfrac{{3}}{{5}} - F_1 \\cdot \\sin(\\alpha_1) = {f[1]*(3/5):.2f}\\text{{ N}} - {f[0]*calc['sin1']:.2f} \\text{{ N}} }}$          
    #     ${{\hspace{{4mm}} F_{{Ry}} = {f[1]*(3/5) - f[0]*calc['sin1']:.2f} \\text{{ N}} }}$          
        
    #     $\\textbf{{\\small 2. Ubicación de fuerza resultante: }}$
        
    #     ${{\hspace{{4mm}} \\sum{{M_B}} = d \\cdot F_{{Rx}}}}$     
    #     ${{\hspace{{4mm}} d \\cdot F_{{Rx}} = - F_1 \\cdot \\sin(\\alpha_1) \\cdot d_2 - F_2 \\cdot \\dfrac{{4}}{{5}} \\cdot d_5 - F_2 \\cdot \\dfrac{{3}}{{5}} \\cdot \\dfrac{{d_1}}{{2}} - F_3 \\cdot (d_5 + d_4)}}$     
    #     ${{\hspace{{4mm}} d \\cdot ({f[0]*calc['cos1'] - f[1]*(4/5) - f[2]:.2f}) \\text{{ N}}  = - {f[0]*calc['sin1']:.2f} \\text{{ N}} \\cdot {(d[0]*2)/10:.2f} \\text{{ m}} - {f[1]*(4/5):.2f} \\text{{ N}} \\cdot {d[12]:.0f} \\text{{ m}} - {f[1]*(3/5):.2f} \\text{{ N}} \\cdot {d[0]/20:.2f} \\text{{ m}} - {f[2]:.0f} \\text{{ N}} \\cdot {d[12] + d[9]:.0f} \\text{{ m}}}}$     
    #     ${{\hspace{{4mm}} d \\cdot ({f[0]*calc['cos1'] - f[1]*(4/5) - f[2]:.2f}) \\text{{ N}}  = - {f[0]*calc['sin1']*(2*(d[0]/10)) + f[1]*(4/5)*d[12] + f[1]*(3/5)*(d[0]/20) + f[2]*(d[12] + d[9]):.2f} \\text{{ N}} \\cdot \\text{{ m}}}}$     
    #     ${{\hspace{{4mm}} d = {(f[0]*calc['sin1']*(2*(d[0]/10)) + f[1]*(4/5)*d[12] + f[1]*(3/5)*(d[0]/20) + f[2]*(d[12] + d[9]))/(-f[0]*calc['cos1'] + f[1]*(4/5) + f[2]):.2f} \\text{{ m}}}}$     
        
    #     """,   
    #     respuesta_P2 = lambda f, a, calc, c, d, m: f"",
    #     respuesta_P3 = lambda f, a, calc, c, d, m: f"",
    #     calculos='operations'
    #     ),


]