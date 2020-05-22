#### Teoría de los termistores
El termistor es un elemento semiconductor, cuya resistencia es función de la temperatura. A diferencia de lo que ocurre con los metales la variación de de temperatura es mucho más abrupta. En los metales se tiene un comportamiento lineal, mientras que en los termistores es de tipo exponencial. Como dato histórico, la primera evidencia de los termistores la realizó Faraday, cuando investigaba las propiedades del sulfuro de plata.

Se tienen dos tipos de termistores:
* Los NTC (_Negative thermal coefficient_), cuya resistencia disminuye ante un aumento de la temperatura
* Los PTC (_Postitive thermal coefficient_), cuya resistencia aumenta ante un aumento de la temperatura.

El modelo más aceptado para describir el comportamiento de un termistor es el de Steinhart-Hart:
$$R (T) = R_{0}e^{B (\frac{1}{T}-\frac{1}{T_{0}})}$$

o en forma equivalente,
$$\frac{1}{T} = \frac{1}{T_{0}} + \frac{1}{B}\ln (\frac{R}{R_{0}})$$

El parámetro $R_{0}$ es el valor de resistencia a $T_{0}$ (298.15K)

#### Análisis de datos del circuito
**¿Qué es lo que esperamos que hagan?**
Analizar el circuito que propuso la oceanógrafa. Planteen la malla correspondiente y analicen las caídas de potencial.

![circuito_1](circuito_termistor_1.png)

Graficar la diferencia de potencial del termistor en función de la temperatura.

![v_termistor](v_term_temperatura.png)

Una vez descripto el circuito eléctrico, tienen que graficar la resistencia del termistor en función de la temperatura. Además realizar un ajuste sobre los datos experimentales, con el modelo de Steinhart-Hart.

![r_termistor](R_term_temperatura.png)

**Importante:** Reportar los parámetros que se obtienen del modelo, expresar las unidades de cada uno de ellos y con su correspondiente incerteza.

**Segunda Parte** (Propagación de errores)

Hacer la malla del circuito, determinar Vt en función de los parámetros del problema. No olvidar de reportar el valor de Vt y
