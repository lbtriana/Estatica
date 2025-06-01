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

    #----------------------------------------------------- Momentos -------------------------------------------------------
    #------------------------------------------------------ Momento -------------------------------------------------
    #-------------------------------------------------    21000#0       ---------------------------------------------------
    Theory(#1
       code = 2100010, 
       no_pregunta = 1,
       topic = "Momento",
       subtopic = "Momento",
       enunciado ="Se considera que un cuerpo está en equilibrio si cumple con las siguientes condiciones:", 
       opcion_1 = """$ \\sum F_x = 0$ ; $\\sum F_y = 0$ ; $\\sum F_z = 0$ \\
       $ \\sum M_x = \\sum M_y = \\sum M_z$ \\
       $\\text{{    }}$ """,
       opcion_2 = """ $ \\sum F_x = \\sum F_y = \\sum F_z$ \\
       $ \\sum M_x = \\sum M_y = \\sum M_z$    
       $\\text{{    }}$ """,
       opcion_3 = """$ \\sum F_x = 0$ ; $\\sum F_y = 0$ ; $\\sum F_z = 0$ \\
       $ \\sum M_x = 0$ ; $\\sum M_y = 0$ ; $\\sum M_z = 0$ \\
       $\\text{{    }}$ """,
       opcion_4 = """$ \\sum F_x = \\sum F_y = \\sum F_z$ \\
       $ \\sum M_x = 0$ ; $\\sum M_y = 0$ ; $\\sum M_z = 0$ \\
       $\\text{{    }}$ """,
       opcion_correcta = """$ \\sum F_x = 0$ ; $\\sum F_y = 0$ ; $\\sum F_z = 0$ \\
       $ \\sum M_x = 0$ ; $\\sum M_y = 0$ ; $\\sum M_z = 0$ \\
       $\\text{{    }}$ """,
       respuesta_P1 = "Un cuerpo está en equilibrio cuando la sumatoria de las fuerzas y los momentos respecto a todos sus ejes es igual a cero, esto indica que el cuerpo se encuentra completamente en reposo.",     
       respuesta_P2 = "",
       ),
         
    Theory(#2
        code = 2100020, 
        no_pregunta = 2,
        topic = "Momento",
        subtopic = "Momento",
        enunciado ="""
        Con respecto a un par de fuerzas es correcto afirmar que:     

        I. Son dos fuerzas paralelas de igual magnitud y direcciones opuestas.    
        II. No generan momento, debido que el efecto de las fuerzas del par anula el efecto de la otra.    
        III. Generan un único efecto de rotación en el cuerpo, en una dirección específica, independiente del punto de referencia.     
        IV. Generan un momento en una dirección específica, cuyo valor corresponde a la suma de los momentos producidos por cada fuerza con respecto a un punto de referencia.    
        """, 
        opcion_1 = "I, II",
        opcion_2 = "I, IV",
        opcion_3 = "I, III",
        opcion_4 = "Solamente I",
        opcion_correcta = "I, III",
        respuesta_P1 = """
        Las opciones correctas son I y III:

        I. La afirmación corresponde a la definición un par de fuerzas.      
        III. Un par de fuerzas no tiene un efecto de traslación, pero si de rotación. El momento generado por un par de fuerzas es único y no depende del punto de referencia escogido. 
        """,
        respuesta_P2 = "",
        ),

    Theory(#3
        code = 2100030, 
        no_pregunta = 3,
        topic = "Momento",
        subtopic = "Momento",
        enunciado ="El momento es:",
        opcion_1 ="Un escalar positivo.",
        opcion_2 ="Un vector perpendicular al plano formado entre $\\overrightarrow{r}$ y $\\overrightarrow{F}.$",
        opcion_3 = "Un vector con un ángulo variable respecto al plano formado entre $\\overrightarrow{r}$ y $\\overrightarrow{F}$.",
        opcion_4 ="Un escalar negativo.",
        opcion_correcta = "Un vector perpendicular al plano formado entre $\\overrightarrow{r}$ y $\\overrightarrow{F}.$",
        respuesta_P1 = "El momento es un vector perpendicular al plano formado entre $\\overrightarrow{r}$ y $\\overrightarrow{F}$, es decir, representa el eje alrededor del cual el cuerpo tenderá a rotar. Por tal motivo, el momento se calcula por medio del producto cruz ($\\overrightarrow{M}$ = $\\overrightarrow{r}$ X $\\overrightarrow{F}$), donde $\\overrightarrow{r}$ es el vector posición y $\\overrightarrow{F}$ el vector fuerza.",
        respuesta_P2 = "",
        ),

    Theory(#4
        code = 2100040, 
        no_pregunta = 4,
        topic = "Momento",
        subtopic = "Momento",
        enunciado ="Para girar la mesa se aplica un par de fuerzas $F$. ¿Cuál de las siguientes expresiones permite calcular el momento generado por este par de fuerzas?", 
        opcion_1 = """$-2F \\cdot cos(\\alpha) \\cdot b - 2F \\cdot sin(\\alpha) \\cdot h$\\
        $\\text{{   }}$""",
        opcion_2 = """$-2F \\cdot \\sqrt{{b^2+h^2}}$ \\
        $\\text{{   }}$""",
        opcion_3 = """$-F \\cdot \\sqrt{{b^2+h^2}}$ \\
        $\\text{{   }}$""",
        opcion_4 = """$-F \\cdot cos(\\alpha) \\cdot b - F \\cdot sin(\\alpha) \\cdot h$\\
        $\\text{{   }}$""",
        opcion_correcta = """$-F \\cdot cos(\\alpha) \\cdot b - F \\cdot sin(\\alpha) \\cdot h$\\
        $\\text{{   }}$""",
        respuesta_P1 = "El momento generado por un par de fuerzas se define como el producto de la magnitud de la fuerza por la distancia perpendicular entre sus líneas de acción. En este caso, es incorrecto asumir que la distancia perpendicular entre las fuerzas es la hipotenusa formada por $b$ y $h$. Por lo tanto, el momento total se obtiene sumando los momentos generados por cada componente de la fuerza respecto a su respectiva distancia perpendicular: $-F \\cdot cos(\\alpha) \\cdot b - F \\cdot sin(\\alpha) \\cdot h$.",
        respuesta_P2 = "",
        ),

    Theory(#5
        code = 2100050, 
        no_pregunta = 5,
        topic = "Momento",
        subtopic = "Momento",
        enunciado ="Aplicando la regla de la mano derecha, ¿cuál es la dirección del momento generado por la componente $x$ de la fuerza y la componente $y$ del vector posición?", 
        opcion_1 = "$\\hat{{i}}$",
        opcion_2 = "$-\\hat{{k}}$",
        opcion_3 = "$-\\hat{{i}}$",
        opcion_4 = "$\\hat{{k}}$",
        opcion_correcta = "$-\\hat{{k}}$",
        respuesta_P1 = "Para aplicar la regla de la mano derecha, se coloca la mano derecha siguiendo la dirección del vector posición, y se gira la mano en el sentido de la fuerza hasta cerrar los dedos hacia ella. En este caso, al cerrar la mano el pulgar apunta hacia adentro del plano. Esto indica que la dirección del momento es negativa en el eje $z$, es decir, -$\\hat{{k}}$.",
        respuesta_P2 = "",
        ),
             
    Theory(#6
        code = 2100060, 
        no_pregunta = 6,
        topic = "Momento",
        subtopic = "Momento",
        enunciado =
        """ 
        Considere la siguiente figura e indique cualés de las siguientes afirmaciones son falsas:    

        I. El cuerpo se encuentra en equilibrio.         
        II. La dirección del momento es - $\\hat{{k}}$.     
        III. La dirección del momento es - $\\^j$.      
        IV. La viga tiene una tendencia a la rotación en sentido horario.      
        """,             
        opcion_1 = "I, II",
        opcion_2 = "II, IV",
        opcion_3 = "I, IV",
        opcion_4 = "I, III",
        opcion_correcta = "I, III",
        respuesta_P1 = """
        Las afirmaciones falsas son I y III:

        I. El cuerpo no está en equilibrio, dado que, aunque la sumatoria de fuerzas es cero, la sumatoria de momentos no lo es.        
        II. El momento es un vector perperdincular al plano que contiene la fuerza y el brazo del momento. En este caso, el plano es bidimensional (x, y), por lo que el momento se encuentra en la dirección de z.
        """,
        respuesta_P2 = "",
        ),
             
    Theory(#7
        code = 2100070, 
        no_pregunta = 7,
        topic = "Momento",
        subtopic = "Momento",
        enunciado ="¿Es un requisito que la línea de acción de la fuerza no pase por el punto en el que se evalúa el momento para que exista un momento?",
        opcion_1 = "Incorrecto. Basta con que la fuerza no esté aplicada directamente sobre el punto para que exista momento.",
        opcion_2 = "Correcto. Dado que, la magnitud de la fuerza se vuelva nula, por lo que no existe momento.",
        opcion_3 = "Correcto. Dado que, esto hace que el vector posición $(\\overrightarrow{r})$ sea cero, y por lo tanto el momento es nulo.", 
        opcion_4 = "No es posible responder con la información dada. Es necesario considerar la geometría del cuerpo.",
        opcion_correcta = "Correcto. Dado que, esto hace que el vector posición $(\\overrightarrow{r})$ sea cero, y por lo tanto el momento es nulo.", 
        respuesta_P1 = "La afirmación es correcta. Cuando la línea de acción de la fuerza cruza por el punto de evaluación, el momento es igual a cero, dado que, no existe una excentricidad entre el punto de evaluación y la línea de acción de la fuerza $(\\overrightarrow{r})$ que genere la tendencia a la rotación. Matemáticamente, el momento es $\\overrightarrow{M}=\\overrightarrow{r} \\text{{  X  }} \\overrightarrow{F}$, al ser el vector posición $(\\overrightarrow{r})$ igual a cero, el momento también es cero.",
        respuesta_P2 = "",
        ),

    Theory(#8
        code = 2100080, 
        no_pregunta = 8,
        topic = "Momento",
        subtopic = "Momento",
        enunciado ="""
        Para calcular la magnitud del momento generado por la fuerza $F$ respecto al poste $OL$, se realiza el siguiente procedimiento:
        
        1. Se calcula el momento generado por la fuerza en el punto $L$: $(\\overrightarrow{{M_L}})$.
        2. Se determina el vector unitario del eje $OL$: $\\overrightarrow{{\\lambda_{{OL}}}}$.
        3. Se proyecta el momento $\\overrightarrow{{M_L}}$ sobre el eje $\\overrightarrow{{\\lambda_{{OL}}}}$ utilizando el producto punto.

        Con base en este procedimiento, se puede afirmar que:
        """,
        opcion_1 = "Es incorrecto. En el paso 1, el momento debe calcularse con respecto al origen.",
        opcion_2 = "Es correcto. Los pasos descritos permiten hallar la magnitud del momento de la fuerza $F$ respecto al eje $OL$.",
        opcion_3 = "Es incorrecto. En el paso 2, no es necesario calcular el vector unitario del eje.", 
        opcion_4 = "Es incorrecto. En el paso 3, se debe utilizar el producto cruz para realizar la proyección.",
        opcion_correcta = "Es correcto. Los pasos descritos permiten hallar la magnitud del momento de la fuerza $F$ respecto al eje $OL$.",
        respuesta_P1 = """
        El procedimiento descrito es correcto para calcular la magnitud del momento de una fuerza respecto a un eje. Primero se determina el vector momento respecto a un punto del eje (en este caso, el punto $L$). Luego, se obtiene el vector unitario del eje para definir su dirección. Finalmente, se proyecta el momento sobre ese eje utilizando el producto punto: 

        $\\overrightarrow{{M_OL}} = \\overrightarrow{M_L} \\cdot \\overrightarrow{\\lambda_{OL}}$

        Esto proporciona la magnitud del momento de la fuerza en la dirección del eje $OL$.""",
        respuesta_P2 = "",
        ),
             
             

    #--------------------------------------------------- Incertidumbre ----------------------------------------------------------
    #-------------------------------------------------       31000#0      ---------------------------------------------------
    Theory(#1
        code = 3100010, 
        no_pregunta = 1,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        enunciado ="Considere que la cuerda $AB$ de la Figura 1 está sometida a una tensión de $800$ $N$. Según el histograma de frecuencia relativa acumulada de la Figura 2, indique cuál es la probabilidad de que la cuerda falle.", 
        opcion_1 = "$0.5$, correspondiente al área bajo la curva acumulada hasta $800$ $N$.",
        opcion_2 = "$0.45$, correspondiente a 1 menos el área bajo la curva hasta $800$ $N$.",
        opcion_3 = "$0.4$, correspondiente a la probabilidad de ocurrencia.",
        opcion_4 = "$0.6$, correspondiente a la probabilidad de excedencia.",
        opcion_correcta = "$0.4$, correspondiente a la probabilidad de ocurrencia.",
        respuesta_P1 = "La probabilidad de falla es $0.4$, correspondiente a la probabilidad de que la resistencia de la cuerda sea menor que la carga aplicada de $800$ $N$. Esta probabilidad, es la probabilidad de ocurrencia que es dada directamente por el histograma de frecuencia acumulada.",
        respuesta_P2 = "",
        ),

    Theory(#2
        code = 3100020, 
        no_pregunta = 2,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        enunciado ="¿Cuál es una característica de la función de densidad de probabilidad (FDP)?", 
        opcion_1 = "Su valor máximo siempre es 1.",
        opcion_2 = "El área bajo la curva es igual a 1.",
        opcion_3 = "El rango de la función puede ser negativo.",
        opcion_4 = "Siempre es simétrica.",
        opcion_correcta = "El área bajo la curva es igual a 1.",
        respuesta_P1 = "Una función de densidad de probabilidad (FDP) describe la distribución de los valores de una variable aleatoria continua. Una de sus propiedades clave es que el área total bajo la curva de la FDP es igual a 1, ya que esta área representa la probabilidad total de todos los eventos posibles, la cual debe ser 100%.",
        respuesta_P2 = "",
        ),

    Theory(#3
        code = 3100030, 
        no_pregunta = 3,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        enunciado ="¿Cuál de las siguientes afirmaciones es verdadera con respecto a obtener la probabilidad a partir de la función de densidad de probabilidad y la función de distribución acumulada?", 
        opcion_1 = "Para la función de densidad, la probabilidad se obtiene directamente del eje y. Para la distribución acumulada, la probabilidad se obtiene a partir del área bajo la curva.",
        opcion_2 = "Para la función de densidad, no se puede obtener la probabilidad. Para la distribución acumulada, la probabilidad se obtiene directamente del eje y.",
        opcion_3 = "Para la función de densidad, la probabilidad se obtiene a partir del área bajo la curva. Para la distribución acumulada, no se puede obtener la probabilidad.",
        opcion_4 = "Para la función de densidad, la probabilidad se obtiene a partir del área bajo la curva. Para la distribución acumulada, la probabilidad se obtiene directamente del eje y.",
        opcion_correcta = "Para la función de densidad, la probabilidad se obtiene a partir del área bajo la curva. Para la distribución acumulada, la probabilidad se obtiene directamente del eje y.",
        respuesta_P1 = """
        La función de distribución acumulada muestra directamente la probabilidad de que una variable aleatoria tome un valor menor o igual a una variable determinada. Por ello, su valor en el eje Y representa la probabilidad acumulada hasta ese punto, y su máximo es 1.

        En cambio, la función de densidad de probabilidad no entrega directamente la probabilidad en un punto, sino que indica qué tan probable es un valor relativo a otros. La probabilidad de un intervalo se obtiene calculando el área bajo la curva en ese rango.""",
        respuesta_P2 = "",
        ),

    Theory(#4
        code = 3100040, 
        no_pregunta = 4,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        enunciado ="Considere la siguiente figura. ¿Cuál es forma correcta de determinar la probabilidad de que la tensión máxima resistida sea menor o igual a 850 N?", 
        opcion_1 = "La probabilidad es el valor de Y para 850 N.",
        opcion_2 = "La probabilidad es el área total bajo la curva menos el Y para 850 N.",
        opcion_3 = "La probabilidad es la suma acumulada de la frecuencia relativa en el dominio desde 0 hasta 850.",
        opcion_4 = "La probabilidad es el área total bajo la curva menos la suma acumulada de la frecuencia relativa en el dominio desde 0 hasta 850.",
        opcion_correcta = "La probabilidad es el valor de Y para 850 N.",
        respuesta_P1 = "El histograma de frecuencia relativa acumulada proporciona la probabilidad de ocurrencia, es decir, la probabilidad de que la Tensión máxima resistida sea menor o igual a un valor determinado. Por lo tanto, en este caso se busca el valor en el eje Y correspondiente a 850 N (0.7).",
        respuesta_P2 = "",
        ),

    Theory(#5
        code = 3100050, 
        no_pregunta = 5,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        enunciado ="Considere la siguiente figura. ¿Cuál es la probabilidad de que la tensión máxima resistida sea mayor a 900 N?", 
        opcion_1 = "La probabilidad es el valor de Y en ese punto (0.2).",
        opcion_2 = "La probabilidad es el área total bajo la curva menos el Y en ese punto (0.8).",
        opcion_3 = "La probabilidad es la suma acumulada de la frecuencia relativa en el dominio desde 0 hasta 900 (0.9).",
        opcion_4 = "La probabilidad es el área total bajo la curva menos la suma acumulada de la frecuencia relativa en el dominio desde 0 hasta 900 (0.1).",
        opcion_correcta = "La probabilidad es el área total bajo la curva menos la suma acumulada de la frecuencia relativa en el dominio desde 0 hasta 900 (0.1).",
        respuesta_P1 = """
        La probabilidad de que la tensión máxima resistida sea mayor o igual a 900 N es equivalente a la probabilidad de excedencia, es decir, la probabilidad con la que se excede el valor de 900 N. La probabilidad de excedencia se calcula como:

        $\\text{{Probabilidad de excedencia}}$ = $1$ - $\\text{{Probabilidad de ocurrencia}}$

        1 hace referencia al área total bajo la curva y la probabilidad de ocurrencia es la suma acumulada de la frecuencia relativa en el dominio desde 0 hasta 900 de la función (0.1).
        """,
        respuesta_P2 = "",
        ),

    Theory(#6
        code = 3100060, 
        no_pregunta = 6,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        enunciado ="¿Qué valor toma la función de distribución acumulada (FDA) en el extremo derecho de su dominio?", 
        opcion_1 = "-1",
        opcion_2 = "1",
        opcion_3 = "0.5",
        opcion_4 = "Un valor entre 0 y 1.",
        opcion_correcta = "1",
        respuesta_P1 = "El valor máximo de la función de distribución acumulada (FDA) es 1, dado que, esta se construye sumando (acumulando) las probabilidades de todos los posibles valores que puede tomar la variable aleatoria.",
        respuesta_P2 = "",
        ),



    #-------------------------------------------------  Sistemas equivalentes ---------------------------------------------------
    #-------------------------------------------------       41000##0         ---------------------------------------------------
    Theory(#1
        code = 4100010, 
        no_pregunta = 1,
        topic = "Sistemas equivalentes",
        subtopic = "Sistemas equivalentes",
        enunciado ="Dos sistemas de fuerzas se consideran equivalentes cuando:", 
        opcion_1 = "Tienen el mismo número de fuerzas con igual magnitud pero diferente ubicación.",
        opcion_2 = "Actúan sobre cuerpos con la misma geometría.",
        opcion_3 = "Tienen la misma fuerza resultante y el mismo momento en cualquier punto del cuerpo.",
        opcion_4 = "La sumatoria de las fuerzas resultantes de cada sistema es igual a cero. ",
        opcion_correcta = "Tienen la misma fuerza resultante y el mismo momento en cualquier punto del cuerpo.",
        respuesta_P1 = "Dos sistemas son equivalentes si, generan la misma fuerza resultante y el mismo momento respecto a un punto dado. Esto significa que, el efecto global de los dos sistemas sobre el cuerpo es idéntico.",
        respuesta_P2 = "",
        ),

    # Theory(#2
    #     code = 4100020, 
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
    #     code = 4100030, 
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
    #     code = 4100040, 
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


    # #------------------------------------------------------ Apoyos ----------------------------------------------------------
    # #-------------------------------------------------    51000##0       ---------------------------------------------------
    # Theory(#1
    #     code = 5100010, 
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
    #     code = 5100030, 
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

    Theory(#4
        code = 5100040, 
        no_pregunta = 4,
        topic = "Apoyos y reacciones",
        subtopic = "Apoyos y reacciones",
        enunciado = "¿Cuáles reacciones genera un apoyo empotrado en un estructura bidimensional?",
        opcion_1 = "Una fuerza.",
        opcion_2 = "Dos fuerzas y un momento.",
        opcion_3 = "Dos fuerzas sin momento.",
        opcion_4 = "Un momento.",
        opcion_correcta = "Dos fuerzas y un momento.",
        respuesta_P1 = "Un apoyo empotrado en una estructura bidimensional es un apoyo de tercer grado. Este tipo de apoyo restringe todos los movimientos del cuerpo, es decir, impide la traslación (horizontal y vertical) y la rotación. Debido a esto, genera dos reacciones (horizontal y vertical) y un momento.",
        respuesta_P2 = "",
        ),
                 

    #-----------------------------------------------------  Armaduras ----------------------------------------------------------
    #------------------------------------------------------  Cerchas -----------------------------------------------------------
    #-------------------------------------------------      61000##0         ---------------------------------------------------
    # Theory(#1
    #     code = 6100010, 
    #     no_pregunta = 1,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Cerchas",
    #     enunciado ="¿Cuáles de las siguientes son las hipótesis de diseño de armaduras o cerchas?", 
    #     opcion_1 = "Todas las cargas se aplican en los nodos y no existe fricción en las uniones.",
    #     opcion_2 = "Las cargas se alican en los nodos en elemento horizontales y verticales. Y, en elementos inclinados se aplican en el centro del elemento.",
    #     opcion_3 = "Todas las cargas se aplican en el centro de los elementos y no existe fricción en las uniones.",
    #     opcion_4 = "Todas las cargas se aplican en los nodos y existe fricción en las uniones.",
    #     opcion_correcta =  "Todas las cargas se aplican en los nodos y no existe fricción en las uniones.",
    #     respuesta_P1 = " ",
    #     respuesta_P2 = "",
    #     ),

    # Theory(#2
    #     code = 6100020, 
    #     no_pregunta = 2,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Cerchas",
    #     enunciado ="¿Cuál es la condición básica para que una cercha sea estáticamente determinada?", 
    #     opcion_1 = "El número de elementos debe ser igual al número de nodos.",
    #     opcion_2 = "El número de elementos debe ser mayor que el número de nodos.",
    #     opcion_3 = "El número de elementos debe ser igual a 2n−3.",
    #     opcion_4 = "El número de nodos debe ser igual al número de apoyos.",
    #     opcion_correcta = "El número de elementos debe ser igual a 2n−3.",
    #     respuesta_P1 = "Para que una cercha sea estáticamente determinada, el número de barras debe cumplir la ecuación m=2n−3, donde m es el número de barras y n es el número de nodos. Esta relación asegura que la estructura puede analizarse usando las ecuaciones de equilibrio sin necesidad de recurrir a métodos avanzados de análisis.",
    #     respuesta_P2 = "",
    #     ),

    # Theory(#3
    #     code = 6100030, 
    #     no_pregunta = 3,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Cerchas",
    #     enunciado ="Convencionalmente se dice que un elemento está en tensión cuando:", 
    #     opcion_1 = " ",
    #     opcion_2 = "Las flechas en los extremos apuntan hacia fuera del elemento generando el alargamiento del elemento.",
    #     opcion_3 = " ",
    #     opcion_4 = " ",
    #     opcion_correcta = "Las flechas en los extremos apuntan hacia fuera del elemento generando el alargamiento del elemento.",
    #     respuesta_P1 = """ """,
    #     respuesta_P2 = "",
    #     ),
                     
    # Theory(#4
    #     code = 6100040, 
    #     no_pregunta = 4,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Cerchas",
    #     enunciado ="Convencionalmente se dice que un elemento está en compresión cuando:", 
    #     opcion_1 = " ",
    #     opcion_2 = " ",
    #     opcion_3 = " ",
    #     opcion_4 = "Las flechas en los extremos apuntan hacia el elemento generando el acortamiento del elemento.",
    #     opcion_correcta = "Las flechas en los extremos apuntan hacia el elemento generando el acortamiento del elemento.",
    #     respuesta_P1 = """ """,
    #     respuesta_P2 = "",
    #     ),
                     
    # Theory(#5
    #     code = 6100050, 
    #     no_pregunta = 5,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Cerchas",
    #     enunciado =""""
    #     Cuáles de las siguientes afirmaciones son verdaderas:
    #         I.	Si una armadura es estable sus nodos están en equilibrio.
    #         II.	Para analizar cerchas deben conocerse las reacciones
    #         III.	En los nodos el momento siempre es 0. En 2d Las fuerzas son coplanares y concurrentes. Solo se hacen sumatorias de fuerzas para determinar el equilibrio 
    #     """, 
    #     opcion_1 = " ",
    #     opcion_2 = " ",
    #     opcion_3 = " ",
    #     opcion_4 = " ",
    #     opcion_correcta = " ",
    #     respuesta_P1 = """ """,
    #     respuesta_P2 = "",
    #     ),
                         
    # Theory(#6
    #     code = 6100060, 
    #     no_pregunta = 6,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Cerchas",
    #     enunciado ="Cuando se hace el diagrama de cuerpo libre de un nodo una recomendación es:", 
    #     opcion_1 = " ",
    #     opcion_2 = " ",
    #     opcion_3 = "Imaginar que las fuerzas están saliendo del nodo.",
    #     opcion_4 = " ",
    #     opcion_correcta = "Las flechas en los extremos apuntan hacia el elemento generando el acortamiento del elemento.",
    #     respuesta_P1 = """De esta forma, si el escalar da positivo es correcto asumir que el elemento está a tensión y si da negativo, se sabe que el elemento está en compresión. """,
    #     respuesta_P2 = "",
    #     ),

    # Theory(#7
    #     code = 6100070, 
    #     no_pregunta = 7,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Cerchas",
    #     enunciado ="Un elemento de la cercha es de fuerza cero cuando:", 
    #     opcion_1 = " ",
    #     opcion_2 = " ",
    #     opcion_3 = "Imaginar que las fuerzas están saliendo del nodo.",
    #     opcion_4 = " ",
    #     opcion_correcta = "Las flechas en los extremos apuntan hacia el elemento generando el acortamiento del elemento.",
    #     respuesta_P1 = """De esta forma, si el escalar da positivo es correcto asumir que el elemento está a tensión y si da negativo, se sabe que el elemento está en compresión. """,
    #     respuesta_P2 = "",
    #     ),                 


