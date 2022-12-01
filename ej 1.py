"""
Implementación de un árbol de decisión de regresión básico.
Conjunto de datos de entrada: el conjunto de datos de entrada debe ser unidimensional con etiquetas continuas.
Salida: el árbol de decisiones asigna una entrada de número real a una salida de número real.
"""
importar  numpy  como  np


 árbol de decisión de clase :
    def  __init__ ( self , profundidad = 5 , min_leaf_size = 5 ):
        uno mismo profundidad  =  profundidad
        uno mismo límite_decisión  =  0
        uno mismo izquierda  =  Ninguno
        uno mismo derecho  =  ninguno
        uno mismo min_leaf_size  =  min_leaf_size
        uno mismo predicción  =  Ninguno

    def  mean_squared_error ( self , etiquetas , predicción ):
        """
        error medio cuadrado:
        Etiquetas @param: una matriz numpy unidimensional
        @param predicción: un valor de coma flotante
        valor de retorno: mean_squared_error calcula el error si se utiliza la predicción para
            estimar las etiquetas
        >>> probador = Árbol de decisión()
        >>> etiquetas_prueba = np.matriz([1,2,3,4,5,6,7,8,9,10])
        >>> prueba_prediccion = float(6)
        >>> tester.mean_squared_error(test_labels, test_prediction) == (
        ... TestDecisionTree.helper_mean_squared_error_test(test_labels,
        ... prueba_predicción))
        Verdadero
        >>> etiquetas_prueba = np.matriz([1,2,3])
        >>> prueba_prediccion = float(2)
        >>> tester.mean_squared_error(test_labels, test_prediction) == (
        ... TestDecisionTree.helper_mean_squared_error_test(test_labels,
        ... prueba_predicción))
        Verdadero
        """
        si  etiquetas . ndim  !=  1 :
            print ( "Error: las etiquetas de entrada deben ser unidimensionales" )

        volver  np . media (( etiquetas  -  predicción ) **  2 )

    def  entrenar ( self , x , y ):
        """
        tren:
        @param x: una matriz numpy unidimensional
        @param y: una matriz numpy unidimensional.
        Los contenidos de y son las etiquetas para los valores correspondientes de X
        el tren no tiene un valor de retorno
        """

        """
        esta sección es para verificar que las entradas se ajusten a nuestra dimensionalidad
        restricciones
        """
        si  x _ ndim  !=  1 :
            print ( "Error: el conjunto de datos de entrada debe ser unidimensional" )
            devolver
        si  largo ( x ) !=  largo ( y ):
            print ( "Error: X e y tienen longitudes diferentes" )
            devolver
        si  y . ndim  !=  1 :
            print ( "Error: las etiquetas del conjunto de datos deben ser unidimensionales" )
            devolver

        si  len ( x ) <  2  *  self . min_leaf_size :
            uno mismo predicción  =  np . media ( y )
            devolver

        si  uno mismo . profundidad  ==  1 :
            uno mismo predicción  =  np . media ( y )
            devolver

        mejor_división  =  0
        min_error  =  uno mismo . error_cuadrado_medio ( x , np . medio ( y )) *  2

        """
        bucle sobre todas las divisiones posibles para el árbol de decisión. encontrar la mejor división.
        si no existe una división, es menos de 2 * error para toda la matriz
        entonces el conjunto de datos no se divide y el promedio de toda la matriz se usa como
        el predictor
        """
        para  i  en  rango ( len ( x )):
            si  len ( x [: i ]) <  self . min_leaf_size :
                Seguir
            elif  len ( x [ i :]) <  self . min_leaf_size :
                Seguir
            más :
                error_left  =  uno mismo . error_cuadrado_medio ( x [: i ], np . media ( y [: i ]))
                error_right  =  self . error_cuadrado_medio ( x [ i :], np . media ( y [ i :]))
                error  =  error_izquierda  +  error_derecha
                si  error  <  min_error :
                    mejor_split  =  yo
                    min_error  =  error

        si  mejor_división  !=  0 :
            izquierda_x  =  x [: mejor_división ]
            izquierda_y  =  y [: mejor_división ]
            right_x  =  x [ mejor_división :]
            right_y  =  y [ best_split :]

            uno mismo límite_decisión  =  x [ mejor_división ]
            uno mismo izquierda  = árbol de  decisión (
                profundidad = uno mismo . profundidad  -  1 , min_leaf_size = self . min_leaf_size
            )
            uno mismo derecha  = árbol de  decisión (
                profundidad = uno mismo . profundidad  -  1 , min_leaf_size = self . min_leaf_size
            )
            uno mismo izquierda _ tren ( izquierda_x , izquierda_y )
            uno mismo correcto _ tren ( derecha_x , derecha_y )
        más :
            uno mismo predicción  =  np . media ( y )

        devolver

    def  predecir ( self , x ):
        """
        predecir:
        @param x: un valor de punto flotante para predecir la etiqueta de
        la función de predicción funciona llamando recursivamente a la función de predicción
        de los subárboles apropiados en función del límite de decisión del árbol
        """
        si  uno mismo . la predicción  no es  ninguna : 
            devolverse  a uno mismo . predicción
        elif  auto . izquierda  o  uno mismo . el derecho  no es  ninguno : 
            si  x  >=  uno mismo . límite_decisión :
                devolverse  a uno mismo . correcto _ predecir ( x )
            más :
                devolverse  a uno mismo . izquierda _ predecir ( x )
        más :
            print ( "Error: árbol de decisión aún no entrenado" )
            volver  Ninguno


clase  TestDecisionTree :
    """Decisión Clase de prueba Tres"""

    @ método estático
    def  helper_mean_squared_error_test ( etiquetas , predicción ):
        """
        helper_mean_squared_error_test:
        Etiquetas @param: una matriz numpy unidimensional
        @param predicción: un valor de coma flotante
        valor de retorno: helper_mean_squared_error_test calcula el error cuadrático medio
        """
        squared_error_sum  =  float ( 0 )
        para  etiqueta  en  etiquetas :
            squared_error_sum  += ( etiqueta  -  predicción ) **  2

        devolver  flotador ( squared_error_sum  /  etiquetas . tamaño )


def  principal ():
    """
    En esta demostración estamos generando un conjunto de datos de muestra de la función sin en
    entumecido Luego entrenamos un árbol de decisión en el conjunto de datos y usamos el árbol de decisión para
    predecir la etiqueta de 10 valores de prueba diferentes. Entonces el error cuadrático medio sobre
    se muestra esta prueba.
    """
    x  =  np . un rango ( - 1.0 , 1.0 , 0.005 )
    y  =  np . pecado ( x )

    árbol  =  DecisionTree ( profundidad = 10 , min_leaf_size = 10 )
    árbol _ tren ( x , y )

    test_cases  = ( np . aleatorio . rand ( 10 ) *  2 ) -  1
    predicciones  =  np . array ([ árbol . predecir ( x ) para  x  en  test_cases ])
    avg_error  =  np . media (( predicciones  -  test_cases ) **  2 )

    print ( "Valores de prueba:"  +  str ( test_cases ))
    print ( "Predicciones: "  +  str ( predicciones ))
    imprimir ( "Error promedio:"  +  str ( avg_error ))


si  __nombre__  ==  "__principal__" :
    principal ()
    importar  documento

    doctest _ testmod ( nombre = "mean_squarred_error" , detallado = True )