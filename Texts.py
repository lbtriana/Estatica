import math
from Calculos import Calculations


#------------------------------- Complexity -------------------------------------
F = "Fácil"
M = "Medio"
D = "Díficil"


#---------------------------------- Topics --------------------------------------
EQ = "Equilibrio de partículas"
MO = "Momento"
CT = "Centroides"


#-------------------------------  Subtopics -------------------------------------
V2D = "Vectores 2D"
V3D = "Vectores 3D"
VU = "Vector unitario"
E2D = "Equilibrio 2D"
M2D = "Momento en un punto 2D"
M3D = "Momento en un punto 3D"
FD = "Fuerzas distribuidas"
FI = "Fuerzas internas"

#------------------------- Nombres de las respuestas ----------------------------
AX = "Ángulo con el eje X [°]"
AY = "Ángulo con el eje Y [°]"
FX = "Componente con el eje X ${{(F1_x)}}$[kN]"
FY = "Componente con el eje Y ${{(F1_y)}}$[kN]"
Mag = "Magnitud $[kN]$"
Dir = "Dirección [°]"
Ci = "Componente en X $(\\hat{{i}})$"
Cj = "Componente en Y $(\\hat{{j}})$"
Ck = "Componente en Z $(\\hat{{k}})$" 
A3X = "Ángulo respecto a X $(\\alpha)$ [°]"
A3Y = "Ángulo respecto a Y $(\\beta)$ [°]"
A3Z = "Ángulo respecto a Z $(\\gamma)$ [°]"
CosX = "Coseno con X"
CosY = "Coseno con Y"


#----------------------------------- Ayudas --------------------------------------

#EQ_V2D_F
A1 = "¿En cuál cuadrante se encuentra el vector? ¿Por qué esto es importante?"
A2 = "El ángulo con el eje X se puede medir de dos formas: $\\alpha_x$ con respecto al eje X positivo o $180-\\alpha_x$ con respecto al eje X negativo."
A3 = '''
 El ángulo con respecto al eje Y $(\\alpha_y)$ se calcula en función del ángulo con respecto al eje X $(\\alpha_x)$:
 - Primer cuadrante: $\\alpha_y = 90 - \\alpha_x$
 - Segundo cuadrante: $\\alpha_y = \\alpha_x - 90$
 - Tercer cuadrante: $\\alpha_y = \\alpha_x - 90$
 - Cuarto cuadrante: $\\alpha_y = \\alpha_x - 90$
 '''
A4 = "La componente de un vector a lo largo del eje X es la proyección del vector sobre el eje."
A5 = "La proyección del vector sobre el eje depende de la magnitud del vector y del ángulo entre el vector y el eje."
A6 = "La componente se calcula como la magnitud multiplicada por el coseno del ángulo con respecto al eje."
A7 = """
Calcule la diferencia de las coordenadas en X y en Y:  

$dx = x_{{final}} - x_{{inicial}}$  
$dy = y_{{final}} - y_{{inicial}}$
"""
A8 = "¿Qué representan dx y dy?"
A9 = "Calcule la pendiente como: $m = \\dfrac{{dy}}{{dx}}$. ¿Qué signica el signo?"
A10 = "Calcule la magnitud de F1 como: $|F1| = \\sqrt{dx^2 + dy^2}$."
A11 = "$\\hat{{i}}$ representa la componente paralela al eje X y $\\hat{{j}}$ a la componente paralela a Y"
A12 = "Calcule la magnitud como: $\\sqrt{F_x^2 + F_y^2}$"
A13 =  """
El cálculo del ángulo respecto al eje x positivo depende del cuadrante en el que se encuentra el vector:

-Primer cuadrante:  $tan^{-1}\\left(\\dfrac{componente\\hspace{1mm} \\hat{{j}}}{componente\\hspace{1mm} \\hat{{i}}}\\right)$  

-Segundo cuadrante: $180 - tan^{-1}\\left(\\dfrac{componente\\hspace{1mm} \\hat{{j}}}{componente\\hspace{1mm} \\hat{{i}}}\\right)$ 

-Tercer cuadrante:  $180 + tan^{-1}\\left(\\dfrac{componente\\hspace{1mm} \\hat{{j}}}{componente\\hspace{1mm} \\hat{{i}}}\\right)$ 

-Cuarto cuadrante:  $360 - tan^{-1}\\left(\\dfrac{componente\\hspace{1mm} \\hat{{j}}}{componente\\hspace{1mm} \\hat{{i}}}\\right)$  
"""

#EQ_V2D_M
A14 = "Determine las componentes de la fuerza resultante mediante la descomposición de las fuerzas en los ejes x, y o use la ley del paralelogramo. Tenga en cuenta el sentido de cada una de las fuerzas dentro de la sumatoria de las componentes. "
A15 = "Calcula la magnitud como: $\\sqrt{(F_{RX}^2+F_{RY}^2)}$"
A16 = "Calcula la dirección de la fuerza resultante con la función tangente."
A17 = "Realice la sumatoria de fuerzas en X y Y, considere el sentido de cada una de las fuerzas  y a cuánto equivale cada una de las sumatorias."
A18 = "Realice la sumatoria de fuerzas en Y para despejar F2, ¿a cuánto debe igualar la sumatoria?"
A19 = "Para calcular la magnitud de la fuerza resultante realice la sumatoria de fuerzas en X de F1 y F2."
A20 = "La fuerza vertical requerida, equivale a la sumatoria de las componentes en Y de las fuerzas F1 y F2."
A21 = "Para despejar el ángulo, plantee el sistema de ecuaciones y busque formar una ecuación en términos de la fuerza y el ángulo conocido, en donde quede como expresión la tangente del ángulo desconocido. Es decir, reemplace la ecuación de la sumatoria de fuerzas en Y en la ecuación de la sumatoria de fuerzas en X"

