https://aceptaelreto.com/pub/problems/v001/00/st/statements/Spanish/index.html

El matemático indio Dattaraya Ramchandra Kaprekar descubrió en 1949 una curiosa característica del número 6174. Hoy, se conoce a dicho número como constante de Kaprekar en honor a él.

El número es notable por la siguiente propiedad:

    1. Elige un número de cuatro dígitos que tenga al menos dos diferentes (es válido colocar el dígito 0 al principio, por lo que el número 0009 es válido).
    2. Coloca sus dígitos en orden ascendente y en orden descendente para formar dos nuevos números. Puedes añadir los dígitos 0 que necesites al principio.
    3. Resta el menor al mayor.
    4. Vuelve al paso 2.

A este proceso se le conoce como la rutina de Kaprekar, y siempre llegará al número 6174 en, como mucho, 7 iteraciones. Una vez en él, el proceso no avanzará, dado que 7641 − 1467 = 6174.

Por ejemplo, el número 3524 alcanzará la constante de Kaprekar en 3 iteraciones:

5432 − 2345 = 3087
8730 − 0378 = 8352
8532 − 2358 = 6174

Los únicos dígitos de cuatro cifras para los que la rutina de Kaprekar no alcanza el número 6174 son los repdigits, es decir aquellos cuyas cuatro cifras son iguales (como 1111), pues en la primera iteración se alcanzará el valor 0 y no podrá salirse de él. Es por esto que en el paso 1 se pedía explícitamente que el número inicial tuviera al menos dos dígitos diferentes.

El resto de los números de cuatro cifras terminarán siempre en el número 6174.

A continuación se muestran dos ejemplos más:

    - El número 1121 necesita 5 iteraciones:

2111 − 1112 = 0999
9990 − 0999 = 8991
9981 − 1899 = 8082
8820 − 0288 = 8532
8532 − 2358 = 6174

    - El número 1893 necesita 7 iteraciones:

9831 − 1389 = 8442
8442 − 2448 = 5994
9954 − 4599 = 5355
5553 − 3555 = 1998
9981 − 1899 = 8082
8820 − 0288 = 8532
8532 − 2358 = 6174

    - El número 0005 necesita 5 iteraciones:

5000 - 0005 = 4095
9540 - 0459 = 9081
9810 - 0189 = 9621
9621 - 1269 = 8352
8532 - 2358 = 6174

# Entrada

La primera línea de la entrada contendrá el número de casos de prueba. Cada uno contendrá, en una única línea, un número a comprobar.

# Salida

Para cada caso de prueba, el programa indicará el número de vueltas que se debe dar a la rutina de Kaprekar para alcanzar el 6174. Para los números repdigits deberá escribir 8. Para la propia constante de Kaprekar deberá indicar 0.

## Ejemplos

| Entrada | Salida |
| :-----: | :----: |
|    5    |        |
|  3524   |   3    |
|  1111   |   8    |
|  1121   |   5    |
|  6174   |   0    |
|  1893   |   7    |

### Consideraciónes extra

En el reto no se meciona especificamente de que forma tratar a los casos de prueba no validos, por lo que simplemente los ignoraré en la salida, de la misma forma que se hizo con el "5" en los casos de ejemplo.
