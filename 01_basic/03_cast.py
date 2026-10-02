###
# 03 - conversió de tipus (casting)
# Aquest fitxer de Python mostra com convertir tipus de dades (casting) en Python.
# La conversió de tipus és el procés de convertir un valor d'un tipus de dada a un altre.
# És útil quan cal fer operacions entre dades de tipus diferents.
# A continuació es mostren exemples de conversió entre nombres enters, decimals i cadenes de text.
###

import os
import subprocess

clear_command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
subprocess.run(clear_command, check=False)  # Neteja la consola per facilitar la visualització

print("Conversió de tipus")

# Convertir una cadena que conté un nombre a un enter i sumar-lo a un altre enter
# print("100" + 2)  # Això generaria un TypeError perquè no es pot sumar un enter i una cadena
# print(2 + int("100"))  # Converteix "100" a enter i hi suma 2. Resultat: 102

# Convertir un enter a cadena per concatenar-lo amb una altra cadena
# print("100" + str(2))  # Converteix el nombre 2 a cadena i el concatena. Resultat: "1002"

# Convertir una cadena amb un nombre decimal al tipus float
# print(type(float("3.1416")))  # Converteix "3.1416" a float i en mostra el tipus. Resultat: <class 'float'>

# Convertir un nombre decimal a enter (s'elimina la part decimal)
# print(int(3.1416))  # Converteix 3.1416 en 3 eliminant-ne la part decimal. Resultat: 3

# Avaluar valors numèrics com a booleans
# print(bool(3))  # Qualsevol nombre diferent de 0 és True. Resultat: True
# print(bool(0))  # 0 és False. Resultat: False
# print(bool(-1))  # Els nombres negatius també són True. Resultat: True

# Avaluar cadenes com a booleans
# print(bool(""))  # Una cadena buida és False. Resultat: False
# print(bool(" "))  # Una cadena amb espais és True. Resultat: True
# print(bool("False"))  # Una cadena amb text, encara que sigui "False", és True. Resultat: True

# Arrodonir un nombre decimal
# print(round(2.51))  # Arrodoneix 2.51 a l'enter més proper. Resultat: 3

# Aquesta instrucció genera un error i es deixa activa com a exemple
print(int("Hola món"))  # ❌ Genera un ValueError perquè "Hola món" no és un nombre