#EQ_V2D_D
A22 = "Use la ley del paralelogramo o la regla del triángulo para descomponer una fuerza en dos ejes que no son ortogonales"
A23 = "Para construir el paralelogramo, comience en la cola del vector resultante, en este caso $F$ y trace líneas paralelas que formen el paralelogramo. Los lados del paralelogramo que están sobre los ejes, representan las componentes, $F_u$ y $F_v$. La mitad del paralelogramo ilustra la regla del triángulo. Recuerde que los ángulos internos deben sumar 180°"
A24 = "Use la ley de senos o la ley de cosenos para despejar las componentes"
A25 = "Use la ley de senos o la ley de cosenos para despejar la magnitud y la componente desconocida"
A26 = "Use la ley de senos o la ley de cosenos para despejar la magnitud"
A27 = "Primero, halle el ángulo $\\alpha_2$. Para ello, aplique la regla del triángulo y encuentre una ecuación para calcular F2 utilizando la ley de senos. Luego, analice el ángulo entre F1 y F2 que genera que la fuerza F2 es mínima."
A28 = "F2 es mínima cuando F1 y F2 son perpendiculares."
A29 = "Con la ley de senos halle las magnitudes de F1 y F2"
A30 = "Calcule la magnitud y la dirección de la fuerza resultante entre F1 y F3."
A31 = "La fuerza resultante de las tres fuerzas corresponde a la suma de la resultante entre F1 y F3, y F2. Plantee la regla del triángulo, calcule los ángulos internos de forma que FR sea mínima. ¿Qué ángulo forma la fuerza resultante con uno de los lados del triángulo para ser mínima?."
A32 = "Use la ley de senos o el Teorema de Pitágoras para hallar las magnitudes de las fuerzas."

#EQ_V3D_F/M
A33 = "Para hallar las componentes X y Y, proyecte el vector F en el plano XY"
A34 = "Una vez el vector se encuentre en el plano XY, proyecte el vector hacia los ejes X y Y"
A35 = "Considere el sentido de la fuerza en el cálculo de las componentes"
A36 = "Los ángulos directores coordenados se pueden calcular como el arcocoseno de las componentes del vector divididas por la magnitud del vector F"
A37 = "Para encontrar las componentes X y Y, primero proyecte el vector F en el plano XY y luego realice la proyección sobre cada uno de los ejes."
A38 = "La componente Z se puede proyectar directamente con la información dada"
A39 = "Determine el vector F como un vector cartesiano, esto le permitirá identificar cada una de sus componentes. Tenga en cuenta que el dibujo no está a escala."
A40 = "La magnitud de un vector con 3 componentes (X, Y, Z) se define como: $\\sqrt{F_X^2 + F_Y^2 + F_Z^2}$"
A41 = "Los ángulos directores relacionan directamente al vector F con cada uno de los ejes."
A42 = "$\\hat{{i}}$ representa la componente paralela al eje X, $\\hat{{j}}$ a la componente paralela a Y y $\\hat{{k}}$ a la componente paralela a Z."
A43 = "Calcule las componentes de cada eje como la multiplicación de la fuerza por el coseno del ángulo que forma con dicho eje."

#EQ_V3D_M
A44 = "Iguale las componentes dadas a la sumatoria de fuerzas en dichos ejes para formar un sistema de ecuaciones para despejar las magnitudes F1 y F2."
A45 = "Utilice las coordenadas de cada fuerza para determinar el vector unitario o construir un triángulo rectángulo que le permita aplicar el teorema de Pitágoras."
A46 = "Recuerde que, según el teorema de Pitágoras, el coseno de un ángulo $\\alpha$ se define como $cos(\\alpha)=\\dfrac{Cateto\\hspace{{1mm}}adyacente}{Hipotenusa}$. En este caso, el coseno corresponde a $cos(\\alpha)=\\dfrac{Coordenada\\hspace{{1mm}}en\\hspace{{1mm}} X, Y\\hspace{{1mm}} o\\hspace{{1mm}} Z}{Longitud\\hspace{{1mm}} del \\hspace{{1mm}}vector}$"

#EQ_VU_F
A47 = '''
Revise las unidades del ángulo, radianes o grados:  

Para convertir de radianes a grados: $\\alpha_x*\\dfrac{180}{\\pi}$  

Para convertir de grados a radianes: $\\alpha_x*\\dfrac{\\pi}{180}$
'''
A48 = '''
Calcule los ángulos respecto a su eje positivo:  
$\\alpha_x = \\alpha_x$  
$\\alpha_y = \\alpha_x-90°$
'''
A49 = "En un triángulo con un ángulo recto, de lados a y b, la longitud de la hipotenusa se calcula como: $\\sqrt{a^2+b^2}$"
A50 = "Considere que a y b corresponden a los cosenos direccionales"
A51 = "La norma será: $|u| = \\sqrt{(cos(\\alpha_x))^2 + (cos(\\alpha_y))^2)}$."
A52 = "Calcule la longitud de A a B como: $|AB| = \\sqrt{dx^2 + dy^2}$."
A53 = """
Calcule los cosenos direccionales como: 

$cos_x = \\dfrac{{dx}}{{AB}}$  

$cos_y = \\dfrac{{dy}}{{AB}}$
"""
A54 = """
Calcule las componentes como la multiplicación de la magnitud de la fuerza por los cosenos direccionales como: 

$componente i =  \\overrightarrow{{F1}}*\\dfrac{{dx}}{{AB}}$  

$componente j =  \\overrightarrow{{F1}}*\\dfrac{{dy}}{{AB}}$
"""
A55 = "Los ángulos directores coordenados corresponden a los ángulos que relacionan al vector con los ejes x, y, z. Para encontrar estos ángulos, formule el vector unitario en la dirección del vector y determine los cosenos inversos de sus componentes."
A56 = "El vector unitario en la componente del eje ($\\hat{{i}}$ o $\\hat{{j}}$) es equivalente al coseno direccional en dicho eje."
A57 = "El vector unitario se define como $\\lambda_u=\\dfrac{{\\overrightarrow{{u}}}}{{|\\overrightarrow{{u}}|}}$."
A58 = "Compruebe que el vector unitario del eje equivale al coseno direccional en dicho eje. Para ello plantee un triángulo rectángulo cuyos lados sean (X2-X1) y (Y2-Y1)."
A59 = "Realice la sumatoria de fuerzas en X y Y. Determine el vector unitario de F1 y F2."
A60 = "Calcule $\\overrightarrow{{u}}$ como un vector cartesiano. Para ello, calcule la diferencia de coordenadas en X, Y y Z."
A61 = "Calcule $|\\overrightarrow{{u}}|$ como la magnitud del vector. La magnitud de un vector con 3 componentes (X, Y, Z) se define como: $\\sqrt{X^2 + Y^2 + Z^2}$"
A62 = "Calcule las componentes X, Y, Z de la fuerza resultante como la suma de las componentes de cada una de las fuerzas."
A63 = "Halle las componentes de cada una de las fuerzas, para ello, multiplique la magnitud de la fuerza por su vector unitario."
A64 = "Encuentre el vector unitario de los cables AB, AC y AD."
A65 = "Plantee la ecuación de la componente $\\hat{{j}}$ del vector unitario del cable AD."
A66 = "Calcule la componente Y de la fuerza como la multiplicación de la magnitud de la fuerza por el coseno direccional en $y$, es decir, la componente $\\hat{{j}}$ del vector unitario."
A67 = "Plantee la ecuación de cada una de las componentes de la fuerza como la multiplicación de la magnitud de la fuerza y el vector unitario de dicha componente."
A68 = "¿Qué representa la longitud de la cuerda?"
A69 = "Despeje de cada una de las ecuaciones las distancias en X, Y y Z, según corresponda."