#-----------------------------------------------------  Armaduras ----------------------------------------------------------
#------------------------------------------------------  Marcos -----------------------------------------------------------
#-------------------------------------------------      62000##0         ---------------------------------------------------


#------------------------------------------------------  Centroides-----------------------------------------------------------
#-------------------------------------------------       71000#0         ---------------------------------------------------
    Theory(#1
        code = 7100010, 
        no_pregunta = 1,
        topic = "Centroides",
        subtopic = "Centroides",
        enunciado ="¿Qué es el centroide de un cuerpo?", 
        opcion_1 = "Es el punto de simetría de la masa total de un cuerpo.",
        opcion_2 = "Es el punto que divide el área de un cuerpo en dos partes iguales.",
        opcion_3 = "Es el punto donde el cuerpo no siente la aplicación de fuerzas externas.",
        opcion_4 = "Es el punto medio geométrico de un cuerpo.",
        opcion_correcta =  "Es el punto medio geométrico de un cuerpo.",
        respuesta_P1 = "El centroide es un punto en el cual se considera que está concentrado toda el área o volumen del cuerpo, sin tener en cuenta la densidad o la masa. Por lo tanto, está determinado únicamente por su forma y dimensiones.",
        respuesta_P2 = "",
        ),

    Theory(#2
        code = 7100020, 
        no_pregunta = 2,
        topic = "Centroides",
        subtopic = "Centroides",
        enunciado ="Para calcular el centroide de un cuerpo compuesto por figuras comunes, se debe:", 
        opcion_1 = "Promediar el área o volumen de cada una de las figuras conocidas del cuerpo.",
        opcion_2 = "Promediar las coordenadas de los centroides de cada una de las figuras conocidas del cuerpo.",
        opcion_3 = "Realizar la suma producto entre los centroides y áreas de cada una de las figuras.",
        opcion_4 = "Calcular el centroide de cada figura, ponderarlo por el área o volumen respectivo, y luego dividir la suma de estos productos entre el área o volumen total del cuerpo.",
        opcion_correcta = "Calcular el centroide de cada figura, ponderarlo por el área o volumen respectivo, y luego dividir la suma de estos productos entre el área o volumen total del cuerpo.",
        respuesta_P1 = """
        Las coordenadas del centroide de una figura compuesta bidimensional se pueden calcular mediante las siguientes expresiones:      
        
        $\\bar{{X}} = \\dfrac{{\\sum{{\\bar{{X_i}} \\cdot A_i}}}}{{\\sum{{A_i}}}}$      

        $\\bar{{Y}} = \\dfrac{{\\sum{{\\bar{{Y_i}} \\cdot A_i}}}}{{\\sum{{A_i}}}}$         

        Donde:           
        $\\bar{{X}}$ = Coordenada X del centroide de la figura compuesta.              
        $\\bar{{Y}}$ = Coordenada Y del centroide de la figura compuesta.              
        $i$ = Índice que representa cada una de las partes en las que se ha dividido la figura compuesta.                 
        $A$ = Área de la figura. 

        Para el caso de un cuerpo tridimensional, el cálculo se realiza ponderando cada centroide con el volumen de cada figura en lugar del área, y se divide entre el volumen total del cuerpo.                 
        
        Esta ecuación proviene de la igualdad de momentos de dos sistemas equivalentes, es decir, el momento que ejerce cada una de las figuras respecto a un eje de referencia es equivalente al momento que realiza todo el cuerpo respecto a dicho eje de referencia.         
        """,
        respuesta_P2 = "",
        ),

    Theory(#3
        code = 7100030, 
        no_pregunta = 3,
        topic = "Centroides",
        subtopic = "Centroides",
        enunciado ="¿Cuál es la principal diferencia entre el centroide y el centro de masa de un objeto?", 
        opcion_1 = "El centro de masa es siempre el mismo que el centroide.",
        opcion_2 = "El centroide es el centro geométrico y el centro de masa es el centro de distribución de la masa.",
        opcion_3 = "El centroide es el punto medio de equilibrio y el centro de masa depende de las dimensiones.",
        opcion_4 = "El centroide depende de la forma y material, mientras que el centro de masa es el punto de gravedad del cuerpo.",
        opcion_correcta = "El centroide es el centro geométrico y el centro de masa es el centro de distribución de la masa.",
        respuesta_P1 = """El centroide es el punto de simetría geométrico de un objeto, por lo tanto, depende de su forma y dimensiones. Por el contrario, el centro de masa, depende de la distribución de la masa en el objeto.
        Esto quiere decir, que en una figura compuesta por varios distintos materiales, el centroide no coincidirá necesariamente con el centro de masa.""",
        respuesta_P2 = "",
        ),

    Theory(#4
        code = 7100040, 
        no_pregunta = 4,
        topic = "Centroides",
        subtopic = "Centroides",
        enunciado ="Para una placa de densidad constante y forma regular, ¿cómo se relacionan el centroide y el centro de masa?", 
        opcion_1 = "Las coordenadas del centroide y el centro de masa coinciden únicamente en uno de los ejes de referencia.",
        opcion_2 = "El centroide y el centro de masa no coinciden.",
        opcion_3 = "Son idénticos porque la densidad es constante.",
        opcion_4 = "Son idénticos porque la forma es regular.",
        opcion_correcta = "Son idénticos porque la densidad es constante.",
        respuesta_P1 = "En un objeto de densidad constante y forma uniforme, el centroide y el centro de masa coinciden. Dado que, la distribución de la masa es homogénea y se distribuye uniformemente respecto a la geometría del objeto.",
        respuesta_P2 = "",
        ),

    Theory(#5
        code = 7100050, 
        no_pregunta = 5,
        topic = "Centroides",
        subtopic = "Centroides",
        enunciado ="""
        ¿Cuáles de las siguientes afirmaciones son verdaderas?:   

        I.	En un cuerpo compuesto, los centroides de cada figura que lo conforma se deben calcular con respecto al mismo eje de referencia.    
        II.	El centroide de un cuerpo puede estar localizado fuera de él.     
        III. El centro de gravedad está localizado en la zona de mayor peso del objeto.     
        """, 
        opcion_1 = " I, III",
        opcion_2 = "Solamente II",
        opcion_3 = "Solamente I.",
        opcion_4 = "Todas son correctas.",
        opcion_correcta = "Todas son correctas.",
        respuesta_P1 = """
        Todas las afirmaciones son correctas:   

        I. Los centroides de las figuras que conforman un cuerpo compuesto se calculan con respecto al mismo eje de referencia.      
        II. El centroide de un cuerpo puede estar localizado fuera de él, particularmente, si esté es de forma irregular o tiene cavidades.       
        III. El centro de gravedad depende del peso (W) de la figura, el cual está influenciado por la gravedad.     
        """,
        respuesta_P2 = "",
        ),     
        
    Theory(#6
        code = 7100060, 
        no_pregunta = 6,
        topic = "Centroides",
        subtopic = "Centroides",
        enunciado ="¿Cuál es la expresión correcta para calcular el centroide en X de la parábola mostrada en la figura?", 
        opcion_1 = """$\\bar{{X}}=\\dfrac{{\\int_0^6 x^2 \\cdot x^2 dx}}{{\\int_0^6{{x^2 dx}}}}$ \\
        $\\text{{    }}$""",
        opcion_2 = """$\\bar{{X}}=\\dfrac{{\\int_0^6 x \\cdot x^2 dx}}{{\\int_0^6{{x dx}}}}$ \\
        $\\text{{    }}$""",
        opcion_3 = """$\\bar{{X}}=\\dfrac{{\\int_0^6 \\dfrac{{x}}{{2}} \\cdot x^2 dx}}{{\\int_0^6{{x^2 dx}}}}$ \\
        $\\text{{    }}$""",
        opcion_4 = """$\\bar{{X}}=\\dfrac{{\\int_0^6 x \\cdot x^2 dx}}{{\\int_0^6{{x^2 dx}}}}$ \\
        $\\text{{    }}$""",
        opcion_correcta = """$\\bar{{X}}=\\dfrac{{\\int_0^6 x \\cdot x^2 dx}}{{\\int_0^6{{x^2 dx}}}}$ \\
        $\\text{{    }}$""",
        respuesta_P1 = """
        Para calcular el centroide de la parábola, se define un elemento diferencial y se aplica la fórmula:   

        $\\bar{{X}}=\\dfrac{{\\int_{{R(x)}}x dA}}{{\\int_{{R(x)}}{{dA}}}}$
        
        El elemento diferencial se definió de la siguiente forma:""",
        respuesta_P2 = """
        Reemplazando en la fórmula, la expresión para calcular el centroide en X de la parábola es:

        $\\bar{{X}}=\\dfrac{{\\int_0^6 x \\cdot x^2 dx}}{{\\int_0^6{{x^2 dx}}}}$
        """,
        ),      
    
    Theory(#7
        code = 7100070, 
        no_pregunta = 7,
        topic = "Centroides",
        subtopic = "Centroides",
        enunciado ="Considere la siguiente figura e indique cuál es su centroide en $x$ con respecto al origen:", 
        opcion_1 = """$\\bar{{x}}=\\dfrac{{1 \\cdot (2)}}{{3}}$ \\
        $\\text{{    }}$""",
        opcion_2 = """$\\bar{{x}}=\\dfrac{{\\int_{{0}}^{{2}}x dx}}{{2}}$ \\
        $\\text{{    }}$""",
        opcion_3 = """$\\bar{{x}}=\\dfrac{{2 \\cdot (2)}}{{3}}$ \\
        $\\text{{    }}$""",
        opcion_4 = """$\\bar{{x}}=\\dfrac{{\\int_{{0}}^{{2}}x^3 dx}}{{2}}$ \\
        $\\text{{    }}$""",
        opcion_correcta = """$\\bar{{x}}=\\dfrac{{2 \\cdot (2)}}{{3}}$ \\
        $\\text{{    }}$""",
        respuesta_P1 = """En este caso, la línea recta forma un triángulo con base 2. El centroide de un triángulo rectángulo se ubica a una distancia de $\\dfrac{{1}}{{3}}$ de la base si se mide desde el vértice del ángulo recto, y a $\\dfrac{{2}}{{3}}$ si se mide desde el vértice del ángulo agudo, como ocurre en esta situación.""",
        respuesta_P2 = "",
        ),
    
    Theory(#9
        code = 7100090, 
        no_pregunta = 9,
        topic = "Centroides",
        subtopic = "Centroides",
        enunciado ="¿Dónde se encuentra el centro de masa de la placa compuesta mostrada en la siguiente figura?", 
        opcion_1 = "En el eje $y$, se ubica en $h/2$; en el eje $x$, en $b/2$.",
        opcion_2 = "En el eje $y$, se ubica en $h/2$; en el eje $x$, se ubica más cerca del lado de la madera.",
        opcion_3 = "En el eje $y$, se ubica en $h/2$; y en el eje $x$, se ubica más cerca del lado del acero.",
        opcion_4 = "En el eje $y$, se ubica en la base; y en el eje $x$, se ubica más cerca del lado del acero.",
        opcion_correcta = "En el eje $y$, se ubica en $h/2$; y en el eje $x$, se ubica más cerca del lado del acero.",
        respuesta_P1 = "El centro de masa de un sistema compuesto se encuentra más cerca del material que aporta mayor masa. En este caso, aunque la madera y el acero tienen el mismo volumen, el acero tiene mayor densidad, por lo que su contribución de masa es mayor. Por ello, el centro de masa se ubicará hacia el lado del acero, manteniéndose a $h/2$ sobre el eje y ya que ambas mitades tienen igual altura.",
        respuesta_P2 = "",
        ),
    
    Theory(#10
        code = 7100100, 
        no_pregunta = 10,
        topic = "Centroides",
        subtopic = "Centroides",
        enunciado = "Considere el cilindro compuesto por dos materiales distribuidos equitativamente en volumen (50% y 50%). Si el material de la mitad inferior tiene una mayor densidad que el de la mitad superior, ¿cuál de las siguientes afirmaciones describe correctamente la ubicación del centro de masa?", 
        opcion_1 = "El centro de masa se ubicará en el centro geométrico del cilindro.",
        opcion_2 = "El centro de masa estará más cerca de la sección superior del cilindro.",
        opcion_3 = "El centro de masa estará más cerca de la sección inferior del cilindro.",
        opcion_4 = "El centro de masa coincidirá con la línea divisoria entre los dos materiales.",
        opcion_correcta = "El centro de masa estará más cerca de la sección inferior del cilindro.",
        respuesta_P1 = """El centro de masa se desplaza hacia la región con mayor densidad, ya que esta concentra más masa en el mismo volumen. En este caso, como el material inferior es más denso, el centro de masa se ubicará por debajo del centro geométrico, más cerca de la sección inferior del cilindro.""",
        respuesta_P2 = "",
        ),

