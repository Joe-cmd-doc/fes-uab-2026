###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

nom_tecnic = input("Quin és el nom del tècnic? ")
nom_xarxa = input("Quin és el nom de la xarxa? ")
print(f"El tècnic {nom_tecnic} està instal·lant la xarxa {nom_xarxa}")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

longitud_enllaç = float(input("Quina és la longitud de l'enllaç de fibra en quilòmetres? "))
velocitat_transmissió = float(input("Quina és la velocitat de transmissió en Gbps? "))
segons_per_transmitir_1_gb = longitud_enllaç / velocitat_transmissió
print(f"Calen {segons_per_transmitir_1_gb} segons per transmetre 1 GB de dades")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores_treball = float(input("Quantes hores de feina s'han realitzat? "))
preu_hora = float(input("Quin és el preu per hora? "))
preu_material = float(input("Quin és el preu del material? "))
cost_total = hores_treball * preu_hora + preu_material
print(f"El cost total de la instal·lació és: {cost_total}")