#EQ_V2D_F
A70 = "Para garantizar la condición de equilibrio de una partícula, la sumatoria de las fuerzas en cada uno de los ejes debe ser igual a cero."
A71 = "Plantee las ecuaciones de equilibrio correspondientes a la sumatoria de fuerzas en X y Y."
A72 = "Para facilitar el despeje de las magnitudes, intente formar una tangente de uno de los ángulos, lo cual reducirá el número de términos en el proceso de despeje."
A73 = "Realice el diagrama de cuerpo libre (DCL) de la polea."
A74 = "Realice un corte en las cuerdas que sostiene la polea."
A75 = "Plantee las ecuaciones de equilibrio y resuelva."
A76 = "Realice el diagrama de cuerpo libre (DCL) de la polea."
A77 = "Incluya dentro de la sumatoria las componentes de la fuerza que se debe aplicar y resuelva."
A78 = "Dibuje el diagrama de cuerpo libre (DCL) de cada una de las poleas, identifique correctamente los cambios de cuerda entre las poleas."

#MOMENTO EN UN PUNTO
MP1 = "El momento se define como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se calcula desde el punto en el que se evalúa el momento a la línea de acción de la fuerza."
MP2 = "Para calcular el momento en el punto de evaluación, primero obtenga las componentes del vector fuerza $\\overrightarrow{{F}}$ y el vector posición $\\overrightarrow{{r}}$. Luego, identifique la componente de la fuerza que es perpendicular al vector de posición. El momento se calcula como la multiplicación de esta componente perpendicular de la fuerza por la distancia desde el punto de evaluación."
MP3 = "Recuerde utilizar la regla de la mano derecha para definir el signo del momento."
MP4 = "Recuerde que el producto cruz no tiene la propiedad conmutativa. Por lo cual, $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$ no es igual a $\\overrightarrow{{F}}$ X $\\overrightarrow{{r}}$."
MP5 = "Recuerde que los signos de los componentes de $\\overrightarrow{{r}}$  y $\\overrightarrow{{F}}$ son importantes para determinar correctamente la dirección del momento. El vector momento no solo indica magnitud, sino también el eje alrededor del cual se produce la rotación, siendo perpendicular tanto al vector $\\overrightarrow{{r}}$ como al vector $\\overrightarrow{{F}}$."
MP6 = "Para hallar incógnitas, primero identifique los datos disponibles y analice cómo se relacionan entre sí."
MP7 = "Se puede dividir el problema en las componentes del momento $\\hat{{i}}$, $\\hat{{j}}$ y $\\hat{{k}}$, y resolver de manera independiente."

#MOMENTO ALREDEDOR DE UN EJE
MAE1 = """Los pasos generales para calcular el momento alrededor de un eje son:   
1. Calcular el momento en un punto $\\overrightarrow{{M_O}}$ que está sobre el vector unitario del eje.
2. Para calcular el momento que actúa sobre el eje, se proyecta el vector momento $\\overrightarrow{{M_O}}$ sobre el vector unitario del eje $\\overrightarrow{{\\lambda}}$. Esta proyección se realiza con producto punto."""
MAE2 = "El momento en un punto se calcula como $\\overrightarrow{{r}}$ X $\\overrightarrow{{F}}$. El vector posición $\\overrightarrow{{r}}$ se define desde el punto en el que se evalúa el momento hasta cualquier punto de la línea de acción de la fuerza."
MAE3 = "El producto punto se utiliza para la proyección entre vectores. Si $\\vec{{v}} = (x_1,y_1,z_1)$ y $\\vec{{u}} = (x_2,y_2,z_2)$, entonces: $\\vec{{v}} \\cdot \\vec{{u}} = (x_1)(x_2) + (y_1)(y_2) + (z_1)(z_2)$."
MAE4 = "Recuerde que $\\vec{r}$ es el vector de posición medido desde el punto de evaluación hasta cualquier punto de la línea de acción de la fuerza."
MAE5 = "El momento con respecto a un punto se define como $\\vec{r} X \\vec{F}$. Si $\\vec{r} = x\\hat{i} + y\\hat{j} + z\\hat{k}$ y $\\vec{F} = a\\hat{i} + b\\hat{j} + c\\hat{k}$, entonces $\\vec{M} = (yc-bz)\\hat{i} - (xc-az)\\hat{j} + (xb-ay)\\hat{k}$."

#MOMENTO PAR
MPP1 = "El momento generado por un par de fuerzas se define como $M = F \\cdot d$, donde $F$ es la magnitud de las fuerzas pares y $d$ es la distancia perpendicular entre estas"
MPP2 = "Encuentre la distancia perpendicular entre las fuerzas utilizando el triángulo dado."
MPP3 = "Recuerde que la distancia dada está en $cm$; realice la conversión a $m$ antes de calcular el momento."
MPP4 = "Recuerde que el momento generado por un par de fuerzas no está asociado a un punto específico del cuerpo, su efecto se siente de igual manera en todos los puntos del cuerpo."
MPP5 = "De acuerdo con la ecuación del momento generado por un par de fuerzas, la magnitud de la fuerza se puede determinar como $F = \\dfrac{{M}}{{d}}$."
MPP6 = "Realice la sumatoria de momentos generados por las fuerzas $F_1$ y $F_2$, e iguale el resultado al momento total proporcionado en el enunciado. A partir de esta ecuación, determine la magnitud de la fuerza $F_2$."
MPP7 = "Realice la sumatoria de momentos generados por las fuerzas $F_1$ y $F_2$ por cada una de sus componentes."

