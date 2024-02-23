"""
Crear un programa  on es demani un nom d'usuari i una contrasenya i
la quantitat  d’intents per fer login. Si l’usuari encerta la
combinació de nom d’usuari i contrasenya, el programa li mostrarà el
missatge “Benvingut al Sistema!” i una foto de la seva cara feta amb
caràcters ASCII.
En cas contrari, el programa li mostrarà un missatge d’error
(“Error: Nom d'usuari o contrasenya errònia!”) i tornarà a demanar-li
les dades.  Si després dels intents, l’usuari no l’encerta,
el programa mostrarà el missatge “Error: s’ha esgotat el nombre
d’intents!” i acabarà.
Crear, com a mínim,  una funció anomenada “setLogin”, que rep tres
paràmetres:
nomUsuari: el nom d'usuari que vol fer “login”
contrasenya: la contrasenya que es vol fer servir per fer “login” amb
l’usuari donat
intents: el nombre d’intents dels que es disposa per a fer login
Si els valors passats com a paràmetre són “usuari1” per al nom d'usuari
i “asdasd” per a la contrasenya, aleshores la funció retorna True i el
nombre d’intents tal qual. En cas contrari, la funció retorna False i
el valor dels intents restants
v2.0: Multiusuari. mínim 2 max 10 usuaris diferents.
v3.0: Password validator: Les contrasenyes han de complir els requisits
de complexitat
"""