#---------------------------------------------- Fuerzas distribuidas ----------------------------------
#----------------------------------------------------- Vigas ------------------------------------------
#-------------------------------------------------   81000##0   ---------------------------------------
    
    Theory(#1
        code = 8100010, 
        no_pregunta = 1,
        topic = "Fuerzas distribuidas",
        subtopic = "Vigas",
        enunciado = "¿Cuál es la reacción en cada uno de los apoyos debido al peso propio del puente de luz $(L)$ simplemente apoyado?.", 
        opcion_1 = """$W \\cdot L$ \\
        $\\text{{    }}$""",
        opcion_2 = """$\\dfrac{{W \\cdot L}}{{4}}$ \\
        $\\text{{    }}$""",
        opcion_3 = """$\\dfrac{{W \\cdot L}}{{2}}$ \\
        $\\text{{    }}$""",
        opcion_4 = """$\\dfrac{{3 \\cdot W \\cdot L}}{{4}}$ \\
        $\\text{{    }}$""",
        opcion_correcta = """$\\dfrac{{W \\cdot L}}{{2}}$ \\
        $\\text{{    }}$""",
        respuesta_P1 = "Para una carga uniformemente distribuida sobre una viga simplemente apoyada, la carga total se distribuye equitativamente entre los dos soportes. En este caso la carga total es $W \\cdot L$, por lo tanto, cada apoyo soporta la mitad de esta carga, $\\left(\\dfrac{{W \\cdot L}}{{2}} \\right)$.",
        respuesta_P2 = "",
        ),

    Theory(#2
        code = 8100020, 
        no_pregunta = 2,
        topic = "Fuerzas distribuidas",
        subtopic = "Vigas",
        enunciado =" La fuerza distribuida mostrada en la figura es equivalente a una fuerza puntual de magnitud:",    
        opcion_1 = """$(W_2 - W_1) \\cdot L $ \\
        $\\text{{    }}$""",
        opcion_2 = """$W_1 \\cdot x + (W_2 - W_1) \\cdot x $ \\
        $\\text{{    }}$""",
        opcion_3 = """$(W_2 - W_1) \\cdot x $ \\
        $\\text{{    }}$""",
        opcion_4 = """$\\dfrac{{W_2+W_1}}{{2}} \\cdot x$ \\
        $\\text{{    }}$""",
        opcion_correcta = """$\\dfrac{{W_2+W_1}}{{2}} \\cdot x$ \\
        $\\text{{    }}$""",
        respuesta_P1 = """
        Se puede calcular una fuerza puntual a partir de una fuerza distribuida calculando el área de esta. En este caso, la fuerza puntual puede determinarse como el área del trapecio con base $x$, o se puede dividir la figura en partes más simple cuyos resultados se pueden sumar:

        Área del trapecio:

        $\\dfrac{{W_2+W_1}}{{2}} \\cdot x$

        División en un rectángulo de altura $W_1$ y base $x$, y un triángulo de altura $(W_2-W_1)$ y base $x$:    
        
        $W_1 \\cdot x + \\dfrac{{(W_2-W_1) \\cdot x}}{{2}}$

        Al simplificar la anterior expresión, se obtiene la misma área del trapecio.        
        """,
        respuesta_P2 = "",
        ),
        
    Theory(#3
        code = 8100030, 
        no_pregunta = 3,
        topic = "Fuerzas distribuidas",
        subtopic = "Vigas",
        enunciado ="Considerando la siguiente figura, ¿Cómo se puede determinar una fuerza puntual equivalente para la carga distribuida?", 
        opcion_1 = "Dividir la fuerza distribuida en figuras comunes y conocidas.",
        opcion_2 = "Integrar la función f(x).",
        opcion_3 = "Restar el producto entre L y la mayor magnitud de la carga distribuida con el producto entre L y la menor magnitud de la carga distribuida. ",
        opcion_4 = "Multiplicar L por el promedio de las magnitudes de la carga distribuida. ",
        opcion_correcta = "Integrar la función f(x).",
        respuesta_P1 = "Para cargas distribuidas descritas por funciones, la fuerza puntual equivalente se calcula como la integral definida de la función, la cual representa el área bajo la curva.",
        respuesta_P2 = "",
        ),
    
    Theory(#4
        code = 8100040, 
        no_pregunta = 4,
        topic = "Fuerzas distribuidas",
        subtopic = "Vigas",
        enunciado ="La ubicación de una fuerza puntual equivalente para una carga distribuida es:", 
        opcion_1 = "El punto medio de la carga distribuida.",
        opcion_2 = "El centroide de la carga distribuida.",
        opcion_3 = "En un punto sobre la línea de acción de la carga, de forma que no genere momento.",
        opcion_4 = "En el punto donde la carga distribuida es máxima.",
        opcion_correcta = "El centroide de la carga distribuida.",
        respuesta_P1 = "El centroide de una carga distribuida corresponde al punto de aplicación de su representación puntual. De esta manera, se garantiza un sistema equivalente a la carga original.",
        respuesta_P2 = "",
        ),
    
    Theory(#5
        code = 8100050, 
        no_pregunta = 5,
        topic = "Fuerzas distribuidas",
        subtopic = "Vigas",
        enunciado ="Si una carga distribuida uniformemente se convierte en una carga triangular manteniendo la misma fuerza total, ¿cómo se ve afectado el momento generado con respecto al apoyo A?", 
        opcion_1 = "Disminuye, porque la fuerza se aplica más cerca del apoyo.",
        opcion_2 = "Aumenta, porque la distribución uniforme tiene una menor distancia al apoyo.",
        opcion_3 = "Aumenta, porque la forma triangular concentra más carga.",
        opcion_4 = "Permanece igual, porque la carga total no cambia.",
        opcion_correcta = "Disminuye, porque la fuerza se aplica más cerca del apoyo.",
        respuesta_P1 = """Aunque ambas distribuciones tienen la misma fuerza total (área bajo la curva), el punto de aplicación de la fuerza cambia el momento.
        En la carga uniforme, la fuerza equivalente actúa en el centro del tramo.
        En cambio, en la carga triangular, la fuerza resultante se aplica más cerca del apoyo A (a $1/3$ de la base desde el ángulo recto), lo que reduce la distancia al punto de evaluación y, por tanto, el momento generado disminuye.""",
        respuesta_P2 = "",
        ),

    Theory(#6
        code = 8100060, 
        no_pregunta = 6,
        topic = "Fuerzas distribuidas",
        subtopic = "Vigas",
        enunciado ="Considere la viga sometida a una carga distribuida que varía de uniforme a triangular. ¿Dónde se debe localizar el apoyo A para garantizar el equilibrio de la viga?", 
        opcion_1 = "En el punto de transición entre la carga uniforme y la carga triangular.",
        opcion_2 = "En el centroide de la carga distribuida.",
        opcion_3 = "En la zona donde la carga es mayor.",
        opcion_4 = "En el punto donde se genera el mayor momento sobre la viga.",
        opcion_correcta = "En el centroide de la carga distribuida.",
        respuesta_P1 = """En este caso, la carga distribuida tiene una forma variable, comenzando como uniforme y terminando como triangular. Para equilibrar la viga, el apoyo debe colocarse en el centroide de la carga distribuida, que es el punto en el que se puede considerar que toda la carga total actúa como una carga concentrada.""",
        respuesta_P2 = "",
        ),


