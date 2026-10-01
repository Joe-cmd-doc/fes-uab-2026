###
# Solucions - input()
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
tecnic = input("Nom del tècnic: ")
xarxa = input("Nom de la xarxa: ")
print(f"{tecnic} està instal·lant la xarxa {xarxa}.")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud_fibra = float(input("Longitud de la fibra en km: "))
velocitat_gbps = float(input("Velocitat de transmissió en Gbps: "))
temps_segons = 8 / velocitat_gbps
print(f"L'enllaç de {longitud_fibra} km necessita {temps_segons} segons per transmetre 1 GB.")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores_feina = float(input("Hores de feina: "))
preu_hora = float(input("Preu per hora en euros: "))
preu_material = float(input("Preu del material en euros: "))
cost_total = hores_feina * preu_hora + preu_material
print(f"El cost total de la instal·lació és de {cost_total} euros.")