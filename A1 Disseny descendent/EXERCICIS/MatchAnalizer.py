# region CODIGO
# region FUNCIONES
# region OBTENER EQUIPOS
def obtener_equipos():
    equipo1 = input("")
    equipo2 = input("")
    return equipo1, equipo2


# endregion

# region OBTENER PUNTUACIONES
def obtener_puntuaciones():
    puntuaciones = []
    puntuacion_anterior = (0, 0)
    fin_del_juego = False
    while not fin_del_juego:
        puntuacion = [int(x) for x in input("").split()]
        if puntuacion[0] == -1:
            fin_del_juego = True
        else:
            if puntuacion != puntuacion_anterior and not any(
                    i - p > 3 for i, p in zip(puntuacion, puntuacion_anterior)) and not (
                    puntuacion[0] != puntuacion_anterior[0] and puntuacion[1] != puntuacion_anterior[1]):
                puntuaciones.append(tuple(puntuacion))
                puntuacion_anterior = puntuacion
            else:
                print(
                    "Puntuación inválida. Por favor, introduce una puntuación mayor que la anterior y con una "
                    "diferencia de 1, 2 o 3. Solo un equipo puede puntuar en cada turno.")
    return puntuaciones


# endregion

# region COMPARAR PUNTUACIONES
def comparar_puntuaciones(puntuaciones, equipo1, equipo2):
    resultados = []
    puntuacion_anterior = (0, 0)
    for puntuacion in puntuaciones:
        diferencia_equipo1 = puntuacion[0] - puntuacion_anterior[0]
        diferencia_equipo2 = puntuacion[1] - puntuacion_anterior[1]
        if diferencia_equipo1 == 1:
            resultados.append("Tir lliure de " + equipo1)
        elif diferencia_equipo1 == 2:
            resultados.append("Cistella de " + equipo1)
        elif diferencia_equipo1 == 3:
            resultados.append("Triple de " + equipo1)
        if diferencia_equipo2 == 1:
            resultados.append("Tir lliure de " + equipo2)
        elif diferencia_equipo2 == 2:
            resultados.append("Cistella de " + equipo2)
        elif diferencia_equipo2 == 3:
            resultados.append("Triple de " + equipo2)
        puntuacion_anterior = puntuacion
    return resultados


# endregion

# region MOSTRAR RESULTADOS
def mostrar_resultados(resultados, puntuaciones, equipo1, equipo2):
    for resultado in resultados:
        print(resultado)
    if puntuaciones[-1][0] > puntuaciones[-1][1]:
        print("Guanya " + equipo1)
    else:
        print("Guanya " + equipo2)


# endregion

# region MOSTRAR GANADORES
def mostrar_ganadores():
    equipo1, equipo2 = obtener_equipos()
    puntuaciones = obtener_puntuaciones()
    resultados = comparar_puntuaciones(puntuaciones, equipo1, equipo2)
    mostrar_resultados(resultados, puntuaciones, equipo1, equipo2)


# endregion
# endregion
mostrar_ganadores()
# endregion