#---------------------------------------------- Fuerzas distribuidas ----------------------------------
#---------------------------------------------- Presión hidrostática ----------------------------------
#-------------------------------------------------   82000##0    --------------------------------------

    Theory(#1
        code = 8200010, 
        no_pregunta = 1,
        topic = "Fuerzas distribuidas",
        subtopic = "Presión hidrostática",
        enunciado ="Considere la siguiente figura. ¿Cuál de las configuraciones mostradas presenta la mayor y la menor presión hidrostática, respectivamente?", 
        opcion_1 = "$II$, $I$",
        opcion_2 = "$II$, $III$",
        opcion_3 = "$IV$, $I$",
        opcion_4 = "$IV$, $III$",
        opcion_correcta = "$IV$, $I$",
        respuesta_P1 = "La configuración con la mayor presión hidrostática es la $IV$, mientras que la configuración con la menor presión hidrostática es la $I$. Dado que, a mayor densidad del fluido, mayor será la presión ejercida. Además, en condiciones de igual altura sumergida, las paredes inclinadas experimentan una mayor presión debido al componente del peso del agua que actúa sobre la inclinación.",
        respuesta_P2 = "",
        ),

    Theory(#2
        code = 8200020, 
        no_pregunta = 2,
        topic = "Fuerzas distribuidas",
        subtopic = "Presión hidrostática",
        enunciado =""" 
        ¿Cuál(es) de la(s) siguiente(s) opcion(es) es(son) correcta(s)?:  

        I. la presión es una carga distribuida perpendicular a la superficie.    
        II. Las presiones hidrostáticas para una superficie lineal son una fuerza distribuida triangular.    
        III. Si la altura del agua es mayor a la altura del muro, es decir, el muro está sumergido, debe tenerse en cuenta el peso de la columna de agua sobre él.     
        IV.  Para simplificar los cálculos, es correcto dividir la presión en componentes; la vertical es el peso del agua y la horizontal la presión del fluido.    
        """, 
        opcion_1 = "I, II y IV",
        opcion_2 = "II y III",
        opcion_3 = "I",
        opcion_4 = "Todas son correctas",
        opcion_correcta = "Todas son correctas",
        respuesta_P1 = """
        Todas las afirmaciones son correctas y deben considerarse en los cálculos:
        
        Para superficies rectas, la representación de la presión hidrostática es una carga distribuida triangular, debido a que la presión aumenta linealmente con la profundidad. Esta presión actúa siempre a 90° de la superficie, por lo tanto, cuando la carga es inclinada se tienen componentes en x, y. La componente en x es la presión hidrostática del fluido representada por una carga distribuida triangular y la componente vertical es el peso del fluido.
        """,
        respuesta_P2 = "",
        ),

    Theory(#3
        code = 8200030, 
        no_pregunta = 3,
        topic = "Fuerzas distribuidas",
        subtopic = "Presión hidrostática",
        enunciado ="Considerando la siguiente figura ¿cuál(es) es(son) el(los) diagrama(s) correcto(s)?", 
        opcion_1 = "Solamente I",
        opcion_2 = "I y II",
        opcion_3 = "I y III",
        opcion_4 = "Solamente II.",
        opcion_correcta = "I y III",
        respuesta_P1 = "Las representaciones correctas son I y III. El diagrama III representa correctamente la presión triangular perpendicular a la superficie y el diagrama I es su forma descompuesta, utilizada como método de cálculo.",
        respuesta_P2 = "",
        ),
    
    Theory(#4
        code = 8200040, 
        no_pregunta = 4,
        topic = "Fuerzas distribuidas",
        subtopic = "Presión hidrostática",
        enunciado = "Al momento de determinar las dimensiones de la base de una presa, ¿cuál de los siguientes criterios garantiza la estabilidad de la estructura?", 
        opcion_1 = "Que los momentos generados por las fuerzas actuantes (presión del agua) y las fuerzas resistentes (peso de la presa) estén en equilibrio.",
        opcion_2 = "Que la sumatoria de momentos en un punto de la presa sea mayor que cero.",
        opcion_3 = "Que la base de la presa sea mayor que la altura del nivel del agua.",
        opcion_4 = "Que la sumatoria de momentos generados por las fuerzas actuantes sea igual a cero.",
        opcion_correcta = "Que los momentos generados por las fuerzas actuantes (presión del agua) y las fuerzas resistentes (peso de la presa) estén en equilibrio.",
        respuesta_P1 = """Para diseñar una presa estable, es fundamental asegurar el equilibrio de momentos entre las fuerzas actuantes (como la presión del agua) y las fuerzas resistentes (como el peso propio de la presa), este equilibrio evita el volcamiento.""",
        respuesta_P2 = "",
        ),

    Theory(#5
        code = 8200050, 
        no_pregunta = 5,
        topic = "Fuerzas distribuidas",
        subtopic = "Presión hidrostática",
        enunciado = "Considere una esfera sumergida en un fluido. ¿Cuál de las siguientes representaciones de la presión sobre la esfera es incorrecta?", 
        opcion_1 = "La representación incorrecta es I. Porque la presión en un fluido actúa únicamente de forma horizontal. ",
        opcion_2 = "La representación incorrecta es II. Porque la presión en un punto sumergido debe actuar perpendicularmente a la superficie, no con ángulos menores a 90°.",
        opcion_3 = "La representación incorrecta es III. Porque la presión en un fluido no solo se ejerce en una dirección horizontal, sino en todas las direcciones perpendiculares a la superficie.",
        opcion_4 = "La representación incorrecta es IV. Porque las flechas representan el peso del fluido y no la presión ejercida sobre el punto.",
        opcion_correcta = "La representación incorrecta es II. Porque la presión en un punto sumergido debe actuar perpendicularmente a la superficie, no con ángulos menores a 90°.",
        respuesta_P1 = """La presión en un fluido se ejerce de manera perpendicular a cualquier superficie en contacto con el fluido. Por lo tanto, la representación incorrecta es II, ya que las flechas están orientadas en un ángulo menor a 90° con respecto a la superficie.""",
        respuesta_P2 = "",
        ),
    
    Theory(#6
        code = 8200060, 
        no_pregunta = 6,
        topic = "Fuerzas distribuidas",
        subtopic = "Presión hidrostática",
        enunciado = "Determine las ecuaciones que describen las componentes vertical $(W)$ y horizontal $(P)$ de la presión del fluido que actúa sobre la compuerta $AB$. Considere el ancho de la compuerta como $1$ y el peso específico del fluido como $\\gamma$.", 
        opcion_1 = """$W = \\gamma \\cdot \\dfrac{{b_1 \\cdot h_2}}{{2}} \\cdot 1$ \\
        $P = \\gamma \\cdot \\dfrac{{(h_2)^2}}{{2}} \\cdot 1$ \\
        $\\text{{    }}$""",
        opcion_2 = """$W = \\gamma \\cdot b_1 \\cdot h_1 \\cdot 1 + \\gamma \\cdot \\dfrac{{b_1 \\cdot h_2}}{{2}} \\cdot 1$ \\
        $P = \\gamma \\cdot \\dfrac{{(h_2)^2}}{{2}} \\cdot 1$ \\
        $\\text{{    }}$""",
        opcion_3 = """$W = \\gamma \\cdot b_1 \\cdot h_1 \\cdot 1 + \\gamma \\cdot \\dfrac{{b_1 \\cdot h_2}}{{2}} \\cdot 1$ \\
        $P = \\gamma \\cdot h_1 \\cdot h_2 \\cdot 1 + \\gamma \\cdot \\dfrac{{(h_2)^2}}{{2}} \\cdot 1$ \\
        $\\text{{    }}$""",
        opcion_4 = """$W = \\gamma \\cdot b_1 \\cdot h_2 \\cdot 1 + \\gamma \\cdot \\dfrac{{b_1 \\cdot h_2}}{{2}} \\cdot 1$ \\
        $P = \\gamma \\cdot h_1 \\cdot h_2 \\cdot 1 + \\gamma \\cdot \\dfrac{{h_1 \\cdot h_2}}{{2}} \\cdot 1$ \\
        $\\text{{    }}$""",
        opcion_correcta = """$W = \\gamma \\cdot b_1 \\cdot h_1 \\cdot 1 + \\gamma \\cdot \\dfrac{{b_1 \\cdot h_2}}{{2}} \\cdot 1$ \\
        $P = \\gamma \\cdot h_1 \\cdot h_2 \\cdot 1 + \\gamma \\cdot \\dfrac{{(h_2)^2}}{{2}} \\cdot 1$ \\
        $\\text{{    }}$""",
        respuesta_P1 = """
        La opción correcta es:

        $W = \\gamma \\cdot b_1 \\cdot h_1 \\cdot 1 + \\gamma \\cdot \\dfrac{{b_1 \\cdot h_2}}{{2}} \\cdot 1$     
        $P = \\gamma \\cdot \\dfrac{{(h_2)^2}}{{2}} \\cdot 1$ 
        
        Para determinar las componentes de la presión hidrostática que actúan sobre la compuerta $AB$, se diagraman las fuerzas de presión que actúan sobre esta. Tal y como se muestra en la siguiente figura:
        """,
        respuesta_P2 = """
        A continuación se presenta el desglose de cada ecuación:

        $W = W_1 + W_2$    
        $W_1 = \\gamma \\cdot b_1 \\cdot h_1 \\cdot 1$     
        $W_2 = \\gamma \\cdot \\dfrac{{b_1 \\cdot h_2}}{{2}} \\cdot 1$     
        $W = \\gamma \\cdot b_1 \\cdot h_1 \\cdot 1 + \\gamma \\cdot \\dfrac{{b_1 \\cdot h_2}}{{2}} \\cdot 1$

        $P = P_1 + P_2$    
        $P_1 = \\gamma \\cdot h_1 \\cdot h_2 \\cdot 1$     
        $P_2 = \\gamma \\cdot \\dfrac{{(h_2)^2}}{{2}} \\cdot 1$       
        $P = \\gamma \\cdot h_1 \\cdot h_2 \\cdot 1 + \\gamma \\cdot \\dfrac{{(h_2)^2}}{{2}} \\cdot 1$
        """,
        ),

    Theory(#7
        code = 8200070, 
        no_pregunta = 7,
        topic = "Fuerzas distribuidas",
        subtopic = "Presión hidrostática",
        enunciado = "Para la estructura mostrada a continuación, seleccione el diagrama que representa correctamente la distribución de presiones hidrostáticas.", 
        opcion_1 = "$I$",
        opcion_2 = "$II$",
        opcion_3 = "$III$",
        opcion_4 = "$IV$",
        opcion_correcta = "$I$",
        respuesta_P1 = """
        El diagrama $I$ representa adecuadamente las presiones hidrostáticas aplicadas sobre la estructura:

        1. De $A$ a $B$, la presión inicia en cero en la superficie y aumenta linealmente con la profundidad hasta alcanzar $P_B$.
        2. De $B$ a $C$, la presión inicia en $P_B$ y continúa aumentando linealmente hasta $P_C$. Esto se debe a que, la presión en un punto sumergido actúa perpendicular a la superficie y su magnitud es igual en todas las direcciones.
        3. De $C$ a $D$, la presión se mantiene constante en $P_C$, dado que, no hay cambio en la profundidad.
        """,
        respuesta_P2 = "",
        ),

    Theory(#8
        code = 8200080, 
        no_pregunta = 8,
        topic = "Fuerzas distribuidas",
        subtopic = "Presión hidrostática",
        enunciado = "Considere la presa mostrada en la figura. ¿Cuál de las siguientes afirmaciones describe correctamente cómo varía la presión a lo largo de la superficie curva?.", 
        opcion_1 = "La presión es constante en toda la superficie porque la profundidad promedio se mantiene igual.",
        opcion_2 = "La presión aumenta uniformemente a lo largo de la curva.",
        opcion_3 = "La presión aumenta de manera lineal a lo largo de la curva.",
        opcion_4 = "La presión varía en función de la profundidad de cada punto, por lo que no sigue una distribución lineal en la superficie curva.",
        opcion_correcta = "La presión varía en función de la profundidad de cada punto, por lo que no sigue una distribución lineal en la superficie curva.",
        respuesta_P1 = "La presión aumenta con la profundidad según la relación $P = \\gamma \\cdot h$, donde $\\gamma$ es el peso específico del fluido y $h$ es la profundidad. En una superficie curva, cada punto se encuentra a una profundidad distinta, lo que hace que la presión no aumente de forma lineal respecto a la superficie, sino que siga una distribución que depende de la geometría y la orientación de la curva.",
        respuesta_P2 = "",
        ),


