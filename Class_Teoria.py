#class Concepts stores the information of each theory exercises
class Theory:
    def __init__(self, code, no_pregunta, topic, subtopic, enunciado, opcion_1, opcion_2, opcion_3, opcion_4, opcion_correcta, respuesta_P1,respuesta_P2):
        self.code = code #Tema #Subtema #Nivel de dificultad (0) #No. pregunta (001) #no_version (0)
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
        conceptuales_filtradas = [
            pregunta for pregunta in preguntas_teoria
            if (topic is None or pregunta.topic == topic) and
               (subtopic is None or pregunta.subtopic == subtopic)
        ]
        return conceptuales_filtradas

conceptuales = [
    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------       Vectores         ---------------------------------------------------
    #-------------------------------------------------       11000##0         ---------------------------------------------------

    Theory(#1
        code = 1100010, 
        no_pregunta = 1,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "Considere el vector $\\overrightarrow{{P}}$ que se encuentre a $\\alpha [°]$ del eje X. Determine la magnitud y dirección del vector $\\overrightarrow{{Q}}$ para que |$\\overrightarrow{{P}} + \\overrightarrow{{Q}}$| sea mínima:",
        opcion_1 = "$\\overrightarrow{{Q}} = -\\overrightarrow{{P}}$",
        opcion_2 = "$\\overrightarrow{{Q}} = \\overrightarrow{{P}} \\cdot cos(\\alpha)$",
        opcion_3 = "$\\overrightarrow{{Q}} = \\overrightarrow{{P}} \\cdot sin(\\alpha)$",
        opcion_4 = "$\\overrightarrow{{Q}} = \\overrightarrow{{P}}$",
        opcion_correcta = "$\\overrightarrow{{Q}} = -\\overrightarrow{{P}}$",
        respuesta_P1 = """
        Para que la magnitud de la suma sea mínima, los vectores deben tener la misma magnitud y dirección pero sentidos opuestos. De esta manera, su sumatoria es 0:

        |$\\overrightarrow{{P}} + \\overrightarrow{{Q}}$| = $\\overrightarrow{{P}} + \\overrightarrow{{Q}}$ =  $\\overrightarrow{{P}} + \\overrightarrow{{-P}} = 0$
        """,
        respuesta_P2 = "",
        ),
    
    Theory(#2
        code = 1100020, 
        no_pregunta = 2,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "Considere los vectores $\overrightarrow{A}$ y $\overrightarrow{B}$, ¿Cuál es el ángulo ($\\alpha [°]$) entre ellos que minimiza la magnitud de su suma ($\overrightarrow{A} + \overrightarrow{B}$)?.",
        opcion_1 = "$0^\circ$",
        opcion_2 = "$180^\circ$",
        opcion_3 = "$90^\circ$",
        opcion_4 = "$45^\circ$",
        opcion_correcta = "$180^\circ$",
        respuesta_P1 = "Un ángulo de 180° entre dos vectores indica que tienen la misma dirección pero sentidos opuestos, lo cual minimiza la magnitud del vector resultante.",
        respuesta_P2 = "",
        ),

    Theory(#3
        code = 1100030, 
        no_pregunta = 3,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "Considere los vectores $\overrightarrow{A}$ y $\overrightarrow{B}$, ¿Cuál es el ángulo ($\\alpha [°]$) entre ellos que maximiza la magnitud de su suma ($\overrightarrow{A} + \overrightarrow{B}$)?.",
        opcion_1 = "$0^\circ$",
        opcion_2 = "$180^\circ$",
        opcion_3 = "$90^\circ$",
        opcion_4 = "$45^\circ$",
        opcion_correcta = "$0^\circ$",
        respuesta_P1 = "Un ángulo de 0° entre dos vectores indica que tienen la misma dirección y sentido, lo cual maximiza la magnitud del vector resultante.",
        respuesta_P2 = "",
        ),     
    
    Theory(#4
        code = 1100040,
        no_pregunta = 4,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "A partir del vector $\overrightarrow{F}$ mostrado en la figura, ¿Es correcto afirmar que un vector unitario con la misma dirección es: $\\overrightarrow{{u}} = \\dfrac{{3}}{{5}} \\hat{{i}} + \\dfrac{{4}}{{5}} \hat{{j}}$?",
        opcion_1 = "Sí, ya que el vector $\overrightarrow{F}$ tiene magnitud 5 y al dividir cada componente de $\overrightarrow{F}$ entre su magnitud se obtiene que su dirección es igual a $\overrightarrow{u}.$",
        opcion_2 = "No, ya que $\overrightarrow{F}$ y $\overrightarrow{u}$ tienen magnitudes diferentes y por ende, direcciones diferentes.",
        opcion_3 = "No, ya que $\overrightarrow{u}$ no es un vector unitario.",
        opcion_4 = "Sí, ya que $\overrightarrow{u}$ es un vector de magnitud 5 y al multiplicar su magnitud por $\\dfrac{{3}}{{5}} \\hat{i} + \\dfrac{4}{5} \\hat{j}$ se obtiene un vector de $\overrightarrow{F}.$",
        opcion_correcta = "Sí, ya que el vector $\overrightarrow{F}$ tiene magnitud 5 y al dividir cada componente de $\overrightarrow{F}$ entre su magnitud se obtiene que su dirección es igual a $\overrightarrow{u}.$",
        respuesta_P1 = "Un vector se expresa de la forma $\overrightarrow{V} = \|\overrightarrow{V}\|\overrightarrow{U}_v$ donde $\overrightarrow{U}_v$ es un vector unitario que se obtiene al calcular $\\dfrac{{\\overrightarrow{{V}}}}{{|\\overrightarrow{{V}}|}}$ y representa la dirección de un vector. Por ello, encontrar un vector unitario con la misma dirección a un vector $\overrightarrow{F}$ es equivalente a encontrar la dirección de $\overrightarrow{F}$ normalizándolo. Es decir, dividiendo sus componentes entre su magnitud para obtener un vector de magnitud 1.",
        respuesta_P2 = "",
        ),
    
    Theory(#5
        code = 1100050, 
        no_pregunta = 5,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "El vector unitario se utiliza para:",
        opcion_1 = "Representar la magnitud de un vector en una dirección específica.",
        opcion_2 = "Indicar la dirección de un vector.",
        opcion_3 = "Escalar vectores a una magnitud deseada.",
        opcion_4 = "Operar vectores.",
        opcion_correcta = "Indicar la dirección de un vector.",
        respuesta_P1 = "El vector unitario representa la dirección de un vector, dado que, su magnitud es 1. Esto asegura que no se alteren los valores de las componentes de dirección de un vector.",
        respuesta_P2 = "",
        ),

    Theory(#6
        code = 1100060, 
        no_pregunta = 6,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = """
        ¿Cuál(es) de las siguientes afirmaciones son ciertas respecto al vector unitario?:

        I. Siempre tiene magnitud 1.   
        II. Es un vector cuya magnitud puede ser cualquier número entero.    
        III. Se obtienen al dividir la magnitud de un vector entre sus componentes.      
        IV. Se obtiene al dividir las componentes de un vector entre su magnitud.     
        """,
        opcion_1 = "I, III",
        opcion_2 = "II, IV",
        opcion_3 = "I, IV",
        opcion_4 = "II, III",
        opcion_correcta = "I, IV",
        respuesta_P1 = """
        Las opciones correctas son I, IV:

        I. Por definición, la magnitud de un vector unitario es siempre 1.        
        IV. El vector unitario se obtiene mediante la normalización de un vector, el cual consiste en dividir sus componentes entre su magnitud con el objetivo de obtener su dirección. Asimismo, como un vector unitario representa la dirección de un vector, encontrar su dirección es equivalente a encontrar su vector unitario.
        """,
        respuesta_P2 = "",
        ),    
    
    Theory(#7
        code = 1100070, 
        no_pregunta = 7,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "Los vectores $\overrightarrow{P}$ y $\overrightarrow{Q}$ pueden ser escritos de forma vectorial como:",
        opcion_1 = """ $\\overrightarrow{P} = cos(\\alpha) \\hat{i} + sen(\\alpha)\\hat{{j}}$ \\
        $\\overrightarrow{Q} = sin(\\theta) \\hat{i} + cos(\\theta)\\hat{{j}}$""",
        opcion_2 = """$\\overrightarrow{P} = sen(\\alpha) \\hat{i} + cos(\\alpha) \\hat{j}$ \\
        $\\overrightarrow{Q} = cos (\\theta) \\hat{i} + sin(\\theta) \\hat{j}$""",
        opcion_3 = """$\\overrightarrow{P} = (sen(\\alpha) \\hat{i} + cos(\\alpha) \\hat{j}) |\overrightarrow{P}|$ \\
        $\\overrightarrow{Q} = (cos (\\theta) \\hat{i} + sen(\\theta) \\hat{j}) |\\overrightarrow{Q}|$""",
        opcion_4 = """$\\overrightarrow{P} = (cos(\\alpha) \\hat{i} + sen(\\alpha) \\overrightarrow{j}) |\\overrightarrow{P}|$ \\
        $\\overrightarrow{Q} = (sen(\\theta) \\hat{i} + cos(\\theta) \\hat{j}) |\\overrightarrow{Q}|$""",
        opcion_correcta = """$\\overrightarrow{P} = (sen(\\alpha) \\hat{i} + cos(\\alpha) \\hat{j}) |\overrightarrow{P}|$ \\
        $\\overrightarrow{Q} = (cos (\\theta) \\hat{i} + sen(\\theta) \\hat{j}) |\\overrightarrow{Q}|$""",
        respuesta_P1 = """
        El seno es la razón entre el lado opuesto al ángulo y la hipotenusa, mientras que el coseno es la razón entre el lado adyacente al ángulo y la hipotenusa. De tal forma que, el seno no siempre se relaciona con el eje y (componente $\\hat{{i}}$) y el coseno con el eje x (componente $\\hat{{j}}$). 
        Para determinar las componentes usando ángulos se recomienda identificar la ubicación del ángulo y aplicar las razones mencionadas.
        """,
        respuesta_P2 = "",
        ),
    
    Theory(#8
        code = 1100080, 
        no_pregunta = 8,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "¿Qué pasa con $\|\overrightarrow{V}\|$ cuando se multiplica por $a$?",
        opcion_1 = "Aumenta $a^2$ veces",
        opcion_2 = "Aumenta $a$ veces",
        opcion_3 = "Disminuye $a^2$ veces",
        opcion_4 = "Disminuye $a$ veces",
        opcion_correcta = "Aumenta $a$ veces",
        respuesta_P1 = """
        Cuando se multiplica a un vector por $a$, su magnitud aumenta $a$ veces. Esto ocurre, porque al ser $a$ un número entero positivo, la magnitud se afecta en la misma proporción sin alterar su dirección:

        $a*\|\overrightarrow{V}\| = a*\\overrightarrow{{V}} = a*V_x + a*V_y = a*(V_x + V_y)$ 

        Por el contrario, si se multiplica por $-a$ el resultado será un cambio de dirección y de magnitud. Y, si $a$ es un número fraccionario menor a 1,su magnitud disminuye.
        """,
        respuesta_P2 = "",
        ),

    Theory(#9
        code = 1100090, 
        no_pregunta = 9,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = """
        El producto punto es utilizado para:    

        I. Encontrar el vector resultante entre 2 vectores.   
        II. Determinar el ángulo entre 2 vectores.   
        III. Calcular el área del paralelogramo formado entre 2 vectores.    
        IV. Encontrar la proyección de un vector sobre el otro.
        """,
        opcion_1 = "I, III",
        opcion_2 = "II, IV",
        opcion_3 = "I, IV",
        opcion_4 = "II, III",
        opcion_correcta = "II, IV",
        respuesta_P1 = """
        Las opciones correctas son II, IV.
        
        II. El producto punto (o producto escalar) permite determinar el ángulo entre dos vectores, dado que, está directamente relacionado con el coseno del ángulo entre ellos ($\\overrightarrow{{A}} \\cdot \\overrightarrow{{B}} = |\\overrightarrow{{A}}||\\overrightarrow{{B}}|cos(\\theta)$). Al despejar el ángulo ($\\theta$) de la ecuación, este puede conocerse.       
        IV. El producto punto permite encontrar la proyección de un vector sobre otro, dado que, permite encontrar la proyección de un vector sobre el otro ($\\overrightarrow{{A}} \\cdot cos(\\theta))$ en su misma dirección ($\\overrightarrow{{B}}$). 
        """,
        respuesta_P2 = "",
        ),    
    
    Theory(#10
        code = 11000100, 
        no_pregunta = 10,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = """
        ¿Cuál(es) de las siguientes afirmaciones son ciertas respecto al producto punto entre vectores?:    
        
        $\\text{{I. }} A \\cdot B = B \\cdot A$                               
        $\\text{{II. }} A \\cdot B \\text{{ es un vector}}$           
        $\\text{{III. }} A \\cdot B = -B \\cdot A$                      
        $\\text{{IV. }}  A \\cdot B \\text{{ es un escalar}}$     
        $\\text{{V. }} \\text{{Cuando }}A \\cdot B = 0, \\text{{el ángulo entre A y B es 45°}}$      
        $\\text{{VI. }} \\text{{Cuando }}A \\cdot B = 0, \\text{{el ángulo entre A y B es 90°}}$        
        """,
        opcion_1 = "$\\text{{IV}}$",
        opcion_2 = "$\\text{{I, III,IV}}$",
        opcion_3 = "$\\text{{II, V, VI}}$",
        opcion_4 = "$\\text{{I, IV, VI}}$",
        opcion_correcta = "$\\text{{I, IV, VI}}$",
        respuesta_P1 = """
        Las opciones correctas son I, IV, VI. Dentro de las características principales del producto punto se encuentran:  

        1. Es conmutativo.    
        2. Su resultado es un número real.     
        3. Su resultado es 0 cuando los ángulos son perpendiculares, dado que, $cos(90°)=0$.     
        """,  
        respuesta_P2 = "",
        ),

    Theory(#11
        code = 11000110, 
        no_pregunta = 11,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "La dirección de los vectores puede expresarse por medio de cosenos directores ó ángulos en grados o radianes. Indique cuál de las siguientes es la forma correcta para pasar de grados a radianes:",
        opcion_1 = "$\\theta_{radianes}$ = $\\theta_{grados} \cdot\\frac{\pi}{180}$",
        opcion_2 = "$\\theta_{radianes}$ = $\\theta_{grados} \cdot\\frac{180}{\pi}$",
        opcion_3 = "$\\theta_{radianes}$ = $\\theta_{grados} \cdot \\pi$",
        opcion_4 = "$\\theta_{radianes}$ = $\\theta_{grados}\cdot 2\cdot\pi$",
        opcion_correcta = "$\\theta_{radianes}$ = $\\theta_{grados} \cdot\\frac{\pi}{180}$",
        respuesta_P1 = """
        La respuesta correcta es: $\\theta_{radianes}$ = $\\theta_{grados} \cdot\\frac{\pi}{180}$. Dado que, en $360°$ se recorren $2\\pi$ radianes de longitud.
        """,
        respuesta_P2 = "",
        ),  

    Theory(#12
        code = 11000120, 
        no_pregunta = 12,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado = "El producto punto se calcula a partir de las siguientes expresiones equivalentes:",
        opcion_1 = "$A \\cdot B = ABcos(\\theta)$ = $a_xb_x + a_yb_y + a_zb_z$",
        opcion_2 = "$A \\cdot B = ABcos(\\theta)$ = $a_xb_y - a_yb_x$",
        opcion_3 = "$A \\cdot B = ABsen(\\theta)$ = $a_xb_x + a_yb_y + a_zb_z$",
        opcion_4 = "$A \\cdot B = ABsen(\\theta)$ = $a_xb_y - a_yb_x$",
        opcion_correcta = "$A \\cdot B = ABcos(\\theta)$ = $a_xb_x + a_yb_y + a_zb_z$",
        respuesta_P1 = "El producto punto relaciona las magnitudes de los vectores con  el coseno del ángulo entre ellos ($ABcos(\\theta)$). Cuando no se conoce el ángulo entre los dos vectores, el producto punto puede calcularse como la suma de la multiplicación componente a componente ($a_xb_x + a_yb_y + a_zb_z$).",
        respuesta_P2 = "",
        ), 
    
    Theory(#13
        code = 11000130, 
        no_pregunta = 13,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        enunciado ="El producto cruz es utilizado para:", 
        opcion_1 = "Determinar la magnitud de la suma entre dos vectores.",
        opcion_2 = "Determinar el ángulo entre 2 vectores.",
        opcion_3 = "Encontrar la proyección de un vector sobre el otro.",
        opcion_4 = "Calcular un vector perpendicular al plano formado por los dos vectores.",
        opcion_correcta = "Calcular un vector perpendicular al plano formado por los dos vectores.",
        respuesta_P1 = "El producto cruz relaciona las magnitudes de dos vectores con el seno del ángulo entre ellos. El resultado del producto cruz entre dos vectores es un vector que es perpendicular al plano formado entre estos. Este vector resultante, indica por ejemplo, la dirección del momento.",
        respuesta_P2 = "",
        ),     

    #------------------------------------------------------ Equilibrio ----------------------------------------------------------
    #-------------------------------------------------       12000##0         ---------------------------------------------------
    
    Theory(#1
        code = 1200010, 
        no_pregunta = 1,
        topic = "Equilibrio de partículas",
        subtopic = "Equilibrio",
        enunciado = "Una partícula se encuentra en equilibrio cuando:", 
        opcion_1 = "La suma de las fuerzas en todas las direcciones es cero.",
        opcion_2 = "La fuerza resultante tiene la misma magnitud en los tres ejes.",
        opcion_3 = "La partícula está en movimiento constante.",
        opcion_4 = "La suma de los momentos alrededor de la partícula es distinta de cero.",
        opcion_correcta = "La suma de las fuerzas en todas las direcciones es cero.",
        respuesta_P1 = "Cuando una partícula está en reposo o se mueve con velocidad constante, se dice que está en equilibrio. Para cumplir esta condición se requiere que todas las fuerzas que actúan sobre la partícula formen una fuerza resultante nula.",
        respuesta_P2 = "",
        ),
     
    Theory(#2
        code = 1200020, 
        no_pregunta = 2,
        topic = "Equilibrio de partículas",
        subtopic = "Equilibrio",
        enunciado ="¿Cuáles son los pasos que deben llevarse a cabo para realizar una sumatoria de fuerzas?", 
        opcion_1 = "Hacer un diagrama de cuerpo libre sobre el sistema. Luego, realizar una sumatoria de la magnitud de las fuerzas actuantes sobre el sistema, sin considerar las direcciones en las que se aplican.",        
        opcion_2 = "Hacer un diagrama de cuerpo libre en un punto en el que las fuerzas sean concurrentes. Luego, hacer una sumatoria de la magnitud de las fuerzas actuantes sobre el cuerpo sin importar la dirección en la que se aplican.",
        opcion_3 = "Hacer un diagrama de cuerpo libre sobre el sistema. Luego, realizar la sumatoria de las componentes de las fuerzas en los ejes X, Y, Z.",
        opcion_4 = "Hacer un diagrama de cuerpo libre en un punto en el que las fuerzas sean concurrentes. Luego, realizar la sumatoria de las componentes de las fuerzas en los ejes X, Y, Z.",
        opcion_correcta = "Hacer un diagrama de cuerpo libre en un punto en el que las fuerzas sean concurrentes. Luego, realizar la sumatoria de las componentes de las fuerzas en los ejes X, Y, Z.",
        respuesta_P1 = "El primer paso para realizar la sumatoria de fuerzas es elaborar un diagrama de cuerpo libre (DCL) en un punto en el cual concurren varias fuerzas. El diagrama de cuerpo libre (DCL) consiste en representar el cuerpo como un punto aislado y situar sobre él todas las fuerzas externas que lo afectan. Posteriormente, se realiza la sumatoria de las fuerzas en cada uno de los ejes (X,Y,Z) teniendo en cuenta el sistema coordenado definido, la referencia de ejes positivos y las direcciones dadas en el DCL.",
        respuesta_P2 = "",
        ),
     
    Theory(#3
        code = 1200030, 
        no_pregunta = 3,
        topic = "Equilibrio de partículas",
        subtopic = "Equilibrio",
        enunciado = """
        La sumatoria de fuerzas igualada a cero permite:  

        I.	Encontrar la ubicación de una fuerza para que la partícula se encuentre en equilibrio.  
        II. Conocer la magnitud de una fuerza desconocida para que la partícula se encuentre en equilibrio.   
        III. Encontrar las reacciones de una viga.    
        IV. Determinar la dirección de una fuerza desconocida para que el sistema se encuentre en equilibrio.     
        V. Encontrar la dirección de movimiento de una partícula.    
        VI. Todas las anteriores.    
        """,
        opcion_1 = "I, II, V",
        opcion_2 = "VI",
        opcion_3 = "II, III, IV",
        opcion_4 = "II, III",
        opcion_correcta = "II, III, IV",
        respuesta_P1 = """
        Con sumatorias de fuerzas no es posible encontrar la ubicación de una fuerza ya que no involucra distancias. Contrario a la sumatoria de momentos que si permite lo dicho en la opción I.
        Además, con la sumatoria de fuerzas puede definirse el sentido de una fuerza particular pero no la dirección de movimiento del sistema. Esto debido a que, al igualar la sumatoria a 0 se asume que el sistema se encuentra en reposo descartandose la opció V.
        Por el contrario la sumatoria de fuerzas igual a 0 permite encontar la magnitud y dirección de una fuerza desconocida que permite mantener el equilibrio por medio del despeje de las fuerzas, sus componentes o sus ángulos
        """,
        respuesta_P2 = "",
        ),    
         
    Theory(#4
        code = 1200040, 
        no_pregunta = 4,
        topic = "Equilibrio de partículas",
        subtopic = "Equilibrio",
        enunciado ="Considere el sistema mostrado en la figura e indique la sumatoria de fuerzas correcta:",
        opcion_1 ="""$\\sum{{F_x}} = F_2 \\left(\\frac{{3}}{{5}}\\right) sen(\\theta_2) + F_1 \\left(\\frac{{12}}{{13}}\\right) sen(\\theta_1) $ \\
        $\\sum{{F_y}} = F_2 \\left(\\frac{{4}}{{5}}\\right) cos(\\theta_2) + F_1 \\left(\\frac{{5}}{{13}}\\right) cos(\\theta_1) $ \\
        $\\sum{{F_z}} = F_2 \\left(\\frac{{4}}{{5}}\\right) + F_1 \\left(\\frac{{5}}{{13}}\\right)$""",
        opcion_2 ="""$\\sum{{F_x}} = F_2 \\left(\\frac{{4}}{{5}}\\right) sen(\\theta_3) + F_1 \\left(\\frac{{5}}{{13}}\\right) cos(\\theta_1)$ \\
        $\\sum{{F_y}} = F_2 \\left(\\frac{{4}}{{5}}\\right) cos(\\theta_3) + F_1 \\left(\\frac{{5}}{{13}}\\right) sen(\\theta_1)$ \\
        $\\sum{{F_z}} = F_2 \\left(\\frac{{3}}{{5}}\\right) - F_1 \\left(\\frac{12}{13}\\right) $""",
        opcion_3 = """$\\sum{{F_x}} = F_2 \\left(\\frac{{4}}{{5}}\\right) sen(\\theta_3) + F_1 cos(\\theta_1)$ \\
        $\\sum{{F_y}} = F_2 \\left(\\frac{{4}}{{5}}\\right) cos(\\theta_3) + F_1 cos(\\theta_2)$ \\
        $\\sum{{F_z}} = F_2 \\left(\\frac{{3}}{{5}}\\right) - F_1 \\left(\\frac{{12}}{{13}}\\right)$""",
        opcion_4 ="""$\\sum{{F_x}} = F_2 \\left(\\frac{{4}}{{5}}\\right) sen(\\theta_3) + F_1 cos(\\theta_1) $ \\
        $\\sum{{F_y}} = F_2 \\left(\\frac{{4}}{{5}}\\right) cos(\\theta_3) - F_1 \cos(\\theta_1) $ \\
        $\\sum{{F_z}} = F_2 \\left(\\frac{{3}}{{5}}\\right) + F_1 \left(\\frac{12}{13}\\right) $""",
        opcion_correcta = """$\\sum{{F_x}} = F_2 \\left(\\frac{{4}}{{5}}\\right) sen(\\theta_3) + F_1 cos(\\theta_1)$ \\
        $\\sum{{F_y}} = F_2 \\left(\\frac{{4}}{{5}}\\right) cos(\\theta_3) + F_1 cos(\\theta_2)$ \\
        $\\sum{{F_z}} = F_2 \\left(\\frac{{3}}{{5}}\\right) - F_1 \\left(\\frac{{12}}{{13}}\\right)$""",
        respuesta_P1 = """
        La sumatoria de fuerzas del sistema mostrado es:

        $\\sum{{F_x}} = F_2 \\left(\\frac{{4}}{{5}}\\right) sen(\\theta_3) + F_1 cos(\\theta_1)$

        $\\sum{{F_y}} = F_2 \\left(\\frac{{4}}{{5}}\\right) cos(\\theta_3) + F_1 cos(\\theta_2)$

        $\\sum{{F_z}} = F_2 \\left(\\frac{{3}}{{5}}\\right) - F_1 \\left(\\frac{{12}}{{13}}\\right)$

        Note que para calcular las componentes X y Y de $F_1$ se utilizan los cosenos directores ($\\theta_1$ y $\\theta_2$), dado que, estos ángulos relacionan al vector directamente con los ejes. 
        
        Por otro lado, para la fuerza $F_2$ se aplica la descomposición por coordenadas cartesianas. Para el cálculo de sus componentes X y Y, primero se proyecta el vector en el plano XY, y luego se descompone con el ángulo $\\theta_3$. La componente Z se obtiene con el seno del triángulo presentado.
        """,
        respuesta_P2 = "",
        ),
         
    Theory(#5
        code = 1200050, 
        no_pregunta = 5,
        topic = "Equilibrio de partículas",
        subtopic = "Equilibrio",
        enunciado ="Considere el sistema mostrado en la figura e indique cual es el diagrama de cuerpo libre equivalente teniendo en cuenta el sistema de coordenadas.", 
        opcion_1 = "Opción 1.",
        opcion_2 = "Opción 2.",
        opcion_3 = "Opción 3.",
        opcion_4 = "Opción 4.",
        opcion_correcta = "Opción 1.",
        respuesta_P1 = """
        El diagrama de cuerpo libre del bloque, que representa al sistema, es la opción 1 por las siguientes razones:

        1. El vector normal ($N$) siempre es un vector perpendicuar a la superficie.     
        2. El vector de peso ($W$) es un vector que siempre es vertical hacia abajo.      
        3. El vector de fricción ($f$) siempre tiene dirección contraria al desplazamiento.
        """,
        respuesta_P2 = "",
        ),
         
    Theory(#6
        code = 1200060, 
        no_pregunta = 6,
        topic = "Equilibrio de partículas",
        subtopic = "Equilibrio",
        enunciado ="Es correcto afirmar que, en una sumatoria de fuerzas, el valor encontrado para una fuerza desconocida siempre será mayor a cero.", 
        opcion_1 = "Sí, si la solución produce un resultado menor a 0, el sistema no está en equilibrio.",
        opcion_2 = "No, si la solución produce un resultado negativo, esto indica que el sentido de la fuerza es el inverso del supuesto sobre el diagrama de cuerpo libre.",
        opcion_3 = "Sí, un valor negativo en el resultado significa un error de cálculo.",
        opcion_4 = "No, pueden existir resultados negativos, y como en la sumatoria de fuerzas solo importa la magnitud del vector, el signo puede ignorarse.",
        opcion_correcta = "No, si la solución produce un resultado negativo, esto indica que el sentido de la fuerza es el inverso del supuesto sobre el diagrama de cuerpo libre.",
        respuesta_P1 = "Dado que la sumatoria de fuerzas se realiza teniendo en cuenta suposiciones de dirección en fuerzas desconocidas presentes en el diagrama de cuerpo libre, es posible obtener escalares negativos, los cuales indican que el sentido correcto es el opuesto al considerado por suposición.",
        respuesta_P2 = "",
        ),
         
    Theory(#7
        code = 1200070, 
        no_pregunta = 7,
        topic = "Equilibrio de partículas",
        subtopic = "Equilibrio",
        enunciado ="""
        Considerando el siguiente sistema conformado por dos alambres con resorte que soportan un bloque de acero, ¿Cuál(es) de las siguientes afirmaciones es(son) falsa(s)?.
             
        I. El diagrama de cuerpo libre para el sistema con resorte será el mismo que el del sistema sin resorte.      
        II.	Es posible hallar el alargamiento del resorte del resorte dividiendo la fuerza del alambre entre la constante de rigidez (k) del resorte respectivo.      
        III. El sistema pierde el estado de equilibrio por efecto de los resortes.       
        IV.	En la sumatoria de fuerzas es necesario multiplicar las tensiones de los alambres por las constantes de rigidez respectivas (k).        
        """,
        opcion_1 = "I, II.",
        opcion_2 = "Solamente II.",
        opcion_3 = "III, IV.",
        opcion_4 = "I, II.",
        opcion_correcta = "III, IV.",
        respuesta_P1 = "Las opciones I y II son correctas. Si el problema implica un resorte elástico lineal, entonces el alargamiento o la compresión $s$ del resorte puede ser relacionado con la fuerza aplicada usando $F=ks$.",
        respuesta_P2 = "",
        ),
         
    Theory(#8
        code = 1200080, 
        no_pregunta = 8,
        topic = "Equilibrio de partículas",
        subtopic = "Equilibrio",
        enunciado ="Considerando la polea A, ¿Cuál de las siguientes sumatorias en Y es correcta?", 
        opcion_1 = "$ \\sum {{F_y}} = F_{1} + F_{2} + F_{3} - W = 3 F_{1} - W = 0  $",
        opcion_2 = "$ \\sum {{F_y}} =  \\left(\\frac{F_{1}}{2}\\right) + \\left(\\frac{F_{2}}{2}\\right) - F_{3} - W = 0 $",
        opcion_3 = "$ \\sum {{F_y}} =  \\left(\\frac{F_{1}}{2}\\right) + \\left(\\frac{F_{2}}{2}\\right) - F_{3}  = 0 $",
        opcion_4 = "$ \\sum {{F_y}} = F_{1} + F_{2} - W = 2 F_{1} - W = 0  $",
        opcion_correcta = "$ \\sum {{F_y}} = F_{1} + F_{2} - W = 2 F_{1} - W = 0  $",
        respuesta_P1 = "Note que la sumatoria en Y sobre la polea no incluye a $F_3$. Además, en las poleas el cable es continuo y por ende $F_1 = F_2 = F_3$.",
        respuesta_P2 = "",
        ),
         
    Theory(#9
        code = 1200090, 
        no_pregunta = 9,
        topic = "Equilibrio de partículas",
        subtopic = "Equilibrio",
        enunciado ="La sumatoria de fuerzas que permite encontrar el valor del peso (W) del bloque es:",
        opcion_1 = "$ \\sum{{F_z}}=T_{BA} \\left(\\frac{{A_z}}{{\\sqrt{{(-B_x)^2 + (-B_y)^2 + (A_Z)^2}}}}\\right)-W=0$",
        opcion_2 = "$ \\sum{{F_y}}=T_{{BA}} \\left(\\frac{{-B_y}}{{\\sqrt{{(-B_x)^2 + (-B_y)^2 + (A_Z)^2}}}}\\right)-W = 0 $",
        opcion_3 = "$ \\sum{{F_x}}=T_{{BA}} \\left(\\frac{{-B_x}}{{\\sqrt{{(-B_x)^2 + (-B_y)^2}}}}\\right) - W = 0 $",
        opcion_4 = "$ \\sum{{F_z}}=T_{{BA}} \\left(\\frac{{A_z}}{{\\sqrt{{(-B_x)^2 + (-B_y)^2}}}}\\right) - W = 0 $",
        opcion_correcta = "$ \\sum{{F_z}}=T_{BA} \\left(\\frac{{A_z}}{{\\sqrt{{(-B_x)^2 + (-B_y)^2 + (A_Z)^2}}}}\\right)-W=0$",
        respuesta_P1 = "Se realiza la sumatoria de fuerzas en Z, dado que, en este eje se encuentra el peso. Se evidencia que solo existen dos fuerzas actuando sobre el eje Z: la componente de la tensión generaada por el cable BA y el peso. La componente de la tensión es igual a la magnitud de la tensión de dicho cable multiplicada por la componente $\\hat{{k}}$ de su vector unitario",
        respuesta_P2 = "",
        ),

    #----------------------------------------------------- Momentos --------------------------------------------------------
    #-------------------------------------------------    15000##0       ---------------------------------------------------
    #Theory(#1
    #    code = 1300010, 
    #    no_pregunta = 1,
    #    topic = "Equilibrio de partículas",
    #    subtopic = "Momentos",
    #    enunciado ="Cuando se hace análisis sobre un cuerpo y no sobre una partícula se dice que este se encuentra en equilibrio cuando:", 
    #    opcion_1 = """
    #    $ \\sum F_x = 0 ; \\sum F_y = 0 ; \\sum F_z = 0 \\
    #    $ \\sum M_x = \\sum M_y = \\sum M_z \\
    #    """,
    #    opcion_2 = """
    #    $ \\sum F_x = \\sum F_y = \\sum F_z \\
    #    $ \\sum M_x = \\sum M_y = \\sum M_z \\    
    #    """,
    #    opcion_3 = """
    #    $ \\sum F_x = 0 ; \\sum F_y = 0 ; \\sum F_z = 0 \\
    #    $ \\sum M_x = 0 ; \\sum M_y = 0 ; \\sum M_z = 0 \\
    #    """,
    #    opcion_4 = """
    #    $ \\sum F_x = \\sum F_y = \\sum F_z \\
    #    $ \\sum M_x = 0 ; \\sum M_y = 0 ; \\sum M_z = 0 \\
    #    """,
    #    opcion_correcta = """
    #    $ \\sum F_x = 0 ; \\sum F_y = 0 ; \\sum F_z = 0 \\
    #    $ \\sum M_x = 0 ; \\sum M_y = 0 ; \\sum M_z = 0 \\
        # """,
        # respuesta_P1 = "Un cuerpo se encuentra en equilibrio cuando la sumatoria de fuerzas y momentos sobre todos sus ejes es igual a cero ya que, esto significa que el cuerpo se encuentra completamente en reposo.",
        # respuesta_P2 = "",
        # ),
         
    # Theory(#2
    #     code = 1300020, 
    #     no_pregunta = 2,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Momentos",
    #     enunciado ="""
    #     De los pares de fuerza es correcto afirmar que:
    #     I. Son fuerzas de igual magnitud, pero diferente sentido.
    #     II. No generan momento debido que el efecto de las fuerzas del par anula el efecto de la otra.
    #     III. Generan un solo momento independiente del punto de referencia. Es decir, del punto desde donde se calcula el momento.
    #     IV. Generan un momento de igual magnitud, pero diferente sentido de acuerdo con el punto de referencia. 
    #     """,
 
    #     opcion_1 = "Opción I y II son correctas.",
    #     opcion_2 = "Opción I y III son correctas.",
    #     opcion_3 = "Opción I y IV son correctas.",
    #     opcion_4 = "Solo opción I es correcta",
    #     opcion_correcta = "Opción I y III son correctas.",
    #     respuesta_P1 = """Los pares de fuerza no generan efecto en la sumatoria de fuerzas pero si sobre la sumatoria de momentos ya que, el momento se calcula como: \\( \\overrightarrow{r} \) X \\( \\overrightarrow{F} \) y, cuando se trata de pares de fuerza, el  vector \\( \\overrightarrow{r} \) representa la distancia entre ellos la cual siempre es la misma. A diferencia de su sentido que si cambia respecto al punto de desde donde se calcula el momento generando esto que se genere un mismo momento.
    #     En otras palabras, si \\( \\overrightarrow{P} \) y \\( \\overrightarrow{Q} \) generan un par de fuerzas, el momento será el mismo independientemente del puento de referencia porque: \\( \\overrightarrow{P} \) = - \\( \\overrightarrow{Q} \) y \\( \\overrightarrow{r_1} \) = - \\( \\overrightarrow{r_2} \)
    #     """,
    #     ),
         
    # Theory(#3
    #     code = 1300030, 
    #     no_pregunta = 3,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Momentos",
    #     enunciado = "En 2D la mejor estrategia para realizar sumatoria de momentos es:",
    #     opcion_1 = "Realizar el producto cruz: \\( \\overrightarrow{r} \) X \( \\overrightarrow{F} \)",
    #     opcion_2 = "Multiplicar las magnitudes de las fuerzas por la distancia perpendicular",
    #     opcion_3 = "Realizar el producto cruz: ,\\( \\overrightarrow{F} \) X \( \\overrightarrow{r} \)",
    #     opcion_4 = "Descomponer las fuerzas sobre los ejes x e y, y multiplicar cada una de ellas por las distancias perpendiculares ",
    #     opcion_correcta = "Descomponer las fuerzas sobre los ejes x e y, y multiplicar cada una de ellas por las distancias perpendiculares ",
    #     respuesta_P1 = """
    #     Siempre que se tenga un sistema en 2D es recomendable utilizar el método de distancias perpendiculares debido a que, muchas veces, al definir el vector \( \overrightarrow{r} \) solo una de sus componentes es diiferente de 0. 
    #     No obstante, es importante tener en cuenta que la aplicación de este método requiere la descomposición de las fuerzas debido a que el ángulo entre \( \overrightarrow{r} \) y \( \overrightarrow{F} \) debe ser 90° para que el producto cruz se convierta en multiplicación de magnitudes.
    #     """,
    #     respuesta_P2 = "",
    #     ),    
             
    # Theory(#4
    #     code = 1300040, 
    #     no_pregunta = 4,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Momentos",
    #     enunciado ="Es momento es:",
    #     opcion_1 ="Un escalar positivo",
    #     opcion_2 ="Un vector perpendicular al plano formado entre  \\( \overrightarrow{r} \) y \\( \overrightarrow{F} \)",
    #     opcion_3 = "Un vector con un ángulo variable respecto al plano formado entre  \\( \overrightarrow{r} \) y \\( \overrightarrow{F} \)",
    #     opcion_4 ="Un escalar negativo",
    #     opcion_correcta = "Un vector perpendicular al plano formado entre  \\( \overrightarrow{r} \) y \\( \overrightarrow{F} \)",
    #     respuesta_P1 = "Dado a que el momento se calcula por medio de un producto cruz, este es un vector perpendicular al plano formado entre el vector de fuerza y el vector de posición.",
    #     respuesta_P2 = "",
    #     ),
             
    # Theory(#5
    #     code = 1300050, 
    #     no_pregunta = 5,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Momentos",
    #     enunciado ="¿Cuál es el entido del momento generado por una fuerza que hace girar a un cuerpo en sentido antihorario?", 
    #     opcion_1 = "Hacia abajo",
    #     opcion_2 = "Hacia arriba",
    #     opcion_3 = "Hacia adentro de un plano imaginario",
    #     opcion_4 = "Hacia afuera de un plano imaginario",
    #     opcion_correcta = "Hacia afuera de un plano imaginario",
    #     respuesta_P1 = """El sentido del momento se determina con el sentido de la rotación que induce una fuerza sobre el cuerpo de tal manera que, por convención, se considera positivo si la rotación es en sentido antihorrio y negativo si la rotación es en sentido horario.
    #     Así mismo su dirección se determina por medio de la regla de la mano derecha donde, si al aplicarla, el pulgar apunta hacia ti el momento es positivo y en esa dirección. Y, si apunta hacia afuera, el momento es negativo y se dirige en esa dirección.""",
    #     respuesta_P2 = "",
    #     ),
             
    # Theory(#6
    #     code = 1300060, 
    #     no_pregunta = 6,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Momentos",
    #     enunciado =
    #     """ Considere la siguiente figura e indique cual de las siguientes afirmaciones son falsas:
    #     I. El cuerpo se encuentra en equilibrio.
    #     II. El momento sobre la viga es negativo.
    #     III. La dirección del momento es - \\( \\overrightarrow{k} \).
    #     IV. La dirección del momento es hacia abajo. Es decir, en - \\( \\overrightarrow{j} \).
    #     V. La viga girará en sentido horario.
    #     """,             
    #     opcion_1 = "II, III, V",
    #     opcion_2 = "Solamente IV.",
    #     opcion_3 = "I, V.",
    #     opcion_4 = "I, IV.",
    #     opcion_correcta = "I, IV.",
    #     respuesta_P1 = """
    #     El cuerpo no se encuentra en equilibrio porque, aunque la sumatoria de fuerzas es 0, la de momentontos no lo es.
    #     Decir que el momento se encuentra en dirección - \\( \\overrightarrow{k} \) es equivalente a decir que el sentido de la rotación es horario y a su vez, que el momento es negativo.
    #     """,
    #     respuesta_P2 = "",
    #     ),
             
    # Theory(#7
    #     code = 1300070, 
    #     no_pregunta = 7,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Momentos",
    #     enunciado ="¿Un requisito para que exista momento es que la linea de acción de la fuerza \\textbf{no} pase por el punto en el cual se está haciendo la sumatoria?",
    #     opcion_1 = "Correcto, ya que esto hace que \\( \overrightarrow{r} \) sea 0", 
    #     opcion_2 = "No, basta con que la fuerza no esté directamente aplicada sobre el punto para que exista mometo.",
    #     opcion_3 = "Correcto, porque esto hace que la magnitud de la fuerza se vuelva nula y por ende no haya momento.",
    #     opcion_4 = "Depende de la geometría del cuerpo",
    #     opcion_correcta = "Correcto, ya que esto hace que \\( \overrightarrow{r} \) sea 0", 
    #     respuesta_P1 = " las fuerzas actúan como vectores libres sobre su misma línea de acción y si esta pasa por el punto, puede ubicarse el vector directamente sobre él haciendo que el vector \\( \overrightarrow{r} \) sea 0 y por consiguiente, el producto cruz tambien. ",
    #     respuesta_P2 = "",
    #     ),
             
    # Theory(#8
    #     code = 1300080, 
    #     no_pregunta = 8,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Momentos",
    #     enunciado ="Considere la siguiente figura e indique cuál de las siguientes situaciones (A ó B) hace más fácil desajustar la tuerca teniendo en cuenta que la fuerza aplicada es igual en ambos casos.",
    #     opcion_1 = "Situación A, ya que a menor \\( \overrightarrow{r} \) mayor momento", 
    #     opcion_2 = "Es igual en ambos casos dado que la fuerza tinene la misma magnitud y dirección",
    #     opcion_3 = "Situación B, ya que a mayor \\( \overrightarrow{r} \) mayor momento",
    #     opcion_4 = "Situación B ya que en esta el momento generado es negativo.",
    #     opcion_correcta = "Situación B, ya que a mayor \\( \overrightarrow{r} \) mayor momento", 
    #     respuesta_P1 = " Dado que el momento se calcula como \\( \overrightarrow{r} \) X \\( \overrightarrow{F} \) a mayor distancia entre la fuerza y el punto de referencia, mayor será la magnitud del momento generado y por ende, será mas facil desajustar la turca. Además, entre mayor sea el r menor fuerza se requerirá. ",
    #     respuesta_P2 = "",
    #     ),
             
    # Theory(#9
    #     code = 1300090, 
    #     no_pregunta = 9,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Momentos",
    #     enunciado ="Considere el poste de luz de la figura e indique las direcciones del momento generado por el peso del transformador y la fuerza de viento respecto al punto O",
    #     opcion_1 = "Momento W = \\( \overrightarrow{j} \); Momento Fv = \\( \overrightarrow{i} \);", 
    #     opcion_2 = "Momento W = \\( \overrightarrow{j} \); Momento Fv = -\\( \overrightarrow{i} \);",
    #     opcion_3 = "Momento W = \\( \overrightarrow{j} \); Momento Fv = \\( \overrightarrow{k} \);",
    #     opcion_4 = "Momento W = \\( \overrightarrow{k} \); Momento Fv = \\( \overrightarrow{i} \);",
    #     opcion_correcta = "Momento W = \\( \overrightarrow{j} \); Momento Fv = \\( \overrightarrow{i} \);", 
    #     respuesta_P1 = """"Para determinar la dirección de momento generado por el peso del transformador se tiene que: \\( \overrightarrow{i} \) X \\( \overrightarrow{-K} \) = \\( \overrightarrow{j} \).
    #     Y para determinar la dirección de momento generado por la fuerza de viento se tiene que: \\( \overrightarrow{k} \) X \\( \overrightarrow{-j} \) = \\( \overrightarrow{i} \).""",
    #     respuesta_P2 = "",
    #     ),   



    # #------------------------------------------------------ Apoyos ----------------------------------------------------------
    # #-------------------------------------------------    51000##0       ---------------------------------------------------
    # Theory(#1
    #     code = 1400010, 
    #     no_pregunta = 1,
    #     topic = "Apoyos y reacciones",
    #     subtopic = "Apoyos y reacciones",
    #     enunciado ="¿Cuál de los siguientes tipos de apoyos genera una reacción vertical y una reacción horizontal, pero no un momento?", 
    #     opcion_1 = "Apoyo fijo o empotramiento",
    #     opcion_2 = "Apoyo con articulación",
    #     opcion_3 = "Apoyo tipo rodillo o patín",
    #     opcion_4 = "Apoyo con collarín",
    #     opcion_correcta = "Apoyo con articulación",
    #     respuesta_P1 = "Un apoyo con articulación es un apoyo de segundo grado.Por ello, genera 2 reacciones las cuales restringen el desplazamiento pero no el giro o momento.",
    #     respuesta_P2 = "",
    #     ),
             
    Theory(#2
        code = 5100020, 
        no_pregunta = 2,
        topic = "Apoyos y reacciones",
        subtopic = "Apoyos y reacciones",
        enunciado = "Un apoyo de primer grado es aquel que:",
        opcion_1 = "Tiene una sola restricción.",
        opcion_2 = "Permite un solo movimiento.",
        opcion_3 = "Tiene más de una restricción.",
        opcion_4 = "No tiene ninguna restricción",
        opcion_correcta = "Tiene una sola restricción.",
        respuesta_P1 = "Los apoyos de primer grado, tanto en 2D como en 3D, son aquellos que impiden el desplazamiento en una sola dirección, lo cual genera una sola reacción.",
        respuesta_P2 = "",
        ),
             
    # Theory(#3
    #     code = 1400030, 
    #     no_pregunta = 3,
    #     topic = "Apoyos y reacciones",
    #     subtopic = "Apoyos y reacciones",
    #     enunciado = "Considere las siguientes figuras e indique el número de restricciones o reacciones que generan teniendo en cuenta un sistema de tres cordenadas (3D) :",
    #     opcion_1 = "I: 6; II: 3; III: 2",
    #     opcion_2 = "I: 3; II: 2; III: 1",
    #     opcion_3 = "I: 5; II: 6; III: 0",
    #     opcion_4 = "I: 6; II: 5; III: 1",
    #     opcion_correcta = "I: 6; II: 5; III: 1",
    #     respuesta_P1 = """
    #     La figura 1 es un apoyo fijo que no permite desplazamieto ni momento en ninguna dirección (x,y,z).
    #     La figura 2 es un pasador y por ende permite únicamente el giro en una sola dirección. De tal forma que: #reacciones (3D) = 6 - Grados de libertad = 6 - 1 = 5.
    #     La figura 3 permite el giro en las tres direcciones (Mx, My, Mz) y el desplazamiento en todo el plano del suelo (convencionalmente x-y) pero no hacia arriba. Del tal forma que: #reacciones (3D) = 6 - Grados de libertad = 6 - 5 = 1.""",
    #     respuesta_P2 = "",
    #     ),    
                 

    # #-------------------------------------------------  Sistemas equivalentes ---------------------------------------------------
    # #-------------------------------------------------       15000##0         ---------------------------------------------------
    # Theory(#1
    #     code = 1500010, 
    #     no_pregunta = 1,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Sistemas equivalentes",
    #     enunciado ="Dos sistemas de fuerzas son equivalentes cuando:", 
    #     opcion_1 = "Tienen el mismo número de fuerzas con igual magnitud pero diferente ubicación.",
    #     opcion_2 = "Actúan sobre cuerpos con la misma geometría.",
    #     opcion_3 = "Tienen la misma resultante y el mismo momento con respecto a un punto.",
    #     opcion_4 = "La sumatoria de las resultantes de cada sistema es igual a 0. ",
    #     opcion_correcta = "Tienen la misma resultante y el mismo momento con respecto a un punto.",
    #     respuesta_P1 = "Dos sistemas son equivalentes si, al reducirlos, generan la misma fuerza resultante y el mismo momento respecto a un punto dado. Esto significa que, aunque las fuerzas individuales sean diferentes, su efecto global sobre el cuerpo es el mismo.",
    #     respuesta_P2 = "",
    #     ),

    # Theory(#2
    #     code = 1500020, 
    #     no_pregunta = 2,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Sistemas equivalentes",
    #     enunciado ="¿Cuál es la principal utilidad de reducir un sistema de fuerzas a una fuerza resultante y un momento?", 
    #     opcion_1 = "Simplificar el análisis de equilibrio y distribución de cargas en un cuerpo rígido.",
    #     opcion_2 = "Aumentar la precisión en el cálculo de deformaciones en estructuras.",
    #     opcion_3 = "Determinar el centro de masa exacto de un objeto.",
    #     opcion_4 = "Estudiar cómo una estructura se deforma",
    #     opcion_correcta = "Simplificar el análisis de equilibrio y distribución de cargas en un cuerpo rígido.",
    #     respuesta_P1 = "Reducir un sistema de fuerzas a una fuerza resultante y un momento permite trabajar con una representación más sencilla del sistema. Esto es especialmente útil en estructuras, donde analizar todas las fuerzas individualmente sería complejo.",
    #     respuesta_P2 = "",
    #     ),

    # Theory(#3
    #     code = 1500030, 
    #     no_pregunta = 3,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Sistemas equivalentes",
    #     enunciado ="La forma de reducir un sistema de fuerzas es:", 
    #     opcion_1 = "Encontrar la resultante y ubicarla en el punto medio entre ellas.",
    #     opcion_2 = "Convertir las fuerzas distribuidas en fuerzas puntuales y viceversa.",
    #     opcion_3 = "Cambiar las magnitudes de la fuerzas de tal forma que la resultante sea la misma.",
    #     opcion_4 = "Encontrar la resultante y ubicarla en el punto en el que el momento generado por esta sea el mismo.",
    #     opcion_correcta = "Encontrar la resultante y ubicarla en el punto en el que el momento generado por esta sea el mismo.",
    #     respuesta_P1 = """El procedimiento general para encontrar un sistema de fuerzas equivalentes es:
    #     1. Se hace la suma vectorial de todas las fuerzas aplicadas al sistema. 
    #     2. Se calcula el momento en el sistema original respecto a un punto cualquiera (O) usando producto cruz y se suman los momentos.
    #     3. Se calcula la posición de la resultante \\( \overrightarrow{r} \) utilizando producto cruz. Esto teniendo en cuenta que la fuerza que debe tomarse es la resultante calculada y que el momento tomado es el calculado en el paso anterior.
    #     De esta forma se encuentra la ubicación de la resultante que permite que los momentos en ambos sean iguales medido desde el mismo punto (O).
    #     Nota: Cuando es un sistema en 2D lo usual es calcular el momento con las distancias perpendiculares.""",
    #     respuesta_P2 = "",
    #     ),
                     
    # Theory(#4
    #     code = 1500040, 
    #     no_pregunta = 4,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Sistemas equivalentes",
    #     enunciado ="El sistema de fuerzas equivalente al de la siguiente figura es:", 
    #     opcion_1 = "Opción I",
    #     opcion_2 = "Opción II",
    #     opcion_3 = "Opción III",
    #     opcion_4 = "Ninguna",
    #     opcion_correcta = "Opción I",
    #     respuesta_P1 = "Note que la opción I tiene la fuerza resultante ubicada a una distancia x calculada a partir del momento del sistema original.",
    #     respuesta_P2 = "",
    #     ),
                     
     
]


