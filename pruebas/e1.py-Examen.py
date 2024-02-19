"""
    Nom: Izan Arnáiz
    Data: 02/02/2024
    Grup: ASIXc1A
    Prova: PP3-A
    Descripció:
    Implementar un programa que faci les següents operacions:
    · Demanar a l'usuari, la quantitat de files i columnes d'una matriu 2D
    · Comprobar que la matriu sigui quadrada(Mateixes files i columnes) i que siguin senars
    · Omplir la matriu amb 0's tret de la primera i última columna i la filera central, ques'han d'omplir amb 1's
    · Guardar la matriu a una variable anomenada "matriu"
    · Mostrar la matriu resultant per pantalla
    El resultat ha de ser un dibuix d'una "H" amb els 1's dins de la matriu de 0's.
"""
# Control de errores
try:
    print("--Tip-- Introdueix el número de files, prem intro i després el número de columnes:")
    files = int(input(""))
    columnes = int(input(""))
    # Mismas columnas y filsa
    if files == columnes:
        # Tienen que ser impares
        if files % 2 != 0 and columnes % 2 != 0:
            matriu = [[0] * columnes for x in range(files)]
            for x in range(files):
                for y in range(columnes):
                    if y == 0 or y == files - 1 or x == files // 2:
                        matriu[x][y] = int(1)
            for x in matriu:
                print(x)
        else:
            print("Los valores de las filas y columnas deben ser impares")
    else:
        print("Introduce las mismas filas que columnas")
except ValueError:
    print("\nIntroduce valores enteros")
finally:
    print("\nPrograma terminado")