#INCERTIDUMBRE
I1 = "La distribución acumulada de una variable aleatoria $(X)$ proporciona información sobre la probabilidad de ocurrencia de dicha variable, es decir, la probabilidad de que $X$ tome un valor menor o igual al que se está evaluando ($P(X \\leq x)).$"
I2 = "La probabilidad de excedencia es la probabilidad de que la variable aleatoria $X$ tome un valor mayor al que se está evaluando."
I3 = "La probabilidad de excedencia se calcula como: $P(X > x) = 1-P(X \\leq x)$."
I4 = "Para determinar el valor de la variable aleatoria $X$ asociada a una probabilidad de ocurrencia dada, primero ubique dicha fuerza en el eje $X$ y proyecte su correspondiente valor en el eje $Y$. Este será el valor buscado."
I5 = "La probabilidad de ocurrencia de un valor en evaluación corresponde a la probabilidad acumulada hasta ese punto. Es decir, es la probabilidad de que la variable aleatoria $X$ tome un valor menor o igual al evaluado ($P(X \\leq x)).$"
I6 = "Para determinar la probabilidad de ocurrencia de un valor específico de la variable aleatoria $X$ a partir de su función de densidad, es necesario calcular el área bajo la curva de densidad desde su inicio hasta el valor en evaluación."
I7 = "Para hallar la probabilidad de ocurrencia correspondiente a la probabilidad de excedencia dada, calcule la ecuación de la recta y despeje el valor de la variable solicitada."

#CERCHAS
C1 = "El grado de un apoyo corresponde al número de reacciones que genera. Si es de primer grado tiene una reacción perpendicular a la superficie. Si es de segundo grado tiene dos restricciones, impidiendo la traslación en cualquier direccion. Si es de tercer grado tiene tres restricciones, evitando la traslación y la rotación."
C2 = "Para determinar las reacciones se deben considerar las condiciones de equilibrio del sistema, es decir, la sumatoria de fuerzas en cualquier dirección debe ser cero y la sumatoria de momentos con respecto a cualquier punto debe ser cero."
C3 = "Uno de los métodos para analizar las fuerzas en los elementos de una cercha es el Método de los Nodos, que consiste en evaluar el equilibrio de fuerzas en cada nodo. Para realizar el análisis de manera efectiva, es importante dibujar el diagrama de cuerpo libre del nodo, en el cual se incluyan todas las fuerzas que actúan sobre él."
C4 = "Revisar el equilibrio de cada nodo para determinar cuáles elementos deben tener fuerza cero y así cumplir con la condición de equilibrio. No es necesario involucrar cálculos."
C5 = "Una manera de identificar los elementos de fuerza cero es localizar aquellos que son colineales entre sí y no tienen una carga externa aplicada. Según las condiciones de equilibrio, el elemento que es perpendicular a los colineales será un elemento de fuerza cero."
C6 = "Un miembro sometido a compresión ejerce una fuerza hacia el nodo (la fuerza entra al nodo). Por el contrario, un miembro sometido a tensión genera una fuerza que hala hacia afuera del nodo (la fuerza sale del nodo)."
C7 = "Uno de los métodos para analizar las fuerzas en los elementos de las cerchas es el Método de secciones. Este método se basa en el principio de que, si la armadura está en equilibrio, cualquier parte de ella lo estará."

#MARCOS
MA1 = "Para comprender mejor el ejercicio, es útil desensamblar los elementos del marco y dibujar un diagrama de cuerpo libre para cada uno."
MA2 = "Una vez se despiezan los elementos, las reacciones en los pasadores son visibles. Para que haya equilibrio en el pasador, las reacciones sobre el pasador deben ser opuestas entre los dos elementos conectados. Por ejemplo, si en el elemento 1 la reacción $R_y$ es positiva, en el elemento 2 la reacción $R_y$ es negativa."
MA3 = "Cada elemento debe cumplir las condiciones de equilibrio, es decir, la sumatoria de fuerzas en cualquier dirección debe ser cero y que la sumatoria de momentos respecto a cualquier punto también debe ser cero."
MA4 = "Para encontrar las reacciones de los apoyos, es útil verficar el equilibrio global de la estructura."

#SISTEMAS EQUIVALENTES
SE1 = """Dos sistemas ($A$ y $B$) son equivalentes si se cumplen las siguientes condiciones:
1. $∑ F_{{yA}} = ∑ F_{{yB}}$
2. $∑ F_{{xA}} = ∑ F_{{xB}}$
3. $∑ M_A = ∑ M_B$
"""
SE2 = "La fuerza resultante será equivalente a la suma de todas las fuerzas aplicadas en el sistema, mientras que el momento de la fuerza resultante será igual a la suma de los momentos originales en un punto."
SE3 = "Para determinar la ubicación de la fuerza resultante con respecto a un punto de referencia, se utiliza la condición de que el momento producido por la fuerza resultante respecto a dicho punto debe ser igual a la sumatoria de los momentos generados por las fuerzas originales del sistema con respecto al mismo punto."
SE4 = "La fuerza resultante será equivalente a la suma de todas las fuerzas aplicadas en el sistema."
SE5 = "El par equivalente de un sistema equivalente fuerza-par se calcula sumando los momentos de las fuerzas originales respecto al punto de referencia."
SE6 = "El momento de la fuerza resultante será igual a la suma de los momentos originales en un punto."