#---------------------------------------------- Fuerzas distribuidas -------------------------------
#------------------------------------------------ Empuje de suelo ----------------------------------
#-------------------------------------------------    83000##0   -----------------------------------
    
    Theory(#1
        code = 8300010, 
        no_pregunta = 1,
        topic = "Fuerzas distribuidas",
        subtopic = "Empuje de suelo",
        enunciado = "En la figura se muestra un muro de contención con un sistema de anclaje. Considerando el equilibrio de fuerzas, ¿en qué dirección actúa la fuerza que genera el anclaje y por qué?", 
        opcion_1 = "Hacia la izquierda, para apoyar el peso del muro.",
        opcion_2 = "Hacia la izquierda, para generar fricción entre el muro y la base.",
        opcion_3 = "Hacia la derecha, para contrarrestar la presión lateral del suelo.",
        opcion_4 = "Hacia la derecha, para equilibrar el peso propio del muro.",
        opcion_correcta = "Hacia la derecha, para contrarrestar la presión lateral del suelo.",
        respuesta_P1 = "El anclaje actúa hacia la derecha, en dirección opuesta a la presión del terreno. Su objetivo es equilibrar las fuerzas horizontales que tienden a empujar el muro hacia la izquierda, asegurando así la estabilidad de la estructura.",
        respuesta_P2 = "",
        ),

    Theory(#2
        code = 8300020, 
        no_pregunta = 2,
        topic = "Fuerzas distribuidas",
        subtopic = "Empuje de suelo",
        enunciado ="Considere la situación mostrada en la siguiente figura. ¿Es necesario instalar un anclaje en el muro para evitar su volcamiento?", 
        opcion_1 = "No. Porque la presión del suelo es menor que la del agua, y un anclaje podría inducir un volcamiento hacia el terreno.",
        opcion_2 = "No. Porque el momento generado por la presión del suelo es menor que el del agua, el anclaje no es la solución adecuada, ya que aumentaría este desequilibrio.",
        opcion_3 = "Sí. Porque la presión del agua es menor que la del suelo, y el anclaje debe contrarrestar la fuerza ejercicda por el suelo.",
        opcion_4 = "Sí. Porque el momento generado por la presión del suelo es mayor que el del agua, y el anclaje debe contrarrestar ese momento para evitar el volcamiento.",
        opcion_correcta = "Sí. Porque el momento generado por la presión del suelo es mayor que el del agua, y el anclaje debe contrarrestar ese momento para evitar el volcamiento.",
        respuesta_P1 = "Se requiere instalar un anclaje cuando el momento generado por la presión del suelo es mayor que el generado por la presión del agua, ya que en ese caso el muro tiende a volcarse hacia el lado del agua. En este caso, es necesario instalar un anclaje del lado del suelo para contrarrestar ese momento y mantener el equilibrio del sistema.",
        respuesta_P2 = "",
        ),
    


