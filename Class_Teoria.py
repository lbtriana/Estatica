#class Concepts stores the information of each theory exercises
class Theory:
    def __init__(self, code, no_pregunta, topic, subtopic, enunciado, opcion_1, opcion_2, opcion_3, opcion_4, opcion_correcta, respuesta_P1,respuesta_P2):
        self.code = code ##### Topic, Subtopic, No de la pregunta
        self.no_pregunta = no_pregunta
        self.topic = topic
        self.subtopic = subtopic
        self.enunciado = enunciado
        self.opcion_1 = opcion_1
        self.opcion_2 = opcion_2
        self.opcion_3 = opcion_3
        self.opcion_4 = opcion_4
        self.opcion_correcta = opcion_correcta
        self.respuesta_P1 = respuesta_P1
        self.respuesta_P2 = respuesta_P2

    #Function to filter the theory questions according to the user's selection
    def filtrar_preguntas_teoria(preguntas_teoria, topic=None, subtopic=None):
        preguntas_filtradas_teoria = [
            pregunta for pregunta in preguntas_teoria
            if (topic is None or pregunta.topic == topic) and
               (subtopic is None or pregunta.subtopic == subtopic)
        ]
        return preguntas_filtradas_teoria

conceptuales = [
    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------       Vectores         ---------------------------------------------------
    #-------------------------------------------------          11#           ---------------------------------------------------

    Theory(#1
        code = 1100010, #Tema #Subtema #Nivel de dificultad (0) #No. pregunta (001) #no_version (0)
        no_pregunta = 1,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "Pregunta 1 Prueba",
        opcion_1 = "O1 _ Prueba 1",
        opcion_2 = "O2 _ Prueba 1",
        opcion_3 = "O3 _ Prueba 1",
        opcion_4 = "O4 _ Prueba 1",
        opcion_correcta = "O1 _ Prueba 1",
        respuesta_P1 = "Esta es la respuesta correcta O1_Prueba 1",
        respuesta_P2 = "",
        ),
    
    Theory(#2
        code = 112,
        no_pregunta = 2,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "Pregunta 2 prueba",
        opcion_1 = "O1 _ Prueba 2",
        opcion_2 = "O2 _ Prueba 2",
        opcion_3 = "O3 _ Prueba 2",
        opcion_4 = "O4 _ Prueba 2",
        opcion_correcta = "O3 _ Prueba 2",
        respuesta_P1 = "Esta es la respuesta correcta O3_Prueba 2",
        respuesta_P2 = "",
        ),
     
]