#CENTROIDES
CT1 = "Las figuras complejas pueden dividirse en formas más simples cuyos centroides son conocidos o fáciles de encontrar."
CT2 = """
El centroide representa el centro geométrico de un objeto. Para calcular las coordenadas del centroide de un área compuesta se utilizan las siguientes ecuaciones:   

$\\bar{{X}} = \\dfrac{{\\sum{{\\bar{{X_i}} \\cdot A_i}}}}{{\\sum{{A_i}}}}$      

$\\bar{{Y}} = \\dfrac{{\\sum{{\\bar{{Y_i}} \\cdot A_i}}}}{{\\sum{{A_i}}}}$         

Donde:     
$\\bar{{X}}$ = Coordenada X del centroide de la figura compuesta    
$\\bar{{Y}}$ = Coordenada Y del centroide de la figura compuesta    
$i$ = Elementos de la figura conocida, una vez se divide la figura compuesta.   
$A$ = Área de la figura   
"""
CT3 = "Un recurso útil para visualizar y organizar los datos es la creación de una tabla con las áreas y las coordenadas de los centroides de cada elemento."
CT4 = """El centro de masa representa el promedio de las posiciones de cada punto o segmento de un objeto, ponderado según sus masas. Para calcular las coordenadas se utilizan las siguientes ecuaciones:

$\\bar{{X}} = \\dfrac{{\\sum{{\\bar{{X_i}} \\cdot M_i}}}}{{\\sum{{M_i}}}}$      

$\\bar{{Y}} = \\dfrac{{\\sum{{\\bar{{Y_i}} \\cdot M_i}}}}{{\\sum{{M_i}}}}$         

Donde:     
$\\bar{{X}}$ = Coordenada X del centroide del elemento.  
$\\bar{{Y}}$ = Coordenada Y del centroide del elemento.    
$i$ = Índice de cada elemento.     
$M$ = Masa del elemento. 
"""
CT5 = "El centro de masa es el punto en el cual se puede considerar que toda la masa del cuerpo está concentrada para los análisis de equilibrio."
CT6 = "Un recurso útil para vizualizar y organizar los datos es la creación de una tabla con las masas y las coordenadas de los centroides de cada elemento."
CT7 = """
El centroide representa el centro geométrico de un objeto. Para calcular las coordenadas del centroide de un objeto lineal compuesto se utilizan las siguientes ecuaciones:   

$\\bar{{X}} = \\dfrac{{\\sum{{\\bar{{X_i}} \\cdot L_i}}}}{{\\sum{{L_i}}}}$      

$\\bar{{Y}} = \\dfrac{{\\sum{{\\bar{{Y_i}} \\cdot L_i}}}}{{\\sum{{L_i}}}}$         

Donde:     
$\\bar{{X}}$ = Coordenada X del centroide de la figura compuesta.        
$\\bar{{Y}}$ = Coordenada Y del centroide de la figura compuesta.      
$i$ = Elementos de la figura conocida, una vez se divide la figura compuesta.       
$L$ = Longitud del segemento.   
"""
CT8 = "El centroide es el punto en el que se puede apoyar un objeto de material uniforme y mantenerse en equilibrio."


#FUERZAS DISTRIBUIDAS
FD1 = "La magnitud de la fuerza resultante es igual al área bajo la curva de la fuerza distribuida."
FD2 = "La localización de la fuerza resultante se encuentra en el centroide de la fuerza distribuida."
FD3 = "Para simplificar el problema, se puede dividir el área bajo la curva de la distribución en figuras más sencillas."
FD4 = "Realice la sumatoria de fuerzas y momentos globales para encontrar las reacciones en los apoyos."
FD5 = "La fuerza es el área bajo la curva de la integral, se calcula mediante la expresión: $\\int dA$."
FD6 = "El centroide de la carga distribuida se calcula con la siguiente expresión: $\\dfrac{{\\int x \\cdot dA \\text{{ }}}}{{\\int dA \\text{{ }}}}$."
FD7 = "Determine la fuerza generada por cada una de las secciones en que se divide la carga distribuida, teniendo en cuenta la geometría de cada una. Además, calcule la posición del centroide correspondiente a cada sección."


#PRESIONES HIDROSTÁTICAS
PH1 = "La presión hidrostática es la presión ejercida por un fluido en reposo. Esta presión se genera en todos los puntos del fluido y actúa perpendicularmente a las superificies sumergidas."
PH2 = """
La presión hidrostática aumenta con la profundidad y medida como una fuerza por área unitaria se calcula como:   

$P = \\rho \\cdot g \\cdot h$   

Donde:

$\\rho$ = la densidad del fluido.      
$g$ = Aceleración debido a la gravedad.      
$h$ = Profundidad desde la superficie al punto a evaluar.    
"""
PH3 = """
La fuerza resultante debida a una distribución lineal (triangular) de presión hidrostática sobre una superficie se calcula mediante:    

$F_R = \\dfrac{{P \\cdot h \\cdot a}}{{2}}$     

Donde:     
$P$ = Presión hidrostática distribuida sobre la superficie.      
$h$ = Profundidad desde la superficie al punto a evaluar. 
$a$ = Ancho de la estructura.  
"""
PH4 = "Las dimensiones mínimas que debe tener una presa, o el nivel máximo de agua permitido para evitar el volcamiento, se determinan a partir de la sumatoria de momentos de las fuerzas actuantes (peso de la presa y presión hidrostática del agua) respecto al extremo en el que puede ocurrir el volcamiento."
PH5 = "La presión sobre las compuertas ubicadas por debajo del nivel de la superficie se distribuye de forma trapezoidal."


#EMPUJE DEL SUELO
ES1 = "Para el cálculo de la presión horizontal del suelo, se debe considerar el coeficiente de presión lateral de tierra $k$. La presión horizontal del suelo a una profundidad $h$ se expresa como: $P = k \\cdot \\gamma_s \\cdot h$."
ES2 = "La distribución de la presión horizontal del suelo es de forma triangular, y la fuerza resultante del empuje actúa a un tercio de la altura desde la base del triángulo."
ES3 = "Para verificar la estabilidad frente al volcamiento, se debe comprobar que el momento resistente sea mayor o igual al momento actuante."

#FUERZAS INTERNAS
FI1 = "Antes de determinar las fuerzas internas, identifique todas las fuerzas externas que actúan sobre la viga y las reacciones en los apoyos."
FI2 = "Para calcular las fuerzas cortantes y los momentos flectores en un punto específico, se reliza un corte en dicho punto, se realiza un diagrama de cuerpo libre de la nueva sección con las fuerzas internas, y se aplican las ecuaciones de equilibrio."
FI3 = "Cuando se realiza un corte, la convención indica que en el lado izquierdo el cortante es negativo y el momento flector es positivo. Para que exista equilibrio, en el lado derecho el cortante es positivo y el momento flector es negativo."
FI4 = "Para resolver este ejercicio, se recomienda expresar en valor absoluto tanto el momento flector interno máximo en el tramo $AB$ como el momento flector en el punto $B$ en función de las variables $w$, $d_1$ y $d_2$."
FI5 = "Después de realizar el corte, seleccione la sección que permita encontrar las fuerzas internas más fácilmente."

#------------------------------------- Textos para las respuestas ---------------------------------------

#EQ_V2D_D
T1 = f"""
        A continuación se presenta la solución sugerida para el ejercicio:   

        $\\textbf{{\\small 1. Aplicación de la Ley del paralelogramo o la Regla del triángulo:}}$

        El ángulo $\\alpha_3$ corresponde a${{\hspace{{4mm}}\\alpha_3 = 180 - \\alpha_1 - \\alpha_2}}$
    """

