## Repositorio de Física 3 unsam
Acá pretendemos escribir algunos de los lineamientos para las prácticas de laboratorio y los informes que tienen que realizar los estudiantes

#### Resistencia en metales
Es usual hacer referencia a un _coeficiente de temperatura_ para describir la dependencia con la temperatura de los distintos materiales. En el caso de los metales se observa que este coeficiente es constante y que por lo tanto existe una relación lineal con la temperatura. La resistencia de un material es entonces,

$$ R(T) = R(T_{0}) \{1 + \alpha \Delta T \} = R(T_{0}) \{1 + \alpha (T-T_{0}) \}$$

En donde $T_{0}$ es la temperatura ambiente, 298.15 K, mientras que $R(T_{0})$ es el valor de resistencia a dicha temperatura.

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

### Algunos comandos para git
Algunos comandos para una carpeta que ya tenemos con archivos
1. Abrimos una terminal en esa carpeta y tipeamos
```console
foo@bar:~$ git init
```
2. Con esto hemos iniciado el repositorio. Aquí un breve esquema de como es el flujo de trabajo en este sistema de versionado. Tenemos tres instancias una el direcotrio de trabajo, luego el index que es una zona intermedia y finalmente el commit que nos deja con la "última versión" del proyecto.
![git working flux](git.png)
3. Una vez que iniciamos el repositorio pasamos a agregar los archivos en los que hemos estado trabajando. Lo hacemos mediante el comando add,
```console
foo@bar:~$ git add .
```
4. Cuando estamos conformes con el nivel de desarrollo logrado podemos actualizar todo el repositorio y establecer una nueva versión de nuestro proyecto. Para ello recurrimos al comando commit. No olvidar de hacer una breve descripción de la nueva versión, en el editor de texto que se despliega.
```console
foo@bar:~$ git commit -a
```
5. Finalmente, podemos actualizar nuestro repositorio remoto en caso que lo tengamos. Lo primero es agregar la dirección de tal repositorio, que se realiza de la siguiente manera
```console
foo@bar:~$ git remote add origin https://github.com/mrisaro/fisica3_unsam.git
```
6. Por último, actualizamos todo que tengamos en nuestro repositorio local hacia el repositorio remoto con el comando push.
```console
foo@bar:~$ git push -u origin master
```
