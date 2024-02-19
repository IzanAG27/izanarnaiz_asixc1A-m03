"""
    Nom: Izan Arnáiz
    Data: 02/02/2024
    Grup: ASIXc1A
    Prova: PP3-A
    Descripció:
    Programa que vagi llegint frases pel teclat i, en acabar cada entrada
    d'una frase mostri la frase encriptada. Per encript
    ar la frase, ha de canviar les vocals per numeros de l'1 al 5.
    No fer diferències entre majúscules i minúscules, ni lletres
    amb accents, totes s'han de tractar com si fossin minúscules i
    sense accent. No es por fer servir la funció replace.
    El programa acaba en escriure la frase "eso es t'odo amigos, que no s'ha d'encriptar.
    Exemple:
        Do not worry be Javi
        D4 n4t w4rry b2 J1v3
"""

continuar = True
while continuar:
    cadena = str(input(""))
    cadena = cadena.lower()
    if cadena == "eso es todo amigos":
        continuar = False
    else:
        for x in range(len(cadena)):
            if cadena[x] == "a" or cadena[x] == "á" or cadena[x] == "à":
                print("1", end="")
            elif cadena[x] == "e" or cadena[x] == "é" or cadena[x] == "è":
                print("2", end="")
            elif cadena[x] == "i" or cadena[x] == "í" or cadena[x] == "ì":
                print("3", end="")
            elif cadena[x] == "o" or cadena[x] == "ó" or cadena[x] == "ò":
                print("4", end="")
            elif cadena[x] == "u" or cadena[x] == "ú" or cadena[x] == "ù":
                print("5", end="")
            else:
                print(cadena[x], end="")
        print("")