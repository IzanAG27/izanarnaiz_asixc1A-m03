import random

def crear_tablero(filas, columnas, num_minas):
    # Crear un tablero vacío
    tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]

    # Colocar minas aleatoriamente
    minas_colocadas = 0
    while minas_colocadas < num_minas:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        if tablero[fila][columna] != 'X':
            tablero[fila][columna] = 'X'
            minas_colocadas += 1

    return tablero

def mostrar_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))

def main():
    filas = 10
    columnas = 10
    num_minas = 10

    tablero = crear_tablero(filas, columnas, num_minas)
    mostrar_tablero(tablero)

if __name__ == '__main__':
    main()