T2 = f"""
        A continuación se presenta la solución sugerida para el ejercicio:   

        $\\textbf{{\\small 1. Cálculo del ángulo:}}$

        Primero, se aplica la regla del triángulo y se plantea mediante la ley de senos la ecuación para hallar F2:
    """

T3 = f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Diagrama de cuerpo libre de la polea:}}$
    """




#----------------------------------- Funciones para las respuestas --------------------------------------

def rta_EQ_V2D_F_P2(f, calc, version):
    return f"""
    La descomposición del vector F1 depende de su magnitud y ángulo. Se sugiere el siguiente método para la solución del ejercicio:

    $\\textbf{{\\small 1. Componente de la fuerza con respecto al eje X:}}$

    ${{\hspace{{4mm}}F1_x = |\\overrightarrow{{F1}}| \\cdot \\cos(\\alpha_x) \\text{{ = }}}}{f[0]:.0f}{{\\text{{ kN}}\\hspace{{1mm}}\\cdot\\hspace{{1mm}}}}{calc[f'cos{version}']:.2f}{{\\text{{ = }}}}{f[0]*calc[f'cos{version}']:.2f}{{ \\text{{ kN}}}}$
    
    $\\textbf{{\\small 2. Componente de la fuerza con respecto al eje Y:}}$

    ${{\hspace{{4mm}}F1_y = |\\overrightarrow{{F1}}| \\cdot \\sin(\\alpha_x) \\text{{ = }}}}{f[0]:.0f}{{\\text{{ kN}}\\hspace{{1mm}}\\cdot\\hspace{{1mm}}}}{calc[f'sin{version}']:.2f}{{\\text{{ = }}}}{f[0]*calc[f'sin{version}']:.2f}{{ \\text{{ kN}}}}$
    """

def rta_EQ_V2D_F_P3(ax, ay, bx, by):
    return f"""
    A continuación se presenta la solución sugerida para el ejercicio:

    $\\textbf{{\\small 1. Cálculo de la diferencia de coordenadas en X y Y:}}$

    ${{\hspace{{4mm}}dx \\text{{ = }}}} {bx:.0f} {{\\text{{ - (}}}} {ax:.2f} {{\\text{{) = }}}} {bx-ax:.0f}$  
    ${{\hspace{{4mm}}dy \\text{{ = }}}} {by:.0f} {{\\text{{ - (}}}} {ay:.2f} {{\\text{{) = }}}} {by-ay:.0f}$ 

    $\\textbf{{\\small 2. Cálculo de la pendiente:}}$
        
    ${{\hspace{{4mm}} m = \\dfrac{{dy}}{{dx}} = \\dfrac{{{by-ay}}}{{{bx-ax}}} = {(by-ay)/(bx-ax):.2f}}}$
    """

def rta_EQ_V2D_F_P4(ax, ay, bx, by):
    return f"""
    A continuación se presenta la solución sugerida para el ejercicio:

    $\\textbf{{\\small 1. Cálculo de la diferencia de coordenadas en X y Y:}}$

    ${{\hspace{{4mm}}dx \\text{{ = }}}} {bx:.0f} {{\\text{{ - (}}}} {ax:.2f} {{\\text{{) = }}}} {bx-ax:.0f}$  
    ${{\hspace{{4mm}}dy \\text{{ = }}}} {by:.0f} {{\\text{{ - (}}}} {ay:.2f} {{\\text{{) = }}}} {by-ay:.0f}$ 

    $\\textbf{{\\small 2. Cálculo de la magnitud:}}$
        
    ${{\hspace{{4mm}} |\\overrightarrow{{F1}}| = \\sqrt{{dx^2+dy^2}} = {math.sqrt((by-ay)**2+(bx-ax)**2):.2f}}}$

    Este resultado implica que el vector cartesiano de $\\overrightarrow{{F1}}$ es: $\\overrightarrow{{F1}} = ({bx-ax}) \\hat{{i}} + ({by-ay}) \\hat{{j}}$.
    """

def rta_EQ_V2D_M_P1(F1x, F1y, F2x, F2y, calc, a1,a2):
    return f"""
    La fuerza resultante corresponde a la suma de los dos vectores. Se sugiere para la solución del ejercicio el siguiente método:

    $\\textbf{{\\small 1. Descomposición de los vectores F1 y F2:}}$

    ${{\hspace{{4mm}} F1_x = F1*cos(\\alpha_1) = {F1x*calc[f'cos{a1}']:.2f} \\text{{ kN}} }}$  
    ${{\hspace{{4mm}} F1_y = F1*sen(\\alpha_1) = {F1y*calc[f'sin{a1}']:.2f} \\text{{ kN}} }}$  
    ${{\hspace{{4mm}} F2_x = F2*cos(\\alpha_2) = {F2x*calc[f'cos{a2}']:.2f} \\text{{ kN}} }}$  
    ${{\hspace{{4mm}} F2_y = F2*sen(\\alpha_2) = {F2y*calc[f'sin{a2}']:.2f} \\text{{ kN}} }}$  
	    
    $\\textbf{{\\small 2. Sumatoria en X y Y:}}$  

    ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = F1_x + F2_x = {F1x*calc[f'cos{a1}']+F2x*calc[f'cos{a2}']:.2f} \\text{{ kN}} }}$  
    ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{RY}} = F1_y + F2_y = {F1y*calc[f'sin{a1}']+F2y*calc[f'sin{a2}']:.2f} \\text{{ kN}} }}$  
       
    $\\textbf{{\\small 3. Cálculo de la magnitud:}}$

    ${{\hspace{{4mm}} |\\overrightarrow{{F_R}}|=\\sqrt{{F_{{RX}}^2+F_{{RY}}^2}} = {Calculations.magnitude(F1x*calc[f'cos{a1}']+F2x*calc[f'cos{a2}'],F1y*calc[f'sin{a1}']+F2y*calc[f'sin{a2}']):.2f} \\text{{ kN}}}}$

    $\\textbf{{\\small 4. Cálculo de la dirección:}}$

    ${{\hspace{{4mm}} \\alpha_R ={Calculations.define_angle(F1x*calc[f'cos{a1}']+F2x*calc[f'cos{a2}'],F1y*calc[f'sin{a1}']+F2y*calc[f'sin{a2}']):.2f}° }}$

    El cálculo del ángulo respecto al eje x positivo depende del cuadrante en el que se encuentra el vector:

    -Primer cuadrante:  $tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$  
    -Segundo cuadrante: $180 - tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$  
    -Tercer cuadrante:  $180 + tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$  
    -Cuarto cuadrante:  $360 - tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$ 
    """

def rta_EQ_V2D_M_P2(F1x, F1y, F2x, F2y, calc, a1,a2):
    return f"""
    La fuerza resultante corresponde a la suma de los dos vectores. Se sugiere para la solución del ejercicio el siguiente método:

    $\\textbf{{\\small 1. Descomposición de los vectores F1 y F2:}}$

    ${{\hspace{{4mm}} F1_x = F1*sen(\\alpha_1) = {F1x*calc[f'sin{a2}']:.2f} \\text{{ kN}} }}$  
    ${{\hspace{{4mm}} F1_y = F1*cos(\\alpha_1) = {F1y*calc[f'cos{a2}']:.2f} \\text{{ kN}} }}$  
    ${{\hspace{{4mm}} F2_x = F2*cos(\\alpha_2) = {F2x*calc[f'cos{a1}']:.2f} \\text{{ kN}} }}$  
    ${{\hspace{{4mm}} F2_y = F2*sen(\\alpha_2) = {F2y*calc[f'sin{a1}']:.2f} \\text{{ kN}} }}$  
	    
    $\\textbf{{\\small 2. Sumatoria en X y Y:}}$  

    ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = F1_x + F2_x = {F1x*calc[f'sin{a2}']+F2x*calc[f'cos{a1}']:.2f} \\text{{ kN}} }}$  
    ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{RY}} = F1_y + F2_y = {F1y*calc[f'cos{a2}']+F2y*calc[f'sin{a1}']:.2f} \\text{{ kN}} }}$  
       
    $\\textbf{{\\small 3. Cálculo de la magnitud:}}$

    ${{\hspace{{4mm}} |\\overrightarrow{{F_R}}|=\\sqrt{{F_{{RX}}^2+F_{{RY}}^2}} = {Calculations.magnitude(F1x*calc[f'sin{a2}']+F2x*calc[f'cos{a1}'],F1y*calc[f'cos{a2}']+F2y*calc[f'sin{a1}']):.2f} \\text{{ kN}}}}$

    $\\textbf{{\\small 4. Cálculo de la dirección:}}$

     ${{\hspace{{4mm}} \\alpha_R ={Calculations.define_angle(F1x*calc[f'sin{a2}']+F2x*calc[f'cos{a1}'],F1y*calc[f'cos{a2}']+F2y*calc[f'sin{a1}']):.2f}° }}$

    El cálculo del ángulo respecto al eje x positivo depende del cuadrante en el que se encuentra el vector:

    -Primer cuadrante:  $tan^{-1}\\left(\\dfrac{{F_{{RY}}}}{{F_{{RX}}}}\\right)$  

    -Segundo cuadrante: $180 - tan^{-1}\\left(\\dfrac{{F_{{RY}}}}{{F_{{RX}}}}\\right)$  

    -Tercer cuadrante:  $180 + tan^{-1}\\left(\\dfrac{{F_{{RY}}}}{{F_{{RX}}}}\\right)$  

    -Cuarto cuadrante:  $360 - tan^{-1}\\left(\\dfrac{{F_{{RY}}}}{{F_{{RX}}}}\\right)$ 
    """

def rta_EQ_V2D_D_P1(f, a, calc):
    return f"""
    $\\textbf{{\\small 2. Aplicación de la Ley de senos para hallar las componentes:}}$  

    $\\underline{{Componente \\hspace{{2mm}} u}}$    

    ${{\hspace{{4mm}} \\dfrac{{F_u}}{{sen(\\alpha_1)}} = \\dfrac{{F}}{{sen(\\alpha_3)}}}}$      

    ${{\hspace{{4mm}} F_u = \\dfrac{{F*sen(\\alpha_1)}}{{sen(\\alpha_3)}}}}$    

    ${{\hspace{{4mm}} F_u = {(f[0]*calc['sin1'])/Calculations.sine(180-a[0]-a[4]):.2f} \\text{{kN}}}}$       

    $\\underline{{Componente \\hspace{{2mm}} v}}$     

    ${{\hspace{{4mm}} \\dfrac{{F_v}}{{sen(\\alpha_2)}} = \\dfrac{{F}}{{sen(180-\\alpha_1-\\alpha_2)}}}}$   

    ${{\hspace{{4mm}} F_v = \\dfrac{{F*sen(\\alpha_2)}}{{sen(180-\\alpha_1-\\alpha_2)}}}}$     

    ${{\hspace{{4mm}} F_v = {(f[0]*calc['sin5'])/Calculations.sine(180-a[0]-a[4]):.2f} \\text{{kN}} }}$    
    """

def rta_EQ_V2D_D_P2(f, a, calc):
    return f"""
    $\\textbf{{\\small 2. Aplicación de la Ley de senos para hallar la magnitud de F y la componente desconocida:}}$  

    $\\underline{{Magnitud \\hspace{{2mm}} F}}$  

    ${{\hspace{{4mm}} \\dfrac{{F}}{{sen(\\alpha_3)}} = \\dfrac{{F_v}}{{sen(\\alpha_2)}}}}$

    ${{\hspace{{4mm}} F = \\dfrac{{F_v*sen(\\alpha_3)}}{{sen(\\alpha_2)}}}}$

    ${{\hspace{{4mm}} F = {(f[0]*Calculations.sine(180-a[0]-a[4]))/calc['sin5']:.2f} \\text{{ kN}}}}$

    $\\underline{{Componente \\hspace{{2mm}} u}}$  

    ${{\hspace{{4mm}} \\dfrac{{F_u}}{{sen(\\alpha_1)}} = \\dfrac{{F_v}}{{sen(\\alpha_2)}}}}$

    ${{\hspace{{4mm}} F_u = \\dfrac{{F_v*sen(\\alpha_1)}}{{sen(\\alpha_2)}}}}$

    ${{\hspace{{4mm}} F_u = {(f[0]*calc['sin1'])/calc['sin5']:.2f} \\text{{ kN}}}}$
    """

def rta_EQ_V2D_D_P3(f, a, calc):
    return f"""
    $\\textbf{{\\small 2. Aplicación de la Ley de senos para hallar la magnitud de F:}}$  

    ${{\hspace{{4mm}} \\dfrac{{F_u}}{{sen(\\alpha_v)}} = \\dfrac{{F}}{{sen(\\alpha_w)}}}}$   

    ${{\hspace{{4mm}} F = \\dfrac{{F_u*sen(\\alpha_w)}}{{sen(\\alpha_v)}}}}$

    ${{\hspace{{4mm}} F = {(f[0]*Calculations.sine(180-a[0]-a[8]))/calc['sin9']:.2f} \\text{{ kN}}}}$

    $\\textbf{{\\small 3. Cálculo de las componentes X y Y:}}$

    ${{\hspace{{4mm}} F_x = F*sen(\\alpha_Y) = {((f[0]*Calculations.sine(180-a[0]-a[8]))/calc['sin9'])*calc['sin5']:.2f} \\text{{kN}}}}$

    ${{\hspace{{4mm}} F_y = F*cos(\\alpha_Y) = {((f[0]*Calculations.sine(180-a[0]-a[8]))/calc['sin9'])*calc['cos5']:.2f} \\text{{kN}}}}$
    """

def rta_EQ_V2D_D_P4(f, a, calc):
    return f"""
    ${{\hspace{{4mm}} \\dfrac{{FR}}{{sen(\\alpha_3)}} = \\dfrac{{F2}}{{sen(\\alpha_1)}}}}$

    ${{\hspace{{4mm}} F2 = \\dfrac{{FR*sen(\\alpha_1)}}{{sen(\\alpha_3)}}}}$

    Al analizar la fórmula F2 para despejar F2, se observa que a medida que el denominador disminuye, F2 se convierte en un máximo. Por tanto, es necesario maximizar el denominador, en este caso es 1, esto se logra cuando $\\alpha_3$ es 90°. 
    De lo anterior, se concluye que F2 es mínima cuando F1 y F2 son perpendiculares. Teniendo en cuenta esto $\\alpha_3$ se calcula como:

    ${{\hspace{{4mm}} \\alpha_2 = 180° - \\alpha_3 - \\alpha_1 = {180-a[0]-90:.0f}°}}$


    $\\textbf{{\\small 2. Cálculo de las magnitudes F1 y F2:}}$  

    $\\underline{{Magnitud \\hspace{{2mm}} F1}}$  

    ${{\hspace{{4mm}} \\dfrac{{F1}}{{sen(\\alpha_2)}} = \\dfrac{{FR}}{{sen(\\alpha_3)}}}}$

    ${{\hspace{{4mm}} F1 = \\dfrac{{FR*sen(\\alpha_2)}}{{sen(90)}}}}$

    ${{\hspace{{4mm}} F1 = {(f[0]*Calculations.sine(180-a[0]-90)):.2f} \\text{{kN}}}}$

    $\\underline{{Magnitud \\hspace{{2mm}} F2}}$  

    ${{\hspace{{4mm}} \\dfrac{{FR}}{{sen(\\alpha_3)}} = \\dfrac{{F2}}{{sen(\\alpha_1)}}}}$

    ${{\hspace{{4mm}} F2 = \\dfrac{{FR*sen(\\alpha_1)}}{{sen(\\alpha_3)}}}}$

    ${{\hspace{{4mm}} F2 = {(f[0]*Calculations.sine(a[0])):.2f} \\text{{kN}}}}$
    """

def rta_EQ_V2D_D_P5_P1(fx1, fy1, a): #Pregunta Equilibrio de partículas, vectores 2D, nivel de complejidad díficil, pregunta 5, parte 1
    return f"""
    A continuación se presenta la solución sugerida para el ejercicio:
    
    $\\textbf{{\\small 1. Cálculo de la magnitud de la fuerza resultante entre F1 y F3:}}$

    ${{\hspace{{4mm}}  |\\overrightarrow{{FR'}}| = \\sqrt{{(F1_x + F3_x)^2+(F1_y + F3_y)^2}}}}$    
    ${{\hspace{{4mm}}  |\\overrightarrow{{FR'}}| = {Calculations.magnitude(fx1,fy1):.2f} \\text{{ kN}} }}$

    $\\textbf{{\\small 2. Cálculo de la dirección de la fuerza resultante entre F1 y F3:}}$

    ${{\hspace{{4mm}} \\theta = tan^{{-1}} \\left(\\dfrac{{F1_y + F3_y}}{{F1_x + F3_x}}\\right)}}$     
    ${{\hspace{{4mm}} \\theta = {Calculations.define_angle(fx1,fy1):.2f}°}}$

    $\\textbf{{\\small 3. Construcción de la regla del triángulo:}}$

    Para el cálculo de los ángulos internos considere que:     
    ${{\hspace{{4mm}} \\theta_1 = 180-\\theta_2-\\theta_3}}={180-90-85:.0f}°$
    ${{\hspace{{4mm}} \\theta_2 = 90°}} \\text{{. La fuerza resultante mínima es perpendicular a una de las fuerzas de la sumatoria.}}$
    ${{\hspace{{4mm}} \\theta_3 = \\alpha_1 + \\theta = {85:.0f}}}°$
    """

def rta_EQ_V2D_D_P5_P2(fx1, fy1, a): #Pregunta Equilibrio de partículas, vectores 2D, nivel de complejidad díficil, pregunta 5, parte 2
    return f"""
    $\\textbf{{\\small 4. Cálculo de la magnitud de la fuerza resultante entre F1 y F3:}}$

    ${{\hspace{{4mm}} \\dfrac{{FR}}{{sen(\\theta_3)}} = \\dfrac{{FR'}}{{sen(\\theta_2)}}}}$

    ${{\hspace{{4mm}} FR = \\dfrac{{FR'*sen(\\theta_3)}}{{sen(\\theta_2)}}}}$

    ${{\hspace{{4mm}} FR = {Calculations.magnitude(fx1,fy1)*Calculations.sine(85):.2f} \\text{{ kN}}}}$

    $\\textbf{{\\small 5. Cálculo de la magnitud de F2:}}$

    ${{\hspace{{4mm}} \\dfrac{{F2}}{{sen(\\theta_1)}} = \\dfrac{{FR'}}{{sen(\\theta_2)}}}}$

    ${{\hspace{{4mm}} F2 = \\dfrac{{FR'*sen(\\theta_1)}}{{sen(\\theta_2)}}}}$

    ${{\hspace{{4mm}} F2 = {Calculations.magnitude(fx1,fy1)*Calculations.sine(180-90-85):.2f} \\text{{ kN}}}}$
    """


