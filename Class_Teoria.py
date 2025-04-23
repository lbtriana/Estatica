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
         
    # Theory(#3
    #     code = 2100030, 
    #     no_pregunta = 3,
    #     topic = "Momento",
    #     subtopic = "Momento",
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
             
    Theory(#4
        code = 2100040, 
        no_pregunta = 4,
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

   
    #--------------------------------------------------- Incertidumbre ----------------------------------------------------------
    #-------------------------------------------------       31000#0      ---------------------------------------------------
    # Theory(#1
    #     code = 3100010, 
    #     no_pregunta = 1,
    #     topic = "Incertidumbre",
    #     subtopic = "Incertidumbre",
    #     enunciado ="Considere la siguiente figura e indique la forma correcta de obtener la probabilidad de falla para cualquier valor en las abscisas (eje X).", 
    #     opcion_1 = "En la gráfica presentada, la probabilidad de falla corresponde a la probabilidad de excedencia.",
    #     opcion_2 = "En la gráfica presentada, la probabilidad de falla corresponde al área bajo la curva desde X=0 hasta el valor de tensión que se quiere.",
    #     opcion_3 = "En la gráfica presentada, la probabilidad de falla corresponde a la probabilidad de ocurrencia.",
    #     opcion_4 = "En la gráfica presentada, la probabilidad de falla corresponde a 1 menos al área bajo la curva desde X=0 hasta el valor de tensión que se quiere.",
    #     opcion_correcta = "En la gráfica presentada, la probabilidad de falla corresponde a la probabilidad de excedencia.",
    #     respuesta_P1 = """Para dar respuestaa esta pregunta es necesario realizarse 2 preguntas:
    #        1. ¿Es de frecuencia acumulada o no? ya que, en este caso, nos permite identificar que no es necesario calcular las áreas debajo la curva. 
    #        2. ¿Cuál es la variable independiente? En caso de que sea la tensión máxima resistida, la falla se obtiene como la excedencia debido a que después de ese valor se supera la resistencia máxima del material llevandolo a falla. """,
    #     respuesta_P2 = "",
    #     ),

    # Theory(#2
    #     code = 3100020, 
    #     no_pregunta = 2,
    #     topic = "Incertidumbre",
    #     subtopic = "Incertidumbre",
    #     enunciado ="Considere la siguiente figura e indique la forma correcta de obtener la probabilidad de falla para cualquier valor en las abscisas (eje X).", 
    #     opcion_1 = "En la gráfica presentada, la probabilidad de falla corresponde a la probabilidad de excedencia.",
    #     opcion_2 = "En la gráfica presentada, la probabilidad de falla corresponde al área bajo la curva desde X=0 hasta el valor de resistencia que se quiere.",
    #     opcion_3 = "En la gráfica presentada, la probabilidad de falla corresponde a la probabilidad de ocurrencia.",
    #     opcion_4 = "En la gráfica presentada, la probabilidad de falla corresponde a 1 menos al área bajo la curva desde X=0 hasta el valor de resistencia que se quiere.",
    #     opcion_correcta = "En la gráfica presentada, la probabilidad de falla corresponde a la probabilidad de ocurrencia.",
    #     respuesta_P1 = """Para dar respuestaa esta pregunta es necesario realizarse 2 preguntas:
    #        1. ¿Es de frecuencia acumulada o no? ya que, en este caso, nos permite identificar que no es necesario calcular las áreas debajo la curva. 
    #        2. ¿Cuál es la variable independiente? En caso de que sea la resistencia, la falla se obtiene como la ocurrencia debido a que el valor en el eje X correspondería a la resistencia en la que falla.""",
    #     respuesta_P2 = "",
    #     ),

    # Theory(#3
    #     code = 3100030, 
    #     no_pregunta = 3,
    #     topic = "Incertidumbre",
    #     subtopic = "Incertidumbre",
    #     enunciado ="Indique cual de las siguientes afirmaciones en verdadera:", 
    #     opcion_1 = "cuando se tiene la función de densidad (frecuencia relativa) la probabilidad se obtiene directamente del eje y. Si se tiene la de frecuencia acumulada, la probabilidad se obtiene a partir del área adecuada debajo de la curva.",
    #     opcion_2 = "cuando se tiene la función de densidad (frecuencia relativa) la probabilidad no se puede obtener. Si se tiene la de frecuencia acumulada, la probabilidad se obtiene directamente del eje y.",
    #     opcion_3 = "cuando se tiene la función de densidad (frecuencia relativa) la probabilidad se obtiene a partir del área adecuada debajo de la curva. Si se tiene la de frecuencia acumulada, la probabilidad no se puede obtener.",
    #     opcion_4 = "cuando se tiene la función de densidad (frecuencia relativa) la probabilidad se obtiene a partir del área adecuada debajo de la curva. Si se tiene la de frecuencia acumulada, la probabilidad se obtiene directamente del eje y.",
    #     opcion_correcta = "cuando se tiene la función de densidad (frecuencia relativa) la probabilidad se obtiene a partir del área adecuada debajo de la curva. Si se tiene la de frecuencia acumulada, la probabilidad se obtiene directamente del eje y.",
    #     respuesta_P1 = "Las gráficas de frecuencia acumulada representan inmediatamente una probabilidad y es por ello que su valor máximo en el eje Y es 1 el cual corresponde al 100% de las probabilidades. En cambio, en las gráficas de desidad se tienen proporciones que deben ser sumadas por medio de una integral.",
    #     respuesta_P2 = "",
    #     ),

    # Theory(#4
    #     code = 3100040, 
    #     no_pregunta = 4,
    #     topic = "Incertidumbre",
    #     subtopic = "Incertidumbre",
    #     enunciado ="Considere la siguiente figura e indique cual es la probabilidad de que la tensión máxima resistida sea menor o igual a 850 N?", 
    #     opcion_1 = "Sería la probabilidad de ocurrencia.Es decir, el valor de Y en ese punto.",
    #     opcion_2 = "Sería restando a la unidad el valor de Y en ese punto.",
    #     opcion_3 = "Sería la integral desde 0 hasta 850 de la función.",
    #     opcion_4 = "Sería 1 - la integral desde 0 hasta 850 de la función.",
    #     opcion_correcta = "Sería la probabilidad de ocurrencia.Es decir, el valor de Y en ese punto.",
    #     respuesta_P1 = """Cuando no se habla de probabilidad de falla no es necesario saber cuál es la variable independiente. Basta con saber que menor o igual hace referencia a la probabilidad de ocurrencia.
    #     Adicionalmente es importante reconocer que debido a que es una gráfica de frecuencias acumulada, no es necesario calcular integrales.""",
    #     respuesta_P2 = "",
    #     ),

    Theory(#5
        code = 3100050, 
        no_pregunta = 5,
        topic = "Incertidumbre",
        subtopic = "Incertidumbre",
        enunciado ="Considere la siguiente figura. ¿Indique cuál es la probabilidad de que la tensión máxima resistida sea mayor o igual a 900 N?", 
        opcion_1 = "La probabilidad es el valor de Y en ese punto (0,2).",
        opcion_2 = "La probabilidad es el área total bajo la curva menos el Y en ese punto (0,8).",
        opcion_3 = "La probabilidad es la suma acumulada de la frecuencia relativa en el dominio desde 0 hasta 900 de la función (0,9).",
        opcion_4 = "La probabilidad es el área total bajo la curva menos la suma acumulada de la frecuencia relativa en el dominio desde 0 hasta 900 de la función (0,1).",
        opcion_correcta = "La probabilidad es el área total bajo la curva menos la suma acumulada de la frecuencia relativa en el dominio desde 0 hasta 900 de la función (0,1).",
        respuesta_P1 = """La probabilidad de que la tensión máxima resistida sea mayor o igual a 900 N es equivalente a la probabilidad de excedencia, es decir, la probabilidad con la que se excede el valor de 900 N. La probabilidad de excedencia se calcula como:

        $\\text{{Probabilidad de excedencia}} = $1$ - $\\text{{Probabilidad de ocurrencia}}$

        1 hace referencia al área total bajo la curva y la probabilidad de ocurrencia es la suma acumulada de la frecuencia relativa en el dominio desde 0 hasta 900 de la función (0,1).
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

    Theory(#7
        code = 3100070, 
        no_pregunta = 7,
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

    #------------------------------------------------------  Cerchas ------------------------------------------------------------
    #-------------------------------------------------       16000##0         ---------------------------------------------------
    # Theory(#1
    #     code = 1600010, 
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
    #     code = 1600020, 
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
    #     code = 1600030, 
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
    #     code = 1600040, 
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
    #     code = 1600050, 
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
    #     code = 1600060, 
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
    #     code = 1700060, 
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
    
    # Theory(#7
    #     code = 7100070, 
    #     no_pregunta = 7,
    #     topic = "Centroides",
    #     subtopic = "Centroides",
    #     enunciado ="Considere la siguiente figura e indique cual es su centroide en x respecto al punto O:", 
    #     opcion_1 = "I",
    #     opcion_2 = "II",
    #     opcion_3 = "III",
    #     opcion_4 = "IV",
    #     opcion_correcta = "IV",
    #     respuesta_P1 = """Recuerde que el centroide de un triangulos es 1/3b si se toma desde el angulo recto y 2/3b si se toma desde un ángulo agudo como ocurre en este caso. 
    #     Dado que 2/3b no se encuentra entre las opciones, se emplea la definición de centroide cuando se tiene una ecuación.""",
    #     respuesta_P2 = "",
    #     ),
    
    # Theory(#8
    #     code = 7100080, 
    #     no_pregunta = 8,
    #     topic = "Centroides",
    #     subtopic = "Centroides",
    #     enunciado ="Considere la siguiente figura e indique cual es su centroide en Y respecto al punto O:", 
    #     opcion_1 = "I",
    #     opcion_2 = "II",
    #     opcion_3 = "III",
    #     opcion_4 = "IV",
    #     opcion_correcta = "II",
    #     respuesta_P1 = """Recuerde que el centroide de un triangulos es 1/3b si se toma desde el angulo recto y 2/3b si se toma desde un ángulo agudo como ocurre en este caso. 
    #     Dado que 2/3b no se encuentra entre las opciones, se emplea la definición de centroide cuando se tiene una ecuación.
    #     Evidencie que dado que la base y la altura del triangulo es la misma, los limetes de la integral para x e y son los mismos.""",
    #     respuesta_P2 = "",
    #     ),
    
    # Theory(#9
    #     code = 7100090, 
    #     no_pregunta = 9,
    #     topic = "Centroides",
    #     subtopic = "Centroides",
    #     enunciado ="¿Dónde se encuentra el centro de masa de la placa compuesta mostrada en la siguiente figura?: ", 
    #     opcion_1 = "En el eje y se ubica en h/2 y en el eje x en b/2",
    #     opcion_2 = "En el eje y se ubica en h/2 y en el eje x se ubica más cerca del lado de la madera.",
    #     opcion_3 = "En el eje y se ubica en h/2 y en el eje x se ubica más cerca del lado del acero.",
    #     opcion_4 = "En el eje y se ubica en la base y en el eje x se ubica más cerca del lado de la acero.",
    #     opcion_correcta = "En el eje y se ubica en h/2 y en el eje x se ubica más cerca del lado del acero.",
    #     respuesta_P1 = "El centro de masa se encuentra más cerca del material que tiene mayor densidad. Como el metal tiene una densidad mayor que la madera, el centro de masa se desplazará hacia el lado del metal, ya que esta parte contribuye con más masa al objeto total.",
    #     respuesta_P2 = "",
    #     ),
    
    # Theory(#10
    #     code = 7100100, 
    #     no_pregunta = 10,
    #     topic = "Centroides",
    #     subtopic = "Centroides",
    #     enunciado ="Considerando la siguiente figura, si se sabe que la densidad del material inferior es mayor y que los materiales componen al cilindro en un 50-50, ¿Cuál de las siguientes afirmaciones es correcta sobre la ubicación del centro de masa? ", 
    #     opcion_1 = "El centro de masa estará en el centro geométrico del cilindro.",
    #     opcion_2 = "El centro de masa estará más cerca de la sección superior",
    #     opcion_3 = "El centro de masa estará más cerca de la sección inferior.",
    #     opcion_4 = "El centro de masa se ubicará en la línea de unión entre las dos secciones",
    #     opcion_correcta = "El centro de masa estará más cerca de la sección inferior",
    #     respuesta_P1 = """El centro de masa se encuentra más cerca del material que tiene mayor densidad. Como el material inferior tiene una densidad mayor, el centro de masa se desplazará hacia abajo.""",
    #     respuesta_P2 = "",
    #     ),


#---------------------------------------------- Fuerzas distribuidas- VIGAS -------------------------------------------------
#-------------------------------------------------       81000##0         ---------------------------------------------------
    
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
        enunciado =" La fuerza distribuida mostrada en la figura es equivalente luna fuerza puntual de magnitud:",    
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
    
     #-------------------------------------- Fuerzas distribuidas- PRESIÓN HIDROSTÁTICA ------------------------------------------
     #-------------------------------------------------       82000##0         ---------------------------------------------------
    
#---------------------------------------------- Fuerzas distribuidas- PRESIONES HIDROSTÁTICAS -------------------------------------------------
#-------------------------------------------------       82000##0         ---------------------------------------------------

    # Theory(#1
    #     code = 8200010, 
    #     no_pregunta = 1,
    #     topic = "Fuerzas distribuidas",
    #     subtopic = "Presiones hidrostáticas",
    #     enunciado ="Considere la siguiente figura y ordene de mayor a menor presión hidrostática", 
    #     opcion_1 = "II, IV, I, III",
    #     opcion_2 = "III,I,IV,III",
    #     opcion_3 = "IV, II, III, I",
    #     opcion_4 = "I, III, II, IV",
    #     opcion_correcta = "IV, II, III, I",
    #     respuesta_P1 = """Los principales factores que influyen en la presión hidrostática son la densidad y profundidad. 
    #     Por un lado, a mayor densidad del fluido mayor será la presión hirostática.
    #     Por otro, la presión hidrostática en paredes inclinadas es mayor que en paredes completamente verticales debido a la influencia del peso del agua que aparece sobre la inclinación siempre y cuando estas se encuentren a la misma altura sumergida.""",
    #     respuesta_P2 = "",
    #     ),

    Theory(#2
        code = 8200020, 
        no_pregunta = 2,
        topic = "Fuerzas distribuidas",
        subtopic = "Presiones hidrostáticas",
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
        subtopic = "Presiones hidrostáticas",
        enunciado ="Considerando la siguiente figura ¿cuál(es) es(son) el(los) diagrama(s) correcto(s)?", 
        opcion_1 = "Solamente I",
        opcion_2 = "I y II",
        opcion_3 = "I y III",
        opcion_4 = "Solamente II.",
        opcion_correcta = "I y III",
        respuesta_P1 = "Las representaciones correctas son I y III. El diagrama III representa correctamente la presión triangular perpendicular a la superficie y el diagrama I es su forma descompuesta, utilizada como método de cálculo.",
        respuesta_P2 = "",
        ),
    
    # Theory(#4
    #     code = 8200040, 
    #     no_pregunta = 4,
    #     topic = "Equilibrio de partículas",
    #     subtopic = "Fuerzas distribuidas",
    #     enunciado ="Si se quiere determinar las dimensiones de una base debe buscarse:", 
    #     opcion_1 = "Que los momentos generados por las fuerzas actuantes (presiones) y las fuerzas resistentes (pesos) sean iguales.",
    #     opcion_2 = "Que la sumatoria de momentos en un punto de la presa sea mayor a 0.",
    #     opcion_3 = "Que la base sea mayor a la altura del agua.",
    #     opcion_4 = "Que la sumatoria de momentos generados por las fuerzas actuantes (actuantes) sea 0.",
    #     opcion_correcta = "Que los momentos generados por las fuerzas actuantes (presiones) y las fuerzas resistentes (pesos) sean iguales.",
    #     respuesta_P1 = """Para diseñar presas en importante tener en cuenta las fuerzas actuantes y resistentes para evitar volcamientos y/o hundimientos de la estructura.""",
    #     respuesta_P2 = "",
    #     ),
    
    #  #-------------------------------------- Fuerzas distribuidas- EMPUJE DE SUELO ----------------------------------------------
    #  #-------------------------------------------------       83000##0         ---------------------------------------------------
    
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
    
    # Theory(#2
    #     code = 9100020, 
    #     no_pregunta = 2,
    #     topic = "Fuerzas internas",
    #     subtopic = "Fuerzas internas",
    #     enunciado ="El análisis de fuerzas internas requiere de:", 
    #     opcion_1 = "Igualar la resultante de fuerzas externas con las fuerzas internas sin incluir reacciones.",
    #     opcion_2 = "Cortar la estructura en puntos cercanos a lo largo de toda la estructura y luego calcular las reacciones.",
    #     opcion_3 = "Igualar la resultante de momentos a los momentos internos sin incluir reacciones.",
    #     opcion_4 = "Conocer las reacciones sobre la estructura, dividirla en tramos y realizar cortes.",
    #     opcion_correcta = "Conocer las reacciones sobre la estructura, dividirla en tramos y realizar cortes.",
    #     respuesta_P1 = """"Para conocer las fuerzas internas de un elemento es necesario realizar, en primer lugar, un análisis global para conocer las reacciones.
    #     Despues de esto, se divide la estructura en tramos de acuerdo con las condiciones de carga y se realizan cortes en el interior de cada tramo.""",
    #     respuesta_P2 = "",
    #     ),

    # Theory(#3
    #     code = 9100030, 
    #     no_pregunta = 3,
    #     topic = "Fuerzas internas",
    #     subtopic = "Fuerzas internas",
    #     enunciado ="En el análisis de fuerzas internas, dónde es correcto realizar los cortes:", 
    #     opcion_1 = "En el punto de aplicación de una fuerza.",
    #     opcion_2 = "Antes y después del punto de aplicación de una fuerza.",
    #     opcion_3 = "En puntos con momento nulo.",
    #     opcion_4 = "En el inicio y fin de cada elemento de la estructura.",
    #     opcion_correcta = "Antes y después del punto de aplicación de una fuerza.",
    #     respuesta_P1 = "El objetivo de los cortes es conocer los efectos de las cargas en el interior del elemento, es decir, los cambios que las fuerzas externas producen en los elementos. Por ello, se deben determinar las fuerzas internas antes y después del punto de aplicacón de la carga.",
    #     respuesta_P2 = "",
    #     ),

    # Theory(#4
    #     code = 9100040, 
    #     no_pregunta = 4,
    #     topic = "Fuerzas internas",
    #     subtopic = "Fuerzas internas",
    #     enunciado ="Considere la siguiente figura e indique cuántos tramos son necesarios para el análsis de fuerzas internas en la viga mostrada", 
    #     opcion_1 = "5",
    #     opcion_2 = "4",
    #     opcion_3 = "3",
    #     opcion_4 = "6",
    #     opcion_correcta = "4",
    #     respuesta_P1 = "La viga mostrada tiene 4 condiciones de carga diferentes debido a fuerzas puntuales, reacciones y la carga distribuida.",
    #     respuesta_P2 = "",
    #     ),

    # Theory(#5
    #     code = 9100050, 
    #     no_pregunta = 5,
    #     topic = "Fuerzas internas",
    #     subtopic = "Fuerzas internas",
    #     enunciado =""""Indique cuáles de las siguientes afirmaciones son verdaderas:
    #     I. Cuando se tienen cargas distribuidas, los diagramas de cortante y momento van aumentando de grado. Es decir, si la carga es triangular el cortante es un polinomio de grado 2 y el momento uno de grado 3.
    #     II. Cuando se tienen cargas distribuidas, los diagramas de cortante y momento van disminuyendo de grado. Es decir, si la carga es triangular el cortante es un polinomio de grado 3 y el momento uno de grado 2.
    #     III. Para conosiderar una carga puntual, en el diagrama de cortante se suma o resta su magnitud en el punto de aplicación.
    #     IV. Los diagramas de momentos se determinan calculando las áreas formadas en el diagrama de cortante.
    #     V. Los momentos puntuales en un elemento deben sumarse o restarse en el diagrama de momentos y cortante.
           
    #         """, 
    #     opcion_1 = "I,III,V",
    #     opcion_2 = "II, III,IV",
    #     opcion_3 = "I,III,IV",
    #     opcion_4 = "II,IV,V",
    #     opcion_correcta = "I,III,IV",
    #     respuesta_P1 = """En los diagramas de cortante se tienen en cuenta las cargas externas y reacciones. En este, las distribuidas generan un diaagrama de grado mayor y las puntuales afectan únicamente en su punto de aplicación.
    #     En el caso de los diagramas de momnento deben icluirse los momentos puntuales sobre la estructura y se deve tener en cuenta que el mometo es la integral del cortante. 
    #     """,
    #     ),

    # Theory(#6
    #     code = 9100060, 
    #     no_pregunta = 6,
    #     topic = "Fuerzas internas",
    #     subtopic = "Fuerzas internas",
    #     enunciado ="Considere la siguiente figura e indique cual es convención de signos correcta.", 
    #     opcion_1 = "I.",
    #     opcion_2 = "II.",
    #     opcion_3 = "III.",
    #     opcion_4 = "IV.",
    #     opcion_correcta = "II.",
    #     respuesta_P1 = """La conveción de signos estable que en el lado izquierdo de un corte, el cortante resultante (V) debe generar un momento contrario al momento puntual resultante (M). Mientras que, en el lado derecho del corte el cortante y momento generan la misma flexión sobre la viga.
    #     Así mismo, debe tenerse en cuenta que los signos de la resultante de un lado y del otro deben ser contrarios para que la sumatoria de fuerzas y momento sea cero en el corte.""",
    #     respuesta_P2 = "",
    #     ),

    # Theory(#7
    #     code = 9100070, 
    #     no_pregunta = 7,
    #     topic = "Fuerzas internas",
    #     subtopic = "Fuerzas internas",
    #     enunciado ="En un diagrama de momentos flectores, un cambio lineal en el diagrama de fuerzas cortantes indica que el momento flector:", 
    #     opcion_1 = "Es constante.",
    #     opcion_2 = "Tiene un cambio cuadrático.",
    #     opcion_3 = "Tiene un cambio lineal.",
    #     opcion_4 = "Tiene un cambio cúbico.",
    #     opcion_correcta = "Tiene un cambio lineal.",
    #     respuesta_P1 = """"Un cambio lineal en el esfuerzo cortante implica que el momento cambia con una pendiente constante debido a que la integral de una constante es la constante multiplicada por la variable. Es decir, la pendiente del diagrama de momentos flectores es igual al valor del diagrama de fuerzas cortantes. """,
    #     respuesta_P2 = "",
    #     ),

    # Theory(#8
    #     code = 9100080, 
    #     no_pregunta = 8,
    #     topic = "Fuerzas internas",
    #     subtopic = "Fuerzas internas",
    #     enunciado ="¿Qué indica un salto (cambio brusco) en el diagrama de fuerzas cortantes de una viga?",
    #     opcion_1 = "Una carga distribuida.",
    #     opcion_2 = "Un momento aplicado.",
    #     opcion_3 = "Una carga puntual.",
    #     opcion_4 = "Una reacción en un apoyo fijo.",
    #     opcion_correcta = "Una carga puntual.",
    #     respuesta_P1 = " Un salto en el diagrama de fuerzas cortantes ocurre debido a la aplicación de una carga puntual que genera una diferencia instantánea en el esfuerzo cortante. Esto mismo ocurre en el diagrama de momentos cuando se tiene un momento puntual aplicado.",
    #     respuesta_P2 = "",
    #     ),

    # Theory(#9
    #     code = 9100090, 
    #     no_pregunta = 9,
    #     topic = "Fuerzas internas",
    #     subtopic = "Fuerzas internas",
    #     enunciado ="Si una viga simplemente apoyada tiene una carga distribuida uniforme, el diagrama de momentos flectores resultante será:", 
    #     opcion_1 = "Un triángulo: lineal.",
    #     opcion_2 = "Un rectángulo: constante.",
    #     opcion_3 = "Una parábola.",
    #     opcion_4 = "Un trapecio.",
    #     opcion_correcta = "Una parábola.",
    #     respuesta_P1 = "Para pasar de cargas extenas a momento se realiza la doble integral o se aumenta de grado dos veces.",
    #     respuesta_P2 = "",
    #     ),

    # Theory(#10
    #     code = 9100001, 
    #     no_pregunta = 10,
    #     topic = "Fuerzas internas",
    #     subtopic = "Fuerzas internas",
    #     enunciado ="¿Qué significa el punto donde el cortante cruza el eje cero (corte el eje horizontal)?", 
    #     opcion_1 = "Un punto de máximo esfuerzo cortante.",
    #     opcion_2 = "Un punto de máxima deformación.",
    #     opcion_3 = "Un punto de inflexión.",
    #     opcion_4 = "Un punto de momento máximo.",
    #     opcion_correcta = "Un punto de momento máximo.",
    #     respuesta_P1 = """Esto se debe a que el cortante es igual a la derivada del momento. Y, la pendiente (derivada) en un punto es igual a cero cuando se tiene un mínimo o máximo.
    #     """,
    #     ),


]


