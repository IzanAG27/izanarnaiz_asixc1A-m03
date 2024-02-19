def print_taulell(taulell):
    for fila in reversed(taulell):  # Invertimos el orden de las filas aquí
        print(' '.join(fila))
    print()

def comprovar_victoria(taulell):
    for fila in taulell:
        if fila.count('X') == 3:
            return 'X'
        if fila.count('O') == 3:
            return 'O'
    for columna in range(3):
        if [fila[columna] for fila in taulell].count('X') == 3:
            return 'X'
        if [fila[columna] for fila in taulell].count('O') == 3:
            return 'O'
    if [taulell[i][i] for i in range(3)].count('X') == 3 or [taulell[i][2 - i] for i in range(3)].count('X') == 3:
        return 'X'
    if [taulell[i][i] for i in range(3)].count('O') == 3 or [taulell[i][2 - i] for i in range(3)].count('O') == 3:
        return 'O'
    return None

taulell = [['·' for _ in range(3)] for _ in range(3)]
jugador_actual = 'X'

while True:
    print_taulell(taulell)
    fila, columna = map(int, input().split())  # Intercambiamos las coordenadas aquí
    if taulell[2 - fila][columna] != '·':  # Comprobamos si la casilla está vacía
        print("Esta casilla ya está ocupada. Por favor, elige una casilla diferente.")
        continue
    taulell[2 - fila][columna] = jugador_actual  # Invertimos la fila aquí
    guanyador = comprovar_victoria(taulell)
    if guanyador is not None:
        print(f'guanyen les {guanyador}')
        break
    if all(casella != '·' for fila in taulell for casella in fila):
        print('empat')
        break
    jugador_actual = 'O' if jugador_actual == 'X' else 'X'