"""
    Nom: Izan Arnáiz
    Data: 02/02/2024
    Grup: ASIXc1A
    Prova: PP3-A
    Descripció:
    Implementar un programa que faci les següents operacions:
    · Crear una variable per a emmagatzemar 333 paraules.
     (Que poden ser milions)
    · Mostra tot el seu contingut
    · Omplir-la, pel teclat, amb paraules. No cal omplir-la del tot.
    Quan la paraula introduïda es "\\q" es deixa d'introduir paraules.
    · Mostra tot el seu contingut
    · Calcula la llargada mitjana de les paraules introduïdes i mostra-la per pantalla.
    · Copiar a una tupla, totes les paraules,m més petites que la mitjana amb la seva mida.
    · Mostra la tupla amb les paraules i mides corresponents.
"""

# Variables
LONGUITUD = 333
palabras = [''] * LONGUITUD
paraulesPetites = []
mitjana = 0
indice = 0
numPalabras = 0
continuar = True
print(palabras)
palabra = ""
# Control de errores
while indice < len(palabras) and continuar:
    palabra = input("Introduce una palabra o el símbolo '\\q' para salir): ")
    numPalabras += 1
    mitjana += len(palabra)
    if palabra == "\\q":
        continuar = False
    else:
        palabras[indice] = palabra
        indice += 1

# Creamos una tupla a partir de una lista
tupla_palabras_longitudes = tuple((palabra, len(palabra)) for palabra in palabras if palabra)
print("\nTupla con palabras y medias:")
print(tupla_palabras_longitudes)
print("\nLa mitjana de totes les paraules es:", mitjana // (numPalabras - 1))
# Copiamos las palabras mas pequeñas que la media a una lista
for palabra in palabras:
    if palabra:
        if len(palabra) < (mitjana // (numPalabras - 1)):
            paraulesPetites.append(palabra)
print(paraulesPetites)