#--------------------------------------------------- Fuerzas internas -------------------------------------------------------
#-------------------------------------------------       91000##0         ---------------------------------------------------

    Theory(#1
        code = 9100010, 
        no_pregunta = 1,
        topic = "Fuerzas internas",
        subtopic = "Fuerzas internas",
        enunciado ="¿En qué lugares es correcto realizar los cortes al analizar las fuerzas internas en una estructura?", 
        opcion_1 = "En los puntos de aplicación de una fuerza.",
        opcion_2 = "En los puntos donde ocurre un cambio en las condiciones de carga.",
        opcion_3 = "En los puntos donde el momento interno es nulo.",
        opcion_4 = "En los extremos de la estructura.",
        opcion_correcta = "En los puntos donde ocurre un cambio en las condiciones de carga.",
        respuesta_P1 = "Los cortes se realizan para identificar cómo varían las fuerzas internas a lo largo del elemento. Es fundamental hacerlos cuando ocurre un cambio en las cargas aplicadas, como una fuerza puntual o un cambio en una carga distribuida.",
        respuesta_P2 = "",
        ),

    Theory(#2
        code = 9100020, 
        no_pregunta = 2,
        topic = "Fuerzas internas",
        subtopic = "Fuerzas internas",
        enunciado ="Considere la viga mostrada en la figura. ¿Cuántos tramos deben analizarse para determinar correctamente las fuerzas internas a lo largo de la viga?", 
        opcion_1 = "5",
        opcion_2 = "4",
        opcion_3 = "3",
        opcion_4 = "6",
        opcion_correcta = "4",
        respuesta_P1 = "Para realizar el análisis de fuerzas internas, la viga debe dividirse en tramos según los cambios en las condiciones de carga. En este caso, la viga presenta cuatro tramos diferenciados debido a variaciones como cargas puntuales y una carga distribuida. Estos cambios determinan los puntos clave donde deben efectuarse los cortes para identificar correctamente las fuerzas internas, tal como se muestra en la figura.",
        respuesta_P2 = "",
        ),

    Theory(#3
        code = 9100030, 
        no_pregunta = 3,
        topic = "Fuerzas internas",
        subtopic = "Fuerzas internas",
        enunciado ="""
        Indique cuáles de las siguientes afirmaciones son verdaderas respecto al análisis de los diagramas de esfuerzo cortante y momento flector:

        I. Cuando se aplican cargas distribuidas, los diagramas de cortante y momento aumentan su grado. Por ejemplo, si la carga es triangular (grado 1), el cortante será un polinomio de grado 2 y el momento uno de grado 3.    
        II. Cuando se aplican cargas distribuidas, los diagramas de cortante y momento disminuyen su grado. Por ejemplo, si la carga es triangular, el cortante será de grado 3 y el momento de grado 2.    
        III. Una carga puntual genera un salto en el diagrama de cortante, en el punto de aplicación, igual a su magnitud, sumándose o restándose según la dirección de la carga.    
        IV. El diagrama de momento se obtiene integrando el diagrama de cortante, es decir, calculando el área bajo la curva del cortante.    
        V. Los momentos puntuales deben considerarse tanto en el diagrama de momento como en el de cortante, sumándolos o restándolos según su sentido.   
        """, 
        opcion_1 = "I, III, V",
        opcion_2 = "II, III, IV",
        opcion_3 = "I, III, IV",
        opcion_4 = "II, IV, V",
        opcion_correcta = "I, III, IV",
        respuesta_P1 = "Los diagramas de cortante y momento flector se construyen a partir de las condiciones de carga sobre una estructura. Cuando se aplican cargas distribuidas, el grado del polinomio del diagrama de cortante aumenta en relación con el de la carga, y el del momento aumenta con respecto al cortante (por integración). Por ejemplo, una carga triangular (grado 1) genera un cortante de grado 2 y un momento de grado 3. Una carga puntual afecta únicamente el diagrama de cortante, provocando un salto de magnitud igual a la carga. El diagrama de momento se construye integrando el cortante, lo que equivale a calcular el área bajo su curva. Los momentos puntuales solo afectan el diagrama de momento, no el de cortante.",
        respuesta_P2 = "",
        ),

    Theory(#4
        code = 9100040, 
        no_pregunta = 4,
        topic = "Fuerzas internas",
        subtopic = "Fuerzas internas",
        enunciado ="Considere la figura mostrada e indique cuál de las siguientes representaciones corresponde a la convención de signos correcta.", 
        opcion_1 = "$I$",
        opcion_2 = "$II$",
        opcion_3 = "$III$",
        opcion_4 = "$IV$",
        opcion_correcta = "$II$",
        respuesta_P1 = "El diagrama correcto es la opción $II$. La convención de signos establece que, al realizar un corte en una viga, el cortante (V) y el momento flector (M) deben aplicarse de forma que aseguren el equilibrio interno del elemento. En el lado izquierdo del corte, el cortante se representa apuntando hacia abajo y el momento en sentido antihorario. En el lado derecho, el cortante va hacia arriba y el momento en sentido horario.",
        respuesta_P2 = "",
        ),

    Theory(#5
        code = 9100050, 
        no_pregunta = 5,
        topic = "Fuerzas internas",
        subtopic = "Fuerzas internas",
        enunciado ="¿Cómo se comporta el diagrama de momento flector si el diagrama de fuerzas cortantes es uniforme?", 
        opcion_1 = "El diagrama de momento flector es constante.",
        opcion_2 = "El diagrama de momento flector es cuadrático.",
        opcion_3 = "El diagrama de momento flector es lineal.",
        opcion_4 = "El diagrama de momento flector es cúbico.",
        opcion_correcta = "El diagrama de momento flector es lineal.",
        respuesta_P1 = "Cuando el esfuerzo cortante es constante (uniforme), el momento flector varía linealmente a lo largo del tramo. Esto ocurre porque el momento flector es la integral del esfuerzo cortante. Integrar una constante produce una función lineal.",
        respuesta_P2 = "",
        ),

    Theory(#6
        code = 9100060, 
        no_pregunta = 6,
        topic = "Fuerzas internas",
        subtopic = "Fuerzas internas",
        enunciado ="¿Qué representa un salto en el diagrama de fuerzas cortantes de una viga?",
        opcion_1 = "Una carga distribuida.",
        opcion_2 = "Un momento aplicado.",
        opcion_3 = "Una carga puntual.",
        opcion_4 = "Una reacción en un apoyo fijo.",
        opcion_correcta = "Una carga puntual.",
        respuesta_P1 = " Un salto en el diagrama de fuerzas cortantes ocurre cuando se aplica una carga puntual en la viga. Esta carga provoca una discontinuidad instantánea en el esfuerzo cortante. De manera similar, en el diagrama de momentos, un momento puntual aplicado también genera un salto en el diagrama de momento flector.",
        respuesta_P2 = "",
        ),

    Theory(#7
        code = 9100070, 
        no_pregunta = 7,
        topic = "Fuerzas internas",
        subtopic = "Fuerzas internas",
        enunciado ="Una viga está sometida a una carga distribuida uniforme, ¿cuál es la forma del diagrama de momento flector resultante?", 
        opcion_1 = "Lineal (triángulo).",
        opcion_2 = "Uniforme (rectángulo).",
        opcion_3 = "Parábola.",
        opcion_4 = "Trapecio.",
        opcion_correcta = "Parábola.",
        respuesta_P1 = "El diagrama de momento flector generado por una carga distribuida uniforme tiene forma parabólica. Esto se debe a que el momento flector es la integral del esfuerzo cortante. Dado que la carga distribuida uniforme produce un esfuerzo cortante lineal, la integral de esta fuerza da como resultado una variación cuadrática del momento a lo largo de la viga, lo que genera un diagrama de momento con forma parabólica.",
        respuesta_P2 = "",
        ),

    Theory(#8
        code = 9100008, 
        no_pregunta = 8,
        topic = "Fuerzas internas",
        subtopic = "Fuerzas internas",
        enunciado ="¿Qué indica el punto donde el diagrama de fuerza cortante es cero (donde corta el eje horizontal)?", 
        opcion_1 = "Un punto de máximo esfuerzo cortante.",
        opcion_2 = "Un punto de máxima deformación.",
        opcion_3 = "Un punto de inflexión.",
        opcion_4 = "Un punto de momento máximo.",
        opcion_correcta = "Un punto de momento máximo.",
        respuesta_P1 = "El esfuerzo cortante es la derivada del diagrama de momentos. Cuando el diagrama de cortante cruza el eje cero, la pendiente del diagrama de momentos es cero, lo que indica que el momento flector alcanza un valor máximo o mínimo en ese punto. En este caso corresponde a un punto de momento máximo.",
        respuesta_P2 = "",
        ),

    Theory(#9
        code = 9100009, 
        no_pregunta = 9,
        topic = "Fuerzas internas",
        subtopic = "Fuerzas internas",
        enunciado ="Determine la ecuación de cortante $(V(x))$ y de momento flector $(M(x))$ para la viga mostrada.", 
        opcion_1 = """$V(x) = W \\left(\\dfrac{{L}}{{2}}+x\\right)$\\
        $M(x) = \\dfrac{{W}}{{2}}x^2 - \\dfrac{{WL}}{{2}}x + M_1$ \\
        $\\text{{    }}$""",
        opcion_2 = """$V(x) = W \\left(\\dfrac{{L}}{{2}}-x\\right)$\\
        $M(x) = -\\dfrac{{W}}{{2}}x^2 + \\dfrac{{WL}}{{2}}x - M_1$ \\
        $\\text{{    }}$""",
        opcion_3 = """$V(x) = W \\left(L-x\\right)$\\
        $M(x) = -\\dfrac{{WL}}{{2}}x^2 + \\dfrac{{WL}}{{2}}x - M_1$ \\
        $\\text{{    }}$""",
        opcion_4 = """$V(x) = W \\left(L+x\\right)$\\
        $M(x) = \\dfrac{{WL}}{{2}}x^2 - \\dfrac{{WL}}{{2}}x + M_1$ \\
        $\\text{{    }}$""",
        opcion_correcta = """$V(x) = W \\left(\\dfrac{{L}}{{2}}-x\\right)$\\
        $M(x) = -\\dfrac{{W}}{{2}}x^2 + \\dfrac{{WL}}{{2}}x - M_1$ \\
        $\\text{{    }}$""",
        respuesta_P1 = """
        Las ecuaciones de cortante y momento son: 

        $V(x) = W \\left(\\dfrac{{L}}{{2}}-x\\right)$\\
        $M(x) = -\\dfrac{{W}}{{2}}x^2 + \\dfrac{{WL}}{{2}}x - M_1$ \\
        $\\text{{    }}$
        
        Para determinar las ecuaciones, primero se hayan las reacciones verticales en los apoyos. Dado que la viga y las cargas aplicadas son simétricas, ambas reacciones son iguales:

        $\\sum{{M_A}}=B_y \\cdot L + M_1 - M_1 - \\cdot W\\dfrac{{L^2}}{{2}}$         
        $A_y = B_y = \\dfrac{{WL}}{{2}}$

        Luego, se procede a cortar la viga y a calcular las ecuaciones:
        """,
        respuesta_P2 = """
        Para hallar la ecuación de cortante se realiza la sumatoria de fuerzas en y:

        $\\sum{{F_y}}= -V(x) -Wx + \\dfrac{{WL}}{{2}} = 0$       
        $V(x) = -Wx + \\dfrac{{WL}}{{2}} = W\\left(\\dfrac{{L}}{{2}}-x\\right)$

        Para hallar la ecuación de momento se realiza sumatoria de momentos en el punto de corte:

        $\\sum{{M}}= M(x) + M_1 + \\dfrac{{W}}{{2}} x^2 - \\dfrac{{WL}}{{2}} x = 0$           
        $M(x) = -\\dfrac{{W}}{{2}}x^2 + \\dfrac{{WL}}{{2}}x - M_1$
        """,
        ),

    Theory(#10
        code = 9100010, 
        no_pregunta = 10,
        topic = "Fuerzas internas",
        subtopic = "Fuerzas internas",
        enunciado ="""
        Considere el siguiente diagrama de momento flector para una viga. ¿Cuáles de las siguientes afirmaciones son incorrectas?

        I. Entre $a$ y $b$ la fuerza cortante es constante.           
        II. Entre $d$ y $e$ hay una carga distribuida triangular.             
        III. Entre $b$ y $d$ la fuerza cortante es menor a cero.            
        IV. En $d$ hay un momento externo aplicado. 
        """, 
        opcion_1 = "I, III",
        opcion_2 = "I, II",
        opcion_3 = "II, III",
        opcion_4 = "II, IV",
        opcion_correcta = "II, IV",
        respuesta_P1 = """
        Las afirmaciones incorrectas son II y IV.             
        
        Entre $d$ y $e$, el diagrama de momento tiene forma parabólica, lo cual indica que la carga distribuida es uniforme. Si la carga fuera triangular, el diagrama tendría una cúbica en este tramo.   
        
        Por otro lado, en $d$ no hay un salto en el diagrama de momento, lo que implica que no hay un momento externo aplicado en este punto.
        """,
        respuesta_P2 = "",
        ),

]


