##
# 04 - Variables
# Les variables serveixen per desar dades a la memòria.
# Python és un llenguatge de tipatge dinàmic i fort.
###

import os
os.system("cls")

# Per assignar una variable, només cal escriure'n el nom i donar-li un valor
nom_complet = "marc esteve"
print(nom_complet)  # Mostra el valor de la variable nom_complet

edat = 32
print(edat)  # Mostra el valor de la variable edat
print(type(edat))  # Mostra el tipus de dada de la variable edat (int)

# Assignar un valor nou a una variable existent
edat = 39
print(edat)  # Ara la variable edat té el valor 39

# Tipatge dinàmic: el tipus de dada es determina durant l'execució
# No cal declarar explícitament el tipus de la variable
nom = "marc"
print(type(nom))  # Mostra el tipus de dada de la variable nom (str)

nom = 32
print(type(nom))  # Ara la variable conté un nombre enter (int)

# Tipatge fort: Python no converteix els tipus automàticament
# Això genera un error perquè no es pot sumar un nombre i una cadena
# print(10 + "2")  # ❌ TypeError: unsupported operand type(s) for +: 'int' and 'str'

# f-string (cadena de text formatada), disponible des de Python 3.6
print(f"Hola {nom_complet}, d'aquí a 5 anys tindré {edat + 5} anys")
# print("Hola " + nom_complet + ", d'aquí a 5 anys tindré " + str(edat + 5) + " anys")

# Forma no recomanada d'assignar variables
nom, edat, ciutat = "pepito", 32, "Madrid"

# Convencions per als noms de variables
el_meu_nom_de_variable = "correcte"  # snake_case
nom = "correcte"

elMeuNomDeVariable = "no recomanat"  # camelCase
ElMeuNomDeVariable = "no recomanat"  # PascalCase
elmeunomdevariable = "no recomanat"  # tot junt

el_meu_nom_de_variable_123 = "correcte"

LA_MEVA_CONSTANT = 3.14  # UPPER_CASE -> constants

LA_MEVA_CONSTANT = 3  # Python no té constants, però se segueix aquesta convenció


# Noms de variables no vàlids (generarien errors)
# 123123_variable = "incorrecte"  # ❌ No pot començar amb un nombre
# el-meu-nom = "incorrecte"  # ❌ No pot contenir guions (-); fes servir guions baixos (_)
# el meu nom = "incorrecte"  # ❌ No pot contenir espais
# True = False  # ❌ No es poden sobreescriure les paraules reservades

# Paraules reservades de Python (no es poden fer servir com a noms de variables)

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

# Anotacions de tipus (opcionals, per fer el codi més clar)
usuari_ha_iniciat_sessio: bool = True  # Indica que la variable és booleana
print(usuari_ha_iniciat_sessio)

# Activa la comprovació de tipus a la configuració de VS Code per veure'n els avisos
# Prem Ctrl + , i cerca "type checking" a la configuració

nom: str = "marc"  # Indica que la variable és una cadena de text
print(nom)